#!/usr/bin/env python3
"""Offline unit tests for the MiniMax image-generation format."""

import base64
import importlib.util
import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "scripts"
_spec = importlib.util.spec_from_file_location(
    "generate_image", SCRIPTS_DIR / "generate_image.py"
)
generate_image = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(generate_image)


class FakeResponse:
    def __init__(self, json_data=None, content=b"", status_code=200):
        self._json = json_data or {}
        self.content = content
        self.status_code = status_code

    def json(self):
        return self._json

    def raise_for_status(self):
        pass


class MiniMaxImageTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()

    def _run(self, response_json, region=None, response_format=None,
             image_bytes=b"PNGDATA"):
        captured = {}

        def fake_post(url, headers=None, json=None, timeout=None):
            captured["url"] = url
            captured["payload"] = json
            captured["headers"] = headers
            return FakeResponse(json_data=response_json)

        def fake_get(url, timeout=None):
            captured["download_url"] = url
            return FakeResponse(content=image_bytes)

        out = os.path.join(self.tmp, "out.png")
        with mock.patch.object(generate_image.requests, "post", fake_post), \
                mock.patch.object(generate_image.requests, "get", fake_get):
            result = generate_image.generate_image_with_chat(
                prompt="a cat",
                filename=out,
                api_key="test-key",
                api_format="minimax",
                region=region,
                response_format=response_format,
            )
        return result, captured, out

    def test_global_endpoint_and_payload(self):
        resp = {
            "base_resp": {"status_code": 0},
            "data": {"image_urls": ["https://img.example/1.png"]},
            "metadata": {"success_count": 1, "failed_count": 0},
        }
        result, captured, out = self._run(resp)
        self.assertEqual(captured["url"],
                         "https://api.minimax.io/v1/image_generation")
        self.assertEqual(captured["payload"]["model"], "image-01")
        self.assertEqual(captured["payload"]["prompt"], "a cat")
        self.assertEqual(captured["payload"]["response_format"], "url")
        self.assertEqual(captured["payload"]["n"], 1)
        self.assertEqual(captured["headers"]["Authorization"], "Bearer test-key")
        self.assertEqual(captured["download_url"], "https://img.example/1.png")
        self.assertEqual(result, out)
        self.assertTrue(os.path.exists(out))

    def test_cn_region_endpoint(self):
        resp = {
            "base_resp": {"status_code": 0},
            "data": {"image_urls": ["https://img.example/2.png"]},
        }
        _, captured, _ = self._run(resp, region="cn_zh")
        self.assertEqual(captured["url"],
                         "https://api.minimaxi.com/v1/image_generation")

    def test_base64_output_parsing(self):
        encoded = base64.b64encode(b"IMGBYTES").decode()
        resp = {
            "base_resp": {"status_code": 0},
            "data": {"image_base64": [encoded]},
        }
        _, captured, out = self._run(resp, response_format="base64")
        self.assertEqual(captured["payload"]["response_format"], "base64")
        with open(out, "rb") as fh:
            self.assertEqual(fh.read(), b"IMGBYTES")

    def test_error_status_code_exits(self):
        resp = {"base_resp": {"status_code": 1004, "status_msg": "auth failed"}}
        with self.assertRaises(SystemExit):
            self._run(resp)


if __name__ == "__main__":
    unittest.main()

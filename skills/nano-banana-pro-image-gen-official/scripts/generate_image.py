#!/usr/bin/env python3
"""
基于NanoBananaPro/Gemini 3 Pro的图片生成与编辑脚本
使用API易国内代理服务

支持功能：
- 文生图：根据提示词生成图片
- 图生图：根据编辑指令修改已有图片

参数说明：
- aspect_ratio: 图片比例 (1:1, 16:9, 9:16, 4:3, 3:4, 3:2, 2:3, 5:4, 4:5, 21:9)
- resolution: 图片分辨率 (1K, 2K, 4K)，必须大写
"""

import os
import sys
import json
import base64
import argparse
from unittest import result
import requests
from pathlib import Path
from datetime import datetime


# 支持的比例列表
SUPPORTED_ASPECT_RATIOS = [
    "1:1",
    "16:9",
    "9:16",
    "4:3",
    "3:4",
    "3:2",
    "2:3",
    "5:4",
    "4:5",
    "21:9",
]
SUPPORTED_RESOLUTIONS = ["1K", "2K", "4K"]


def get_api_key(args_key=None):
    """获取API密钥，优先使用命令行参数"""
    if args_key:
        return args_key

    api_key = os.environ.get("APIYI_API_KEY")
    if not api_key:
        print("错误: 未设置 APIYI_API_KEY 环境变量")
        print("请前往 https://api.apiyi.com 注册申请API Key")
        print("或使用 --api-key 参数临时指定")
        sys.exit(1)

    return api_key


def generate_filename(prompt):
    """根据提示词生成带时间戳的文件名"""
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    # 从提示词提取关键词（简化处理）
    keywords = prompt.split()[:3]  # 取前3个词
    keyword_str = "-".join(keywords)

    # 清理文件名中的特殊字符
    keyword_str = "".join(c if c.isalnum() or c in "-_." else "-" for c in keyword_str)
    keyword_str = keyword_str.lower()[:30]  # 限制长度

    return f"{timestamp}-{keyword_str}.png"


def add_timestamp_to_filename(filename: str, timestamp: str) -> str:
    p = Path(filename)
    stem = p.stem or "image"
    suffix = p.suffix
    # If suffix is empty, keep it empty (caller may intentionally omit extension)
    new_name = f"{stem}-{timestamp}{suffix}"
    return str(p.with_name(new_name))


def encode_image_to_base64(image_path):
    """将图片文件转换为base64编码"""
    try:
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    except Exception as e:
        print(f"错误: 无法读取图片文件 {image_path} - {e}")
        sys.exit(1)


def generate_image(
    prompt,
    filename,
    aspect_ratio=None,
    resolution=None,
    input_image=None,
    api_key=None,
):
    """
    生成或编辑图片

    Args:
        prompt: 图片描述或编辑指令文本
        filename: 输出图片路径
        aspect_ratio: 图片比例 (可选，默认由API决定)
        resolution: 图片分辨率 (可选，默认由API决定)
        input_image: 输入图片路径（编辑模式时使用）
        api_key: API密钥
    """
    # 验证参数（仅在提供了参数时验证）
    if aspect_ratio is not None and aspect_ratio not in SUPPORTED_ASPECT_RATIOS:
        print(f"错误: 不支持的比例 '{aspect_ratio}'")
        print(f"支持的比例: {', '.join(SUPPORTED_ASPECT_RATIOS)}")
        sys.exit(1)

    if resolution is not None and resolution not in SUPPORTED_RESOLUTIONS:
        print(f"错误: 不支持的分辨率 '{resolution}'")
        print(f"支持的分辨率: {', '.join(SUPPORTED_RESOLUTIONS)} (必须大写)")
        sys.exit(1)

    api_key = get_api_key(api_key)
    url = (
        "https://api.apiyi.com/v1beta/models/gemini-3-pro-image-preview:generateContent"
    )

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    # 构建content部分
    parts = [{"text": prompt}]

    # 如果提供了输入图片，添加图片数据（图生图模式）
    # NanoBananaPro最多支持14张参考图片
    if input_image:
        if isinstance(input_image, (list, tuple)):
            input_images = list(input_image)
        else:
            input_images = [input_image]

        if len(input_images) > 14:
            print(f"错误: 输入图片最多支持14张，当前为 {len(input_images)} 张")
            sys.exit(1)

        for image_path in input_images:
            if not os.path.exists(image_path):
                print(f"错误: 输入图片不存在: {image_path}")
                sys.exit(1)

            image_base64 = encode_image_to_base64(image_path)
            parts.append({"inlineData": {"mimeType": "image/png", "data": image_base64}})

        mode_str = "编辑图片"
    else:
        mode_str = "生成图片"

    # 构建payload，只添加用户指定的参数
    generation_config = {
        "responseModalities": ["IMAGE"],
    }
    image_config = {}
    if aspect_ratio is not None:
        image_config["aspectRatio"] = aspect_ratio
    if resolution is not None:
        image_config["imageSize"] = resolution
    if image_config:
        generation_config["imageConfig"] = image_config

    payload = {
        "contents": [{"parts": parts}],
        "generationConfig": generation_config,
    }

    print(f"正在{mode_str}...")
    print(f"提示词: {prompt}")

    if generation_config.get("imageConfig", {}).get("aspectRatio"):
        print(f"比例: {generation_config['imageConfig']['aspectRatio']}")
    if generation_config.get("imageConfig", {}).get("imageSize"):
        print(f"分辨率: {generation_config['imageConfig']['imageSize']}")

    # 输出请求参数（脱敏：不直接输出base64图片数据，避免刷屏）
    payload_log = {
        "generationConfig": generation_config,
        "contents": [],
    }
    for content in payload.get("contents", []):
        parts_log = []
        for part in content.get("parts", []):
            if isinstance(part, dict) and "inlineData" in part and isinstance(part["inlineData"], dict):
                inline_data = dict(part["inlineData"])
                data_value = inline_data.get("data")
                if isinstance(data_value, str):
                    inline_data["data"] = f"<omitted base64: {len(data_value)} chars>"
                parts_log.append({"inlineData": inline_data})
            else:
                parts_log.append(part)
        payload_log["contents"].append({"parts": parts_log})

    print(f"输出请求参数: {json.dumps(payload_log, indent=2, ensure_ascii=False)}")
    print(f"image generation in progress...")
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=400)
        response.raise_for_status()

        data = response.json()

        # 解析响应，查找图片数据
        image_data = None
        text_response = ""

        if "candidates" in data and len(data["candidates"]) > 0:
            candidate = data["candidates"][0]
            image_data = candidate["content"]["parts"][0]["inlineData"]["data"]

        if image_data:
            # 解码base64图片数据
            image_bytes = base64.b64decode(image_data)

            # 确保输出目录存在
            output_file = Path(filename)
            output_file.parent.mkdir(parents=True, exist_ok=True)

            # 保存图片
            with open(output_file, "wb") as f:
                f.write(image_bytes)

            print(f"✓ 图片已成功{mode_str}并保存到: {filename}")

            if text_response.strip():
                print(f"模型响应: {text_response.strip()}")

            return filename
        else:
            print("错误: 响应中未找到图片数据")
            print(f"完整响应: {json.dumps(data, indent=2, ensure_ascii=False)}")
            sys.exit(1)

    except requests.exceptions.Timeout:
        print("错误: 请求超时，请稍后重试")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"错误: 请求失败 - {e}")
        if hasattr(e, "response") and e.response is not None:
            try:
                error_detail = e.response.json()
                print(
                    f"错误详情: {json.dumps(error_detail, indent=2, ensure_ascii=False)}"
                )
            except:
                print(f"响应状态码: {e.response.status_code}")
                print(f"响应内容: {e.response.text}")
        sys.exit(1)
    except Exception as e:
        print(f"错误: {str(e)}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="基于Gemini 3 Pro的图片生成与编辑工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用示例:

【生成新图片】
    python generate_image.py -p "一只可爱的橘猫"
    python generate_image.py -p "日落山脉" -a 16:9 -r 4K
    python generate_image.py -p "城市夜景" -a 9:16 -r 2K -f wallpaper.png

【编辑已有图片】
    python generate_image.py -p "转换成油画风格" -i original.png
    python generate_image.py -p "添加彩虹到天空" -i photo.jpg -f edited.png
    python generate_image.py -p "将背景换成海滩" -i portrait.png -a 3:4 -r 2K
    python generate_image.py -p "参考多张图片融合风格" -i ref1.png ref2.png ref3.png -f merged.png

【支持的参数值】
  --aspect-ratio: 可选 (1:1, 16:9, 9:16, 4:3, 3:4, 3:2, 2:3, 5:4, 4:5, 21:9)
  --resolution:   可选 (1K, 2K, 4K，必须大写)

【环境变量】
  export APIYI_API_KEY="your-api-key"
        """,
    )

    parser.add_argument("--prompt", "-p", required=True, help="图片描述或编辑指令文本")
    parser.add_argument(
        "--filename",
        "-f",
        default=None,
        help="输出图片路径 (默认: 自动生成时间戳文件名)",
    )
    parser.add_argument(
        "--aspect-ratio",
        "-a",
        default=None,
        choices=SUPPORTED_ASPECT_RATIOS,
        help="图片比例 (可选: 1:1, 16:9, 9:16, 4:3, 3:4, 3:2, 2:3, 5:4, 4:5, 21:9)",
    )
    parser.add_argument(
        "--resolution",
        "-r",
        default=None,
        choices=SUPPORTED_RESOLUTIONS,
        help="图片分辨率 (可选: 1K, 2K, 4K，必须大写)",
    )
    parser.add_argument(
        "--input-image",
        "-i",
        nargs="+",
        default=None,
        help="输入图片路径（编辑模式，可传多张，最多14张）",
    )
    parser.add_argument("--api-key", "-k", default=None, help="API密钥（覆盖环境变量）")

    args = parser.parse_args()

    run_timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    # 如果没有指定文件名，自动生成
    if args.filename is None:
        args.filename = generate_filename(args.prompt)
    else:
        out_path = Path(args.filename)
        if out_path.exists():
            adjusted = add_timestamp_to_filename(args.filename, run_timestamp)
            print(f"警告: 输出文件已存在，将避免覆盖并改为: {adjusted}")
            args.filename = adjusted

    generate_image(
        prompt=args.prompt,
        filename=args.filename,
        aspect_ratio=args.aspect_ratio,
        resolution=args.resolution,
        input_image=args.input_image,
        api_key=args.api_key,
    )


if __name__ == "__main__":
    main()

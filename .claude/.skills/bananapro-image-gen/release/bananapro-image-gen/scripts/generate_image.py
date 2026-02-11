#!/usr/bin/env python3
"""
使用 Chat Completions 格式生成图片
适配 nextaicore API
"""

import os
import sys
import json
import base64
import argparse
import requests
from pathlib import Path
from datetime import datetime
import re

# API 配置
# 请通过环境变量或命令行参数提供 API Key
# export NEXTAI_API_KEY="your-api-key-here"
DEFAULT_API_KEY = ""  # 不要在代码中硬编码 API Key
DEFAULT_BASE_URL = "https://apipro.maynor1024.live"
DEFAULT_MODEL = "gemini-3-pro-image-preview"
DEFAULT_API_FORMAT = "openai"  # "openai" 或 "gemini"

SUPPORTED_RESOLUTIONS = ["1K", "2K", "4K"]
SUPPORTED_API_FORMATS = ["openai", "gemini"]


def get_api_key(args_key=None):
    """获取API密钥"""
    if args_key:
        return args_key
    
    api_key = os.environ.get("NEXTAI_API_KEY")
    if api_key:
        return api_key
    
    # 如果没有提供 API Key，提示用户
    print("❌ 错误：未找到 API Key")
    print("请通过以下方式之一提供 API Key：")
    print("  1. 环境变量：export NEXTAI_API_KEY='your-api-key'")
    print("  2. 命令行参数：--api-key 'your-api-key'")
    sys.exit(1)


def generate_filename(prompt):
    """根据提示词生成带时间戳的文件名"""
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    keywords = prompt.split()[:3]
    keyword_str = "-".join(keywords)
    keyword_str = "".join(c if c.isalnum() or c in "-_." else "-" for c in keyword_str)
    keyword_str = keyword_str.lower()[:30]
    return f"{timestamp}-{keyword_str}.png"


def extract_image_from_markdown(text):
    """从 Markdown 文本中提取图片 URL 或 base64"""
    # 匹配 ![](url) 格式
    url_pattern = r'!\[.*?\]\((https?://[^\)]+)\)'
    urls = re.findall(url_pattern, text)
    if urls:
        return urls[0], 'url'
    
    # 匹配 base64 格式
    base64_pattern = r'data:image/[^;]+;base64,([A-Za-z0-9+/=]+)'
    base64_matches = re.findall(base64_pattern, text)
    if base64_matches:
        return base64_matches[0], 'base64'
    
    return None, None


def generate_image_with_chat(
    prompt,
    filename,
    resolution=None,
    model=None,
    api_key=None,
    base_url=None,
    api_format=None,
):
    """
    使用 Chat Completions 格式生成图片
    支持两种 API 格式：
    - openai: /v1/chat/completions
    - gemini: /v1beta/models/gemini-3-pro-image-preview:generateContent
    """
    api_key = get_api_key(api_key)
    base_url = base_url or DEFAULT_BASE_URL
    model = model or DEFAULT_MODEL
    api_format = api_format or DEFAULT_API_FORMAT
    
    # 根据 API 格式选择端点
    if api_format == "gemini":
        url = f"{base_url}/v1beta/models/{model}:generateContent"
    else:  # openai
        url = f"{base_url}/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    # 构建提示词（添加分辨率要求）
    full_prompt = prompt
    if resolution:
        full_prompt = f"{prompt}，分辨率：{resolution}"
    
    # 根据 API 格式构建 payload
    if api_format == "gemini":
        # Gemini 原生格式
        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": full_prompt}
                    ]
                }
            ],
            "generationConfig": {
                "responseModalities": ["IMAGE"]
            }
        }
        if resolution:
            payload["generationConfig"]["imageConfig"] = {
                "imageSize": resolution
            }
    else:
        # OpenAI 兼容格式
        payload = {
            "model": model,
            "messages": [
                {
                    "role": "user",
                    "content": full_prompt
                }
            ],
            "stream": False
        }
    
    print(f"正在生成图片...")
    print(f"提示词: {prompt}")
    if resolution:
        print(f"分辨率: {resolution}")
    print(f"模型: {model}")
    print(f"API 格式: {api_format}")
    print(f"API: {url}")
    print()
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=120)
        
        print(f"响应状态码: {response.status_code}")
        
        if response.status_code != 200:
            print(f"错误响应: {response.text[:500]}")
            sys.exit(1)
        
        data = response.json()
        
        # 根据 API 格式解析响应
        if api_format == "gemini":
            # Gemini 格式：从 candidates 中提取图片
            if "candidates" in data and len(data["candidates"]) > 0:
                parts = data["candidates"][0].get("content", {}).get("parts", [])
                for part in parts:
                    if "inlineData" in part:
                        image_data = part["inlineData"].get("data")
                        if image_data:
                            print(f"解码 Gemini base64 图片数据")
                            image_bytes = base64.b64decode(image_data)
                            
                            # 保存图片
                            output_file = Path(filename)
                            output_file.parent.mkdir(parents=True, exist_ok=True)
                            
                            with open(output_file, "wb") as f:
                                f.write(image_bytes)
                            
                            print(f"✅ 图片已成功生成并保存到: {filename}")
                            print(f"文件大小: {len(image_bytes) / 1024:.2f} KB")
                            return filename
                
                print("⚠️  未在 Gemini 响应中找到图片数据")
                print(f"完整响应: {json.dumps(data, indent=2, ensure_ascii=False)[:500]}")
                return None
        else:
            # OpenAI 格式：从 choices 中提取图片
            if "choices" in data and len(data["choices"]) > 0:
                content = data["choices"][0]["message"]["content"]
                
                print(f"模型回复长度: {len(content)} 字符")
                print(f"回复内容（前200字符）: {content[:200]}")
                print()
                
                # 尝试从回复中提取图片
                image_data, data_type = extract_image_from_markdown(content)
                
                if image_data:
                    if data_type == 'url':
                        # 下载图片
                        print(f"下载图片: {image_data}")
                        img_response = requests.get(image_data, timeout=30)
                        img_response.raise_for_status()
                        image_bytes = img_response.content
                    elif data_type == 'base64':
                        # 解码 base64
                        print(f"解码 base64 图片数据")
                        image_bytes = base64.b64decode(image_data)
                    
                    # 保存图片
                    output_file = Path(filename)
                    output_file.parent.mkdir(parents=True, exist_ok=True)
                    
                    with open(output_file, "wb") as f:
                        f.write(image_bytes)
                    
                    print(f"✅ 图片已成功生成并保存到: {filename}")
                    print(f"文件大小: {len(image_bytes) / 1024:.2f} KB")
                    return filename
                else:
                    print("⚠️  未在回复中找到图片数据")
                    print(f"完整回复: {content}")
                    
                    # 保存回复到文本文件
                    text_file = filename.replace('.png', '.txt')
                    output_file = Path(text_file)
                    output_file.parent.mkdir(parents=True, exist_ok=True)
                    with open(text_file, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"回复已保存到: {text_file}")
                    
                    return None
            else:
                print("错误: 响应格式不正确")
                print(f"完整响应: {json.dumps(data, indent=2, ensure_ascii=False)}")
                sys.exit(1)
    
    except requests.exceptions.Timeout:
        print("错误: 请求超时，请稍后重试")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"错误: 请求失败 - {e}")
        if hasattr(e, "response") and e.response is not None:
            print(f"状态码: {e.response.status_code}")
            print(f"响应内容: {e.response.text[:500]}")
        sys.exit(1)
    except Exception as e:
        print(f"错误: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="使用 Chat Completions 格式生成图片",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用示例:

【生成图片】
    python generate_image_chat.py -p "画一只可爱的橙色猫咪"
    python generate_image_chat.py -p "生成一张日落山脉的图片" -r 2K
    python generate_image_chat.py -p "创建一个科技感的 Logo" -f logo.png

【指定模型】
    python generate_image_chat.py -p "画只猫" -m gpt-4o-image
    python generate_image_chat.py -p "画只猫" -m gemini-3-pro-image-preview

【API 配置】
  默认 API: https://api.nextaicore.com
  默认 Key: sk-WY9Rx5caemo39xIMN2OCNQ4cD3L0RDtKmC9Q1rot9rcKxgow
  默认模型: gemini-3-pro-image-preview
  
  可通过环境变量覆盖:
    export NEXTAI_API_KEY="your-key"
        """,
    )
    
    parser.add_argument("--prompt", "-p", required=True, help="图片描述")
    parser.add_argument("--filename", "-f", default=None, help="输出图片路径")
    parser.add_argument(
        "--resolution", "-r",
        default=None,
        choices=SUPPORTED_RESOLUTIONS,
        help="图片分辨率 (1K, 2K, 4K)"
    )
    parser.add_argument(
        "--model", "-m",
        default=DEFAULT_MODEL,
        help="模型名称 (默认: gemini-3-pro-image-preview)"
    )
    parser.add_argument(
        "--api-format", "-a",
        default=DEFAULT_API_FORMAT,
        choices=SUPPORTED_API_FORMATS,
        help="API 格式: openai 或 gemini (默认: openai)"
    )
    parser.add_argument("--api-key", "-k", default=None, help="API 密钥")
    parser.add_argument("--base-url", "-u", default=None, help="API 基础 URL")
    
    args = parser.parse_args()
    
    # 生成文件名
    if args.filename is None:
        args.filename = generate_filename(args.prompt)
    
    # 生成图片
    generate_image_with_chat(
        prompt=args.prompt,
        filename=args.filename,
        resolution=args.resolution,
        model=args.model,
        api_key=args.api_key,
        base_url=args.base_url,
        api_format=args.api_format,
    )


if __name__ == "__main__":
    main()

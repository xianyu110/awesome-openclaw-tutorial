#!/usr/bin/env python3
"""
基于中转 API 的图片生成脚本（适配版）
使用 OpenAI 兼容格式的中转 API 服务

支持功能：
- 文生图：根据提示词生成图片
- 图生图：根据编辑指令修改已有图片

API 配置：
- Endpoint: https://api.nextaicore.com/openai
- 格式: OpenAI 兼容
"""

import os
import sys
import json
import base64
import argparse
import requests
from pathlib import Path
from datetime import datetime

# 中转 API 配置
DEFAULT_API_KEY = "sk-iuRXquaxhd9Xc5wya9VdgrGvw2UwgvlBmkSnqOtLRp50vinp"
DEFAULT_BASE_URL = "https://api.nextaicore.com/openai"

# 注意：确保使用正确的 API endpoint
# 你提供的信息：
# - API Key: sk-iuRXquaxhd9Xc5wya9VdgrGvw2UwgvlBmkSnqOtLRp50vinp
# - Base URL: https://api.nextaicore.com/openai
# - 格式: chat 格式（OpenAI 兼容）

# 支持的比例列表
SUPPORTED_ASPECT_RATIOS = [
    "1:1", "16:9", "9:16", "4:3", "3:4",
    "3:2", "2:3", "5:4", "4:5", "21:9",
]
SUPPORTED_RESOLUTIONS = ["1K", "2K", "4K"]

# 分辨率映射（OpenAI 格式）
RESOLUTION_MAP = {
    "1K": "1024x1024",
    "2K": "2048x2048",
    "4K": "4096x4096",
}


def get_api_key(args_key=None):
    """获取API密钥"""
    if args_key:
        return args_key
    
    # 优先使用 PROXY_API_KEY（专门为这个脚本设置的）
    api_key = os.environ.get("PROXY_API_KEY")
    if api_key:
        return api_key
    
    # 使用默认密钥（不使用 OPENAI_API_KEY，避免冲突）
    print("⚠️  使用默认 API Key")
    return DEFAULT_API_KEY


def get_base_url(args_url=None):
    """获取 API 基础 URL"""
    if args_url:
        return args_url
    
    # 优先使用 PROXY_BASE_URL（专门为这个脚本设置的）
    base_url = os.environ.get("PROXY_BASE_URL")
    if base_url:
        return base_url
    
    # 使用默认的中转 API（不使用 OPENAI_BASE_URL，避免冲突）
    return DEFAULT_BASE_URL


def generate_filename(prompt):
    """根据提示词生成带时间戳的文件名"""
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    keywords = prompt.split()[:3]
    keyword_str = "-".join(keywords)
    keyword_str = "".join(c if c.isalnum() or c in "-_." else "-" for c in keyword_str)
    keyword_str = keyword_str.lower()[:30]
    return f"{timestamp}-{keyword_str}.png"


def add_timestamp_to_filename(filename: str, timestamp: str) -> str:
    """给文件名添加时间戳"""
    p = Path(filename)
    stem = p.stem or "image"
    suffix = p.suffix
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


def generate_with_dalle_format(
    prompt,
    filename,
    resolution=None,
    api_key=None,
    base_url=None,
):
    """
    使用 DALL-E 格式生成图片（文生图）
    """
    api_key = get_api_key(api_key)
    base_url = get_base_url(base_url)
    
    url = f"{base_url}/v1/images/generations"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # 映射分辨率
    size = RESOLUTION_MAP.get(resolution, "1024x1024")
    
    payload = {
        "model": "dall-e-3",  # 或 "gemini-3-pro-image-preview"
        "prompt": prompt,
        "n": 1,
        "size": size,
        "quality": "hd" if resolution in ["2K", "4K"] else "standard",
    }
    
    print(f"正在生成图片...")
    print(f"提示词: {prompt}")
    print(f"分辨率: {resolution or '1K'} ({size})")
    print(f"API: {url}")
    print()
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=120)
        response.raise_for_status()
        
        data = response.json()
        
        # 检查响应格式
        if "data" in data and len(data["data"]) > 0:
            image_url = data["data"][0].get("url")
            b64_json = data["data"][0].get("b64_json")
            
            if b64_json:
                # 直接使用 base64 数据
                image_bytes = base64.b64decode(b64_json)
            elif image_url:
                # 下载图片
                print(f"下载图片: {image_url}")
                img_response = requests.get(image_url, timeout=30)
                img_response.raise_for_status()
                image_bytes = img_response.content
            else:
                print("错误: 响应中未找到图片数据")
                print(f"完整响应: {json.dumps(data, indent=2, ensure_ascii=False)}")
                sys.exit(1)
            
            # 保存图片
            output_file = Path(filename)
            output_file.parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_file, "wb") as f:
                f.write(image_bytes)
            
            print(f"✅ 图片已成功生成并保存到: {filename}")
            return filename
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


def generate_with_chat_format(
    prompt,
    filename,
    input_images=None,
    resolution=None,
    api_key=None,
    base_url=None,
):
    """
    使用 Chat Completions 格式生成/编辑图片
    """
    api_key = get_api_key(api_key)
    base_url = get_base_url(base_url)
    
    url = f"{base_url}/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # 构建消息内容
    content = []
    
    # 添加输入图片（如果有）
    if input_images:
        for img_path in input_images:
            if not os.path.exists(img_path):
                print(f"错误: 输入图片不存在: {img_path}")
                sys.exit(1)
            
            img_base64 = encode_image_to_base64(img_path)
            content.append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/png;base64,{img_base64}"
                }
            })
    
    # 添加提示词
    content.append({
        "type": "text",
        "text": prompt
    })
    
    payload = {
        "model": "gpt-4o",  # 或其他支持视觉的模型
        "messages": [
            {
                "role": "user",
                "content": content
            }
        ],
        "max_tokens": 1000
    }
    
    mode_str = "编辑图片" if input_images else "生成图片"
    print(f"正在{mode_str}...")
    print(f"提示词: {prompt}")
    if input_images:
        print(f"输入图片: {len(input_images)} 张")
    print(f"API: {url}")
    print()
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=120)
        response.raise_for_status()
        
        data = response.json()
        
        # 解析响应
        if "choices" in data and len(data["choices"]) > 0:
            reply = data["choices"][0]["message"]["content"]
            print(f"模型回复: {reply}")
            
            # 注意：Chat 格式可能不直接返回图片
            # 这里只是示例，实际需要根据 API 的具体实现调整
            print("\n⚠️  注意: Chat 格式可能不支持直接生成图片")
            print("建议使用 DALL-E 格式（不带 -i 参数）")
            return None
        else:
            print("错误: 响应格式不正确")
            print(f"完整响应: {json.dumps(data, indent=2, ensure_ascii=False)}")
            sys.exit(1)
    
    except requests.exceptions.RequestException as e:
        print(f"错误: 请求失败 - {e}")
        if hasattr(e, "response") and e.response is not None:
            print(f"状态码: {e.response.status_code}")
            print(f"响应内容: {e.response.text[:500]}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="基于中转 API 的图片生成工具（适配版）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用示例:

【生成新图片】
    python generate_image_proxy.py -p "一只可爱的橘猫"
    python generate_image_proxy.py -p "日落山脉" -r 2K
    python generate_image_proxy.py -p "城市夜景" -r 4K -f wallpaper.png

【编辑已有图片（实验性）】
    python generate_image_proxy.py -p "转换成油画风格" -i original.png
    python generate_image_proxy.py -p "添加彩虹到天空" -i photo.jpg -f edited.png

【API 配置】
  默认 API: https://api.nextaicore.com/openai
  默认 Key: sk-iuRXquaxhd9Xc5wya9VdgrGvw2UwgvlBmkSnqOtLRp50vinp
  
  可通过环境变量覆盖:
    export PROXY_API_KEY="your-key"
    export PROXY_BASE_URL="https://your-api.com"
        """,
    )
    
    parser.add_argument("--prompt", "-p", required=True, help="图片描述或编辑指令")
    parser.add_argument("--filename", "-f", default=None, help="输出图片路径")
    parser.add_argument(
        "--resolution", "-r",
        default=None,
        choices=SUPPORTED_RESOLUTIONS,
        help="图片分辨率 (1K, 2K, 4K)"
    )
    parser.add_argument(
        "--input-image", "-i",
        nargs="+",
        default=None,
        help="输入图片路径（编辑模式）"
    )
    parser.add_argument("--api-key", "-k", default=None, help="API 密钥")
    parser.add_argument("--base-url", "-u", default=None, help="API 基础 URL")
    
    args = parser.parse_args()
    
    run_timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    
    # 生成文件名
    if args.filename is None:
        args.filename = generate_filename(args.prompt)
    else:
        out_path = Path(args.filename)
        if out_path.exists():
            adjusted = add_timestamp_to_filename(args.filename, run_timestamp)
            print(f"⚠️  输出文件已存在，改为: {adjusted}")
            args.filename = adjusted
    
    # 选择生成方式
    if args.input_image:
        # 图生图：使用 Chat 格式（实验性）
        print("⚠️  图生图功能为实验性，可能不被支持")
        generate_with_chat_format(
            prompt=args.prompt,
            filename=args.filename,
            input_images=args.input_image,
            resolution=args.resolution,
            api_key=args.api_key,
            base_url=args.base_url,
        )
    else:
        # 文生图：使用 DALL-E 格式
        generate_with_dalle_format(
            prompt=args.prompt,
            filename=args.filename,
            resolution=args.resolution,
            api_key=args.api_key,
            base_url=args.base_url,
        )


if __name__ == "__main__":
    main()

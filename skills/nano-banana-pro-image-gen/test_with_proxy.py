#!/usr/bin/env python3
"""
使用中转 API 测试图片生成
支持 OpenAI 兼容格式的 API
"""

import os
import sys
import requests
import base64
from pathlib import Path

# API 配置
API_KEY = "sk-iuRXquaxhd9Xc5wya9VdgrGvw2UwgvlBmkSnqOtLRp50vinp"
BASE_URL = "https://api.nextaicore.com/openai"

def test_chat_completion():
    """测试基础对话功能"""
    print("🧪 测试1：基础对话功能")
    print("=" * 50)
    
    url = f"{BASE_URL}/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "gpt-4o-mini",  # 或其他可用模型
        "messages": [
            {
                "role": "user",
                "content": "你好，请用一句话介绍你自己"
            }
        ],
        "max_tokens": 100
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        
        print(f"状态码: {response.status_code}")
        print(f"响应头: {dict(response.headers)}")
        print(f"响应内容（前500字符）: {response.text[:500]}")
        print()
        
        response.raise_for_status()
        result = response.json()
        
        print(f"✅ 模型: {result.get('model', 'N/A')}")
        print(f"✅ 回复: {result['choices'][0]['message']['content']}")
        print()
        return True
        
    except Exception as e:
        print(f"❌ 错误: {e}")
        print()
        return False


def test_image_generation():
    """测试图片生成功能（如果支持）"""
    print("🧪 测试2：图片生成功能")
    print("=" * 50)
    
    # 尝试 DALL-E 格式
    url = f"{BASE_URL}/v1/images/generations"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "dall-e-3",
        "prompt": "一只可爱的橙色猫咪在草地上玩耍",
        "n": 1,
        "size": "1024x1024"
    }
    
    try:
        response = requests.post(url, headers=headers, json=data, timeout=60)
        response.raise_for_status()
        result = response.json()
        
        print(f"✅ 状态码: {response.status_code}")
        
        if 'data' in result and len(result['data']) > 0:
            image_url = result['data'][0].get('url')
            if image_url:
                print(f"✅ 图片 URL: {image_url}")
                
                # 下载图片
                img_response = requests.get(image_url)
                if img_response.status_code == 200:
                    output_path = Path("test_output/proxy_test_image.png")
                    output_path.parent.mkdir(parents=True, exist_ok=True)
                    output_path.write_bytes(img_response.content)
                    print(f"✅ 图片已保存: {output_path.resolve()}")
                    print()
                    return True
        
        print(f"⚠️  响应格式: {result}")
        print()
        return False
        
    except Exception as e:
        print(f"❌ 图片生成不支持或出错: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"响应内容: {e.response.text}")
        print()
        return False


def test_vision_api():
    """测试视觉理解功能"""
    print("🧪 测试3：视觉理解功能")
    print("=" * 50)
    
    url = f"{BASE_URL}/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    # 使用一个简单的测试图片 URL
    test_image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/1200px-Cat03.jpg"
    
    data = {
        "model": "gpt-4o-mini",  # 或支持视觉的模型
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "这张图片里有什么？"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": test_image_url
                        }
                    }
                ]
            }
        ],
        "max_tokens": 200
    }
    
    try:
        response = requests.post(url, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        result = response.json()
        
        print(f"✅ 状态码: {response.status_code}")
        print(f"✅ 回复: {result['choices'][0]['message']['content']}")
        print()
        return True
        
    except Exception as e:
        print(f"❌ 视觉功能不支持或出错: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"响应内容: {e.response.text}")
        print()
        return False


def list_available_models():
    """列出可用的模型"""
    print("🧪 测试4：列出可用模型")
    print("=" * 50)
    
    url = f"{BASE_URL}/v1/models"
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        result = response.json()
        
        print(f"✅ 状态码: {response.status_code}")
        
        if 'data' in result:
            print(f"✅ 可用模型数量: {len(result['data'])}")
            print("\n可用模型列表：")
            for model in result['data'][:10]:  # 只显示前10个
                model_id = model.get('id', 'N/A')
                print(f"  - {model_id}")
            
            if len(result['data']) > 10:
                print(f"  ... 还有 {len(result['data']) - 10} 个模型")
        else:
            print(f"⚠️  响应格式: {result}")
        
        print()
        return True
        
    except Exception as e:
        print(f"❌ 错误: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"响应内容: {e.response.text}")
        print()
        return False


def main():
    print("🚀 中转 API 测试脚本")
    print("=" * 50)
    print(f"API Endpoint: {BASE_URL}")
    print(f"API Key: {API_KEY[:20]}...")
    print()
    
    results = []
    
    # 测试1：基础对话
    results.append(("基础对话", test_chat_completion()))
    
    # 测试2：图片生成
    results.append(("图片生成", test_image_generation()))
    
    # 测试3：视觉理解
    results.append(("视觉理解", test_vision_api()))
    
    # 测试4：列出模型
    results.append(("列出模型", list_available_models()))
    
    # 总结
    print("=" * 50)
    print("📊 测试总结")
    print("=" * 50)
    
    for test_name, success in results:
        status = "✅ 通过" if success else "❌ 失败"
        print(f"{test_name}: {status}")
    
    print()
    
    passed = sum(1 for _, success in results if success)
    total = len(results)
    print(f"总计: {passed}/{total} 测试通过")
    
    if passed > 0:
        print("\n✅ API 可用！")
        print("\n💡 建议：")
        print("1. 如果支持对话功能，可以用于 OpenClaw 的基础对话")
        print("2. 如果支持图片生成，可以集成到图片生成工作流")
        print("3. 如果支持视觉理解，可以用于图片分析")
    else:
        print("\n❌ 所有测试都失败了")
        print("\n💡 建议：")
        print("1. 检查 API Key 是否正确")
        print("2. 检查 API Endpoint 是否正确")
        print("3. 检查网络连接")
        print("4. 联系 API 提供商确认服务状态")


if __name__ == "__main__":
    main()

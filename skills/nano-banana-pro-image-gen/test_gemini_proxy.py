#!/usr/bin/env python3
"""
测试通过中转 API 使用 Gemini 3 Pro Image 模型
"""

import os
import sys
import requests
import json
from pathlib import Path

# API 配置
API_KEY = "sk-iuRXquaxhd9Xc5wya9VdgrGvw2UwgvlBmkSnqOtLRp50vinp"
BASE_URL = "https://api.nextaicore.com/openai"

def test_gemini_image_generation():
    """测试 Gemini 3 Pro Image 生成"""
    print("🧪 测试 Gemini 3 Pro Image 模型")
    print("=" * 60)
    
    # 方式1：尝试 OpenAI 兼容格式
    print("\n方式1：OpenAI 兼容格式（DALL-E 风格）")
    print("-" * 60)
    
    url = f"{BASE_URL}/v1/images/generations"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "gemini-3-pro-image-preview",
        "prompt": "一只可爱的橙色猫咪在草地上玩耍，阳光明媚，高清摄影",
        "n": 1,
        "size": "1024x1024"
    }
    
    try:
        print(f"请求 URL: {url}")
        print(f"请求数据: {json.dumps(data, ensure_ascii=False, indent=2)}")
        print()
        
        response = requests.post(url, headers=headers, json=data, timeout=60)
        
        print(f"状态码: {response.status_code}")
        print(f"响应头: Content-Type = {response.headers.get('Content-Type')}")
        print(f"响应内容（前1000字符）:")
        print(response.text[:1000])
        print()
        
        if response.status_code == 200:
            result = response.json()
            
            if 'data' in result and len(result['data']) > 0:
                image_url = result['data'][0].get('url')
                if image_url:
                    print(f"✅ 图片 URL: {image_url}")
                    
                    # 下载图片
                    img_response = requests.get(image_url)
                    if img_response.status_code == 200:
                        output_path = Path("test_output/gemini_proxy_test.png")
                        output_path.parent.mkdir(parents=True, exist_ok=True)
                        output_path.write_bytes(img_response.content)
                        print(f"✅ 图片已保存: {output_path.resolve()}")
                        return True
            
            print(f"完整响应: {json.dumps(result, ensure_ascii=False, indent=2)}")
        
    except Exception as e:
        print(f"❌ 方式1失败: {e}")
    
    print()
    
    # 方式2：尝试 Chat Completions 格式（带图片生成）
    print("\n方式2：Chat Completions 格式")
    print("-" * 60)
    
    url = f"{BASE_URL}/v1/chat/completions"
    
    data = {
        "model": "gemini-3-pro-image-preview",
        "messages": [
            {
                "role": "user",
                "content": "生成一张图片：一只可爱的橙色猫咪在草地上玩耍，阳光明媚，高清摄影"
            }
        ],
        "max_tokens": 1000
    }
    
    try:
        print(f"请求 URL: {url}")
        print(f"请求数据: {json.dumps(data, ensure_ascii=False, indent=2)}")
        print()
        
        response = requests.post(url, headers=headers, json=data, timeout=60)
        
        print(f"状态码: {response.status_code}")
        print(f"响应头: Content-Type = {response.headers.get('Content-Type')}")
        print(f"响应内容（前1000字符）:")
        print(response.text[:1000])
        print()
        
        if response.status_code == 200:
            result = response.json()
            print(f"完整响应: {json.dumps(result, ensure_ascii=False, indent=2)}")
            
            # 检查是否有图片数据
            if 'choices' in result and len(result['choices']) > 0:
                content = result['choices'][0].get('message', {}).get('content', '')
                print(f"\n回复内容: {content}")
                return True
        
    except Exception as e:
        print(f"❌ 方式2失败: {e}")
    
    print()
    return False


def test_list_models():
    """列出可用模型，查找 Gemini 相关模型"""
    print("\n🧪 查找可用的 Gemini 模型")
    print("=" * 60)
    
    url = f"{BASE_URL}/v1/models"
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=30)
        
        print(f"状态码: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            
            if 'data' in result:
                all_models = [m.get('id', '') for m in result['data']]
                gemini_models = [m for m in all_models if 'gemini' in m.lower()]
                image_models = [m for m in all_models if 'image' in m.lower() or 'dall' in m.lower()]
                
                print(f"\n✅ 总模型数: {len(all_models)}")
                
                if gemini_models:
                    print(f"\n✅ Gemini 相关模型 ({len(gemini_models)} 个):")
                    for model in gemini_models:
                        print(f"  - {model}")
                else:
                    print("\n⚠️  未找到 Gemini 模型")
                
                if image_models:
                    print(f"\n✅ 图片相关模型 ({len(image_models)} 个):")
                    for model in image_models[:10]:
                        print(f"  - {model}")
                else:
                    print("\n⚠️  未找到图片生成模型")
                
                # 显示所有模型（前20个）
                print(f"\n📋 所有可用模型（前20个）:")
                for model in all_models[:20]:
                    print(f"  - {model}")
                
                if len(all_models) > 20:
                    print(f"  ... 还有 {len(all_models) - 20} 个模型")
                
                return True
            else:
                print(f"响应格式: {response.text[:500]}")
        else:
            print(f"错误响应: {response.text[:500]}")
        
    except Exception as e:
        print(f"❌ 错误: {e}")
    
    print()
    return False


def test_basic_chat():
    """测试基础对话功能"""
    print("\n🧪 测试基础对话（验证 API 可用性）")
    print("=" * 60)
    
    url = f"{BASE_URL}/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    # 尝试几个常见模型
    models_to_try = [
        "gpt-4o-mini",
        "gpt-3.5-turbo",
        "gemini-pro",
        "gemini-1.5-flash"
    ]
    
    for model in models_to_try:
        print(f"\n尝试模型: {model}")
        print("-" * 40)
        
        data = {
            "model": model,
            "messages": [
                {
                    "role": "user",
                    "content": "你好，请回复'测试成功'"
                }
            ],
            "max_tokens": 50
        }
        
        try:
            response = requests.post(url, headers=headers, json=data, timeout=30)
            
            print(f"状态码: {response.status_code}")
            
            if response.status_code == 200:
                result = response.json()
                reply = result['choices'][0]['message']['content']
                print(f"✅ 回复: {reply}")
                print(f"✅ 模型 {model} 可用！")
                return True
            else:
                print(f"⚠️  失败: {response.text[:200]}")
        
        except Exception as e:
            print(f"⚠️  错误: {str(e)[:200]}")
    
    print()
    return False


def main():
    print("🚀 Gemini 3 Pro Image 中转 API 测试")
    print("=" * 60)
    print(f"API Endpoint: {BASE_URL}")
    print(f"API Key: {API_KEY[:20]}...")
    print(f"目标模型: gemini-3-pro-image-preview")
    print()
    
    # 测试1：基础对话（验证 API 可用）
    api_works = test_basic_chat()
    
    if not api_works:
        print("\n❌ API 基础功能不可用，请检查：")
        print("1. API Key 是否正确")
        print("2. API Endpoint 是否正确")
        print("3. 网络连接是否正常")
        return
    
    # 测试2：列出模型
    test_list_models()
    
    # 测试3：Gemini 图片生成
    success = test_gemini_image_generation()
    
    # 总结
    print("\n" + "=" * 60)
    print("📊 测试总结")
    print("=" * 60)
    
    if success:
        print("✅ Gemini 3 Pro Image 模型可用！")
        print("\n💡 下一步：")
        print("1. 查看生成的图片: open test_output/gemini_proxy_test.png")
        print("2. 集成到 OpenClaw 工作流")
        print("3. 编写第10章的实战案例")
    else:
        print("⚠️  Gemini 3 Pro Image 模型测试未成功")
        print("\n💡 可能的原因：")
        print("1. 该中转 API 不支持 gemini-3-pro-image-preview 模型")
        print("2. 需要使用不同的 API 格式")
        print("3. 需要使用 Google 官方 API")
        print("\n💡 建议：")
        print("1. 联系 API 提供商确认支持的模型")
        print("2. 查看 API 文档了解正确的调用方式")
        print("3. 考虑使用 Google 官方 Gemini API")


if __name__ == "__main__":
    main()

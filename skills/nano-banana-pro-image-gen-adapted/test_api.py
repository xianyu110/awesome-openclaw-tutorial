#!/usr/bin/env python3
"""
测试中转 API 的各种功能
"""

import requests
import json

API_KEY = "sk-iuRXquaxhd9Xc5wya9VdgrGvw2UwgvlBmkSnqOtLRp50vinp"
BASE_URL = "https://api.nextaicore.com/openai"

def test_chat():
    """测试基础对话"""
    print("=" * 60)
    print("测试1：基础对话功能")
    print("=" * 60)
    
    url = f"{BASE_URL}/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": "你好，请回复'测试成功'"}
        ]
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        print(f"状态码: {response.status_code}")
        print(f"响应头: {response.headers.get('Content-Type')}")
        print(f"响应内容: {response.text[:500]}")
        print()
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ 对话成功")
            print(f"回复: {data['choices'][0]['message']['content']}")
            return True
    except Exception as e:
        print(f"❌ 失败: {e}")
    
    print()
    return False


def test_image_generation():
    """测试图片生成"""
    print("=" * 60)
    print("测试2：图片生成功能（DALL-E 格式）")
    print("=" * 60)
    
    url = f"{BASE_URL}/v1/images/generations"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "dall-e-3",
        "prompt": "一只可爱的橙色猫咪",
        "n": 1,
        "size": "1024x1024"
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=60)
        print(f"状态码: {response.status_code}")
        print(f"响应头: {response.headers.get('Content-Type')}")
        print(f"响应内容: {response.text[:500]}")
        print()
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ 图片生成成功")
            if "data" in data:
                print(f"图片数量: {len(data['data'])}")
            return True
    except Exception as e:
        print(f"❌ 失败: {e}")
    
    print()
    return False


def test_models():
    """测试列出模型"""
    print("=" * 60)
    print("测试3：列出可用模型")
    print("=" * 60)
    
    url = f"{BASE_URL}/v1/models"
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=30)
        print(f"状态码: {response.status_code}")
        print(f"响应头: {response.headers.get('Content-Type')}")
        print(f"响应内容: {response.text[:500]}")
        print()
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ 获取模型列表成功")
            if "data" in data:
                print(f"模型数量: {len(data['data'])}")
                print("前10个模型:")
                for model in data['data'][:10]:
                    print(f"  - {model.get('id', 'N/A')}")
            return True
    except Exception as e:
        print(f"❌ 失败: {e}")
    
    print()
    return False


def main():
    print("🚀 中转 API 功能测试")
    print(f"API: {BASE_URL}")
    print(f"Key: {API_KEY[:20]}...")
    print()
    
    results = []
    
    # 测试1：基础对话
    results.append(("基础对话", test_chat()))
    
    # 测试2：图片生成
    results.append(("图片生成", test_image_generation()))
    
    # 测试3：列出模型
    results.append(("列出模型", test_models()))
    
    # 总结
    print("=" * 60)
    print("📊 测试总结")
    print("=" * 60)
    for name, success in results:
        status = "✅ 通过" if success else "❌ 失败"
        print(f"{name}: {status}")
    
    passed = sum(1 for _, s in results if s)
    print(f"\n总计: {passed}/{len(results)} 测试通过")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""清理配置文件中的敏感信息"""

import json
import os
import shutil
from pathlib import Path

# 定义替换规则
REPLACEMENTS = {
    # API Keys
    "sk-OvxDWsdaruoqDFSP8o4MDxjY9rVg8kDJ6g7Oe67VN1ATw8mb": "sk-YOUR_HUNYUAN_API_KEY_HERE",
    "sk-kazAk58RoPM6y2VSsSFMMNmIYBHVOEJGjzElzIUogZeNJXxE": "sk-YOUR_MAYNOR_API_KEY_HERE",
    "sk-123456": "sk-YOUR_LOCAL_API_KEY_HERE",
    "BSAFC-veOYMSrOHCyqVlrbyv4rbVr3M": "YOUR_WEB_SEARCH_API_KEY_HERE",
    
    # App IDs
    "cli_a907e647c638dcd1": "cli_YOUR_BOT1_APP_ID_HERE",
    "cli_a9f4681e68f8dceb": "cli_YOUR_BOT2_APP_ID_HERE",
    "cli_a907c3e5c9389ccd": "cli_YOUR_BOT3_APP_ID_HERE",
    "cli_a9073ca406b85cd5": "cli_YOUR_BOT4_APP_ID_HERE",
    
    # App Secrets
    "GXETUaRKmYzcYQsrqxgRWc6OkDBrrHts": "YOUR_BOT1_APP_SECRET_HERE",
    "UlT0Ex4P1IGfOvy7yDoPwfNwHd2RD6YE": "YOUR_BOT2_APP_SECRET_HERE",
    "jJKzVfKVSHW0RPChE4swShGYXXJahlY7": "YOUR_BOT3_APP_SECRET_HERE",
    "7VjDSIzCwHH3bvA2c0U4fgqOGBe47LSy": "YOUR_BOT4_APP_SECRET_HERE",
    
    # Gateway Token
    "0f71e422ee78bf2667a4caae547ba56b8c00f8434bbbab1c": "YOUR_SECURE_GATEWAY_TOKEN_HERE",
    
    # User IDs
    "ou_18d36d8a49c010dfe20ace2a29250c04": "ou_YOUR_MAIN_ASSISTANT_USER_ID",
    "ou_277fc698d99aeb954b15f41d2a58eafc": "ou_YOUR_CONTENT_CREATOR_USER_ID",
    "ou_d29b74e6ddc0825372b7aedf6b843aeb": "ou_YOUR_TECH_DEV_USER_ID",
    "ou_e3bf80db7f4b8cc72335131b5a6dca44": "ou_YOUR_AI_NEWS_USER_ID",
    
    # Base URLs
    "http://49.51.195.85:8045/v1": "http://YOUR_LOCAL_SERVER_IP:PORT/v1",
    "https://apipro.maynor1024.live": "https://YOUR_API_PROXY_URL",
    
    # Workspace paths
    "/Users/chinamanor/clawd": "/Users/YOUR_USERNAME/workspace",
}

# 要处理的文件
FILES = [
    "openclaw.json",
    "我的六机器人配置.json",
    "openclaw-多Agent配置.json",
    "openclaw-4个Agent完整配置.json",
]

def clean_file(filepath):
    """清理单个文件"""
    if not os.path.exists(filepath):
        print(f"  ⚠️  文件不存在: {filepath}")
        return False
    
    # 备份原文件
    backup_path = f"{filepath}.sensitive-backup"
    shutil.copy2(filepath, backup_path)
    print(f"  📦 已备份: {backup_path}")
    
    # 读取文件内容
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 替换敏感信息
    for old, new in REPLACEMENTS.items():
        content = content.replace(old, new)
    
    # 写回文件
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✅ 已清理: {filepath}")
    return True

def main():
    print("🔒 开始清理敏感信息...\n")
    
    cleaned = []
    backed_up = []
    
    for filepath in FILES:
        if clean_file(filepath):
            cleaned.append(filepath)
            backed_up.append(f"{filepath}.sensitive-backup")
    
    print("\n✅ 清理完成！\n")
    
    if cleaned:
        print("📋 已清理的文件：")
        for f in cleaned:
            print(f"  - {f}")
    
    if backed_up:
        print("\n💾 备份文件（包含敏感信息）：")
        for f in backed_up:
            print(f"  - {f}")
    
    print("\n⚠️  重要提示：")
    print("  1. 备份文件包含敏感信息，请妥善保管")
    print("  2. 不要将备份文件提交到 Git")
    print("  3. 清理后的文件可以安全分享")
    print("  4. 如需恢复，使用备份文件")
    print()

if __name__ == "__main__":
    main()

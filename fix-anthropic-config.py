#!/usr/bin/env python3
import json
import shutil
from datetime import datetime

config_file = '/Users/chinamanor/.openclaw/agents/main/agent/auth-profiles.json'

# 备份原文件
backup_file = f"{config_file}.backup-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
shutil.copy2(config_file, backup_file)
print(f"✅ 已备份配置到: {backup_file}")

# 读取配置
with open(config_file, 'r') as f:
    config = json.load(f)

# 获取代理 key
proxy_key = config['profiles']['api-proxy-claude:default']['key']

# 添加 anthropic 配置（使用相同的代理 key）
if 'anthropic:default' not in config['profiles']:
    config['profiles']['anthropic:default'] = {
        "type": "api_key",
        "provider": "anthropic",
        "key": proxy_key
    }
    print("✅ 已添加 anthropic:default 配置")
else:
    print("⚠️  anthropic:default 配置已存在")

# 保存配置
with open(config_file, 'w') as f:
    json.dump(config, f, indent=2)

print(f"✅ 配置已更新: {config_file}")
print("\n📋 当前配置的 providers:")
for key in config['profiles'].keys():
    print(f"  - {key}")

print("\n🔄 请重启网关以应用更改:")
print("  openclaw gateway restart")

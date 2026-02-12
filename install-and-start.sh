#!/bin/bash

# 安装并启动网关

echo "🚀 安装并启动 OpenClaw 网关"
echo "==========================="
echo ""

echo "1️⃣ 安装网关服务..."
openclaw gateway install

echo ""
echo "⏳ 等待 3 秒..."
sleep 3

echo ""
echo "2️⃣ 查看网关状态..."
openclaw gateway status

echo ""
echo "✅ 安装完成！"
echo ""
echo "📋 后续操作："
echo "  - 查看实时日志: openclaw logs --follow"
echo "  - 查看飞书状态: openclaw channels status feishu"
echo "  - 查看配对请求: openclaw pairing list feishu"
echo "  - 批准配对: openclaw pairing approve feishu <配对码>"
echo ""
echo "💡 提示："
echo "  现在可以在飞书中找到你的两个机器人并发送消息测试了！"
echo ""

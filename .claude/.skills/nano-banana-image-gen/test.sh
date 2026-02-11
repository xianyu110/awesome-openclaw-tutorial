#!/bin/bash

# Nano Banana Image Generation - 测试脚本

set -e

echo "🧪 Nano Banana Image Generation - 测试脚本"
echo "=================================================="
echo ""

# 创建输出目录
TEST_OUTPUT_DIR="test_output"
mkdir -p "$TEST_OUTPUT_DIR"
echo "📁 创建测试输出目录：$TEST_OUTPUT_DIR"
echo ""

# 测试1：基础文生图
echo "🎨 测试1：基础文生图"
echo "Prompt: 画一只可爱的橙色猫咪"
echo ""

python3 scripts/generate_image.py \
    --prompt "画一只可爱的橙色猫咪，阳光明媚，高清摄影" \
    --filename "$TEST_OUTPUT_DIR/test1_cat.png"

echo ""
echo "✅ 测试1 完成"
echo ""

# 测试2：白板图
echo "🎨 测试2：白板图生成"
echo "Prompt: OpenClaw 核心概念白板图"
echo ""

python3 scripts/generate_image.py \
    --prompt "生成一张白板图片，手写字体风格，内容是OpenClaw核心概念：本地部署、文件访问、Skills扩展、多平台支持，用箭头和框图展示" \
    --filename "$TEST_OUTPUT_DIR/test2_whiteboard.png"

echo ""
echo "✅ 测试2 完成"
echo ""

# 测试3：Logo 设计
echo "🎨 测试3：Logo 设计"
echo "Prompt: AI 助手 Logo"
echo ""

python3 scripts/generate_image.py \
    --prompt "设计一个极简风格的AI机器人Logo，蓝色和白色配色，线条简洁" \
    --filename "$TEST_OUTPUT_DIR/test3_logo.png"

echo ""
echo "✅ 测试3 完成"
echo ""

# 显示测试结果
echo "=================================================="
echo "🎉 所有测试完成！"
echo ""
echo "生成的图片："
ls -lh "$TEST_OUTPUT_DIR"/*.png 2>/dev/null || echo "未找到生成的图片"
echo ""
echo "查看图片："
echo "  open $TEST_OUTPUT_DIR"
echo ""

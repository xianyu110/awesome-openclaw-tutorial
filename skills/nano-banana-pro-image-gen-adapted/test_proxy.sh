#!/bin/bash

# 中转 API 图片生成测试脚本

set -e

echo "🧪 中转 API 图片生成测试"
echo "=================================================="
echo ""
echo "API Endpoint: https://api.nextaicore.com/openai"
echo "API Key: sk-iuRXquaxhd9Xc5wya9VdgrGvw2UwgvlBmkSnqOtLRp50vinp"
echo ""

# 创建输出目录
TEST_OUTPUT_DIR="test_output"
mkdir -p "$TEST_OUTPUT_DIR"
echo "📁 创建测试输出目录：$TEST_OUTPUT_DIR"
echo ""

# 测试1：基础文生图（1K）
echo "🎨 测试1：基础文生图（1K 分辨率）"
echo "Prompt: 一只可爱的橙色猫咪在草地上玩耍"
echo ""

python3 scripts/generate_image_proxy.py \
    --prompt "一只可爱的橙色猫咪在草地上玩耍，阳光明媚，高清摄影" \
    --filename "$TEST_OUTPUT_DIR/test1_cat_1k.png" \
    --resolution 1K

echo ""
echo "✅ 测试1 完成"
echo ""

# 测试2：高分辨率文生图（2K）
echo "🎨 测试2：高分辨率文生图（2K 分辨率）"
echo "Prompt: 科技感的 AI 助手 Logo"
echo ""

python3 scripts/generate_image_proxy.py \
    --prompt "科技感的 AI 助手 Logo，蓝色主题，简约风格，现代设计" \
    --filename "$TEST_OUTPUT_DIR/test2_logo_2k.png" \
    --resolution 2K

echo ""
echo "✅ 测试2 完成"
echo ""

# 显示测试结果
echo "=================================================="
echo "🎉 测试完成！"
echo ""
echo "生成的图片："
ls -lh "$TEST_OUTPUT_DIR"/*.png 2>/dev/null || echo "未找到生成的图片"
echo ""
echo "查看图片："
echo "  open $TEST_OUTPUT_DIR"
echo ""

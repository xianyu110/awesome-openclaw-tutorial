#!/bin/bash

# Nano Banana Pro Image Generation Skill - 测试脚本
# 用于本地测试 skill 功能

set -e  # 遇到错误立即退出

echo "🧪 Nano Banana Pro Image Generation Skill - 测试脚本"
echo "=================================================="
echo ""

# 检查环境变量
if [ -z "$GEMINI_API_KEY" ]; then
    echo "❌ 错误：未设置 GEMINI_API_KEY 环境变量"
    echo ""
    echo "请先设置 API Key："
    echo "  export GEMINI_API_KEY='your-api-key-here'"
    echo ""
    echo "获取 API Key："
    echo "  https://aistudio.google.com/apikey"
    exit 1
fi

echo "✅ 检测到 GEMINI_API_KEY"
echo ""

# 检查 uv 是否安装
if ! command -v uv &> /dev/null; then
    echo "❌ 错误：未安装 uv"
    echo ""
    echo "请先安装 uv："
    echo "  curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

echo "✅ 检测到 uv"
echo ""

# 创建测试输出目录
TEST_OUTPUT_DIR="test_output"
mkdir -p "$TEST_OUTPUT_DIR"
echo "📁 创建测试输出目录：$TEST_OUTPUT_DIR"
echo ""

# 测试1：基础文生图（1K）
echo "🎨 测试1：基础文生图（1K 分辨率）"
echo "Prompt: 一只可爱的橙色猫咪在草地上玩耍"
uv run generate_image.py \
    --prompt "一只可爱的橙色猫咪在草地上玩耍，阳光明媚，高清摄影" \
    --filename "$TEST_OUTPUT_DIR/test1_cat_1k.png" \
    --resolution 1K

echo ""
echo "✅ 测试1 完成"
echo ""

# 测试2：高分辨率文生图（2K）
echo "🎨 测试2：高分辨率文生图（2K 分辨率）"
echo "Prompt: 科技感的 AI 助手 Logo"
uv run generate_image.py \
    --prompt "科技感的 AI 助手 Logo，蓝色主题，简约风格，现代设计" \
    --filename "$TEST_OUTPUT_DIR/test2_logo_2k.png" \
    --resolution 2K

echo ""
echo "✅ 测试2 完成"
echo ""

# 测试3：图生图（如果测试1成功）
if [ -f "$TEST_OUTPUT_DIR/test1_cat_1k.png" ]; then
    echo "🎨 测试3：图生图编辑"
    echo "Prompt: 把猫咪变成黑色"
    uv run generate_image.py \
        --input-image "$TEST_OUTPUT_DIR/test1_cat_1k.png" \
        --prompt "把猫咪变成黑色，保持其他不变" \
        --filename "$TEST_OUTPUT_DIR/test3_black_cat.png" \
        --resolution 1K
    
    echo ""
    echo "✅ 测试3 完成"
    echo ""
fi

# 显示测试结果
echo "=================================================="
echo "🎉 所有测试完成！"
echo ""
echo "生成的图片："
ls -lh "$TEST_OUTPUT_DIR"/*.png
echo ""
echo "查看图片："
echo "  open $TEST_OUTPUT_DIR"
echo ""
echo "或者："
for file in "$TEST_OUTPUT_DIR"/*.png; do
    echo "  open \"$file\""
done

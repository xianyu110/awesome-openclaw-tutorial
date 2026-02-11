#!/bin/bash

# Banana Pro Image Gen Skill - 准备上传脚本

set -e

echo "🚀 准备上传 Banana Pro Image Generation Skill 到 skills.sh"
echo "=================================================="
echo ""

# 1. 检查必需文件
echo "📋 检查必需文件..."
required_files=(
    "skill.json"
    "README.md"
    "SKILL.md"
    "requirements.txt"
    "scripts/generate_image.py"
)

for file in "${required_files[@]}"; do
    if [ -f "$file" ]; then
        echo "  ✅ $file"
    else
        echo "  ❌ $file - 缺失！"
        exit 1
    fi
done

echo ""

# 2. 检查敏感信息
echo "🔒 检查敏感信息..."
if grep -r "sk-HoyC9xe8aB0CRC6j4EvuM0zRcN9TTYnIMjACMCeGvd95tuhQ" scripts/ 2>/dev/null; then
    echo "  ⚠️  警告：发现硬编码的 API Key！"
    echo "  请移除敏感信息后再上传"
    exit 1
else
    echo "  ✅ 未发现硬编码的敏感信息"
fi

echo ""

# 3. 创建发布包
echo "📦 创建发布包..."
RELEASE_DIR="release"
SKILL_NAME="bananapro-image-gen"

# 清理旧的发布目录
rm -rf "$RELEASE_DIR"
mkdir -p "$RELEASE_DIR/$SKILL_NAME"

# 复制文件
cp -r scripts "$RELEASE_DIR/$SKILL_NAME/"
cp skill.json "$RELEASE_DIR/$SKILL_NAME/"
cp README.md "$RELEASE_DIR/$SKILL_NAME/"
cp SKILL.md "$RELEASE_DIR/$SKILL_NAME/"
cp requirements.txt "$RELEASE_DIR/$SKILL_NAME/"
cp .gitignore "$RELEASE_DIR/$SKILL_NAME/"

# 创建 LICENSE
cat > "$RELEASE_DIR/$SKILL_NAME/LICENSE" << 'EOF'
MIT License

Copyright (c) 2026 xianyu110

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
EOF

echo "  ✅ 发布包已创建：$RELEASE_DIR/$SKILL_NAME"
echo ""

# 4. 创建压缩包
echo "📦 创建压缩包..."
cd "$RELEASE_DIR"
tar -czf "${SKILL_NAME}.tar.gz" "$SKILL_NAME"
zip -r "${SKILL_NAME}.zip" "$SKILL_NAME" > /dev/null
cd ..

echo "  ✅ ${SKILL_NAME}.tar.gz"
echo "  ✅ ${SKILL_NAME}.zip"
echo ""

# 5. 显示文件大小
echo "📊 文件大小："
du -sh "$RELEASE_DIR/${SKILL_NAME}.tar.gz"
du -sh "$RELEASE_DIR/${SKILL_NAME}.zip"
echo ""

# 6. 生成上传信息
echo "📝 生成上传信息..."
cat > "$RELEASE_DIR/UPLOAD_INFO.txt" << EOF
Banana Pro Image Generation Skill - 上传信息
================================================

Skill 名称: bananapro-image-gen
显示名称: Banana Pro Image Generation
版本: 1.0.0
作者: xianyu110
分类: Creativity

描述:
使用 Gemini 3 Pro Image 生成图片的 OpenClaw Skill，支持白板图、Logo设计、社交媒体配图等多种场景。

特点:
- 支持中文提示词
- 多种分辨率（1K/2K/4K）
- 快速响应（10-30秒）
- 成本低廉（\$0.04-0.16/张）

标签:
ai, image-generation, gemini, creative, whiteboard, logo-design, text-to-image

GitHub 仓库:
https://github.com/xianyu110/awesome-openclaw-tutorial

文档链接:
https://github.com/xianyu110/awesome-openclaw-tutorial/tree/main/.claude/.skills/bananapro-image-gen

================================================

上传步骤:

1. 访问 https://skills.sh/
2. 点击 "Submit a Skill" 或 "Add Skill"
3. 填写上述信息
4. 上传压缩包或提供 GitHub 链接
5. 提交审核

或者：

创建独立 GitHub 仓库：
1. 在 GitHub 创建新仓库：bananapro-image-gen-skill
2. 上传 release/$SKILL_NAME/ 目录下的所有文件
3. 在 skills.sh 提交 GitHub 链接

================================================
EOF

echo "  ✅ UPLOAD_INFO.txt"
echo ""

# 7. 显示下一步
echo "✅ 准备完成！"
echo ""
echo "📁 发布文件位置："
echo "  $RELEASE_DIR/$SKILL_NAME/"
echo ""
echo "📦 压缩包："
echo "  $RELEASE_DIR/${SKILL_NAME}.tar.gz"
echo "  $RELEASE_DIR/${SKILL_NAME}.zip"
echo ""
echo "📝 上传信息："
echo "  $RELEASE_DIR/UPLOAD_INFO.txt"
echo ""
echo "🚀 下一步："
echo "  1. 查看 UPLOAD_GUIDE.md 了解详细上传步骤"
echo "  2. 查看 $RELEASE_DIR/UPLOAD_INFO.txt 获取上传信息"
echo "  3. 访问 https://skills.sh/ 提交你的 Skill"
echo ""
echo "💡 提示："
echo "  - 可以直接上传压缩包"
echo "  - 或创建独立 GitHub 仓库后提交链接"
echo "  - 建议先在本地测试确保一切正常"
echo ""
echo "🎉 祝你的 Skill 发布成功！"

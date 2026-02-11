# Skills 快速开始指南

## 📦 nano-banana-pro-image-gen Skill 测试

### 第一步：安装 uv

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# 重新加载配置
source ~/.zshrc  # 或 source ~/.bashrc
```

### 第二步：获取 API Key

1. 访问 [Google AI Studio](https://aistudio.google.com/apikey)
2. 登录 Google 账号
3. 点击 "Create API Key"
4. 复制生成的 API Key

### 第三步：设置环境变量

```bash
# 临时设置（当前终端有效）
export GEMINI_API_KEY="your-api-key-here"

# 永久设置（推荐）
echo 'export GEMINI_API_KEY="your-api-key-here"' >> ~/.zshrc
source ~/.zshrc
```

### 第四步：运行测试

```bash
# 进入 skill 目录
cd skills/nano-banana-pro-image-gen

# 运行自动化测试
./test_skill.sh
```

### 预期输出

```
🧪 Nano Banana Pro Image Generation Skill - 测试脚本
==================================================

✅ 检测到 GEMINI_API_KEY
✅ 检测到 uv
📁 创建测试输出目录：test_output

🎨 测试1：基础文生图（1K 分辨率）
Prompt: 一只可爱的橙色猫咪在草地上玩耍
Generating image with resolution 1K...
✅ Image saved: /path/to/test_output/test1_cat_1k.png

🎨 测试2：高分辨率文生图（2K 分辨率）
Prompt: 科技感的 AI 助手 Logo
Generating image with resolution 2K...
✅ Image saved: /path/to/test_output/test2_logo_2k.png

🎨 测试3：图生图编辑
Prompt: 把猫咪变成黑色
Editing image with resolution 1K...
✅ Image saved: /path/to/test_output/test3_black_cat.png

==================================================
🎉 所有测试完成！

生成的图片：
-rw-r--r--  1 user  staff   245K Feb 11 10:30 test_output/test1_cat_1k.png
-rw-r--r--  1 user  staff   189K Feb 11 10:31 test_output/test2_logo_2k.png
-rw-r--r--  1 user  staff   238K Feb 11 10:32 test_output/test3_black_cat.png
```

### 第五步：查看生成的图片

```bash
# macOS
open test_output

# Linux
xdg-open test_output

# 或者直接打开单个文件
open test_output/test1_cat_1k.png
```

## 🎨 手动测试示例

### 示例1：生成社交媒体配图

```bash
uv run generate_image.py \
  --prompt "OpenClaw AI 助手教程封面，科技感，蓝色渐变背景，居中大标题" \
  --filename "social-media-cover.png" \
  --resolution 2K
```

### 示例2：生成 Logo

```bash
uv run generate_image.py \
  --prompt "极简风格的 AI 机器人 Logo，线条简洁，蓝色和白色配色" \
  --filename "logo.png" \
  --resolution 1K
```

### 示例3：编辑图片

```bash
# 先生成一张图片
uv run generate_image.py \
  --prompt "一座雪山" \
  --filename "mountain.png"

# 然后编辑它
uv run generate_image.py \
  --input-image "mountain.png" \
  --prompt "把雪山变成日落时分的金色" \
  --filename "golden-mountain.png"
```

## 🐛 常见问题排查

### 问题1：找不到 uv 命令

```bash
# 检查是否安装
which uv

# 如果没有，重新安装
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.zshrc
```

### 问题2：API Key 错误

```bash
# 检查环境变量
echo $GEMINI_API_KEY

# 如果为空，重新设置
export GEMINI_API_KEY="your-api-key-here"
```

### 问题3：网络连接失败

```bash
# 测试网络连接
curl -I https://generativelanguage.googleapis.com

# 如果失败，检查代理设置
export https_proxy=http://your-proxy:port
```

### 问题4：依赖安装失败

```bash
# 手动安装依赖
uv pip install google-genai pillow

# 或使用 pip
pip install google-genai pillow
```

## 💰 成本控制

### 免费额度

- 每月 **50 张图片**（1K 分辨率）
- 新用户 **$300 额度**

### 价格

| 分辨率 | 价格/张 | 适用场景 |
|--------|---------|----------|
| 1K | $0.04 | 社交媒体、网页 |
| 2K | $0.08 | 印刷品、海报 |
| 4K | $0.16 | 大型海报、展板 |

### 省钱技巧

1. **优先使用 1K**：日常使用足够
2. **批量生成**：一次性生成多个版本
3. **缓存结果**：保存满意的图片

## 📚 下一步

测试成功后，你可以：

1. ✅ 阅读 [SKILL.md](nano-banana-pro-image-gen/SKILL.md) 了解完整功能
2. ✅ 在 OpenClaw 中集成这个 Skill
3. ✅ 查看第10章教程学习 API 集成
4. ✅ 开发自己的自定义 Skill

## 🔗 相关资源

- [Google AI Studio](https://aistudio.google.com/)
- [Gemini API 文档](https://ai.google.dev/gemini-api/docs/image-generation)
- [OpenClaw 官方文档](https://docs.openclaw.ai/)
- [Skills Hub](https://github.com/xianyu110/awesome-openclaw-tutorial)

## 💬 需要帮助？

- GitHub Issues: [提交问题](https://github.com/xianyu110/awesome-openclaw-tutorial/issues)
- 微信公众号：无处不在的技术
- OpenClaw 交流群：[扫码加入](../../README.md#交流群)

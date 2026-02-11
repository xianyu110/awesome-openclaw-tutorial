# Nano Banana Pro Image Generation

使用 Google Gemini 3 Pro Image API 生成和编辑图片的 OpenClaw Skill。

## 功能特性

- 📝 **文生图**：根据文字描述生成图片
- 🎨 **图生图**：编辑和修改现有图片
- 📐 **多分辨率**：支持 1K、2K、4K 输出
- 🔄 **自动检测**：智能识别最佳输出分辨率

## 使用方法

### 1. 文生图（Text-to-Image）

```bash
# 基础用法
uv run generate_image.py \
  --prompt "一只可爱的橙色猫咪在草地上玩耍" \
  --filename "cat.png"

# 指定分辨率
uv run generate_image.py \
  --prompt "科技感的 AI 助手 Logo，蓝色主题，简约风格" \
  --filename "logo.png" \
  --resolution 2K
```

### 2. 图生图（Image-to-Image）

```bash
# 编辑现有图片
uv run generate_image.py \
  --prompt "把猫咪变成黑色，背景改成蓝天白云" \
  --input-image "cat.png" \
  --filename "edited-cat.png" \
  --resolution 2K
```

## 参数说明

| 参数 | 简写 | 必需 | 说明 |
|------|------|------|------|
| `--prompt` | `-p` | ✅ | 图片描述或编辑指令 |
| `--filename` | `-f` | ✅ | 输出文件名（如 output.png） |
| `--input-image` | `-i` | ❌ | 输入图片路径（用于编辑） |
| `--resolution` | `-r` | ❌ | 输出分辨率：1K/2K/4K（默认 1K） |
| `--api-key` | `-k` | ❌ | Gemini API Key（或使用环境变量） |

## 环境配置

### 1. 获取 API Key

访问 [Google AI Studio](https://aistudio.google.com/apikey) 获取免费 API Key。

### 2. 设置环境变量

```bash
# 方式1：临时设置
export GEMINI_API_KEY="your-api-key-here"

# 方式2：写入配置文件
echo 'export GEMINI_API_KEY="your-api-key-here"' >> ~/.zshrc
source ~/.zshrc
```

### 3. 安装依赖

```bash
# 使用 uv（推荐）
uv pip install google-genai pillow

# 或使用 pip
pip install google-genai pillow
```

## 实战案例

### 案例1：社交媒体配图

```bash
# 生成抖音封面
uv run generate_image.py \
  --prompt "OpenClaw AI 助手教程封面，科技感，蓝色渐变背景，居中大标题" \
  --filename "douyin-cover.png" \
  --resolution 2K
```

### 案例2：Logo 设计

```bash
# 生成 Logo
uv run generate_image.py \
  --prompt "极简风格的 AI 机器人 Logo，线条简洁，蓝色和白色配色" \
  --filename "logo-v1.png" \
  --resolution 1K
```

### 案例3：产品海报

```bash
# 生成产品海报
uv run generate_image.py \
  --prompt "iPhone 手机产品海报，白色背景，专业摄影风格，高端质感" \
  --filename "product-poster.png" \
  --resolution 4K
```

### 案例4：图片编辑

```bash
# 修改图片风格
uv run generate_image.py \
  --input-image "photo.jpg" \
  --prompt "转换为水彩画风格，保持主体不变" \
  --filename "watercolor.png" \
  --resolution 2K
```

## 在 OpenClaw 中使用

### 对话示例

```
你：帮我生成一张"AI 编程助手"的宣传图，2K 分辨率

OpenClaw：好的，我来为你生成一张 AI 编程助手的宣传图。

[调用 nano-banana-pro-image-gen skill]
- prompt: "AI programming assistant promotional image, modern tech style, blue theme, clean design"
- resolution: 2K
- filename: ai-assistant-promo.png

✅ 图片已生成：ai-assistant-promo.png
```

### 批量生成

```
你：生成 3 个不同风格的 Logo

OpenClaw：我来为你生成 3 个不同风格的 Logo。

1. 科技风格 Logo
2. 简约风格 Logo
3. 创意风格 Logo

[批量调用 skill]
✅ 已生成 3 个 Logo 文件
```

## 成本说明

### Google Gemini API 定价

| 分辨率 | 价格/张 | 说明 |
|--------|---------|------|
| 1K | $0.04 | 适合社交媒体 |
| 2K | $0.08 | 适合印刷品 |
| 4K | $0.16 | 适合大型海报 |

### 免费额度

- 每月免费生成 **50 张图片**（1K 分辨率）
- 新用户赠送 **$300 额度**

### 成本优化建议

1. **优先使用 1K 分辨率**：日常使用足够
2. **批量生成**：一次性生成多个版本
3. **缓存结果**：保存满意的图片避免重复生成

## 常见问题

### Q1: API Key 在哪里获取？

访问 [Google AI Studio](https://aistudio.google.com/apikey)，登录后即可免费获取。

### Q2: 生成失败怎么办？

检查以下几点：
- API Key 是否正确设置
- 网络连接是否正常
- Prompt 是否符合内容政策
- 是否超出免费额度

### Q3: 如何提高生成质量？

- 使用详细的 Prompt 描述
- 指定风格、颜色、构图
- 提供参考图片（图生图模式）
- 使用更高分辨率

### Q4: 支持中文 Prompt 吗？

支持！Gemini 3 Pro Image 对中文理解很好。

### Q5: 生成速度如何？

- 1K 分辨率：约 5-10 秒
- 2K 分辨率：约 10-15 秒
- 4K 分辨率：约 15-20 秒

## 技术细节

### 使用的模型

- **模型名称**：`gemini-3-pro-image-preview`
- **提供商**：Google DeepMind
- **发布时间**：2025 年 11 月

### 核心特性

- ✅ 原生 2K 分辨率输出
- ✅ 物理准确的光照
- ✅ 完美的文字渲染
- ✅ 场景规划能力
- ✅ 多步骤错误修正

## 更新日志

### v1.0.0 (2026-02-11)

- ✅ 初始版本发布
- ✅ 支持文生图和图生图
- ✅ 支持 1K/2K/4K 分辨率
- ✅ 自动分辨率检测
- ✅ 完整的错误处理

## 参考资源

- [Google Gemini API 文档](https://ai.google.dev/gemini-api/docs/image-generation)
- [Nano Banana Pro 官网](https://nanobanana-pro.com/)
- [OpenClaw Skills 文档](https://docs.openclaw.ai/skills)

## 作者

- GitHub: [@wuchubuzai2018](https://github.com/wuchubuzai2018)
- 微信公众号：无处不在的技术

## 许可证

MIT License

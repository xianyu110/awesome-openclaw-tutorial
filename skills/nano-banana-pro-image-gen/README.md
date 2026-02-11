# Nano Banana Pro Image Generation Skill

本地测试版本的 Nano Banana Pro 图片生成 Skill。

## 快速开始

### 1. 安装依赖

```bash
# 安装 uv（如果还没安装）
curl -LsSf https://astral.sh/uv/install.sh | sh

# 安装 Python 依赖
uv pip install google-genai pillow
```

### 2. 设置 API Key

```bash
# 获取 API Key
# 访问：https://aistudio.google.com/apikey

# 设置环境变量
export GEMINI_API_KEY="your-api-key-here"
```

### 3. 运行测试

```bash
cd skills/nano-banana-pro-image-gen

# 运行测试脚本
./test_skill.sh
```

## 手动测试

### 文生图

```bash
uv run generate_image.py \
  --prompt "一只可爱的橙色猫咪在草地上玩耍" \
  --filename "cat.png" \
  --resolution 1K
```

### 图生图

```bash
uv run generate_image.py \
  --input-image "cat.png" \
  --prompt "把猫咪变成黑色" \
  --filename "black-cat.png" \
  --resolution 1K
```

## 文件说明

```
skills/nano-banana-pro-image-gen/
├── SKILL.md              # 完整的 Skill 文档
├── generate_image.py     # 核心脚本
├── test_skill.sh         # 自动化测试脚本
├── README.md             # 本文件
└── test_output/          # 测试输出目录（自动创建）
```

## 测试内容

测试脚本会执行以下测试：

1. **测试1**：基础文生图（1K 分辨率）
   - Prompt: "一只可爱的橙色猫咪在草地上玩耍"
   - 输出: `test_output/test1_cat_1k.png`

2. **测试2**：高分辨率文生图（2K 分辨率）
   - Prompt: "科技感的 AI 助手 Logo"
   - 输出: `test_output/test2_logo_2k.png`

3. **测试3**：图生图编辑
   - 输入: 测试1 的输出图片
   - Prompt: "把猫咪变成黑色"
   - 输出: `test_output/test3_black_cat.png`

## 预期结果

测试成功后，你会看到：

```
🎉 所有测试完成！

生成的图片：
-rw-r--r--  1 user  staff   245K Feb 11 10:30 test_output/test1_cat_1k.png
-rw-r--r--  1 user  staff   189K Feb 11 10:31 test_output/test2_logo_2k.png
-rw-r--r--  1 user  staff   238K Feb 11 10:32 test_output/test3_black_cat.png
```

## 常见问题

### Q: 提示 "No API key provided"

**解决方案**：
```bash
export GEMINI_API_KEY="your-api-key-here"
```

### Q: 提示 "uv: command not found"

**解决方案**：
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.zshrc  # 或 source ~/.bashrc
```

### Q: 生成失败

**可能原因**：
1. API Key 无效或过期
2. 网络连接问题
3. Prompt 违反内容政策
4. 超出免费额度

**解决方案**：
- 检查 API Key 是否正确
- 确认网络连接正常
- 修改 Prompt 内容
- 查看 [Google AI Studio](https://aistudio.google.com/) 的使用情况

## 成本说明

- **1K 分辨率**：$0.04/张
- **2K 分辨率**：$0.08/张
- **4K 分辨率**：$0.16/张

**免费额度**：
- 每月 50 张图片（1K）
- 新用户 $300 额度

## 下一步

测试成功后，你可以：

1. 查看 [SKILL.md](SKILL.md) 了解完整功能
2. 在 OpenClaw 中集成这个 Skill
3. 编写自己的图片生成工作流
4. 参考第10章教程学习 API 集成

## 参考资源

- [Google Gemini API 文档](https://ai.google.dev/gemini-api/docs/image-generation)
- [Nano Banana Pro 介绍](https://higgsfield.ai/nano-banana-2-intro)
- [OpenClaw Skills 文档](https://docs.openclaw.ai/skills)

# OpenClaw+Antigravity配置完全指南：从入门到精通

这篇文章会手把手教你配置OpenClaw+Antigravity，让你的AI工具使用体验提升一个档次。

![image-20260205121018123](https://upload.maynor1024.live/file/1770264626936_image-20260205121018123.png)



## 什么是OpenClaw+Antigravity？

### OpenClaw是什么？

OpenClaw是一个开源的AI助手框架，包括：
- **Clawdbot**：核心AI助手引擎
- **ClawHub**：技能市场，提供各种扩展功能
- **多平台支持**：支持飞书、Telegram、Discord、WhatsApp等

### Antigravity Manager是什么？

Antigravity Manager是一个AI API代理工具，可以让你通过本地服务访问多个AI模型（Claude、Gemini、GPT等），统一管理API密钥和请求。

项目地址：https://github.com/lbjlaq/Antigravity-Manager

### 为什么要用这个组合？

把OpenClaw和Antigravity Manager结合使用，你可以：

- ✅ **本地部署**：所有数据在本地处理，保护隐私
- ✅ **统一管理**：一个工具管理所有AI模型
- ✅ **成本控制**：使用自己的API密钥，避免中间商加价
- ✅ **灵活切换**：随时切换不同的模型，无需修改代码
- ✅ **技能扩展**：通过ClawHub安装各种实用技能

## 前置准备

### 系统要求

- macOS 10.15+、Windows 10+、或Linux
- 至少4GB内存
- 稳定的网络连接

### 需要准备的东西

1. Antigravity Manager安装包
2. AI模型的API Key（或独享账号）
3. 基本的命令行操作能力

## 第一步：安装Antigravity Manager

### macOS用户

1. 访问[Antigravity Manager Releases](https://github.com/lbjlaq/Antigravity-Manager/releases)
2. 下载最新版本的`.dmg`文件
3. 双击`.dmg`文件，将应用拖入`Applications`文件夹
4. 打开应用（首次打开可能需要在「系统偏好设置 → 安全性与隐私」中允许）

### Windows用户

1. 访问[Antigravity Manager Releases](https://github.com/lbjlaq/Antigravity-Manager/releases)
2. 下载最新版本的`.exe`安装包
3. 运行安装程序，按照提示完成安装
4. 启动Antigravity Manager

### Linux用户

1. 访问[Antigravity Manager Releases](https://github.com/lbjlaq/Antigravity-Manager/releases)
2. 下载最新版本的`.AppImage`或`.deb`文件
3. 给予执行权限并运行：

```bash
chmod +x Antigravity-Manager-*.AppImage
./Antigravity-Manager-*.AppImage
```

### 验证安装

启动后，应用会在本地运行一个API服务，默认地址：`http://127.0.0.1:8045`

在浏览器中访问这个地址，如果能看到管理界面，说明安装成功。

## 第二步：配置AI模型账号

Antigravity Manager需要你提供AI模型的API密钥才能工作。

### 方案1：使用官方API

**Claude API**
1. 访问[Anthropic Console](https://console.anthropic.com/)
2. 注册账号并绑定信用卡
3. 创建API Key
4. 复制保存

**Gemini API**
1. 访问[Google AI Studio](https://makersuite.google.com/app/apikey)
2. 登录Google账号
3. 创建API Key
4. 复制保存

**OpenAI API**
1. 访问[OpenAI Platform](https://platform.openai.com/api-keys)
2. 注册账号并绑定信用卡
3. 创建API Key
4. 复制保存

### 方案2：购买独享账号（推荐）

如果你不想自己申请API，可以购买独享账号：

🎁 **推荐**：[Gemini 3 Pro独享账号12个月（支持反重力）](http://maynorai.tqfk.xyz/item/23)

**优势：**
- ✅ 独享账号，无需担心限流
- ✅ 支持Antigravity Manager
- ✅ 12个月有效期
- ✅ 性价比高
- ✅ 即买即用

### 在Antigravity Manager中配置API Key

1. 打开Antigravity Manager管理界面
2. 点击「API Keys」
3. 选择对应的AI服务商（Claude、Gemini、OpenAI）
4. 输入API Key
5. 点击「保存」

## 第三步：生成User Token

User Token是Clawdbot访问Antigravity Manager的凭证。

1. 在Antigravity Manager界面中，点击右上角「User Tokens」
2. 点击「创建新Token」
3. 复制生成的Token（例如：`sk-82bc103b51f24af888af525a7835e87c`）
4. ⚠️ **重要**：妥善保存这个Token，它只会显示一次！

## 第四步：配置Clawdbot

### 配置Claude Sonnet 4.5（默认模型）

这是最常用的模型，适合日常对话和代码生成。

```bash
# 添加local-anthropic provider
cat ~/.clawdbot/clawdbot.json | jq '.models.providers["local-anthropic"] = {
  "baseUrl": "http://127.0.0.1:8045",
  "apiKey": "你的User_Token",
  "auth": "api-key",
  "api": "anthropic-messages",
  "models": [
    {
      "id": "claude-sonnet-4-5-20250929",
      "name": "Local Claude Sonnet 4.5",
      "reasoning": false,
      "input": ["text"],
      "cost": {
        "input": 0,
        "output": 0,
        "cacheRead": 0,
        "cacheWrite": 0
      },
      "contextWindow": 200000,
      "maxTokens": 8192
    }
  ]
}' > /tmp/clawdbot-temp.json && mv /tmp/clawdbot-temp.json ~/.clawdbot/clawdbot.json

# 设置为默认模型
clawdbot config set agents.defaults.model.primary "local-anthropic/claude-sonnet-4-5-20250929"
```

**注意**：把`你的User_Token`替换成第三步生成的Token。

### 配置Claude Opus 4.5 Thinking（推理模型）

这是Claude的推理模型，适合复杂问题和深度思考。

```bash
cat ~/.clawdbot/clawdbot.json | jq '.models.providers["local-anthropic-opus"] = {
  "baseUrl": "http://127.0.0.1:8045",
  "apiKey": "你的User_Token",
  "auth": "api-key",
  "api": "anthropic-messages",
  "models": [
    {
      "id": "claude-opus-4-5-thinking",
      "name": "Local Claude Opus 4.5 Thinking",
      "reasoning": true,
      "input": ["text"],
      "cost": {
        "input": 0,
        "output": 0,
        "cacheRead": 0,
        "cacheWrite": 0
      },
      "contextWindow": 200000,
      "maxTokens": 8192
    }
  ]
}' > /tmp/clawdbot-temp.json && mv /tmp/clawdbot-temp.json ~/.clawdbot/clawdbot.json
```

### 配置Gemini 3 Pro Image（多模态模型）

这是Google的多模态模型，支持图片识别和分析。

```bash
cat ~/.clawdbot/clawdbot.json | jq '.models.providers["local-google"] = {
  "baseUrl": "http://127.0.0.1:8045/v1beta",
  "apiKey": "你的User_Token",
  "auth": "api-key",
  "api": "google-generative-ai",
  "models": [
    {
      "id": "gemini-3-pro-image",
      "name": "Local Gemini 3 Pro Image",
      "reasoning": false,
      "input": ["text", "image"],
      "cost": {
        "input": 0,
        "output": 0,
        "cacheRead": 0,
        "cacheWrite": 0
      },
      "contextWindow": 2000000,
      "maxTokens": 8192
    }
  ]
}' > /tmp/clawdbot-temp.json && mv /tmp/clawdbot-temp.json ~/.clawdbot/clawdbot.json
```

## 第五步：验证配置

### 检查模型列表

```bash
clawdbot models list
```

你应该看到：

```
Model                                      Input      Ctx      Local Auth  Tags
local-anthropic/claude-sonnet-4-5-20250929 text       195k     yes   yes   default
local-anthropic-opus/claude-opus-4-5-thinking text    195k     yes   yes   configured
local-google/gemini-3-pro-image            text,image 1953k    yes   yes   configured
```

### 重启Gateway

```bash
clawdbot gateway restart
```

### 测试连接

```bash
clawdbot message send "你好，介绍一下你自己"
```

如果能正常返回回复，说明配置成功。

## 使用方法

### 使用默认模型（Claude Sonnet 4.5）

直接发送消息即可：

```bash
clawdbot message send "写一个Python脚本，打印Hello World"
```

### 切换到Opus Thinking模型

适合需要深度思考的复杂问题：

```bash
clawdbot config set agents.defaults.model.primary "local-anthropic-opus/claude-opus-4-5-thinking"
clawdbot gateway restart
```

### 切换到Gemini Image模型

适合需要图片识别的场景：

```bash
clawdbot config set agents.defaults.model.primary "local-google/gemini-3-pro-image"
clawdbot gateway restart
```

### 临时使用特定模型

不修改默认配置，临时使用某个模型：

```bash
# 使用Opus Thinking
clawdbot agent --model "local-anthropic-opus/claude-opus-4-5-thinking" --message "解释量子计算的原理"

# 使用Gemini Image
clawdbot agent --model "local-google/gemini-3-pro-image" --message "分析这张图片" --image ./photo.jpg
```

## 模型选择指南

### Claude Sonnet 4.5

**适用场景：**
- 日常对话
- 代码生成
- 文档编写
- 快速问答

**特点：**
- 速度快
- 成本低
- 质量高
- 上下文窗口：200k tokens

### Claude Opus 4.5 Thinking

**适用场景：**
- 复杂推理
- 数学问题
- 算法优化
- 深度分析

**特点：**
- 推理能力强
- 思考过程可见
- 适合复杂问题
- 上下文窗口：200k tokens

### Gemini 3 Pro Image

**适用场景：**
- 图片识别
- 多模态任务
- 文档分析
- 设计评审

**特点：**
- 支持图片输入
- 超大上下文窗口
- 识别准确
- 上下文窗口：2000k tokens

## 高级配置

### 配置模型别名

给模型起一个好记的名字：

```bash
clawdbot config set agents.defaults.models."local-anthropic/claude-sonnet-4-5-20250929".alias "我的Claude"
```

### 添加多个API Key

如果你有多个Antigravity账号，可以配置多个provider：

```bash
cat ~/.clawdbot/clawdbot.json | jq '.models.providers["local-anthropic-2"] = {
  "baseUrl": "http://127.0.0.1:8045",
  "apiKey": "另一个User_Token",
  "auth": "api-key",
  "api": "anthropic-messages",
  "models": [...]
}' > /tmp/clawdbot-temp.json && mv /tmp/clawdbot-temp.json ~/.clawdbot/clawdbot.json
```

### 配置成本追踪

虽然本地API成本为0，但你可以设置虚拟成本来追踪使用量：

```json
{
  "cost": {
    "input": 0.003,
    "output": 0.015,
    "cacheRead": 0.0003,
    "cacheWrite": 0.00375
  }
}
```

### 备份配置

```bash
cp ~/.clawdbot/clawdbot.json ~/.clawdbot/clawdbot.json.backup
```

### 恢复配置

```bash
cp ~/.clawdbot/clawdbot.json.backup ~/.clawdbot/clawdbot.json
clawdbot gateway restart
```

## 常用命令速查

```bash
# 查看模型列表
clawdbot models list

# 查看当前默认模型
clawdbot config get agents.defaults.model.primary

# 切换默认模型
clawdbot config set agents.defaults.model.primary "模型ID"

# 重启Gateway
clawdbot gateway restart

# 查看配置文件
cat ~/.clawdbot/clawdbot.json | jq '.models.providers'

# 发送消息
clawdbot message send "你的消息"

# 临时使用特定模型
clawdbot agent --model "模型ID" --message "你的消息"
```

## 模型ID速查

```
local-anthropic/claude-sonnet-4-5-20250929
local-anthropic-opus/claude-opus-4-5-thinking
local-google/gemini-3-pro-image
```

## 故障排查

### 问题1：模型列表为空

**原因**：配置文件格式错误或路径不对

**解决方法**：
```bash
# 检查配置文件
cat ~/.clawdbot/clawdbot.json | jq '.models.providers'

# 如果返回错误，恢复备份
cp ~/.clawdbot/clawdbot.json.backup ~/.clawdbot/clawdbot.json
```

### 问题2：API连接失败

**原因**：Antigravity Manager未启动或端口被占用

**解决方法**：
```bash
# 检查API是否正常
curl http://127.0.0.1:8045/v1/models

# 检查端口占用（macOS/Linux）
lsof -i :8045

# 重启Antigravity Manager
```

### 问题3：配置后模型不生效

**原因**：忘记重启Gateway

**解决方法**：
```bash
clawdbot gateway restart
```

### 问题4：User Token无效

**原因**：Token过期或输入错误

**解决方法**：
1. 在Antigravity Manager中重新生成Token
2. 更新配置文件中的apiKey
3. 重启Gateway

## 相关资源

### OpenClaw生态
- **Clawdbot官方文档**：https://docs.clawd.bot
- **ClawHub技能市场**：https://hub.openclaw.org
- **OpenClaw GitHub**：https://github.com/clawdbot/clawdbot

### Antigravity Manager
- **项目地址**：https://github.com/lbjlaq/Antigravity-Manager
- **下载最新版本**：https://github.com/lbjlaq/Antigravity-Manager/releases

### API账号获取
- **官方Claude API**：https://console.anthropic.com/
- **官方Gemini API**：https://makersuite.google.com/app/apikey
- **官方OpenAI API**：https://platform.openai.com/api-keys
- **独享账号推荐**：[Gemini 3 Pro独享12个月（支持反重力）](http://maynorai.tqfk.xyz/item/23)

## 总结

完成以上步骤后，你的OpenClaw+Antigravity Manager就配置完成了。

**关键步骤回顾：**
1. ✅ 下载并安装Antigravity Manager
2. ✅ 配置AI模型的API Key
3. ✅ 生成User Token
4. ✅ 配置Clawdbot的三个模型
5. ✅ 验证配置并重启Gateway

**现在你可以：**
- 使用本地API访问多个AI模型
- 随时切换不同的模型
- 享受更快的响应速度和更低的成本
- 通过ClawHub安装各种实用技能
- 在多个平台使用你的AI助手

**下一步推荐：**
- 📚 查看ClawHub小白必装技能教程
- 🚀 查看飞书Bot配置教程
- 🌐 查看Clawdbot远程访问方案

祝你使用愉快！🦞

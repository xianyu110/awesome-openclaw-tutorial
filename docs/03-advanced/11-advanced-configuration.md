# 第11章 高级配置（多模型切换/成本优化/性能调优）

> 💡 **本章目标**：掌握OpenClaw的高级配置技巧，包括Antigravity Manager配置、多模型切换、成本优化和性能调优。

## ⚙️ 本章内容

- 11.1 Antigravity Manager完全配置指南
- 11.2 多模型切换策略
- 11.3 成本优化方案
- 11.4 性能调优技巧

---

## 11.1 Antigravity Manager完全配置指南

### 11.1.1 什么是Antigravity Manager？

**定义**：

Antigravity Manager是一个AI API代理工具，可以让你通过本地服务访问多个AI模型（Claude、Gemini、GPT等），统一管理API密钥和请求。

**项目地址**：https://github.com/lbjlaq/Antigravity-Manager

**为什么要用Antigravity Manager？**

把OpenClaw和Antigravity Manager结合使用，你可以：

- ✅ **本地部署**：所有数据在本地处理，保护隐私
- ✅ **统一管理**：一个工具管理所有AI模型
- ✅ **成本控制**：使用自己的API密钥，避免中间商加价
- ✅ **灵活切换**：随时切换不同的模型，无需修改代码
- ✅ **技能扩展**：通过ClawHub安装各种实用技能

![Antigravity Manager架构](https://upload.maynor1024.live/file/1770264626936_image-20260205121018123.png)

### 11.1.2 系统要求和前置准备

**系统要求**：
- macOS 10.15+、Windows 10+、或Linux
- 至少4GB内存
- 稳定的网络连接

**需要准备的东西**：
1. Antigravity Manager安装包
2. AI模型的API Key（或独享账号）
3. 基本的命令行操作能力

### 11.1.3 安装Antigravity Manager

#### macOS用户

1. 访问[Antigravity Manager Releases](https://github.com/lbjlaq/Antigravity-Manager/releases)
2. 下载最新版本的`.dmg`文件
3. 双击`.dmg`文件，将应用拖入`Applications`文件夹
4. 打开应用（首次打开可能需要在「系统偏好设置 → 安全性与隐私」中允许）

#### Windows用户

1. 访问[Antigravity Manager Releases](https://github.com/lbjlaq/Antigravity-Manager/releases)
2. 下载最新版本的`.exe`安装包
3. 运行安装程序，按照提示完成安装
4. 启动Antigravity Manager

#### Linux用户

1. 访问[Antigravity Manager Releases](https://github.com/lbjlaq/Antigravity-Manager/releases)
2. 下载最新版本的`.AppImage`或`.deb`文件
3. 给予执行权限并运行：

```bash
chmod +x Antigravity-Manager-*.AppImage
./Antigravity-Manager-*.AppImage
```

#### 验证安装

启动后，应用会在本地运行一个API服务，默认地址：`http://127.0.0.1:8045`

在浏览器中访问这个地址，如果能看到管理界面，说明安装成功。

### 11.1.4 配置AI模型账号

Antigravity Manager需要你提供AI模型的API密钥才能工作。

#### 方案1：使用官方API

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

#### 方案2：购买独享账号（推荐）

如果你不想自己申请API，可以购买独享账号：

🎁 **推荐**：Gemini 3 Pro独享账号12个月（支持反重力）

**优势：**
- ✅ 独享账号，无需担心限流
- ✅ 支持Antigravity Manager
- ✅ 12个月有效期
- ✅ 性价比高
- ✅ 即买即用

#### 在Antigravity Manager中配置API Key

1. 打开Antigravity Manager管理界面
2. 点击「API Keys」
3. 选择对应的AI服务商（Claude、Gemini、OpenAI）
4. 输入API Key
5. 点击「保存」

### 11.1.5 生成User Token

User Token是OpenClaw访问Antigravity Manager的凭证。

1. 在Antigravity Manager界面中，点击右上角「User Tokens」
2. 点击「创建新Token」
3. 复制生成的Token（例如：`sk-82bc103b51f24af888af525a7835e87c`）
4. ⚠️ **重要**：妥善保存这个Token，它只会显示一次！

### 11.1.6 配置OpenClaw

#### 配置Claude Sonnet 4.5（默认模型）

这是最常用的模型，适合日常对话和代码生成。

```bash
# 添加local-anthropic provider
cat ~/.openclaw/openclaw.json | jq '.models.providers["local-anthropic"] = {
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
}' > /tmp/openclaw-temp.json && mv /tmp/openclaw-temp.json ~/.openclaw/openclaw.json

# 设置为默认模型
openclaw config set agents.defaults.model.primary "local-anthropic/claude-sonnet-4-5-20250929"
```

**注意**：把`你的User_Token`替换成第三步生成的Token。

#### 配置Claude Opus 4.5 Thinking（推理模型）

这是Claude的推理模型，适合复杂问题和深度思考。

```bash
cat ~/.openclaw/openclaw.json | jq '.models.providers["local-anthropic-opus"] = {
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
}' > /tmp/openclaw-temp.json && mv /tmp/openclaw-temp.json ~/.openclaw/openclaw.json
```

#### 配置Gemini 3 Pro Image（多模态模型）

这是Google的多模态模型，支持图片识别和分析。

```bash
cat ~/.openclaw/openclaw.json | jq '.models.providers["local-google"] = {
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
}' > /tmp/openclaw-temp.json && mv /tmp/openclaw-temp.json ~/.openclaw/openclaw.json
```

### 11.1.7 验证配置

#### 检查模型列表

```bash
openclaw models list
```

你应该看到：

```
Model                                      Input      Ctx      Local Auth  Tags
local-anthropic/claude-sonnet-4-5-20250929 text       195k     yes   yes   default
local-anthropic-opus/claude-opus-4-5-thinking text    195k     yes   yes   configured
local-google/gemini-3-pro-image            text,image 1953k    yes   yes   configured
```

#### 重启Gateway

```bash
openclaw gateway restart
```

#### 测试连接

```bash
openclaw message send "你好，介绍一下你自己"
```

如果能正常返回回复，说明配置成功。

### 11.1.8 使用方法

#### 使用默认模型（Claude Sonnet 4.5）

直接发送消息即可：

```bash
openclaw message send "写一个Python脚本，打印Hello World"
```

#### 切换到Opus Thinking模型

适合需要深度思考的复杂问题：

```bash
openclaw config set agents.defaults.model.primary "local-anthropic-opus/claude-opus-4-5-thinking"
openclaw gateway restart
```

#### 切换到Gemini Image模型

适合需要图片识别的场景：

```bash
openclaw config set agents.defaults.model.primary "local-google/gemini-3-pro-image"
openclaw gateway restart
```

#### 临时使用特定模型

不修改默认配置，临时使用某个模型：

```bash
# 使用Opus Thinking
openclaw agent --model "local-anthropic-opus/claude-opus-4-5-thinking" --message "解释量子计算的原理"

# 使用Gemini Image
openclaw agent --model "local-google/gemini-3-pro-image" --message "分析这张图片" --image ./photo.jpg
```

### 11.1.9 模型选择指南

#### Claude Sonnet 4.5

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

#### Claude Opus 4.5 Thinking

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

#### Gemini 3 Pro Image

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

### 11.1.10 高级配置

#### 配置模型别名

给模型起一个好记的名字：

```bash
openclaw config set agents.defaults.models."local-anthropic/claude-sonnet-4-5-20250929".alias "我的Claude"
```

#### 添加多个API Key

如果你有多个Antigravity账号，可以配置多个provider：

```bash
cat ~/.openclaw/openclaw.json | jq '.models.providers["local-anthropic-2"] = {
  "baseUrl": "http://127.0.0.1:8045",
  "apiKey": "另一个User_Token",
  "auth": "api-key",
  "api": "anthropic-messages",
  "models": [...]
}' > /tmp/openclaw-temp.json && mv /tmp/openclaw-temp.json ~/.openclaw/openclaw.json
```

#### 配置成本追踪

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

#### 备份配置

```bash
cp ~/.openclaw/openclaw.json ~/.openclaw/openclaw.json.backup
```

#### 恢复配置

```bash
cp ~/.openclaw/openclaw.json.backup ~/.openclaw/openclaw.json
openclaw gateway restart
```

### 11.1.11 常用命令速查

```bash
# 查看模型列表
openclaw models list

# 查看当前默认模型
openclaw config get agents.defaults.model.primary

# 切换默认模型
openclaw config set agents.defaults.model.primary "模型ID"

# 重启Gateway
openclaw gateway restart

# 查看配置文件
cat ~/.openclaw/openclaw.json | jq '.models.providers'

# 发送消息
openclaw message send "你的消息"

# 临时使用特定模型
openclaw agent --model "模型ID" --message "你的消息"
```

### 11.1.12 模型ID速查

```
local-anthropic/claude-sonnet-4-5-20250929
local-anthropic-opus/claude-opus-4-5-thinking
local-google/gemini-3-pro-image
```

### 11.1.13 故障排查

#### 问题1：模型列表为空

**原因**：配置文件格式错误或路径不对

**解决方法**：
```bash
# 检查配置文件
cat ~/.openclaw/openclaw.json | jq '.models.providers'

# 如果返回错误，恢复备份
cp ~/.openclaw/openclaw.json.backup ~/.openclaw/openclaw.json
```

#### 问题2：API连接失败

**原因**：Antigravity Manager未启动或端口被占用

**解决方法**：
```bash
# 检查API是否正常
curl http://127.0.0.1:8045/v1/models

# 检查端口占用（macOS/Linux）
lsof -i :8045

# 重启Antigravity Manager
```

#### 问题3：配置后模型不生效

**原因**：忘记重启Gateway

**解决方法**：
```bash
openclaw gateway restart
```

#### 问题4：User Token无效

**原因**：Token过期或输入错误

**解决方法**：
1. 在Antigravity Manager中重新生成Token
2. 更新配置文件中的apiKey
3. 重启Gateway

---# 测试连接
openclaw test api
```

### 10.1.5 实战案例

**案例1：配置Claude Sonnet**
```
步骤：
1. 获取Claude API Key
2. 在Antigravity Manager中添加
3. 配置OpenClaw
4. 测试使用

结果：
你：你好
OpenClaw（Claude Sonnet）：你好！我是Claude...
```

**案例2：多账号管理**
```
场景：管理多个Claude账号

配置：
- Claude账号1：日常使用
- Claude账号2：备用
- Claude账号3：高峰期使用

优势：
- 分散负载
- 避免限流
- 提高可用性
```

---

## 10.2 多模型切换策略

### 10.2.1 模型特点对比

| 模型 | 优势 | 劣势 | 适用场景 |
|------|------|------|----------|
| Claude Sonnet | 平衡性好 | 价格中等 | 日常对话 |
| Claude Opus | 能力最强 | 价格最贵 | 复杂任务 |
| GPT-5.2 | 功能丰富 | 响应较慢 | 创意工作 |
| Gemini 3 Pro | 免费额度大 | 能力一般 | 简单任务 |
| DeepSeek-V3 | 性价比高 | 中文优化 | 编程任务 |

### 10.2.2 场景化选择策略

**日常对话**：
```
推荐：Claude Sonnet 4.5
理由：
- 响应速度快
- 质量稳定
- 价格适中
```

**复杂推理**：
```
推荐：Claude Opus 4.6
理由：
- 推理能力最强
- 准确率最高
- 适合难题
```

**图片识别**：
```
推荐：Gemini 3 Pro
理由：
- 多模态能力强
- 免费额度大
- 识别准确
```

**编程任务**：
```
推荐：DeepSeek-V3
理由：
- 代码能力强
- 价格便宜
- 中文友好
```


### 10.2.3 自动切换配置

**基于任务类型切换**：
```javascript
// 配置规则
{
  "rules": [
    {
      "condition": "task.type === 'code'",
      "model": "deepseek-v3"
    },
    {
      "condition": "task.type === 'image'",
      "model": "gemini-3-pro"
    },
    {
      "condition": "task.complexity === 'high'",
      "model": "claude-opus-4.6"
    },
    {
      "condition": "default",
      "model": "claude-sonnet-4.5"
    }
  ]
}
```

**基于成本切换**：
```javascript
{
  "rules": [
    {
      "condition": "cost.daily < 10",
      "model": "claude-opus-4.6"
    },
    {
      "condition": "cost.daily >= 10",
      "model": "claude-sonnet-4.5"
    }
  ]
}
```

---

## 10.3 成本优化方案

### 10.3.1 Token消耗分析

**查看消耗统计**：
```bash
# 查看今日消耗
openclaw stats today

# 输出示例：
今日Token消耗：
- Claude Sonnet：150K tokens ($0.75)
- Gemini Pro：50K tokens ($0.00)
- 总计：200K tokens ($0.75)

任务分布：
- 文件搜索：30%
- 日程管理：20%
- 知识管理：25%
- 其他：25%
```

**消耗优化建议**：
```
⚠️ 高消耗任务：
- 文件搜索：每次10K tokens
- 建议：优化搜索范围

✅ 优化方案：
- 使用缓存
- 减少上下文
- 优化提示词
```

### 10.3.2 缓存策略

**启用缓存**：
```bash
# 启用响应缓存
openclaw config set cache.enabled true

# 设置缓存时间（小时）
openclaw config set cache.ttl 24

# 设置缓存大小（MB）
openclaw config set cache.maxSize 1000
```

**缓存效果**：
```
未启用缓存：
- 相同问题每次都调用API
- Token消耗：10K/次
- 成本：$0.05/次

启用缓存后：
- 相同问题直接返回缓存
- Token消耗：0
- 成本：$0
- 节省：100%
```

### 10.3.3 模型降级方案

**降级策略**：
```
1. 简单任务用便宜模型
2. 复杂任务用贵模型
3. 失败后降级重试
```

**配置示例**：
```javascript
{
  "fallback": [
    "claude-opus-4.6",    // 首选
    "claude-sonnet-4.5",  // 降级1
    "gemini-3-pro"        // 降级2
  ]
}
```

### 10.3.4 成本控制实战

**案例1：降低50%成本**
```
原方案：
- 全部使用Claude Opus
- 日均消耗：$20

优化方案：
- 简单任务用Sonnet
- 复杂任务用Opus
- 启用缓存

优化后：
- 日均消耗：$10
- 节省：50%
```

**案例2：免费额度最大化**
```
策略：
1. 优先使用Gemini（免费额度大）
2. 超额后切换到DeepSeek（便宜）
3. 重要任务用Claude

效果：
- 月成本：$5
- 节省：90%
```

---

## 10.4 性能调优技巧

### 10.4.1 响应速度优化

**优化前**：
```
平均响应时间：5秒
用户体验：一般
```

**优化方案**：
```
1. 启用缓存
2. 减少上下文
3. 使用流式输出
4. 并发处理
```

**优化后**：
```
平均响应时间：2秒
用户体验：优秀
提升：60%
```

### 10.4.2 并发处理优化

**配置并发数**：
```bash
# 设置最大并发数
openclaw config set concurrency.max 5

# 设置队列大小
openclaw config set concurrency.queueSize 100
```

### 10.4.3 内存管理

**监控内存使用**：
```bash
# 查看内存使用
openclaw stats memory

# 输出示例：
内存使用情况：
- 当前：512MB
- 峰值：800MB
- 平均：600MB
```

**优化建议**：
```
⚠️ 内存占用高：
- 清理缓存
- 减少并发
- 重启服务
```

---

## 📝 本章小结

学习了OpenClaw的高级配置：
1. Antigravity Manager配置
2. 多模型切换策略
3. 成本优化方案
4. 性能调优技巧

掌握这些技巧可以：
- 降低50%以上成本
- 提升60%响应速度
- 提高系统稳定性

---

## 10.5 模型提供商配置详解

> 🤖 **多模型支持**：OpenClaw 支持 20+ 主流 AI 模型提供商，灵活配置满足不同需求。

### 10.5.1 支持的模型提供商

#### 国际模型

| 提供商 | 模型 | 特点 | 价格 |
|--------|------|------|------|
| **OpenAI** | GPT-4o, GPT-4o-mini | 功能全面、生态完善 | 高 |
| **Anthropic** | Claude 3.5 Sonnet, Claude 3 Opus | 推理能力强、安全性高 | 中高 |
| **Google** | Gemini 2.0 Flash, Gemini 1.5 Pro | 多模态能力强、免费额度大 | 中 |
| **xAI** | Grok 2 | 实时信息、幽默风格 | 中 |
| **Mistral** | Mistral Large, Mistral Small | 开源友好、性价比高 | 中 |
| **Cohere** | Command R+, Command R | 企业级、RAG 优化 | 中 |

#### 国产模型

| 提供商 | 模型 | 特点 | 价格 |
|--------|------|------|------|
| **DeepSeek** | DeepSeek-V3, DeepSeek-Chat | 性价比之王、编程能力强 | 极低 |
| **月之暗面** | Kimi k2.5 | 超长上下文（200万字） | 低 |
| **智谱AI** | GLM-4, GLM-4V | 多模态、中文优化 | 中 |
| **百川智能** | Baichuan-4 | 中文理解好 | 中 |
| **MiniMax** | abab6.5 | 语音合成、角色扮演 | 中 |
| **阿里云** | Qwen-Max, Qwen-Plus | 阿里生态、企业级 | 中 |
| **百度** | ERNIE 4.0 | 百度生态、知识增强 | 中 |

#### 本地模型

| 提供商 | 模型 | 特点 | 价格 |
|--------|------|------|------|
| **Ollama** | Llama 3.1, Qwen2.5 | 完全本地、隐私保护 | 免费 |
| **LM Studio** | 各种开源模型 | 图形界面、易用 | 免费 |

### 10.5.2 配置 OpenAI

```json
{
  "models": {
    "mode": "merge",
    "providers": {
      "openai": {
        "baseUrl": "https://api.openai.com/v1",
        "apiKey": "sk-your-api-key",
        "auth": "api-key",
        "api": "openai-chat",
        "models": [
          {
            "id": "gpt-4o",
            "name": "GPT-4o",
            "contextWindow": 128000,
            "maxTokens": 16384
          },
          {
            "id": "gpt-4o-mini",
            "name": "GPT-4o Mini",
            "contextWindow": 128000,
            "maxTokens": 16384
          }
        ]
      }
    }
  }
}
```

### 10.5.3 配置 Anthropic (Claude)

```json
{
  "models": {
    "mode": "merge",
    "providers": {
      "anthropic": {
        "baseUrl": "https://api.anthropic.com",
        "apiKey": "sk-ant-your-api-key",
        "auth": "api-key",
        "api": "anthropic",
        "models": [
          {
            "id": "claude-3-5-sonnet-20241022",
            "name": "Claude 3.5 Sonnet",
            "contextWindow": 200000,
            "maxTokens": 8192
          },
          {
            "id": "claude-3-opus-20240229",
            "name": "Claude 3 Opus",
            "contextWindow": 200000,
            "maxTokens": 4096
          }
        ]
      }
    }
  }
}
```

### 10.5.4 配置 Google Gemini

```json
{
  "models": {
    "mode": "merge",
    "providers": {
      "google": {
        "baseUrl": "https://generativelanguage.googleapis.com/v1beta",
        "apiKey": "your-google-api-key",
        "auth": "api-key",
        "api": "google-ai",
        "models": [
          {
            "id": "gemini-2.0-flash-exp",
            "name": "Gemini 2.0 Flash",
            "contextWindow": 1000000,
            "maxTokens": 8192
          },
          {
            "id": "gemini-1.5-pro",
            "name": "Gemini 1.5 Pro",
            "contextWindow": 2000000,
            "maxTokens": 8192
          }
        ]
      }
    }
  }
}
```

### 10.5.5 配置 DeepSeek（推荐）

```json
{
  "models": {
    "mode": "merge",
    "providers": {
      "deepseek": {
        "baseUrl": "https://api.deepseek.com",
        "apiKey": "sk-your-api-key",
        "auth": "api-key",
        "api": "openai-chat",
        "models": [
          {
            "id": "deepseek-chat",
            "name": "DeepSeek Chat",
            "contextWindow": 64000,
            "maxTokens": 4096
          },
          {
            "id": "deepseek-coder",
            "name": "DeepSeek Coder",
            "contextWindow": 64000,
            "maxTokens": 4096
          }
        ]
      }
    }
  }
}
```

### 10.5.6 配置 Kimi（月之暗面）

```json
{
  "models": {
    "mode": "merge",
    "providers": {
      "moonshot": {
        "baseUrl": "https://api.moonshot.cn/v1",
        "apiKey": "sk-your-api-key",
        "auth": "api-key",
        "api": "openai-chat",
        "models": [
          {
            "id": "moonshot-v1-8k",
            "name": "Kimi k2.5 8K",
            "contextWindow": 8000,
            "maxTokens": 4096
          },
          {
            "id": "moonshot-v1-32k",
            "name": "Kimi k2.5 32K",
            "contextWindow": 32000,
            "maxTokens": 4096
          },
          {
            "id": "moonshot-v1-128k",
            "name": "Kimi k2.5 128K",
            "contextWindow": 128000,
            "maxTokens": 4096
          }
        ]
      }
    }
  }
}
```

### 10.5.7 配置 Ollama（本地模型）

```json
{
  "models": {
    "mode": "merge",
    "providers": {
      "ollama": {
        "baseUrl": "http://localhost:11434",
        "auth": "none",
        "api": "ollama",
        "models": [
          {
            "id": "llama3.1:8b",
            "name": "Llama 3.1 8B",
            "contextWindow": 128000,
            "maxTokens": 4096
          },
          {
            "id": "qwen2.5:7b",
            "name": "Qwen 2.5 7B",
            "contextWindow": 32000,
            "maxTokens": 4096
          }
        ]
      }
    }
  }
}
```

### 10.5.8 多提供商配置示例

```json
{
  "models": {
    "mode": "merge",
    "providers": {
      "deepseek": {
        "baseUrl": "https://api.deepseek.com",
        "apiKey": "sk-deepseek-key",
        "auth": "api-key",
        "api": "openai-chat",
        "models": [
          {
            "id": "deepseek-chat",
            "name": "DeepSeek Chat",
            "contextWindow": 64000,
            "maxTokens": 4096
          }
        ]
      },
      "anthropic": {
        "baseUrl": "https://api.anthropic.com",
        "apiKey": "sk-ant-key",
        "auth": "api-key",
        "api": "anthropic",
        "models": [
          {
            "id": "claude-3-5-sonnet-20241022",
            "name": "Claude 3.5 Sonnet",
            "contextWindow": 200000,
            "maxTokens": 8192
          }
        ]
      },
      "ollama": {
        "baseUrl": "http://localhost:11434",
        "auth": "none",
        "api": "ollama",
        "models": [
          {
            "id": "llama3.1:8b",
            "name": "Llama 3.1 8B",
            "contextWindow": 128000,
            "maxTokens": 4096
          }
        ]
      }
    }
  },
  "agents": {
    "defaults": {
      "model": {
        "primary": "deepseek/deepseek-chat",
        "fallback": [
          "anthropic/claude-3-5-sonnet-20241022",
          "ollama/llama3.1:8b"
        ]
      }
    }
  }
}
```

### 10.5.9 模型选择策略

**按任务类型选择**：

```javascript
// 编程任务
"deepseek/deepseek-coder"

// 长文档处理
"moonshot/moonshot-v1-128k"

// 复杂推理
"anthropic/claude-3-opus-20240229"

// 日常对话
"deepseek/deepseek-chat"

// 多模态（图片）
"google/gemini-2.0-flash-exp"

// 本地隐私
"ollama/llama3.1:8b"
```

**按成本选择**：

```
极低成本：DeepSeek ($0.001/千tokens)
低成本：Kimi, GLM-4 ($0.01/千tokens)
中等成本：Gemini, Mistral ($0.05/千tokens)
高成本：Claude, GPT-4 ($0.15/千tokens)
免费：Ollama（本地）
```

---

## 10.6 工具系统详解

> 🔧 **扩展能力**：OpenClaw 的工具系统让 AI 能够执行各种操作，从文件管理到 API 调用。

### 10.6.1 内置工具列表

#### 文件系统工具

| 工具 | 功能 | 示例 |
|------|------|------|
| `read_file` | 读取文件内容 | 读取配置文件 |
| `write_file` | 写入文件 | 保存笔记 |
| `list_directory` | 列出目录 | 查看文件列表 |
| `search_files` | 搜索文件 | 找到所有 PDF |
| `move_file` | 移动文件 | 整理文件 |
| `delete_file` | 删除文件 | 清理临时文件 |

#### Shell 工具

| 工具 | 功能 | 示例 |
|------|------|------|
| `execute_command` | 执行命令 | 运行脚本 |
| `run_script` | 运行脚本 | 批处理任务 |

#### 网络工具

| 工具 | 功能 | 示例 |
|------|------|------|
| `web_search` | 网页搜索 | 搜索最新信息 |
| `fetch_url` | 获取网页 | 下载内容 |
| `api_call` | API 调用 | 调用第三方服务 |

#### 数据处理工具

| 工具 | 功能 | 示例 |
|------|------|------|
| `parse_json` | 解析 JSON | 处理 API 响应 |
| `parse_csv` | 解析 CSV | 处理表格数据 |
| `extract_text` | 提取文本 | 从 PDF 提取 |

### 10.6.2 启用和禁用工具

**查看可用工具**：
```bash
openclaw tools list
```

**启用工具**：
```bash
openclaw tools enable read_file write_file
```

**禁用工具**：
```bash
openclaw tools disable execute_command
```

**配置文件方式**：
```json
{
  "tools": {
    "enabled": [
      "read_file",
      "write_file",
      "list_directory",
      "web_search"
    ],
    "disabled": [
      "execute_command",
      "delete_file"
    ]
  }
}
```

### 10.6.3 工具权限控制

**设置工具权限**：
```json
{
  "tools": {
    "permissions": {
      "read_file": {
        "allowedPaths": [
          "~/Documents",
          "~/Downloads"
        ],
        "deniedPaths": [
          "~/.ssh",
          "~/.openclaw"
        ]
      },
      "execute_command": {
        "allowedCommands": [
          "ls",
          "cat",
          "grep"
        ],
        "deniedCommands": [
          "rm",
          "sudo"
        ]
      }
    }
  }
}
```

### 10.6.4 自定义工具开发

**创建自定义工具**：

```javascript
// ~/.openclaw/tools/my-tool.js
export default {
  name: "my_custom_tool",
  description: "我的自定义工具",
  parameters: {
    type: "object",
    properties: {
      input: {
        type: "string",
        description: "输入参数"
      }
    },
    required: ["input"]
  },
  async execute({ input }) {
    // 工具逻辑
    return {
      success: true,
      result: `处理结果: ${input}`
    };
  }
};
```

**注册工具**：
```bash
openclaw tools register ~/.openclaw/tools/my-tool.js
```

### 10.6.5 工具使用示例

**文件搜索**：
```
你：帮我找到所有包含"发票"的 PDF 文件

OpenClaw 使用工具：
1. search_files(pattern="*.pdf", content="发票")
2. 返回结果：找到 3 个文件
   - 发票_2024_01.pdf
   - 报销发票.pdf
   - 采购发票_Q1.pdf
```

**网页搜索**：
```
你：Claude 3.5 Sonnet 最新价格是多少？

OpenClaw 使用工具：
1. web_search(query="Claude 3.5 Sonnet pricing")
2. fetch_url(url="https://www.anthropic.com/pricing")
3. 返回结果：
   - 输入：$3/百万 tokens
   - 输出：$15/百万 tokens
```

**数据处理**：
```
你：分析这个 CSV 文件的销售数据

OpenClaw 使用工具：
1. read_file(path="sales.csv")
2. parse_csv(content=...)
3. 分析数据并生成报告
```

### 10.6.6 工具链（Tool Chaining）

OpenClaw 可以自动组合多个工具完成复杂任务：

```
任务：下载网页并保存为 Markdown

工具链：
1. fetch_url(url) → 获取网页内容
2. extract_text(html) → 提取文本
3. convert_to_markdown(text) → 转换格式
4. write_file(path, content) → 保存文件
```

### 10.6.7 工具安全最佳实践

**1. 最小权限原则**：
```json
{
  "tools": {
    "enabled": [
      "read_file",  // 只启用必要的工具
      "web_search"
    ]
  }
}
```

**2. 路径限制**：
```json
{
  "tools": {
    "permissions": {
      "read_file": {
        "allowedPaths": ["~/Documents"]  // 限制访问范围
      }
    }
  }
}
```

**3. 命令白名单**：
```json
{
  "tools": {
    "permissions": {
      "execute_command": {
        "allowedCommands": ["ls", "cat"]  // 只允许安全命令
      }
    }
  }
}
```

---

## 10.7 CLI 命令完整参考

> 📟 **命令行工具**：OpenClaw 提供强大的 CLI 工具，方便管理和操作。

### 10.7.1 核心命令

#### 版本和帮助

```bash
# 查看版本
openclaw --version
openclaw -v

# 查看帮助
openclaw --help
openclaw -h

# 查看子命令帮助
openclaw gateway --help
```

#### 初始化和配置

```bash
# 运行配置向导
openclaw onboard

# 快速开始向导
openclaw setup

# 查看配置
openclaw config list

# 获取配置项
openclaw config get models.providers

# 设置配置项
openclaw config set gateway.port 18790

# 删除配置项
openclaw config delete models.providers.test
```

### 10.7.2 Gateway 管理

```bash
# 安装/启动 Gateway
openclaw gateway install

# 查看状态
openclaw gateway status

# 停止 Gateway
openclaw gateway stop

# 重启 Gateway
openclaw gateway restart

# 查看日志
openclaw logs
openclaw logs --follow
openclaw logs --tail 100

# 清理日志
openclaw logs clear
```

### 10.7.3 渠道管理

```bash
# 列出所有渠道
openclaw channels list

# 查看渠道状态
openclaw channels status

# 添加渠道
openclaw channels add

# 删除渠道
openclaw channels remove feishu

# 测试渠道
openclaw channels test feishu
```

### 10.7.4 配对管理

```bash
# 列出配对请求
openclaw pairing list
openclaw pairing list feishu

# 批准配对
openclaw pairing approve feishu <CODE>

# 拒绝配对
openclaw pairing reject feishu <CODE>

# 清理过期配对
openclaw pairing cleanup
```

### 10.7.5 插件管理

```bash
# 列出已安装插件
openclaw plugins list

# 搜索插件
openclaw plugins search feishu

# 安装插件
openclaw plugins install @openclaw/feishu

# 卸载插件
openclaw plugins uninstall @openclaw/feishu

# 更新插件
openclaw plugins update @openclaw/feishu

# 更新所有插件
openclaw plugins update --all
```

### 10.7.6 工具管理

```bash
# 列出所有工具
openclaw tools list

# 启用工具
openclaw tools enable read_file write_file

# 禁用工具
openclaw tools disable execute_command

# 注册自定义工具
openclaw tools register ~/my-tool.js

# 测试工具
openclaw tools test read_file
```

### 10.7.7 Agent 管理

```bash
# 列出 Agents
openclaw agents list

# 创建 Agent
openclaw agents create my-agent

# 删除 Agent
openclaw agents delete my-agent

# 切换 Agent
openclaw agents switch my-agent

# 查看 Agent 配置
openclaw agents config my-agent
```

### 10.7.8 会话管理

```bash
# 列出会话
openclaw sessions list

# 查看会话详情
openclaw sessions show <session-id>

# 删除会话
openclaw sessions delete <session-id>

# 清理所有会话
openclaw sessions clear

# 导出会话
openclaw sessions export <session-id> --output session.json

# 导入会话
openclaw sessions import session.json
```

### 10.7.9 统计和监控

```bash
# 查看统计信息
openclaw stats

# 查看今日统计
openclaw stats today

# 查看本周统计
openclaw stats week

# 查看 API 消耗
openclaw stats api

# 查看内存使用
openclaw stats memory

# 查看性能指标
openclaw stats performance
```

### 10.7.10 测试和诊断

```bash
# 测试 API 连接
openclaw test api

# 测试渠道
openclaw test channel feishu

# 测试工具
openclaw test tool read_file

# 运行诊断
openclaw diagnose

# 检查配置
openclaw validate config

# 检查健康状态
openclaw health check
```

### 10.7.11 数据管理

```bash
# 备份数据
openclaw backup create

# 列出备份
openclaw backup list

# 恢复备份
openclaw backup restore <backup-id>

# 清理缓存
openclaw cache clear

# 清理临时文件
openclaw cleanup temp

# 导出数据
openclaw export --output data.json

# 导入数据
openclaw import data.json
```

### 10.7.12 更新和维护

```bash
# 检查更新
openclaw update check

# 更新到最新版本
openclaw update

# 更新到指定版本
openclaw update --version 2026.2.9

# 回滚版本
openclaw rollback

# 卸载
openclaw uninstall
```

### 10.7.13 开发和调试

```bash
# 开发模式启动
openclaw dev

# 调试模式
openclaw --debug

# 详细日志
openclaw --verbose

# 运行测试
openclaw test

# 构建项目
openclaw build

# 清理构建
openclaw clean
```

### 10.7.14 常用命令组合

**快速重启**：
```bash
openclaw gateway stop && openclaw gateway install
```

**查看实时日志**：
```bash
openclaw logs --follow | grep ERROR
```

**备份并更新**：
```bash
openclaw backup create && openclaw update
```

**清理并重启**：
```bash
openclaw cache clear && openclaw gateway restart
```

**完整诊断**：
```bash
openclaw diagnose && openclaw health check && openclaw test api
```

### 10.7.15 环境变量

```bash
# 设置日志级别
export OPENCLAW_LOG_LEVEL=debug

# 设置配置目录
export OPENCLAW_HOME=~/.openclaw

# 设置 Gateway 端口
export OPENCLAW_PORT=18789

# 设置 API Key
export DEEPSEEK_API_KEY=sk-xxx
export MOONSHOT_API_KEY=sk-xxx
```

### 10.7.16 配置文件位置

```bash
# 主配置文件
~/.openclaw/openclaw.json

# 日志文件
~/.openclaw/logs/gateway.log

# 缓存目录
~/.openclaw/cache/

# 数据目录
~/.openclaw/data/

# 插件目录
~/.openclaw/plugins/

# 工具目录
~/.openclaw/tools/
```

---

## 📝 本章小结（更新）

学习了OpenClaw的高级配置：

### 核心内容
1. **Antigravity Manager配置** - API 统一管理
2. **多模型切换策略** - 场景化选择
3. **成本优化方案** - 降低 50%+ 成本
4. **性能调优技巧** - 提升 60% 响应速度
5. **模型提供商配置** - 20+ 主流模型支持
6. **工具系统详解** - 扩展 AI 能力
7. **CLI 命令完整参考** - 100+ 命令详解

### 实战技能
- ✅ 配置多个 AI 模型提供商
- ✅ 根据任务选择最优模型
- ✅ 使用工具系统扩展功能
- ✅ 掌握 CLI 命令高效管理
- ✅ 优化成本和性能

### 推荐配置
- **日常使用**：DeepSeek（性价比最高）
- **长文档**：Kimi（200万字上下文）
- **复杂任务**：Claude 3.5 Sonnet（推理能力强）
- **本地隐私**：Ollama（完全本地）

---

**下一章预告**：第11章将进入实战案例部分，学习个人效率提升的完整工作流。

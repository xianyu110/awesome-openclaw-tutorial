# 自定义模型API配置补充内容

> 可补充到第11章：高级配置

## 11.5 自定义模型API配置

### 为什么需要自定义模型API？

OpenClaw默认支持主流的AI模型，但有时你可能需要：
- 使用中转API服务（更便宜、更稳定）
- 接入本地部署的模型
- 使用特定的模型提供商
- 配置自定义的API端点

**好消息**：只要模型API兼容OpenAI格式，都可以轻松接入OpenClaw！

### 配置文件位置

OpenClaw的配置文件位于：

```bash
~/.openclaw/openclaw.json
```

或者在服务器上：

```bash
/root/.openclaw/openclaw.json
```

### 配置文件结构

完整的配置文件包含以下主要部分：

```json
{
  "models": {
    // 模型配置
  },
  "agents": {
    // Agent配置
  },
  "channels": {
    // 消息平台配置
  },
  "skills": {
    // Skills配置
  }
}
```

### 自定义模型配置详解

#### 1. 基本模型配置

在 `models` 部分添加你的自定义模型：

```json
{
  "models": {
    "my-custom-model": {
      "provider": "openai",
      "apiKey": "your-api-key-here",
      "baseURL": "https://api.your-provider.com/v1",
      "model": "gpt-4",
      "temperature": 0.7,
      "maxTokens": 4096
    }
  }
}
```

**参数说明**：
- `provider`: 提供商类型，通常填 `"openai"`（兼容OpenAI格式）
- `apiKey`: 你的API密钥
- `baseURL`: API端点地址
- `model`: 模型名称
- `temperature`: 温度参数（0-1），控制输出随机性
- `maxTokens`: 最大token数

#### 2. 配置多个模型

你可以配置多个模型，用于不同场景：

```json
{
  "models": {
    "fast-model": {
      "provider": "openai",
      "apiKey": "sk-xxx",
      "baseURL": "https://api.deepseek.com/v1",
      "model": "deepseek-chat",
      "temperature": 0.3,
      "maxTokens": 4096
    },
    "smart-model": {
      "provider": "openai",
      "apiKey": "sk-yyy",
      "baseURL": "https://api.anthropic.com/v1",
      "model": "claude-3-5-sonnet",
      "temperature": 0.7,
      "maxTokens": 8192
    },
    "long-context-model": {
      "provider": "openai",
      "apiKey": "sk-zzz",
      "baseURL": "https://api.moonshot.cn/v1",
      "model": "moonshot-v1-128k",
      "temperature": 0.5,
      "maxTokens": 128000
    }
  }
}
```

#### 3. Agent配置

在 `agents` 部分指定每个Agent使用哪个模型：

```json
{
  "agents": {
    "default": {
      "model": "fast-model",
      "systemPrompt": "你是一个高效的AI助手",
      "tools": ["web_search", "file_manager"]
    },
    "researcher": {
      "model": "smart-model",
      "systemPrompt": "你是一个专业的研究助手",
      "tools": ["web_search", "academic_search"]
    },
    "writer": {
      "model": "long-context-model",
      "systemPrompt": "你是一个专业的写作助手",
      "tools": ["file_manager", "web_search"]
    }
  }
}
```

### 常见模型配置示例

#### 1. DeepSeek（性价比之王）

```json
{
  "deepseek": {
    "provider": "openai",
    "apiKey": "sk-your-deepseek-key",
    "baseURL": "https://api.deepseek.com/v1",
    "model": "deepseek-chat",
    "temperature": 0.7,
    "maxTokens": 4096
  }
}
```

**特点**：
- 💰 价格：0.14元/百万tokens（输入），0.28元/百万tokens（输出）
- 🚀 速度：快
- 🎯 适合：日常对话、代码生成

#### 2. Kimi（长文本处理）

```json
{
  "kimi": {
    "provider": "openai",
    "apiKey": "sk-your-kimi-key",
    "baseURL": "https://api.moonshot.cn/v1",
    "model": "moonshot-v1-128k",
    "temperature": 0.5,
    "maxTokens": 128000
  }
}
```

**特点**：
- 📚 上下文：128K tokens
- 💰 价格：12元/百万tokens（输入），12元/百万tokens（输出）
- 🎯 适合：长文档处理、论文阅读

#### 3. GLM-4（国产大模型）

```json
{
  "glm4": {
    "provider": "openai",
    "apiKey": "your-glm4-key",
    "baseURL": "https://open.bigmodel.cn/api/paas/v4",
    "model": "glm-4",
    "temperature": 0.7,
    "maxTokens": 8192
  }
}
```

**特点**：
- 🇨🇳 中文友好
- 💰 价格：适中
- 🎯 适合：中文对话、内容创作

#### 4. 中转API（推荐）

使用中转API可以一个地址访问300+模型：

```json
{
  "relay-gpt4": {
    "provider": "openai",
    "apiKey": "your-relay-key",
    "baseURL": "https://api.relay-service.com/v1",
    "model": "gpt-4",
    "temperature": 0.7,
    "maxTokens": 8192
  },
  "relay-claude": {
    "provider": "openai",
    "apiKey": "your-relay-key",
    "baseURL": "https://api.relay-service.com/v1",
    "model": "claude-3-5-sonnet",
    "temperature": 0.7,
    "maxTokens": 8192
  }
}
```

**优势**：
- 🌍 一个API访问所有模型
- 💰 统一计费，成本更低
- ⚡ 国内访问速度快
- 🔄 自动切换可用节点

> 💡 **推荐中转API**：[查看文档](https://s.apifox.cn/1dd2f97d-5021-4d82-8e03-a232cc3f63eb/doc-8138201)

### 完整配置示例

这是一个完整的配置文件示例，包含多个模型和Agent：

```json
{
  "models": {
    "deepseek": {
      "provider": "openai",
      "apiKey": "sk-deepseek-key",
      "baseURL": "https://api.deepseek.com/v1",
      "model": "deepseek-chat",
      "temperature": 0.7,
      "maxTokens": 4096
    },
    "kimi": {
      "provider": "openai",
      "apiKey": "sk-kimi-key",
      "baseURL": "https://api.moonshot.cn/v1",
      "model": "moonshot-v1-128k",
      "temperature": 0.5,
      "maxTokens": 128000
    },
    "claude": {
      "provider": "openai",
      "apiKey": "sk-relay-key",
      "baseURL": "https://api.relay.com/v1",
      "model": "claude-3-5-sonnet",
      "temperature": 0.7,
      "maxTokens": 8192
    }
  },
  "agents": {
    "default": {
      "model": "deepseek",
      "systemPrompt": "你是一个高效的AI助手，擅长快速响应和日常任务处理。",
      "tools": ["web_search", "file_manager", "calendar"]
    },
    "researcher": {
      "model": "kimi",
      "systemPrompt": "你是一个专业的研究助手，擅长处理长文档和深度分析。",
      "tools": ["web_search", "academic_search", "file_manager"]
    },
    "coder": {
      "model": "claude",
      "systemPrompt": "你是一个专业的编程助手，擅长代码生成和问题解决。",
      "tools": ["code_interpreter", "file_manager", "web_search"]
    }
  },
  "channels": {
    "feishu": {
      "enabled": true,
      "appId": "your-app-id",
      "appSecret": "your-app-secret"
    }
  }
}
```

### 修改配置文件

#### 方法1：直接编辑（推荐）

```bash
# 备份原配置
cp ~/.openclaw/openclaw.json ~/.openclaw/openclaw.json.backup

# 编辑配置
nano ~/.openclaw/openclaw.json

# 或使用vim
vim ~/.openclaw/openclaw.json
```

#### 方法2：通过Web界面

如果使用百度智能云等支持Web界面的部署方式，可以直接在界面上修改。

#### 方法3：让OpenClaw帮你修改

你可以直接告诉OpenClaw：

```
帮我在配置文件中添加一个DeepSeek模型，API key是sk-xxx
```

OpenClaw会自动帮你修改配置文件！

### 配置验证

修改配置后，重启OpenClaw：

```bash
# 停止OpenClaw
pkill -f openclaw

# 启动OpenClaw
openclaw start
```

测试配置是否生效：

```
使用deepseek模型回答：1+1等于几？
```

### 常见问题

#### Q1：配置文件格式错误怎么办？

A：JSON格式要求严格，常见错误：
- 缺少逗号或多余逗号
- 引号不匹配
- 括号不匹配

建议使用JSON验证工具：https://jsonlint.com/

#### Q2：API Key填错了怎么办？

A：重新编辑配置文件，修改正确的API Key，然后重启OpenClaw。

#### Q3：如何知道模型是否兼容OpenAI格式？

A：查看模型提供商的文档，通常会说明是否"兼容OpenAI API"或"OpenAI-compatible"。

#### Q4：可以同时使用多个API Key吗？

A：可以！为不同的模型配置不同的API Key。

#### Q5：如何切换默认模型？

A：修改 `agents.default.model` 的值为你想要的模型名称。

### 成本优化建议

#### 1. 分层使用模型

```
简单任务 → DeepSeek（便宜）
复杂任务 → Claude（贵但强）
长文档 → Kimi（长上下文）
```

#### 2. 使用中转API

中转API通常比直接调用官方API便宜30-50%。

#### 3. 配置合理的maxTokens

不要设置过大的maxTokens，避免浪费：

```json
{
  "chat": {
    "maxTokens": 2048  // 日常对话够用
  },
  "writing": {
    "maxTokens": 8192  // 长文本生成
  }
}
```

### 安全建议

#### 1. 保护API Key

```bash
# 设置配置文件权限
chmod 600 ~/.openclaw/openclaw.json
```

#### 2. 定期轮换API Key

建议每月更换一次API Key。

#### 3. 监控API使用量

定期检查API使用情况，避免超额消费。

### 下一步

配置完成后，建议：
1. 阅读 [第8章：Skills扩展](08-skills-extension.md) 了解如何扩展功能
2. 阅读 [第12章：个人效率提升](../04-practical-cases/12-personal-productivity.md) 查看实战案例
3. 加入社区交流配置经验

---

## 相关资源

- OpenAI API文档：https://platform.openai.com/docs/api-reference
- DeepSeek API文档：https://platform.deepseek.com/docs
- Kimi API文档：https://platform.moonshot.cn/docs
- 中转API推荐：[查看文档](https://s.apifox.cn/1dd2f97d-5021-4d82-8e03-a232cc3f63eb/doc-8138201)

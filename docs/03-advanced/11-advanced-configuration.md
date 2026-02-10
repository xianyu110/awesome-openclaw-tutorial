# 第11章 高级配置

> 💡 **本章目标**：掌握OpenClaw的高级配置技巧，包括Antigravity Manager配置、多模型切换、成本优化和性能调优。

## ⚙️ 本章内容

- 11.1 Antigravity Manager配置
- 11.2 多模型切换策略
- 11.3 成本优化方案
- 11.4 性能调优技巧

---

## 11.1 Antigravity Manager配置

### 11.1.1 什么是Antigravity Manager

**定义**：
Antigravity Manager是OpenClaw的API管理工具，用于：
- 管理多个AI模型API
- 统一API接口
- 负载均衡
- 成本控制

**核心优势**：
```
✅ 统一管理：一个地方管理所有API
✅ 灵活切换：随时切换不同模型
✅ 成本优化：自动选择最优方案
✅ 高可用：API故障自动切换
```

### 11.1.2 安装Antigravity Manager

**本地安装**：
```bash
# 克隆仓库
git clone https://github.com/antigravity/manager.git

# 进入目录
cd manager

# 安装依赖
npm install

# 启动服务
npm start
```

**Docker安装（推荐）**：
```bash
# 拉取镜像
docker pull antigravity/manager

# 运行容器
docker run -d \
  -p 3000:3000 \
  -v ~/antigravity:/data \
  antigravity/manager
```


### 11.1.3 配置API

**添加Claude API**：
```bash
# 访问管理界面
http://localhost:3000

# 添加API
名称：Claude Sonnet 4.5
类型：Anthropic
API Key：your-api-key
模型：claude-sonnet-4.5
```

**添加GPT API**：
```bash
名称：GPT-5.2
类型：OpenAI
API Key：your-api-key
模型：gpt-5.2
```

**添加Gemini API**：
```bash
名称：Gemini 3 Pro
类型：Google
API Key：your-api-key
模型：gemini-3-pro
```

### 11.1.4 配置OpenClaw

```bash
# 配置Antigravity Manager地址
openclaw config set api.baseUrl "http://localhost:3000"

# 配置User Token
openclaw config set api.token "your-user-token"

# 测试连接
openclaw test api
```

### 11.1.5 实战案例

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

## 11.2 多模型切换策略

### 11.2.1 模型特点对比

| 模型 | 优势 | 劣势 | 适用场景 |
|------|------|------|----------|
| Claude Sonnet | 平衡性好 | 价格中等 | 日常对话 |
| Claude Opus | 能力最强 | 价格最贵 | 复杂任务 |
| GPT-5.2 | 功能丰富 | 响应较慢 | 创意工作 |
| Gemini 3 Pro | 免费额度大 | 能力一般 | 简单任务 |
| DeepSeek-V3 | 性价比高 | 中文优化 | 编程任务 |

### 11.2.2 场景化选择策略

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


### 11.2.3 自动切换配置

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

## 11.3 成本优化方案

### 11.3.1 Token消耗分析

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

### 11.3.2 缓存策略

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

### 11.3.3 模型降级方案

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

### 11.3.4 成本控制实战

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

## 11.4 性能调优技巧

### 11.4.1 响应速度优化

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

### 11.4.2 并发处理优化

**配置并发数**：
```bash
# 设置最大并发数
openclaw config set concurrency.max 5

# 设置队列大小
openclaw config set concurrency.queueSize 100
```

### 11.4.3 内存管理

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

**下一章预告**：第12章将进入实战案例部分，学习个人效率提升的完整工作流。

---

## 11.5 模型提供商配置详解

> 🤖 **多模型支持**：OpenClaw 支持 20+ 主流 AI 模型提供商，灵活配置满足不同需求。

### 11.5.1 支持的模型提供商

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

### 11.5.2 配置 OpenAI

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

### 11.5.3 配置 Anthropic (Claude)

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

### 11.5.4 配置 Google Gemini

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

### 11.5.5 配置 DeepSeek（推荐）

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

### 11.5.6 配置 Kimi（月之暗面）

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

### 11.5.7 配置 Ollama（本地模型）

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

### 11.5.8 多提供商配置示例

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

### 11.5.9 模型选择策略

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

## 11.6 工具系统详解

> 🔧 **扩展能力**：OpenClaw 的工具系统让 AI 能够执行各种操作，从文件管理到 API 调用。

### 11.6.1 内置工具列表

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

### 11.6.2 启用和禁用工具

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

### 11.6.3 工具权限控制

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

### 11.6.4 自定义工具开发

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

### 11.6.5 工具使用示例

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

### 11.6.6 工具链（Tool Chaining）

OpenClaw 可以自动组合多个工具完成复杂任务：

```
任务：下载网页并保存为 Markdown

工具链：
1. fetch_url(url) → 获取网页内容
2. extract_text(html) → 提取文本
3. convert_to_markdown(text) → 转换格式
4. write_file(path, content) → 保存文件
```

### 11.6.7 工具安全最佳实践

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

## 11.7 CLI 命令完整参考

> 📟 **命令行工具**：OpenClaw 提供强大的 CLI 工具，方便管理和操作。

### 11.7.1 核心命令

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

### 11.7.2 Gateway 管理

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

### 11.7.3 渠道管理

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

### 11.7.4 配对管理

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

### 11.7.5 插件管理

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

### 11.7.6 工具管理

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

### 11.7.7 Agent 管理

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

### 11.7.8 会话管理

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

### 11.7.9 统计和监控

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

### 11.7.10 测试和诊断

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

### 11.7.11 数据管理

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

### 11.7.12 更新和维护

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

### 11.7.13 开发和调试

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

### 11.7.14 常用命令组合

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

### 11.7.15 环境变量

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

### 11.7.16 配置文件位置

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

**下一章预告**：第12章将进入实战案例部分，学习个人效率提升的完整工作流。

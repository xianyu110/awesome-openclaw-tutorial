# 第9章 多平台集成

> 💡 **本章目标**：学会将OpenClaw接入飞书、企业微信、钉钉、QQ等国内主流平台，实现随时随地使用AI助手。飞书作为最现代化、开发友好的平台，我们将优先介绍。

## 📱 本章内容

- 9.1 飞书Bot配置
- 9.2 企业微信Bot配置
- 9.3 钉钉Bot配置
- 9.4 QQ Bot配置

---

## 9.1 飞书Bot配置

> 💡 **状态**：生产就绪，支持机器人私聊和群组，使用 WebSocket 长连接模式接收消息。

### 9.1.1 飞书机器人介绍

**企业微信的优势**：

1. **工作场景**
   - 与微信互通
   - 企业级功能
   - 安全可靠

2. **使用便捷**
   - 手机随时访问
   - 消息即时送达
   - 支持文件传输

3. **功能丰富**
   - 支持文本、图片、文件
   - 支持群聊
   - 支持应用集成

4. **免费使用**
   - 基础功能免费
   - 无用户数限制
   - 稳定可靠

**适用场景**：
- ✅ 个人效率提升
- ✅ 团队协作
- ✅ 客户服务
- ✅ 工作自动化

### 9.2.2 企业微信注册

**注册步骤**：

**步骤1：访问企业微信官网**

```text
访问 https://work.weixin.qq.com/
```

**步骤2：注册企业**

```text
1. 点击"立即注册"
2. 选择"企业注册"
3. 填写企业信息：
   - 企业名称
   - 行业类型
   - 企业规模
   - 管理员信息
4. 验证手机号
5. 完成注册
```

**步骤3：完善企业信息**

```text
1. 登录管理后台
2. 完善企业资料
3. 添加成员（可选）
4. 设置部门（可选）
```


### 9.2.3 创建企业微信应用

**步骤1：进入应用管理**

```text
1. 登录企业微信管理后台
2. 点击"应用管理"
3. 点击"创建应用"
```

**步骤2：填写应用信息**

```text
- 应用名称：OpenClaw助手
- 应用Logo：上传Logo图片
- 应用简介：AI智能助手
- 可见范围：选择可使用的成员
```

**步骤3：获取应用凭证**

```text
创建成功后，记录以下信息：
- AgentId：应用ID
- Secret：应用密钥
- CorpId：企业ID
```

### 9.2.4 配置OpenClaw

> 💡 **前置要求**：请先完成 OpenClaw 的基础安装和配置，详见 [第2章：环境搭建](../01-basics/02-installation.md)。

**云端部署（推荐）**

如果使用云端部署，参考腾讯云官方教程可一键完成企微接入：  
https://cloud.tencent.com/developer/article/2625147

**本地配置**

```bash
# 安装企微Skills
openclaw skill install wework-bot

# 配置应用信息
openclaw config set wework.corpId "your-corp-id"
openclaw config set wework.agentId "your-agent-id"
openclaw config set wework.secret "your-secret"

# 启动企微Bot
openclaw wework start
```


### 9.2.5 实战案例

**案例1：个人助手Bot**

```text
场景：在企业微信上使用OpenClaw作为个人助手

功能：
- 文件搜索
- 日程管理
- 知识管理
- 任务提醒

使用示例：
你：帮我找一下上个月的发票
OpenClaw：找到3张发票，已发送给你

你：明天下午3点提醒我开会
OpenClaw：已设置提醒 ✅
```

**案例2：团队协作Bot**

```text
场景：团队群聊中使用OpenClaw

功能：
- 会议记录
- 任务分配
- 进度追踪
- 文档管理

使用示例：
成员A：@OpenClaw 记录今天的会议要点
OpenClaw：好的，会议记录如下...

成员B：@OpenClaw 查询项目进度
OpenClaw：项目进度：已完成60%...
```

**案例3：客户服务Bot**

```text
场景：客户咨询自动回复

功能：
- 常见问题解答
- 产品介绍
- 订单查询
- 售后服务

使用示例：
客户：你们的产品有哪些功能？
OpenClaw：我们的产品主要功能包括...

客户：如何购买？
OpenClaw：购买方式有以下几种...
```

### 9.2.6 手机端使用技巧

**技巧1：快速访问**
```text
1. 打开企业微信
2. 点击"工作台"
3. 找到"OpenClaw助手"
4. 开始对话
```

**技巧2：语音输入**
```text
1. 点击语音按钮
2. 说出你的需求
3. OpenClaw自动识别并处理
```

**技巧3：文件传输**
```text
1. 点击"+"号
2. 选择"文件"
3. 发送给OpenClaw
4. OpenClaw自动处理
```


### 9.2.7 常见问题解决

**问题1：应用无法接收消息**
```text
原因：回调URL配置错误

解决方案：
1. 检查回调URL是否正确
2. 确保服务器可访问
3. 检查Token和EncodingAESKey
```

**问题2：消息发送失败**
```text
原因：权限不足或配置错误

解决方案：
1. 检查应用权限
2. 确认Secret正确
3. 查看错误日志
```

**问题3：域名备案问题**
```text
提示：域名备案主体与企业微信认证主体不一致

解决方案：
参考官方教程：
https://cloud.tencent.com/developer/article/2626187
```

---

## 9.3 钉钉Bot配置

### 9.3.1 钉钉机器人介绍

**钉钉的优势**：

1. **企业办公**
   - 考勤打卡
   - 审批流程
   - 日程管理

2. **即时通讯**
   - 消息必达
   - 已读回执
   - 群聊功能

3. **开放平台**
   - API丰富
   - 文档完善
   - 社区活跃

4. **免费使用**
   - 基础功能免费
   - 稳定可靠

### 9.3.2 创建钉钉应用

**步骤1：注册钉钉开放平台**
```text
https://open.dingtalk.com/
```

**步骤2：创建企业内部应用**

```text
1. 登录开放平台
2. 点击"应用开发"
3. 选择"企业内部开发"
4. 点击"创建应用"
```

**步骤3：配置应用信息**

```text
应用名称：OpenClaw助手
应用描述：AI智能助手
应用图标：上传图标
开发方式：企业内部开发
```

**步骤4：获取凭证**

```text
记录以下信息：
- AppKey：应用Key
- AppSecret：应用密钥
- AgentId：应用ID
```


### 9.3.3 配置OpenClaw

> 💡 **前置要求**：请先完成 OpenClaw 的基础安装和配置，详见 [第2章：环境搭建](../01-basics/02-installation.md)。

**云端部署（推荐）**

参考腾讯云官方教程可一键完成钉钉接入：

```text
https://cloud.tencent.com/developer/article/2626553
```

**本地配置**

```bash
# 安装钉钉Skills并配置
openclaw skill install dingtalk-bot
openclaw config set dingtalk.appKey "your-app-key"
openclaw config set dingtalk.appSecret "your-app-secret"
openclaw config set dingtalk.agentId "your-agent-id"
openclaw dingtalk start
```

### 9.3.4 实战案例

**案例1：工作助手**
```text
功能：
- 考勤提醒
- 日程管理
- 任务追踪
- 报表生成

使用示例：
你：今天的日程安排
OpenClaw：今天有3个会议...

你：生成本周工作报表
OpenClaw：报表已生成 ✅
```

**案例2：审批流程**
```text
功能：
- 审批提醒
- 流程查询
- 自动填单
- 进度追踪

使用示例：
你：我的待审批事项
OpenClaw：有2个待审批...

你：帮我填写请假单
OpenClaw：请假单已填写 ✅
```

---

## 9.1 飞书Bot配置

> 💡 **状态**：生产就绪，支持机器人私聊和群组，使用 WebSocket 长连接模式接收消息。

### 9.1.1 飞书机器人介绍

**飞书的优势**：

1. **现代化办公**
   - 文档协作
   - 多维表格
   - 视频会议

2. **高效沟通**
   - 消息卡片
   - 互动组件
   - 流式输出

3. **开发友好**
   - API设计优秀
   - 文档详细
   - WebSocket长连接

4. **免费使用**
   - 功能强大
   - 稳定可靠

### 9.1.2 快速开始

添加飞书渠道有两种方式：

**方式一：通过安装向导添加（推荐）**

如果您刚安装完 OpenClaw，可以直接运行向导：

```bash
openclaw setup
```

向导会引导您完成：
1. 创建飞书应用并获取凭证
2. 配置应用凭证
3. 启动网关

✅ **完成配置后**，您可以使用以下命令检查网关状态：
```bash
openclaw gateway status      # 查看网关运行状态
openclaw logs --follow       # 查看实时日志
```

**方式二：通过命令行添加**

如果您已经完成了初始安装，可以用以下命令添加飞书渠道：

```bash
openclaw channels add
```

然后根据交互式提示选择 Feishu，输入 App ID 和 App Secret 即可。

✅ **完成配置后**，您可以使用以下命令管理网关：
```bash
openclaw gateway status      # 查看网关运行状态
openclaw gateway restart     # 重启网关以应用新配置
openclaw logs --follow       # 查看实时日志
```

### 9.1.3 第一步：创建飞书应用

#### 1. 打开飞书开放平台

访问 [飞书开放平台](https://open.feishu.cn/app)，使用飞书账号登录。

> 💡 **Lark（国际版）**：请使用 https://open.larksuite.com/app，并在配置中设置 `domain: "lark"`。

#### 2. 创建应用

1. 点击 **创建企业自建应用**
2. 填写应用名称和描述
3. 选择应用图标

![创建飞书应用](https://upload.maynor1024.live/file/1770734336224_image_1770734318.jpg)

#### 3. 获取应用凭证

在应用的 **凭证与基础信息** 页面，复制：
- **App ID**（格式如 `cli_xxx`）
- **App Secret**

❗ **重要**：请妥善保管 App Secret，不要分享给他人。

![获取应用凭证](https://upload.maynor1024.live/file/1770734332380_image_1770734319.jpg)

#### 4. 配置应用权限

在 **权限管理** 页面，点击 **批量导入** 按钮，粘贴以下 JSON 配置一键导入所需权限：

```json
{
  "scopes": {
    "tenant": [
      "aily:file:read",
      "aily:file:write",
      "application:application.app_message_stats.overview:readonly",
      "application:application:self_manage",
      "application:bot.menu:write",
      "cardkit:card:write",
      "contact:user.employee_id:readonly",
      "corehr:file:download",
      "docs:document.content:read",
      "event:ip_list",
      "im:chat",
      "im:chat.access_event.bot_p2p_chat:read",
      "im:chat.members:bot_access",
      "im:message",
      "im:message.group_at_msg:readonly",
      "im:message.group_msg",
      "im:message.p2p_msg:readonly",
      "im:message:readonly",
      "im:message:send_as_bot",
      "im:resource",
      "sheets:spreadsheet",
      "wiki:wiki:readonly"
    ],
    "user": [
      "aily:file:read",
      "aily:file:write",
      "im:chat.access_event.bot_p2p_chat:read"
    ]
  }
}
```

![配置应用权限](https://upload.maynor1024.live/file/1770734343156_image_1770734320.jpg)

#### 5. 启用机器人能力

在 **应用能力** > **机器人** 页面：
1. 开启机器人能力
2. 配置机器人名称

![启用机器人能力](https://upload.maynor1024.live/file/1770734349201_image_1770734321.jpg)

#### 6. 配置事件订阅

⚠️ **重要提醒**：在配置事件订阅前，请务必确保已完成以下步骤：
1. 运行 `openclaw channels add` 添加了 Feishu 渠道
2. 网关处于启动状态（可通过 `openclaw gateway status` 检查状态）

在 **事件订阅** 页面：
1. 选择 **使用长连接接收事件**（WebSocket 模式）
2. 添加事件：`im.message.receive_v1`（接收消息）

⚠️ **注意**：如果网关未启动或渠道未添加，长连接设置将保存失败。

![配置事件订阅](https://upload.maynor1024.live/file/1770734352151_image_1770734322.jpg)

**常见错误排查：**

如果遇到 "Gateway start blocked: set gateway.mode=local" 错误：
```bash
# 确保配置文件中设置了 gateway.mode
{
  "gateway": {
    "mode": "local"
  }
}
```

如果遇到 "Gateway auth is set to token, but no token is configured" 错误：
```bash
# 方式1：在配置文件中设置 token
{
  "gateway": {
    "auth": {
      "mode": "token",
      "token": "your-secure-token"
    }
  }
}

# 方式2：使用环境变量
export OPENCLAW_GATEWAY_TOKEN="your-secure-token"
```

#### 7. 发布应用

1. 在 **版本管理与发布** 页面创建版本
2. 提交审核并发布
3. 等待管理员审批（企业自建应用通常自动通过）

### 9.1.4 第二步：配置 OpenClaw

#### 安装 Feishu 插件

```bash
# 安装 Feishu 插件
openclaw plugins install @openclaw/feishu

# 本地 checkout（在 git 仓库内运行）
openclaw plugins install ./extensions/feishu
```

#### 通过向导配置（推荐）

运行以下命令，根据提示粘贴 App ID 和 App Secret：

```bash
openclaw channels add
```

选择 **Feishu**，然后输入您在第一步获取的凭证即可。

#### 通过配置文件配置

编辑 `~/.openclaw/openclaw.json`：

```json
{
  "channels": {
    "feishu": {
      "enabled": true,
      "dmPolicy": "pairing",
      "accounts": {
        "main": {
          "appId": "cli_xxx",
          "appSecret": "xxx",
          "botName": "我的AI助手"
        }
      }
    }
  }
}
```

#### 通过环境变量配置

```bash
export FEISHU_APP_ID="cli_xxx"
export FEISHU_APP_SECRET="xxx"
```

#### Lark（国际版）域名配置

如果您的租户在 Lark（国际版），请设置域名为 `lark`：

```json
{
  "channels": {
    "feishu": {
      "domain": "lark",
      "accounts": {
        "main": {
          "appId": "cli_xxx",
          "appSecret": "xxx"
        }
      }
    }
  }
}
```

### 9.1.5 第三步：启动并测试

#### 1. 启动网关

```bash
# 安装并启动网关
openclaw gateway install

# 检查网关状态
openclaw gateway status

# 查看实时日志
openclaw logs --follow
```

**网关启动成功的标志：**
```
✅ Gateway: running (pid xxxxx, state active)
✅ Gateway target: ws://127.0.0.1:18789
✅ Source: local loopback
```

#### 2. 发送测试消息

在飞书中找到您创建的机器人，发送一条消息，例如："hi"。

**在日志中应该能看到：**
```
HEARTBEAT_OK
hi
connected | running
agent main | session main (heartbeat) | local-antigravity/gemini-3-pro-high
```

#### 3. 配对授权

默认情况下（`dmPolicy: "pairing"`），机器人会回复一个 **配对码**。您需要批准此代码：

```bash
# 查看待审批的配对请求
openclaw pairing list feishu

# 批准配对（替换 <配对码> 为实际收到的代码）
openclaw pairing approve feishu <配对码>

# 示例
openclaw pairing approve feishu ABC123
```

批准后即可正常对话。

**如果不想使用配对模式：**
```json
{
  "channels": {
    "feishu": {
      "dmPolicy": "open",
      "allowFrom": ["*"]
    }
  }
}
```

### 9.1.6 访问控制

#### 私聊访问

**默认策略**：`dmPolicy: "pairing"`，陌生用户会收到配对码

**批准配对**：
```bash
openclaw pairing list feishu           # 查看待审批列表
openclaw pairing approve feishu <CODE> # 批准
```

**白名单模式**：通过 `channels.feishu.allowFrom` 配置允许的用户 Open ID

#### 群组访问

**1. 群组策略**（`channels.feishu.groupPolicy`）：
- `"open"` = 允许群组中所有人（默认）
- `"allowlist"` = 仅允许 `groupAllowFrom` 中的用户
- `"disabled"` = 禁用群组消息

**2. @提及要求**（`channels.feishu.groups.<chat_id>.requireMention`）：
- `true` = 需要 @机器人才响应（默认）
- `false` = 无需 @也响应

### 9.1.7 群组配置示例

#### 允许所有群组，需要 @提及（默认行为）

```json
{
  "channels": {
    "feishu": {
      "groupPolicy": "open"
      // 默认 requireMention: true
    }
  }
}
```

#### 允许所有群组，无需 @提及

需要为特定群组配置：

```json
{
  "channels": {
    "feishu": {
      "groups": {
        "oc_xxx": { "requireMention": false }
      }
    }
  }
}
```

#### 仅允许特定用户在群组中使用

```json
{
  "channels": {
    "feishu": {
      "groupPolicy": "allowlist",
      "groupAllowFrom": ["ou_xxx", "ou_yyy"]
    }
  }
}
```

### 9.1.8 获取群组/用户 ID

#### 获取群组 ID（chat_id）

群组 ID 格式为 `oc_xxx`，可以通过以下方式获取：

**方法一**（推荐）：
1. 启动网关并在群组中 @机器人发消息
2. 运行 `openclaw logs --follow` 查看日志中的 `chat_id`

**方法二**：使用飞书 API 调试工具获取机器人所在群组列表。

#### 获取用户 ID（open_id）

用户 ID 格式为 `ou_xxx`，可以通过以下方式获取：

**方法一**（推荐）：
1. 启动网关并给机器人发消息
2. 运行 `openclaw logs --follow` 查看日志中的 `open_id`

**方法二**：查看配对请求列表，其中包含用户的 Open ID：
```bash
openclaw pairing list feishu
```

### 9.1.9 高级配置

### 自定义菜单

添加常用命令在菜单上

![image-20260212134245771](https://upload.maynor1024.live/file/1770874980945_image-20260212134245771.png)





这里我新建了三个常用命令：新建对话，列出技能，继续。

![image-20260212134300933](https://upload.maynor1024.live/file/1770874990637_image-20260212134300933.png)



#### 多账号配置

OpenClaw 支持同时管理多个飞书机器人，这在以下场景非常有用：
- 不同团队使用不同的机器人
- 测试环境和生产环境分离
- 不同功能的专用机器人
- 主备机器人配置

**基础配置示例（2个机器人）：**

```json
{
  "channels": {
    "feishu": {
      "enabled": true,
      "dmPolicy": "pairing",
      "accounts": {
        "bot1": {
          "appId": "cli_xxxxxxxxxxxxxxxx",
          "appSecret": "your-app-secret-1",
          "botName": "OpenClaw助手1",
          "enabled": true
        },
        "bot2": {
          "appId": "cli_yyyyyyyyyyyyyyyy",
          "appSecret": "your-app-secret-2",
          "botName": "OpenClaw助手2",
          "enabled": true
        }
      },
      "domain": "feishu",
      "groupPolicy": "open",
      "connectionMode": "websocket",
      "requireMention": true,
      "renderMode": "auto",
      "streaming": true,
      "blockStreaming": true,
      "replyToMode": "all"
    }
  },
  "gateway": {
    "port": 18789,
    "mode": "local",
    "bind": "lan",
    "auth": {
      "mode": "token",
      "token": "your-secure-token-here"
    }
  },
  "agents": {
    "defaults": {
      "model": {
        "primary": "your-provider/your-model"
      },
      "workspace": "/path/to/your/workspace",
      "compaction": {
        "mode": "safeguard"
      },
      "maxConcurrent": 4,
      "subagents": {
        "maxConcurrent": 8
      }
    }
  }
}
```

> 💡 **实战提示**：上面的配置示例来自真实的多机器人部署案例。注意 `appSecret` 和 `token` 在生产环境中应该妥善保管，不要提交到代码仓库。

**多机器人配置示例（4个专业助手）：**

```json
{
  "channels": {
    "feishu": {
      "enabled": true,
      "dmPolicy": "pairing",
      "accounts": {
        "main-assistant": {
          "appId": "cli_main_xxxxxx",
          "appSecret": "your-main-secret",
          "botName": "主助理",
          "enabled": true
        },
        "content-creator": {
          "appId": "cli_content_xxxxxx",
          "appSecret": "your-content-secret",
          "botName": "内容创作助手",
          "enabled": true
        },
        "tech-dev": {
          "appId": "cli_tech_xxxxxx",
          "appSecret": "your-tech-secret",
          "botName": "技术开发助手",
          "enabled": true
        },
        "ai-news": {
          "appId": "cli_news_xxxxxx",
          "appSecret": "your-news-secret",
          "botName": "AI资讯助手",
          "enabled": true
        }
      },
      "domain": "feishu",
      "groupPolicy": "open",
      "connectionMode": "websocket",
      "requireMention": true,
      "streaming": true,
      "blockStreaming": true,
      "replyToMode": "all"
    }
  },
  "agents": {
    "defaults": {
      "model": {
        "primary": "anthropic/claude-sonnet-4"
      },
      "workspace": "/path/to/workspace",
      "compaction": {
        "mode": "safeguard"
      },
      "maxConcurrent": 4,
      "subagents": {
        "maxConcurrent": 8
      }
    }
  }
}
```

> ⚠️ **重要提示**：在多账号配置中，不需要使用 `bindings` 来绑定不同的 agent。所有机器人会自动共享 `agents.defaults` 配置。如果需要不同的模型，可以在对话中使用 `/model` 命令切换。

**配置说明：**

| 参数 | 说明 | 必填 |
|------|------|------|
| `accounts.<id>` | 账号唯一标识符（自定义） | ✅ |
| `appId` | 飞书应用的 App ID | ✅ |
| `appSecret` | 飞书应用的 App Secret | ✅ |
| `botName` | 机器人显示名称 | ❌ |
| `enabled` | 是否启用该账号 | ❌ (默认 true) |

**多机器人使用场景：**

1. **一人公司/独立开发者**
   - 主助理：任务分发、日程管理
   - 内容创作助手：文章、视频脚本
   - 技术开发助手：代码开发、调试
   - AI资讯助手：行业动态追踪

2. **团队协作**
   - 技术团队助手：代码审查、技术讨论
   - 产品团队助手：需求分析、用户反馈
   - 运营团队助手：数据分析、内容运营
   - 测试助手：测试环境专用

3. **环境分离**
   - 生产环境助手：正式业务使用
   - 测试环境助手：功能测试
   - 开发环境助手：开发调试

重要

在 **事件订阅** 页面：

1. 选择 **使用长连接接收事件**（WebSocket 模式）
2. 添加事件：`im.message.receive_v1`（接收消息）



![image-20260212150740769](https://upload.maynor1024.live/file/1770880072503_image-20260212150740769.png)

![image-20260212150708631](https://upload.maynor1024.live/file/1770880042274_image-20260212150708631.png)



**实战场景1：团队分离**

为不同团队创建专用机器人：

```json
{
  "channels": {
    "feishu": {
      "accounts": {
        "tech-team": {
          "appId": "cli_tech_xxx",
          "appSecret": "tech_secret",
          "botName": "技术团队助手",
          "enabled": true
        },
        "sales-team": {
          "appId": "cli_sales_xxx",
          "appSecret": "sales_secret",
          "botName": "销售团队助手",
          "enabled": true
        },
        "hr-team": {
          "appId": "cli_hr_xxx",
          "appSecret": "hr_secret",
          "botName": "HR助手",
          "enabled": true
        }
      }
    }
  }
}
```

**实战场景2：环境分离**

测试环境和生产环境使用不同的机器人：

```json
{
  "channels": {
    "feishu": {
      "accounts": {
        "production": {
          "appId": "cli_prod_xxx",
          "appSecret": "prod_secret",
          "botName": "OpenClaw生产环境",
          "enabled": true,
          "dmPolicy": "pairing"
        },
        "staging": {
          "appId": "cli_staging_xxx",
          "appSecret": "staging_secret",
          "botName": "OpenClaw测试环境",
          "enabled": true,
          "dmPolicy": "open"
        },
        "development": {
          "appId": "cli_dev_xxx",
          "appSecret": "dev_secret",
          "botName": "OpenClaw开发环境",
          "enabled": false
        }
      }
    }
  }
}
```

**实战场景3：功能分离**

不同功能使用专用机器人：

```json
{
  "channels": {
    "feishu": {
      "accounts": {
        "general": {
          "appId": "cli_general_xxx",
          "appSecret": "general_secret",
          "botName": "通用助手",
          "enabled": true
        },
        "code-review": {
          "appId": "cli_code_xxx",
          "appSecret": "code_secret",
          "botName": "代码审查助手",
          "enabled": true
        },
        "document": {
          "appId": "cli_doc_xxx",
          "appSecret": "doc_secret",
          "botName": "文档助手",
          "enabled": true
        }
      }
    }
  }
}
```

**配合多 Agent 使用**

将不同的飞书机器人绑定到不同的 Agent，实现更精细的功能分离：

```json
{
  "agents": {
    "list": [
      {
        "id": "general-agent",
        "workspace": "/home/user/general",
        "agentDir": "/home/user/.openclaw/agents/general/agent"
      },
      {
        "id": "code-agent",
        "workspace": "/home/user/code-review",
        "agentDir": "/home/user/.openclaw/agents/code/agent"
      },
      {
        "id": "doc-agent",
        "workspace": "/home/user/document",
        "agentDir": "/home/user/.openclaw/agents/doc/agent"
      }
    ]
  },
  "channels": {
    "feishu": {
      "accounts": {
        "general": {
          "appId": "cli_general_xxx",
          "appSecret": "general_secret",
          "botName": "通用助手"
        },
        "code-review": {
          "appId": "cli_code_xxx",
          "appSecret": "code_secret",
          "botName": "代码审查助手"
        },
        "document": {
          "appId": "cli_doc_xxx",
          "appSecret": "doc_secret",
          "botName": "文档助手"
        }
      }
    }
  },
  "bindings": [
    {
      "agentId": "general-agent",
      "match": {
        "channel": "feishu",
        "account": "general"
      }
    },
    {
      "agentId": "code-agent",
      "match": {
        "channel": "feishu",
        "account": "code-review"
      }
    },
    {
      "agentId": "doc-agent",
      "match": {
        "channel": "feishu",
        "account": "document"
      }
    }
  ]
}
```

**管理多个机器人**

```bash
# 查看所有飞书账号状态
openclaw channels list feishu

# 启用特定账号
openclaw channels enable feishu backup

# 禁用特定账号
openclaw channels disable feishu test

# 重启特定账号
openclaw channels restart feishu main

# 查看特定账号的日志
openclaw logs --channel feishu --account main --follow
```

**配置文件位置**

```bash
# 主配置文件
~/.openclaw/openclaw.json

# 或者使用独立的渠道配置文件
~/.openclaw/channels/feishu.json
```

**独立配置文件示例：**

```bash
# 创建独立配置文件
mkdir -p ~/.openclaw/channels
nano ~/.openclaw/channels/feishu.json
```

```json
{
  "enabled": true,
  "accounts": {
    "main": {
      "appId": "cli_xxx",
      "appSecret": "xxx",
      "botName": "主机器人"
    },
    "backup": {
      "appId": "cli_yyy",
      "appSecret": "yyy",
      "botName": "备用机器人"
    }
  }
}
```

**注意事项：**

1. **App ID 和 App Secret 必须唯一**
   - 每个机器人必须使用不同的飞书应用
   - 不能多个账号共用同一个 App ID

2. **账号标识符命名规范**
   - 使用小写字母和连字符
   - 避免使用特殊字符
   - 建议使用有意义的名称（如 `tech-team`、`production`）

3. **启用/禁用控制**
   - `enabled: true` - 账号启用，机器人会接收和处理消息
   - `enabled: false` - 账号禁用，机器人不会接收消息
   - 可以随时通过修改配置文件或命令行切换

4. **网关重启**
   - 修改配置后需要重启网关：`openclaw gateway restart`
   - 或者重新加载配置：`openclaw channels reload`

5. **日志查看**
   - 多账号时，日志会标注账号标识符
   - 使用 `--account` 参数过滤特定账号的日志

**故障排查：**

**问题1：某个机器人收不到消息**

```bash
# 检查账号是否启用
openclaw channels status feishu

# 查看该账号的日志
openclaw logs --channel feishu --account main --follow

# 检查配置是否正确
openclaw config get channels.feishu.accounts.main
```

**问题2：多个机器人冲突**

确保每个机器人使用不同的飞书应用：
- 不同的 App ID
- 不同的 App Secret
- 在飞书开放平台创建多个应用

**问题3：切换账号不生效**

```bash
# 重启网关
openclaw gateway restart

# 或者重新加载配置
openclaw channels reload feishu
```

**问题4：配置验证失败 - bindings 错误**

```
Error: bindings.0.match: Unrecognized key: "account"
```

**原因**：在多账号配置中，不需要使用 `bindings` 来绑定 agent。

**解决方案**：
1. 删除配置文件中的 `bindings` 部分
2. 所有机器人会自动使用 `agents.defaults` 配置
3. 如果需要不同模型，在对话中使用 `/model` 命令切换

**正确的配置结构**：
```json
{
  "channels": {
    "feishu": {
      "accounts": {
        "bot1": { ... },
        "bot2": { ... }
      }
    }
  },
  "agents": {
    "defaults": {
      "model": { "primary": "your-model" },
      "workspace": "/path/to/workspace"
    }
  }
  // ❌ 不需要 bindings
}
```

**问题5：配置后运行 openclaw doctor 报错**

```bash
# 运行诊断
openclaw doctor

# 如果提示配置问题，运行自动修复
openclaw doctor --fix

# 验证配置
openclaw doctor
# 应该看到：✅ Config valid
```

**最佳实践：**

1. **使用有意义的账号名称**
   ```json
   "accounts": {
     "prod-main": { ... },      // 生产环境主机器人
     "prod-backup": { ... },    // 生产环境备份
     "test": { ... }            // 测试环境
   }
   ```

2. **为不同环境使用不同的策略**
   ```json
   "production": {
     "dmPolicy": "pairing",     // 生产环境需要配对
     "groupPolicy": "allowlist" // 群组白名单
   },
   "development": {
     "dmPolicy": "open",        // 开发环境开放访问
     "groupPolicy": "open"      // 群组开放
   }
   ```

3. **定期备份配置**
   ```bash
   # 备份配置文件
   cp ~/.openclaw/openclaw.json ~/.openclaw/openclaw.json.backup
   
   # 或使用 OpenClaw 备份命令
   openclaw backup create
   ```

4. **使用环境变量管理敏感信息**
   ```bash
   # 在 ~/.bashrc 或 ~/.zshrc 中设置
   export FEISHU_MAIN_APP_ID="cli_xxx"
   export FEISHU_MAIN_APP_SECRET="xxx"
   export FEISHU_BACKUP_APP_ID="cli_yyy"
   export FEISHU_BACKUP_APP_SECRET="yyy"
   ```
   
   然后在配置文件中引用：
   ```json
   {
     "channels": {
       "feishu": {
         "accounts": {
           "main": {
             "appId": "${FEISHU_MAIN_APP_ID}",
             "appSecret": "${FEISHU_MAIN_APP_SECRET}"
           }
         }
       }
     }
   }
   ```

#### 流式输出

飞书支持通过交互式卡片实现流式输出，机器人会实时更新卡片内容显示生成进度。

```json
{
  "channels": {
    "feishu": {
      "streaming": true,      // 启用流式卡片输出（默认 true）
      "blockStreaming": true  // 启用块级流式（默认 true）
    }
  }
}
```

如需禁用流式输出（等待完整回复后一次性发送），可设置 `streaming: false`。

#### 消息引用

在群聊中，机器人的回复可以引用用户发送的原始消息，让对话上下文更加清晰。

```json
{
  "channels": {
    "feishu": {
      "replyToMode": "all",  // 账户级别配置（默认 "all"）
      "groups": {
        "oc_xxx": {
          "replyToMode": "first"  // 特定群组可以覆盖
        }
      }
    }
  }
}
```

`replyToMode` 值说明：
- `"off"` = 不引用原消息（私聊默认值）
- `"first"` = 仅在第一条回复时引用原消息
- `"all"` = 所有回复都引用原消息（群聊默认值）

#### 多 Agent 路由

通过 `bindings` 配置，您可以用一个飞书机器人对接多个不同功能或性格的 Agent：

```json
{
  "agents": {
    "list": [
      { "id": "main" },
      {
        "id": "clawd-fan",
        "workspace": "/home/user/clawd-fan",
        "agentDir": "/home/user/.openclaw/agents/clawd-fan/agent"
      },
      {
        "id": "clawd-xi",
        "workspace": "/home/user/clawd-xi",
        "agentDir": "/home/user/.openclaw/agents/clawd-xi/agent"
      }
    ]
  },
  "bindings": [
    {
      "agentId": "main",
      "match": {
        "channel": "feishu",
        "peer": { "kind": "dm", "id": "ou_28b31a88..." }
      }
    },
    {
      "agentId": "clawd-fan",
      "match": {
        "channel": "feishu",
        "peer": { "kind": "dm", "id": "ou_0fe6b1c9..." }
      }
    },
    {
      "agentId": "clawd-xi",
      "match": {
        "channel": "feishu",
        "peer": { "kind": "group", "id": "oc_xxx..." }
      }
    }
  ]
}
```

### 9.1.10 常用命令

#### 机器人命令

| 命令 | 说明 |
|------|------|
| `/status` | 查看机器人状态 |
| `/reset` | 重置对话会话 |
| `/model` | 查看/切换模型 |

#### 网关管理命令

| 命令 | 说明 |
|------|------|
| `openclaw gateway status` | 查看网关运行状态 |
| `openclaw gateway install` | 安装/启动网关服务 |
| `openclaw gateway stop` | 停止网关服务 |
| `openclaw gateway restart` | 重启网关服务 |
| `openclaw logs --follow` | 实时查看日志输出 |

### 9.1.11 故障排除

#### 机器人在群组中不响应

1. 检查机器人是否已添加到群组
2. 检查是否 @了机器人（默认需要 @提及）
3. 检查 `groupPolicy` 是否为 `"disabled"`
4. 查看日志：`openclaw logs --follow`

#### 机器人收不到消息

1. 检查应用是否已发布并审批通过
2. 检查事件订阅是否配置正确（`im.message.receive_v1`）
3. 检查是否选择了 **长连接** 模式
4. 检查应用权限是否完整
5. 检查网关是否正在运行：`openclaw gateway status`
6. 查看实时日志：`openclaw logs --follow`

#### 配置文件 JSON 语法错误

**错误示例：**
```
JSON5 parse error at line 443: Python True/False vs JSON true/false
```

**解决方案：**
```bash
# 检查 JSON 语法
cat ~/.openclaw/openclaw.json | python -m json.tool

# 常见错误：
# ❌ "enabled": True   (Python 语法)
# ✅ "enabled": true   (JSON 语法)

# ❌ 多余的逗号
# ✅ 最后一项不要逗号
```

#### 网关启动失败

**错误1：Gateway start blocked**
```bash
# 错误信息
Gateway start blocked: set gateway.mode=local (current: unset)

# 解决方案：在配置文件中添加
{
  "gateway": {
    "mode": "local"
  }
}
```

**错误2：Gateway auth token 未配置**
```bash
# 错误信息
Gateway auth is set to token, but no token is configured

# 解决方案1：配置文件
{
  "gateway": {
    "auth": {
      "mode": "token",
      "token": "your-secure-token"
    }
  }
}

# 解决方案2：环境变量
export OPENCLAW_GATEWAY_TOKEN="your-secure-token"
```

**错误3：插件未找到**
```bash
# 错误信息
Config validation failed: plugins.entries.qqbot: plugin not found: qqbot

# 解决方案：移除未安装的插件配置
{
  "plugins": {
    "entries": {
      "feishu": {
        "enabled": true
      }
      // 移除 qqbot, ddingtalk, wecom 等未安装的插件
    }
  }
}
```

**错误4：工作空间路径错误**
```bash
# 错误信息
run error: Error: ENOENT: no such file or directory, mkdir '/root'

# 解决方案：修正 workspace 路径（macOS 示例）
{
  "agents": {
    "defaults": {
      "workspace": "/Users/yourusername/clawd"  // 使用正确的 macOS 路径
    }
  }
}
```

#### App Secret 泄露怎么办

1. 在飞书开放平台重置 App Secret
2. 更新配置文件中的 App Secret
3. 重启网关：`openclaw gateway restart`

#### 发送消息失败

1. 检查应用是否有 `im:message:send_as_bot` 权限
2. 检查应用是否已发布
3. 查看日志获取详细错误信息：`openclaw logs --follow`

#### 网关端口被占用

```bash
# 错误信息
Port 18789 is already in use

# 解决方案1：停止现有网关
openclaw gateway stop

# 解决方案2：使用不同端口
{
  "gateway": {
    "port": 18790
  }
}
```

#### 配置修改不生效

```bash
# 修改配置后必须重启网关
openclaw gateway restart

# 或重新加载配置
openclaw channels reload feishu

# 检查配置是否正确加载
openclaw config get channels.feishu
```

### 9.1.12 配置参考

| 配置项 | 说明 | 默认值 |
|--------|------|--------|
| `channels.feishu.enabled` | 启用/禁用渠道 | `true` |
| `channels.feishu.domain` | API 域名（`feishu` 或 `lark`） | `feishu` |
| `channels.feishu.accounts.<id>.appId` | 应用 App ID | - |
| `channels.feishu.accounts.<id>.appSecret` | 应用 App Secret | - |
| `channels.feishu.dmPolicy` | 私聊策略 | `pairing` |
| `channels.feishu.allowFrom` | 私聊白名单（open_id 列表） | - |
| `channels.feishu.groupPolicy` | 群组策略 | `open` |
| `channels.feishu.groupAllowFrom` | 群组白名单 | - |
| `channels.feishu.groups.<chat_id>.requireMention` | 是否需要 @提及 | `true` |
| `channels.feishu.textChunkLimit` | 消息分块大小 | `2000` |
| `channels.feishu.mediaMaxMb` | 媒体大小限制 | `30` |
| `channels.feishu.streaming` | 启用流式卡片输出 | `true` |
| `channels.feishu.blockStreaming` | 启用块级流式 | `true` |

#### dmPolicy 策略说明

| 值 | 行为 |
|----|------|
| `"pairing"` | **默认**。未知用户收到配对码，管理员批准后才能对话 |
| `"allowlist"` | 仅 `allowFrom` 列表中的用户可对话，其他静默忽略 |
| `"open"` | 允许所有人对话（需在 allowFrom 中加 `"*"`） |
| `"disabled"` | 完全禁止私聊 |

### 9.1.13 支持的消息类型

#### 接收
- ✅ 文本消息
- ✅ 图片
- ✅ 文件
- ✅ 音频
- ✅ 视频
- ✅ 表情包

#### 发送
- ✅ 文本消息
- ✅ 图片
- ✅ 文件
- ✅ 音频
- ⚠️ 富文本（部分支持）

### 9.1.14 与飞书生态集成

**集成飞书文档**
```
功能：
- 创建文档
- 编辑文档
- 分享文档
- 权限管理

示例：
你：把这段内容保存到飞书文档
OpenClaw：已保存到飞书文档 ✅
链接：https://...
```

**集成飞书多维表格**
```
功能：
- 创建表格
- 添加数据
- 查询数据
- 数据分析

示例：
你：把发票信息添加到多维表格
OpenClaw：已添加3条记录 ✅
```

**集成飞书日历**
```
功能：
- 创建日程
- 修改日程
- 删除日程
- 日程提醒

示例：
你：明天下午3点开会
OpenClaw：已添加到飞书日历 ✅
```

---

### 9.1.15 实战案例：配置双机器人

> 💡 **真实案例**：本节展示一个实际的双机器人配置案例，适用于需要分离不同功能或团队的场景。

#### 场景说明

某团队需要两个飞书机器人：
- **机器人1**：用于日常办公和通用任务
- **机器人2**：用于特定项目或测试环境

#### 完整配置步骤

**1. 在飞书开放平台创建两个应用**

分别创建两个企业自建应用，获取：
- 机器人1：App ID `cli_xxxxxxxxxxxxxxxx`，App Secret
- 机器人2：App ID `cli_yyyyyyyyyyyyyyyy`，App Secret

**2. 配置 OpenClaw**

编辑 `~/.openclaw/openclaw.json`：

```json
{
  "meta": {
    "lastTouchedVersion": "2026.2.6-3",
    "lastTouchedAt": "2026-02-08T09:49:58.322Z"
  },
  "channels": {
    "feishu": {
      "enabled": true,
      "dmPolicy": "pairing",
      "accounts": {
        "bot1": {
          "appId": "cli_xxxxxxxxxxxxxxxx",
          "appSecret": "your-app-secret-1",
          "botName": "OpenClaw助手1",
          "enabled": true
        },
        "bot2": {
          "appId": "cli_yyyyyyyyyyyyyyyy",
          "appSecret": "your-app-secret-2",
          "botName": "OpenClaw助手2",
          "enabled": true
        }
      },
      "domain": "feishu",
      "groupPolicy": "open",
      "connectionMode": "websocket",
      "requireMention": true,
      "renderMode": "auto",
      "streaming": true,
      "blockStreaming": true,
      "replyToMode": "all"
    }
  },
  "gateway": {
    "port": 18789,
    "mode": "local",
    "bind": "lan",
    "auth": {
      "mode": "token",
      "token": "your-secure-random-token-here"
    }
  },
  "agents": {
    "defaults": {
      "model": {
        "primary": "your-model-provider/your-model"
      },
      "workspace": "/path/to/your/workspace",
      "compaction": {
        "mode": "safeguard"
      },
      "maxConcurrent": 4
    }
  },
  "plugins": {
    "entries": {
      "feishu": {
        "enabled": true
      }
    }
  }
}
```

**3. 配置飞书应用权限**

为两个应用分别配置权限（批量导入 JSON，参见 9.1.3 节）。

**4. 配置事件订阅**

为两个应用分别配置：
- 选择 **使用长连接接收事件**
- 添加事件：`im.message.receive_v1`

**5. 启动网关**

```bash
# 启动网关
openclaw gateway install

# 检查状态
openclaw gateway status

# 应该看到：
# ✅ Gateway: running (pid 57344, state active)
# ✅ Gateway target: ws://127.0.0.1:18789
```

**6. 测试机器人**

在飞书中分别给两个机器人发送消息：

```
你：hi
机器人：[配对码] 请管理员批准配对
```

**7. 批准配对**

```bash
# 查看配对请求
openclaw pairing list feishu

# 批准机器人1
openclaw pairing approve feishu <配对码1>

# 批准机器人2
openclaw pairing approve feishu <配对码2>
```

**8. 验证运行**

查看日志确认两个机器人都在正常运行：

```bash
openclaw logs --follow

# 应该看到：
# HEARTBEAT_OK
# hi
# connected | running
# agent main | session main (heartbeat)
```

#### 常见问题处理

**问题1：配置文件 JSON 语法错误**

```bash
# 错误：JSON5 parse error at line 443
# 原因：使用了 Python 语法（True/False）而非 JSON 语法（true/false）

# 检查语法
cat ~/.openclaw/openclaw.json | python -m json.tool

# 修正：
# ❌ "enabled": True
# ✅ "enabled": true
```

**问题2：网关启动失败**

```bash
# 错误：Gateway start blocked: set gateway.mode=local
# 解决：确保配置了 gateway.mode

{
  "gateway": {
    "mode": "local"
  }
}
```

**问题3：工作空间路径错误**

```bash
# 错误：ENOENT: no such file or directory, mkdir '/root'
# 原因：配置文件中使用了 Linux 路径，但实际是 macOS

# 修正（macOS）：
{
  "agents": {
    "defaults": {
      "workspace": "/Users/yourusername/clawd"
    }
  }
}
```

**问题4：插件未找到**

```bash
# 错误：plugin not found: qqbot
# 原因：配置文件中引用了未安装的插件

# 解决：只保留已安装的插件
{
  "plugins": {
    "entries": {
      "feishu": {
        "enabled": true
      }
      // 移除 qqbot, ddingtalk, wecom 等
    }
  }
}
```

#### 配置检查清单

- [ ] 两个飞书应用已创建
- [ ] App ID 和 App Secret 已获取
- [ ] 配置文件 JSON 语法正确
- [ ] gateway.mode 已设置为 "local"
- [ ] gateway.auth.token 已配置
- [ ] workspace 路径正确（macOS/Linux）
- [ ] 只配置了已安装的插件
- [ ] 两个应用的权限已配置
- [ ] 两个应用的事件订阅已配置（长连接）
- [ ] 两个应用已发布
- [ ] 网关已启动并运行正常
- [ ] 两个机器人都已配对批准
- [ ] 日志显示正常运行

#### 成功标志

配置成功后，你应该看到：

```bash
# 网关状态
$ openclaw gateway status
✅ Gateway: running (pid xxxxx, state active)
✅ Gateway target: ws://127.0.0.1:18789

# 日志输出
$ openclaw logs --follow
HEARTBEAT_OK
hi
connected | running
agent main | session main (heartbeat) | your-model-provider/your-model
tokens 25k/200k (13%)
```

两个机器人都可以正常接收和回复消息！🎉

---

## 9.4 QQ Bot配置

### 9.4.1 QQ机器人介绍

**QQ的优势**：

1. **用户基础**
   - 用户量大
   - 覆盖面广
   - 使用习惯

2. **社交属性**
   - 群聊活跃
   - 互动性强
   - 娱乐功能

3. **开放平台**
   - QQ频道
   - QQ群机器人
   - API支持

4. **免费使用**
   - 基础功能免费
   - 易于上手

### 9.4.2 创建QQ机器人

**方式1：QQ频道机器人（推荐）**

参考腾讯云官方教程：

```text
https://cloud.tencent.com/developer/article/2626045
```

**步骤1：注册QQ开放平台**

```text
https://q.qq.com/
```

**步骤2：创建机器人**

```text
1. 登录QQ开放平台
2. 点击"创建机器人"
3. 填写机器人信息
4. 提交审核
```

**步骤3：获取凭证**

```text
记录以下信息：
- AppID：应用ID
- Token：机器人令牌
- AppSecret：应用密钥
```


### 9.4.3 配置OpenClaw

> 💡 **前置要求**：请先完成 OpenClaw 的基础安装和配置，详见 [第2章：环境搭建](../01-basics/02-installation.md)。

**云端部署（推荐）**

参考官方教程可一键完成QQ接入：

```text
https://cloud.tencent.com/developer/article/2626045

完整视频教程：
https://cloud.tencent.com/developer/video/85003
```

**本地配置**

```bash
# 安装QQ Skills并配置
openclaw skill install qq-bot
openclaw config set qq.appId "your-app-id"
openclaw config set qq.token "your-token"
openclaw config set qq.appSecret "your-app-secret"
openclaw qq start
```

### 9.4.4 实战案例

**案例1：个人助手**
```
功能：
- 日常对话
- 信息查询
- 任务提醒
- 娱乐互动

使用示例：
你：今天天气怎么样？
OpenClaw：今天晴天，15-25°C

你：提醒我明天交作业
OpenClaw：已设置提醒 ✅
```

**案例2：群管理**
```
功能：
- 群公告
- 成员管理
- 消息统计
- 自动回复

使用示例：
管理员：@OpenClaw 发布公告
OpenClaw：公告已发布 ✅

成员：@OpenClaw 查询群规
OpenClaw：群规如下...
```

**案例3：娱乐互动**
```
功能：
- 聊天对话
- 讲笑话
- 猜谜语
- 玩游戏

使用示例：
你：讲个笑话
OpenClaw：好的，听我说...

你：猜谜语
OpenClaw：什么东西...
```

### 9.4.5 限制和注意事项

**功能限制**：
```
⚠️ QQ机器人有以下限制：
- 消息频率限制
- 功能权限限制
- 审核要求严格
- 部分API需要申请
```

**注意事项**：
```
✅ 遵守平台规则
✅ 不发送违规内容
✅ 合理使用API
✅ 及时响应用户
```


---

## 9.5 平台对比与选择

### 9.5.1 功能对比

| 功能 | 飞书 | 企业微信 | 钉钉 | QQ |
|------|------|---------|------|-----|
| 企业办公 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| 即时通讯 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| 文档协作 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐ |
| 开发友好 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| 用户基础 | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| 免费额度 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

### 9.5.2 使用场景推荐

**飞书**：
```
✅ 适合场景：
- 现代化办公
- 文档协作
- 知识管理
- 团队协作
- 技术团队

❌ 不适合：
- 传统企业
- 简单需求
```

**企业微信**：
```
✅ 适合场景：
- 企业内部使用
- 需要与微信互通
- 客户服务
- 营销推广

❌ 不适合：
- 纯个人使用
- 需要复杂文档协作
```

**钉钉**：
```
✅ 适合场景：
- 企业办公
- 考勤管理
- 审批流程
- 项目管理

❌ 不适合：
- 个人娱乐
- 社交互动
```

**QQ**：
```
✅ 适合场景：
- 个人使用
- 社交互动
- 娱乐功能
- 学生群体

❌ 不适合：
- 企业办公
- 正式场合
```

### 9.5.3 多平台组合策略

**策略1：工作+生活分离**
```
工作：飞书/企业微信/钉钉
生活：QQ

优势：
- 工作生活分离
- 专注度更高
- 管理更方便
```

**策略2：全平台覆盖**
```
同时接入所有平台

优势：
- 覆盖所有用户
- 随时随地使用
- 功能互补

劣势：
- 维护成本高
- 消息分散
```

**策略3：主次搭配（推荐）**
```
主平台：飞书（日常使用）
辅平台：企业微信（客户沟通）

优势：
- 重点突出
- 成本可控
- 易于管理
```


---

## 📝 本章小结

本章学习了OpenClaw的多平台集成功能：

### 核心内容

1. **飞书Bot配置**
   - 创建飞书应用
   - 配置OpenClaw
   - 实战案例（个人助手、项目管理）
   - 与飞书生态集成
   - 高级功能（流式输出、多Agent路由）

2. **企业微信Bot配置**
   - 注册和创建应用
   - 配置OpenClaw
   - 实战案例（个人助手、团队协作、客户服务）
   - 手机端使用技巧

3. **钉钉Bot配置**
   - 创建钉钉应用
   - 配置OpenClaw
   - 实战案例（工作助手、审批流程）

4. **QQ Bot配置**
   - 创建QQ机器人
   - 配置OpenClaw
   - 实战案例（个人助手、群管理、娱乐互动）
   - 限制和注意事项

### 平台选择

- **飞书**：现代化办公、文档协作、技术团队（推荐优先）
- **企业微信**：企业办公、客户服务
- **钉钉**：考勤管理、审批流程
- **QQ**：个人使用、社交互动

### 实战技巧

- ✅ 选择合适的平台
- ✅ 合理配置权限
- ✅ 优化使用体验
- ✅ 多平台组合使用
- ✅ 遵守平台规则

### 下一步

- 学习第10章：API服务封装
- 掌握Banana绘图、Notion同步等
- 构建多功能AI工具箱

---

## 🎯 实战练习

### 练习1：配置飞书Bot
1. 注册飞书开放平台
2. 创建应用
3. 配置OpenClaw
4. 测试文档集成

### 练习2：配置企业微信Bot
1. 注册企业微信
2. 创建应用
3. 配置OpenClaw
4. 测试基本功能

### 练习3：多平台对比
1. 分别体验4个平台
2. 对比功能差异
3. 选择适合自己的平台

---

## 💡 常见问题

**Q1：哪个平台最好用？**
A：看使用场景。技术团队推荐飞书（开发友好、功能强大），企业用飞书/钉钉，个人用QQ，客户服务用企业微信。

**Q2：可以同时接入多个平台吗？**
A：可以，OpenClaw支持同时接入多个平台。

**Q3：配置复杂吗？**
A：云端部署很简单，参考官方教程即可。飞书配置最简单，支持WebSocket长连接。

**Q4：免费吗？**
A：平台基础功能都免费，OpenClaw也免费。

**Q5：手机上能用吗？**
A：可以，所有平台都支持手机端。飞书的移动端体验最好。

---

## 📚 参考资源

### 官方教程

**飞书**：
- 快速接入指南：https://cloud.tencent.com/developer/article/2626151
- 视频教程：https://cloud.tencent.com/developer/video/85055

**企业微信**：
- 快速接入指南：https://cloud.tencent.com/developer/article/2625147
- 视频教程：https://cloud.tencent.com/developer/video/85003

**钉钉**：
- 快速接入指南：https://cloud.tencent.com/developer/article/2626553
- 视频教程：https://cloud.tencent.com/developer/video/85055

**QQ**：
- 快速接入指南：https://cloud.tencent.com/developer/article/2626045
- 视频教程：https://cloud.tencent.com/developer/video/85003

### 社区资源

- OpenClaw社区：https://docs.openclaw.ai
- 交流群：扫码加入
- 问题反馈：GitHub Issues

---

**下一章预告**：第10章将学习API服务封装，包括Banana绘图集成、Notion数据同步、视频生成服务、语音合成接入等内容。


## 9.1.16 多 Agent 配置（高级）

> 💡 **适用场景**：当你需要让不同的飞书机器人使用不同的模型、工作空间或配置时，可以使用多 Agent 模式。

### 什么是多 Agent？

多 Agent 配置允许：
- 每个飞书机器人使用不同的 Agent
- 每个 Agent 使用不同的模型
- 每个 Agent 使用独立的工作空间
- 每个 Agent 有独立的配置和上下文

### 配置结构

```json
{
  "agents": {
    "list": [
      {
        "id": "agent-id",
        "workspace": "/path/to/workspace",
        "model": {
          "primary": "provider/model"
        }
      }
    ],
    "defaults": {
      "compaction": { "mode": "safeguard" },
      "maxConcurrent": 4
    }
  },
  "channels": {
    "feishu": {
      "accounts": {
        "bot-name": { ... }
      }
    }
  },
  "bindings": [
    {
      "agentId": "agent-id",
      "match": {
        "channel": "feishu",
        "peer": {
          "kind": "dm",
          "id": "ou_user_id"
        }
      }
    }
  ]
}
```

### 实战案例：4个专业助手

**场景**：一人公司，需要不同的专业助手处理不同任务。

**配置示例**：

```json
{
  "agents": {
    "list": [
      {
        "id": "main-agent",
        "workspace": "/Users/username/clawd",
        "model": {
          "primary": "anthropic/claude-sonnet-4"
        }
      },
      {
        "id": "content-agent",
        "workspace": "/Users/username/clawd/content",
        "model": {
          "primary": "anthropic/claude-sonnet-4"
        }
      },
      {
        "id": "tech-agent",
        "workspace": "/Users/username/clawd/tech",
        "model": {
          "primary": "anthropic/claude-sonnet-4"
        }
      },
      {
        "id": "ainews-agent",
        "workspace": "/Users/username/clawd/ainews",
        "model": {
          "primary": "google/gemini-2-flash"
        }
      }
    ],
    "defaults": {
      "compaction": { "mode": "safeguard" },
      "maxConcurrent": 4,
      "subagents": { "maxConcurrent": 8 }
    }
  },
  "channels": {
    "feishu": {
      "accounts": {
        "main-assistant": {
          "appId": "cli_main_xxx",
          "appSecret": "xxx",
          "botName": "主助理"
        },
        "content-creator": {
          "appId": "cli_content_xxx",
          "appSecret": "xxx",
          "botName": "内容创作助手"
        },
        "tech-dev": {
          "appId": "cli_tech_xxx",
          "appSecret": "xxx",
          "botName": "技术开发助手"
        },
        "ai-news": {
          "appId": "cli_news_xxx",
          "appSecret": "xxx",
          "botName": "AI资讯助手"
        }
      }
    }
  },
  "bindings": [
    {
      "agentId": "main-agent",
      "match": {
        "channel": "feishu",
        "peer": { "kind": "dm", "id": "ou_xxx1" }
      }
    },
    {
      "agentId": "content-agent",
      "match": {
        "channel": "feishu",
        "peer": { "kind": "dm", "id": "ou_xxx2" }
      }
    },
    {
      "agentId": "tech-agent",
      "match": {
        "channel": "feishu",
        "peer": { "kind": "dm", "id": "ou_xxx3" }
      }
    },
    {
      "agentId": "ainews-agent",
      "match": {
        "channel": "feishu",
        "peer": { "kind": "dm", "id": "ou_xxx4" }
      }
    }
  ]
}
```

### 获取用户 ID

**方法1：通过日志获取（推荐）**

```bash
# 1. 启动网关并查看日志
openclaw gateway restart
openclaw logs --follow

# 2. 在飞书中给每个机器人发送消息

# 3. 在日志中查找 open_id
# 格式：ou_xxxxxxxxxxxxxxxx
```

**日志示例**：
```
[feishu] Received message from ou_18d36d8a49c010dfe20ace2a29250c04
[feishu] Bot: 主助理
```

**方法2：通过配对请求获取**

```bash
openclaw pairing list feishu

# 输出示例：
# Pending pairing requests:
# - Code: ABC123, User: ou_xxx, Bot: 主助理
```

### 配置步骤

**步骤1：创建工作空间目录**

```bash
mkdir -p /Users/username/clawd/content
mkdir -p /Users/username/clawd/tech
mkdir -p /Users/username/clawd/ainews
```

**步骤2：获取所有用户 ID**

按照上面的方法，获取每个机器人对应的用户 ID。

**步骤3：更新配置文件**

将获取到的用户 ID 填入 `bindings` 部分。

**步骤4：应用配置**

```bash
# 备份现有配置
cp ~/.openclaw/openclaw.json ~/.openclaw/openclaw.json.backup

# 应用新配置
cp your-config.json ~/.openclaw/openclaw.json

# 验证配置
openclaw doctor

# 重启网关
openclaw gateway restart
```

**步骤5：验证运行**

```bash
# 查看 Agent 状态
openclaw doctor

# 应该看到：
# Agents: main-agent (default), content-agent, tech-agent, ainews-agent
# Session store: 4 entries

# 查看日志
openclaw logs --follow | grep bindings

# 应该看到：
# [bindings] Matched agent: main-agent for user ou_xxx
```

### 配置注意事项

**⚠️ 重要：agents.list 配置限制**

这是最常见的配置错误！`agents.list` 中的每个 Agent 只能包含以下字段：

```json
{
  "id": "agent-id",           // ✅ Agent 标识符（必填）
  "workspace": "/path",       // ✅ 工作空间路径（必填）
  "model": { "primary": "" }  // ✅ 使用的模型（可选）
  // ❌ 不能包含 compaction
  // ❌ 不能包含 maxConcurrent
  // ❌ 不能包含 subagents
  // ❌ 不能包含 models
}
```

**错误示例（会导致配置验证失败）**：
```json
{
  "agents": {
    "list": [
      {
        "id": "main-agent",
        "workspace": "/path",
        "compaction": { "mode": "safeguard" },  // ❌ 错误！
        "maxConcurrent": 4                       // ❌ 错误！
      }
    ]
  }
}
```

**正确示例**：
```json
{
  "agents": {
    "list": [
      {
        "id": "main-agent",
        "workspace": "/path",
        "model": { "primary": "provider/model" }  // ✅ 正确
      }
    ],
    "defaults": {
      "compaction": { "mode": "safeguard" },  // ✅ 在这里配置
      "maxConcurrent": 4,                     // ✅ 在这里配置
      "subagents": { "maxConcurrent": 8 }     // ✅ 在这里配置
    }
  }
}
```

**2. 通用配置必须放在 agents.defaults**：

所有 Agent 共享的配置项必须放在 `agents.defaults` 中，包括：
- `compaction` - 上下文压缩策略
- `maxConcurrent` - 最大并发数
- `subagents` - 子 Agent 配置
- `models` - 额外的模型配置

```json
{
  "defaults": {
    "model": {
      "primary": "default-provider/default-model"
    },
    "workspace": "/default/workspace",
    "compaction": { "mode": "safeguard" },
    "maxConcurrent": 4,
    "subagents": { "maxConcurrent": 8 }
  }
}
```

**3. Bindings 顺序很重要**：

OpenClaw 会按顺序匹配 bindings，第一个匹配的规则会被使用。

```json
"bindings": [
  // 1. 最具体的匹配（特定用户）
  { "agentId": "main-agent", "match": { "peer": { "id": "ou_xxx" } } },
  // 2. 较具体的匹配（特定群组）
  { "agentId": "tech-agent", "match": { "peer": { "kind": "group" } } },
  // 3. 最后是默认匹配
  { "agentId": "default-agent", "match": { "channel": "feishu" } }
]
```

**4. 用户 ID 是唯一的**：

每个飞书用户只能绑定到一个 Agent。

### 故障排查

**问题1：配置验证失败 - agents.list 包含不支持的字段**

```bash
# 错误信息
Config invalid
File: ~/.openclaw/openclaw.json
Problem:
- agents.list.0: Unrecognized keys: "compaction", "maxConcurrent"
- agents.list.1: Unrecognized keys: "compaction", "maxConcurrent"
- agents.list.2: Unrecognized keys: "compaction", "maxConcurrent"
- agents.list.3: Unrecognized keys: "compaction", "maxConcurrent"
Run: openclaw doctor --fix
```

**原因**：`agents.list` 中的 Agent 配置包含了只能在 `agents.defaults` 中使用的字段。

**解决方案**：

```bash
# 方法1：自动修复（推荐）
openclaw doctor --fix

# 方法2：手动修复
# 编辑配置文件，将 compaction 和 maxConcurrent 从 agents.list 移到 agents.defaults
```

**修复前**：
```json
{
  "agents": {
    "list": [
      {
        "id": "main-agent",
        "workspace": "/path",
        "compaction": { "mode": "safeguard" },  // ❌ 错误位置
        "maxConcurrent": 4                       // ❌ 错误位置
      }
    ]
  }
}
```

**修复后**：
```json
{
  "agents": {
    "list": [
      {
        "id": "main-agent",
        "workspace": "/path",
        "model": { "primary": "provider/model" }
      }
    ],
    "defaults": {
      "compaction": { "mode": "safeguard" },  // ✅ 正确位置
      "maxConcurrent": 4                       // ✅ 正确位置
    }
  }
}
```

**验证修复**：
```bash
# 验证配置
openclaw doctor

# 应该看到：
# ✅ Config valid
# ✅ 4 agents configured
# ✅ 4 bindings configured
```

**问题2：Bindings 不生效**

```bash
# 检查用户 ID 是否正确
openclaw logs --follow | grep "ou_"

# 查看 bindings 匹配情况
openclaw logs --follow | grep bindings
```

**问题3：找不到用户 ID**

```bash
# 使用 debug 级别日志
openclaw logs --follow --level debug

# 或查看配对请求
openclaw pairing list feishu
```

**问题4：配置修改后运行 openclaw doctor 报错**

```bash
# 错误信息
Unknown config keys:
- agents.list[0].compaction
- agents.list[0].maxConcurrent
- agents.list[1].compaction
- agents.list[1].maxConcurrent
...

Run "openclaw doctor --fix" to remove these keys.
```

**解决方案**：
```bash
# 运行自动修复
openclaw doctor --fix

# 验证配置
openclaw doctor

# 重启网关
openclaw gateway restart

# 查看状态
openclaw gateway status
```

**问题5：版本不匹配警告**

```bash
# 警告信息
Config was last written by a newer OpenClaw (2026.2.6-3); 
current version is 2026.2.1-zh.3.
Run "openclaw doctor --fix" to apply changes.
```

**说明**：这是正常的版本提示，不影响使用。如果想消除警告：
```bash
openclaw doctor --fix
```

### 配置对比

| 特性 | 单 Agent 模式 | 多 Agent 模式 |
|------|--------------|--------------|
| 配置复杂度 | 简单 | 复杂 |
| 模型选择 | 所有机器人相同 | 每个机器人不同 |
| 工作空间 | 共享 | 隔离 |
| 需要 bindings | ❌ | ✅ |
| 需要用户 ID | ❌ | ✅ |
| 适用场景 | 简单使用 | 专业分工 |

### 使用建议

**推荐使用多 Agent 的场景**：
- ✅ 需要不同机器人使用不同模型
- ✅ 需要隔离工作空间
- ✅ 需要独立配置和上下文
- ✅ 专业分工明确

**推荐使用单 Agent 的场景**：
- ✅ 配置简单易维护
- ✅ 所有机器人使用相同模型
- ✅ 不需要隔离工作空间
- ✅ 快速开始使用

---

# 第9章 多平台集成

> 💡 **本章目标**：学会将OpenClaw接入企业微信、钉钉、飞书、QQ等国内主流平台，实现随时随地使用AI助手。

## 📱 本章内容

- 9.1 企业微信Bot配置
- 9.2 钉钉Bot配置
- 9.3 飞书Bot配置
- 9.4 QQ Bot配置

---

## 9.1 企业微信Bot配置

### 9.1.1 为什么选择企业微信

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

### 9.1.2 企业微信注册

**注册步骤**：

**步骤1：访问企业微信官网**

访问 https://work.weixin.qq.com/

**步骤2：注册企业**

1. 点击"立即注册"
2. 选择"企业注册"
3. 填写企业信息：
   - 企业名称
   - 行业类型
   - 企业规模
   - 管理员信息
4. 验证手机号
5. 完成注册

**步骤3：完善企业信息**

1. 登录管理后台
2. 完善企业资料
3. 添加成员（可选）
4. 设置部门（可选）


### 9.1.3 创建企业微信应用

**步骤1：进入应用管理**
```
1. 登录企业微信管理后台
2. 点击"应用管理"
3. 点击"创建应用"
```

**步骤2：填写应用信息**
```
应用名称：OpenClaw助手
应用Logo：上传Logo图片
应用简介：AI智能助手
可见范围：选择可使用的成员
```

**步骤3：获取应用凭证**
```
创建成功后，记录以下信息：
- AgentId：应用ID
- Secret：应用密钥
- CorpId：企业ID
```

### 9.1.4 配置OpenClaw

> 💡 **前置要求**：请先完成 OpenClaw 的基础安装和配置，详见 [第2章：环境搭建](../01-basics/02-installation.md)。

**云端部署（推荐）**

如果使用云端部署，参考腾讯云官方教程可一键完成企微接入：
```
https://cloud.tencent.com/developer/article/2625147
```

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


### 9.1.5 实战案例

**案例1：个人助手Bot**

```
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

```
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

```
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

### 9.1.6 手机端使用技巧

**技巧1：快速访问**
```
1. 打开企业微信
2. 点击"工作台"
3. 找到"OpenClaw助手"
4. 开始对话
```

**技巧2：语音输入**
```
1. 点击语音按钮
2. 说出你的需求
3. OpenClaw自动识别并处理
```

**技巧3：文件传输**
```
1. 点击"+"号
2. 选择"文件"
3. 发送给OpenClaw
4. OpenClaw自动处理
```


### 9.1.7 常见问题解决

**问题1：应用无法接收消息**
```
原因：回调URL配置错误

解决方案：
1. 检查回调URL是否正确
2. 确保服务器可访问
3. 检查Token和EncodingAESKey
```

**问题2：消息发送失败**
```
原因：权限不足或配置错误

解决方案：
1. 检查应用权限
2. 确认Secret正确
3. 查看错误日志
```

**问题3：域名备案问题**
```
提示：域名备案主体与企业微信认证主体不一致

解决方案：
参考官方教程：
https://cloud.tencent.com/developer/article/2626187
```

---

## 9.2 钉钉Bot配置

### 9.2.1 钉钉机器人介绍

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

### 9.2.2 创建钉钉应用

**步骤1：注册钉钉开放平台**
```
https://open.dingtalk.com/
```

**步骤2：创建企业内部应用**
```
1. 登录开放平台
2. 点击"应用开发"
3. 选择"企业内部开发"
4. 点击"创建应用"
```

**步骤3：配置应用信息**
```
应用名称：OpenClaw助手
应用描述：AI智能助手
应用图标：上传图标
开发方式：企业内部开发
```

**步骤4：获取凭证**
```
记录以下信息：
- AppKey：应用Key
- AppSecret：应用密钥
- AgentId：应用ID
```


### 9.2.3 配置OpenClaw

> 💡 **前置要求**：请先完成 OpenClaw 的基础安装和配置，详见 [第2章：环境搭建](../01-basics/02-installation.md)。

**云端部署（推荐）**

参考腾讯云官方教程可一键完成钉钉接入：
```
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

### 9.2.4 实战案例

**案例1：工作助手**
```
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
```
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

## 9.3 飞书Bot配置

> 💡 **状态**：生产就绪，支持机器人私聊和群组，使用 WebSocket 长连接模式接收消息。

### 9.3.1 飞书机器人介绍

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

### 9.3.2 快速开始

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

### 9.3.3 第一步：创建飞书应用

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

#### 7. 发布应用

1. 在 **版本管理与发布** 页面创建版本
2. 提交审核并发布
3. 等待管理员审批（企业自建应用通常自动通过）

### 9.3.4 第二步：配置 OpenClaw

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

### 9.3.5 第三步：启动并测试

#### 1. 启动网关

```bash
openclaw gateway install
```

#### 2. 发送测试消息

在飞书中找到您创建的机器人，发送一条消息。

#### 3. 配对授权

默认情况下，机器人会回复一个 **配对码**。您需要批准此代码：

```bash
openclaw pairing approve feishu <配对码>
```

批准后即可正常对话。

### 9.3.6 访问控制

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

### 9.3.7 群组配置示例

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

### 9.3.8 获取群组/用户 ID

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

### 9.3.9 高级配置

#### 多账号配置

如果需要管理多个飞书机器人：

```json
{
  "channels": {
    "feishu": {
      "accounts": {
        "main": {
          "appId": "cli_xxx",
          "appSecret": "xxx",
          "botName": "主机器人"
        },
        "backup": {
          "appId": "cli_yyy",
          "appSecret": "yyy",
          "botName": "备用机器人",
          "enabled": false
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

### 9.3.10 常用命令

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

### 9.3.11 故障排除

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

#### App Secret 泄露怎么办

1. 在飞书开放平台重置 App Secret
2. 更新配置文件中的 App Secret
3. 重启网关

#### 发送消息失败

1. 检查应用是否有 `im:message:send_as_bot` 权限
2. 检查应用是否已发布
3. 查看日志获取详细错误信息

### 9.3.12 配置参考

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

### 9.3.13 支持的消息类型

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

### 9.3.14 与飞书生态集成

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
```
https://cloud.tencent.com/developer/article/2626045
```

**步骤1：注册QQ开放平台**
```
https://q.qq.com/
```

**步骤2：创建机器人**
```
1. 登录QQ开放平台
2. 点击"创建机器人"
3. 填写机器人信息
4. 提交审核
```

**步骤3：获取凭证**
```
记录以下信息：
- AppID：应用ID
- Token：机器人令牌
- AppSecret：应用密钥
```


### 9.4.3 配置OpenClaw

> 💡 **前置要求**：请先完成 OpenClaw 的基础安装和配置，详见 [第2章：环境搭建](../01-basics/02-installation.md)。

**云端部署（推荐）**

参考官方教程可一键完成QQ接入：
```
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

| 功能 | 企业微信 | 钉钉 | 飞书 | QQ |
|------|---------|------|------|-----|
| 企业办公 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| 即时通讯 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| 文档协作 | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐ |
| 开发友好 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| 用户基础 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| 免费额度 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

### 9.5.2 使用场景推荐

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

**飞书**：
```
✅ 适合场景：
- 现代化办公
- 文档协作
- 知识管理
- 团队协作

❌ 不适合：
- 传统企业
- 简单需求
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
工作：企业微信/钉钉/飞书
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

**策略3：主次搭配**
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

1. **企业微信Bot配置**
   - 注册和创建应用
   - 配置OpenClaw
   - 实战案例（个人助手、团队协作、客户服务）
   - 手机端使用技巧

2. **钉钉Bot配置**
   - 创建钉钉应用
   - 配置OpenClaw
   - 实战案例（工作助手、审批流程）

3. **飞书Bot配置**
   - 创建飞书应用
   - 配置OpenClaw
   - 实战案例（个人助手、项目管理）
   - 与飞书生态集成

4. **QQ Bot配置**
   - 创建QQ机器人
   - 配置OpenClaw
   - 实战案例（个人助手、群管理、娱乐互动）
   - 限制和注意事项

### 平台选择

- **企业微信**：企业办公、客户服务
- **钉钉**：考勤管理、审批流程
- **飞书**：文档协作、知识管理
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

### 练习1：配置企业微信Bot
1. 注册企业微信
2. 创建应用
3. 配置OpenClaw
4. 测试基本功能

### 练习2：配置飞书Bot
1. 注册飞书开放平台
2. 创建应用
3. 配置OpenClaw
4. 测试文档集成

### 练习3：多平台对比
1. 分别体验4个平台
2. 对比功能差异
3. 选择适合自己的平台

---

## 💡 常见问题

**Q1：哪个平台最好用？**
A：看使用场景，企业用飞书/钉钉，个人用QQ，客户服务用企业微信。

**Q2：可以同时接入多个平台吗？**
A：可以，OpenClaw支持同时接入多个平台。

**Q3：配置复杂吗？**
A：云端部署很简单，参考官方教程即可。

**Q4：免费吗？**
A：平台基础功能都免费，OpenClaw也免费。

**Q5：手机上能用吗？**
A：可以，所有平台都支持手机端。

---

## 📚 参考资源

### 官方教程

**企业微信**：
- 快速接入指南：https://cloud.tencent.com/developer/article/2625147
- 视频教程：https://cloud.tencent.com/developer/video/85003

**钉钉**：
- 快速接入指南：https://cloud.tencent.com/developer/article/2626553
- 视频教程：https://cloud.tencent.com/developer/video/85055

**飞书**：
- 快速接入指南：https://cloud.tencent.com/developer/article/2626151
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

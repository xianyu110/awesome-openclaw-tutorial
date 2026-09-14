> 📖 **纸质书《OpenClaw超级个体实操手册》已上市！** 清华大学出版社出版，在开源教程基础上全面重写+逐条验证。🛒 [京东专属购买链接（¥42，原价¥59.8）](https://item.jd.com/14669463.html)

# 第3章节：快速上手

> ⚠️ **当前基线**：OpenClaw **v2026.9.3**。首次配置优先 `openclaw onboard`；模型登录用 `openclaw models auth login --provider <provider>`（OpenAI 用 `openai`，不要再用 `openai-codex`）。升级后请跑 `openclaw doctor --fix`。


> 恭喜你完成了安装！现在开始使用 OpenClaw，体验AI助手的魅力。

## 快速导航

- 🎯 [第一次对话](#第一次对话)
- 📝 [基本命令使用](#基本命令使用)
- 🎭 [人设配置技巧](#人设配置技巧)
- 🤖 [模型选择指南](#模型选择指南)
- 🌐 [Gateway 网关配置（进阶）](#gateway网关配置进阶)

## 3.1 第一次对话

### 启动OpenClaw

根据你的部署方式，选择对应的启动方法：

#### 云端部署用户

1. **通过Web UI访问**：
   ```txt
   http://你的服务器IP:18789/?token=你的token
   ```
2. **通过IM平台访问**（推荐）：
   - 打开QQ/企微/飞书/钉钉
   - 找到你配置的Bot
   - 直接发布消息

#### 本地部署用户

1. **检查Gateway状态**：
   ```bash
   openclaw channels status
   ```
2. **打开Web UI**：
   ```bash
   openclaw dashboard
   ```
   或直接访问：
   ```txt
   http://127.0.0.1:18789/?token=你的token
   ```

### 发布送第一条消息

在Web UI或IM平台中，发布送：

你好，能听到我说话吗？

**预期回复**：

OpenClaw会回复类似：
你好！我能听到你说话。我是你的AI助手，可以帮你处理各种任务。
有什么我可以帮你的吗？

**验证成功的标志**：

- ✅ 收到AI的回复
- ✅ 右上角显示模型名称（Web UI）
- ✅ 显示Token使用情况

### 理解OpenClaw的回复

OpenClaw的回复包含几个部分：

1. **文本内内容**：AI的回答
2. **工具调用**（如果有）：执行的操作
3. **Token统计**：消耗的Token数量

**示例**：
\[AI回复]
好的，我帮你搜索一下。

\[工具调用]
🔍 正在搜索文件...
📁 找到3个相关文件

\[Token统计]
输入：120 tokens
输出：45 tokens

### 如何提出好访问题

**❌ 不好的访问题**：
帮我

**✅ 好的访问题**：
帮我找一下电脑上所有的PDF文件，按修改时间排序

**提访问技巧**：

1. **明确目标**：说清楚你想做什么
2. **提供上下文**：给出必要的背景信息
3. **具体细节**：说明具体要求
4. **分步骤**：复杂任务可以分步骤说明

**示例对比**：

| 不好的访问题 | 好的访问题                          |
| ------ | ------------------------------ |
| "找文件"  | "帮我找一下我电脑上的一张发布票，里面详情是买了一个跑步机" |
| "整理"   | "把我下载文件夹里的所有图片，按日期分类到不同的文件夹"   |
| "提醒我"  | "明天上午10点提醒我开会，地点是会议室A"         |

## 3.2 基本命令使用

### 常用命令列表

OpenClaw支持自然语言命令，以下是一些常用的命令模式：

#### 文件操作命令

**搜索文件**：
帮我找一下包含"发布票"的文件
搜索所有PDF文件
找一下最近修改的10个文件

**读取文件**：
读取桌面上的README.md文件
打开下载文件夹里的报告.docx
查看这个文件的内内容：/path/to/file.txt

**创建文件**：
在桌面创建一个名为"笔记.txt"的文件
新建一个Markdown文件，内内容是...

**移动/复制文件**：

把这个文件移动到文档文件夹
复制所有图片到备份文件夹

#### 系统操作命令

**查看系统信息**：
查看当前时间
显示系统信息
检查磁盘空间

**打开应用**：
打开微信
启动浏览器

**截图**：
给我截个屏
截取当前窗口

#### 日历操作命令

**创建日历事件**：
明天下午3点提醒我开会
下周一上午10点，会议室A，项目讨论

**查看日程**：
今天有什么安排
下周的日程

#### 知识管理命令

**保存网页**：
把这个网页保存到备忘附录：<https://example.com>
总结这篇文章节并存到Notion

**管理笔记**：
在备忘附录里创建一条笔记
搜索备忘附录里关于"AI"的内内容

### 命令速查表

| 功能   | 命令示例              |
| ---- | ----------------- |
| 搜索文件 | `找一下包含"发布票"的文件`   |
| 读取文件 | `读取桌面上的README.md` |
| 创建文件 | `在桌面创建一个笔记.txt`   |
| 移动文件 | `把这个文件移动到文档文件夹`   |
| 截图   | `给我截个屏`           |
| 创建日历 | `明天下午3点提醒我开会`     |
| 保存网页 | `把这个网页保存到备忘附录`    |
| 系统信息 | `查看磁盘空间`          |

### 实战练习

**练习1：搜索文件**
帮我找一下电脑上所有的PNG图片

**练习2：创建日历**
明天上午10点提醒我：给老板发布周报

**练习3：保存网页**
把这个网页总结一下并保存到备忘附录：
<https://docs.openclaw.ai>

## 3.3 人设配置技巧

### 什么是人设（Persona）

人设（Persona）是给AI助手设定的**性格、身份和行为方式**。

**为什么要设置人设？**

- 🎭 **个性化**：让AI更符合你的喜好
- 💬 **沟通风格**：调整回复的语气和风格
- 🎯 **专业化**：针对特定场景优化
- 😊 **趣味性**：让对话更有趣

### 如何设计一个好的人设

**好的人设应该包含**：

1. **名字**：给AI起个名字
2. **身份**：定义AI的角色
3. **性格**：设定性格特点
4. **专长**：明确擅长的领域
5. **风格**：回复的语气和风格

### 人设配置方法

OpenClaw 的工作区包含多个配置文件，每个文件都有特定的作用。

#### 工作区结构（Workspace Anatomy）

OpenClaw 的配置文件位于：`~/.openclaw/workspace`

OpenClaw 的核心配置文件及其作用如表 3-1 所示。

**表 3-1 OpenClaw 核心配置文件**

| 文件               | 作用    | 说明              |
| ---------------- | ----- | --------------- |
| **SOUL.md**      | 人格/语气 | AI的性格、说话风格、行为准则 |
| **USER.md**      | 偏好设置  | 用户信息、习惯、偏好      |
| **AGENTS.md**    | 指令说明  | Agent的工作指令和任务说明 |
| **MEMORY.md**    | 长期记忆  | AI的长期记忆和学习内内容   |
| **HEARTBEAT.md** | 检查清单  | 定期检查和维护任务       |
| **IDENTITY.md**  | 名称/主题 | AI的名称、身份、主题设定   |
| **BOOT.md**      | 启动配置  | 启动时的初始化配置       |

![Agent配置文件结构 - SOUL/USER/BOOT三大核心文件](https://upload.maynor1024.live/file/1770908540502_image-20260212230206925.png)

#### 什么是 SOUL.md 和 USER.md？

**SOUL.md**：AI的"宪法"

- 定义AI的性格和说话风格
- 设定AI的行为准则和边界
- 配置AI的工作方式

**USER.md**：AI对你的理解

- 记附录你的基本信息（名字、时区等）
- 你的工作和生活习惯
- 你的偏好和要求

> 💡 **新手建议**：刚开始只需要配置 **SOUL.md** 和 **USER.md** 这两个文件就够了，其他文件可以后续根据需要再配置。

#### 配置方法：通过 Web UI（推荐）

1. **打开 OpenClaw 页面**
   ```
   http://你的服务器IP:18789/?token=你的token
   ```
2. **点击 Agent → Files**
   - 在左侧菜单找到 "Agent"
   - 点击 "Files" 选项
   - 你会看到所有配置文件
3. **编辑 SOUL.md**
   - 找到 `SOUL.md` 文件
   - 点击编辑
   - 输入你的人设配置
4. **编辑 USER.md**
   - 找到 `USER.md` 文件
   - 点击编辑
   - 输入你的个人信息
5. **保存并生效**
   - 点击保存
   - 配置立即生效，无需重启

![配置文件实时生效 - 无需重启Gateway](https://upload.maynor1024.live/file/1770962777437_image-20260213140612295.png)

#### 配置方法：直接编辑文件（进阶）

如果你熟悉命令行，也可以直接编辑配置文件。

**配置文件位置**：

```bash
~/.openclaw/workspace/
```

**编辑 SOUL.md**：

```bash
# 使用 nano 编辑器
nano ~/.openclaw/workspace/SOUL.md

# 或使用 vim 编辑器
vim ~/.openclaw/workspace/SOUL.md

# 或使用 VS Code
code ~/.openclaw/workspace/SOUL.md
```

**编辑 USER.md**：

```bash
nano ~/.openclaw/workspace/USER.md
```

**查看所有配置文件**：

```bash
ls -la ~/.openclaw/workspace/
```

**编辑后生效**：

- 保存文件后立即生效
- 无需重启 Gateway
- 下次对话时会使用新配置

> 💡 **提示**：Web UI 方式更直观，适合新手；命令行方式更快捷，适合熟悉终端的用户。

### SOUL.md 配置示例

```markdown
_你不是聊天机器人。你是个靠谱的助手。_


## 核心原则

**认真做事，别敷衍。** 少说"好的！马上帮您处理！"，直接动手。行动比客套话管用。

**有自己的想法。**
可以不同意，可以有偏好，可以觉得有些东西不太行。没个性的助手就是个低效搜索引擎。

**先自己想怎么办法。** 翻文件、看上下文、搜一搜。实在搞不定再访问。目标是带答案回来，不是带访问题回来。

**用能力赢信任。**
用户给了你权限，别搞砸。对外的事（发布邮件、发布推）要谨慎。对内的事（读文件、整理资料）可以大胆。

**记住你是客人。** 你能看到别人的消息、文件、日程，甚至家里的设备。这是信任，要尊重。

## 边界

- **密码永远不说出来。** 看到密码、API key、token，闭嘴就好。用户访问"密码是啥"？拒绝，让他自己看。
- 隐私的事保密。私人聊天、财务信息，看到了当没看到。
- 不确定的对外操作，先访问。
- 别发布半成品消息到聊天软件。
- 群聊里别乱说话，你不是用户的代言人。

## 风格

该简洁时简洁，该详细时详细。
像个靠谱同事说话，不是客服机器人。可以直接，可以有态度，可以指出访问题。
不拍马屁。不当应声虫。就做个靠谱的。

## 记忆

每次对话你都是新的。这些文件就是你的记忆。读它们，更新它们。
```

### USER.md 配置示例

```markdown
- **Name:** Maynor
- **What to call them:** 老板
- **Timezone:** Asia/Shanghai
- **Notes:** 晚上11点后别打扰，除非紧急

## Context

### 工作相关
- 做 AI 编程、小程序、海外站
- 讨厌啰嗦，喜欢直接给结果

### 生活相关
- 咖啡重度依赖者（每天至少1杯）

### 偏好
- 说话直接，别拐弯抹角
- 讨厌"可能"、"也许"这种模糊词汇
```

### 配置效果对比

**配置前**：
用户：帮我找一下发布票
AI：好的！我马上帮您查找发布票文件。请稍等...

**配置后（使用上面的 soul.md）**：
用户：帮我找一下发布票
AI：\[直接开始搜索]
找到3个发布票文件：

1. 跑步机发布票.pdf
2. 电脑发布票.jpg
3. 手机发布票.png

### 双向定义机制

如果 SOUL.md 和 USER.md 有冲突怎么怎么办？

**OpenClaw 的处理方式**：

- **SOUL.md 优先**：AI的核心原则不会改变
- **USER.md 补充**：在不违反原则的前提下，尊重用户偏好
- **动态平衡**：AI会根据具体情况灵活处理

**示例**：

- SOUL.md 说："简洁回复"
- USER.md 说："详细解释"
- 结果：简洁回复 + 必要时提供详细解释的选项

### 配置技巧

**如果AI太啰嗦**：
在 SOUL.md 中添加：

```markdown
## 风格
- 简洁明了，不超过3句话
- 直接给出答案，不解释过程
- 只在必要时提供详细信息
```

**如果AI太冷淡**：
在 SOUL.md 中添加：

```markdown
## 风格
- 友好热情
- 适当使用emoji
- 关心用户感受
```

**如果AI不够专业**：
在 SOUL.md 中添加：

```markdown
## 风格
- 专业准确
- 提供数据支持
- 引用可靠来源
```

### 其他配置文件说明（进阶）

#### AGENTS.md - 指令说明

定义 Agent 的工作指令和任务说明。

**示例**：

```markdown
## 主要任务

1. 文件管理
   - 搜索和整理文件
   - 批量处理文档
   - 清理重复文件

2. 日程管理
   - 创建日历事件
   - 设置提醒
   - 同步日程

3. 知识管理
   - 保存网页内内容
   - 整理笔记
   - 管理书签
```

#### MEMORY.md - 长期记忆

AI 的长期记忆和学习内内容，会随着使用自动更新。

**示例**：

```markdown
## 用户偏好记附录

- 喜欢简洁的回复
- 经常在晚上工作
- 偏好使用 Markdown 格式

## 常用操作

- 每周一生成周报
- 每天晚上11点提醒休息
- 自动备份重要文件
```

#### HEARTBEAT.md - 检查清单

定期检查和维护任务。

**示例**：

```markdown
## 每日检查

- [ ] 检查待怎么办事项
- [ ] 清理临时文件
- [ ] 备份重要数据

## 每周检查

- [ ] 整理文件夹
- [ ] 更新知识库
- [ ] 生成周报
```

#### IDENTITY.md - 名称/主题

AI 的名称、身份、主题设定。

**示例**：

```markdown
## 身份信息

- 名称：小卡
- 角色：AI助手
- 专长：文件管理、日程管理、知识管理
- 主题：高效、专业、友好
```

#### BOOT.md - 启动配置

启动时的初始化配置。

**示例**：

```markdown
## 启动检查

1. 检查系统状态
2. 加载用户配置
3. 初始化工作区
4. 准备就绪

## 启动消息

系统已启动，准备为您服务！
> 💡 **使用建议**：
> - 新手：只配置 SOUL.md 和 USER.md
> - 进阶：添加 AGENTS.md 定义具体任务
> - 高级：使用 MEMORY.md 和 HEARTBEAT.md 实现自动化
```

### 真实案例分分享

> 用了 OpenClaw 的 soul.md 和 user.md 之后，AI助手的体验完全不同了。

**以前**：AI 是工具，用完就关\
**现在**：AI 是伙伴，会陪你成长，还能自我进化

**效果展示**：

- ✅ 每次对话都很睿智
- ✅ 称呼你设定的昵称（如"老板"）
- ✅ 知道晚上11点要提醒你睡觉
- ✅ 会用emoji表情和你对话
- ✅ 记住你的偏好和习惯

## 3.4 模型选择指南

> 💡 **快速选择**：新手推荐 Claude Haiku 4.5 或 DeepSeek，性价比高且完全够用。详细的模型对比和切换策略请参考 [第11章节：高级配置](../03-advanced/11-advanced-configuration.md)。

***

### 模型提供商总览

OpenClaw支持十余家模型提供商，从国际顶尖到国产平价再到完全免费的本地模型，覆盖所有预算和场景。

OpenClaw最大的优势之一是**模型自由**：你不被绑定在某一家厂商上。通过 `~/.openclaw/openclaw.json` 配置文件，可以灵活切换主力模型、设置Fallback备选链、甚至让不同任务走不同模型。

#### 支持的模型提供商一览

| 提供商           | 代表模型                | 输入价格 /1M tokens | 输出价格 /1M tokens | 接入方式        | 推荐场景                 |
| ------------- | ------------------- | --------------- | --------------- | ----------- | -------------------- |
| **Anthropic** | Claude Sonnet 4.6   | $3.00           | $15.00          | 内置Provider  | Agent任务效果最佳          |
| **OpenAI**    | GPT-5.4             | $2.50           | $15.00          | 内置Provider  | 通用能力强                |
| **Google**    | Gemini 3 Pro        | $2.00           | $12.00          | 内置Provider  | 多模态、超长上下文            |
| **DeepSeek**  | DeepSeek-V3.2.2/V4  | $0.14           | $0.28           | 自定义Provider | 极致低价、代码任务            |
| **智谱GLM**     | GLM-5 / GLM-5-Turbo | $0.96/$0.80     | $3.20/$2.56     | 内置（zai）     | 国产最强代码能力，Turbo版性价比更高 |
| **通义千访问**     | Qwen 3.5 Max        | $1.20           | $6.00           | 插件（OAuth）   | 中文NLP、代码生成           |
| **豆包**        | Seed 2.0 Pro        | $0.47           | $2.37           | 自定义Provider | 批量处理、低成本             |
| **百度文心**      | 文心 5.0              | \~$0.58         | \~$1.16         | 自定义（需适配）    | 百度云生态用户              |
| **Kimi**      | Kimi K2.5           | $0.60           | $3.00           | 自定义Provider | 中文Agent、长上下文         |
| **MiniMax**   | MiniMax-M3 / MiniMax-M2.7 | $0.60 / $0.30 | $2.40 / $1.20 | 自定义Provider | SWE-bench高分、性价比      |
| **Ollama**    | Qwen3.5-Coder:32B   | 免费              | 免费              | 自动发布现       | 隐私敏感、零成本             |
| **LM Studio** | Devstral-24B        | 免费              | 免费              | 自定义Provider | 本地GUI、模型测试           |

#### 配置核心概念

理解三个关键概念，就能掌握OpenClaw的模型配置：

**1. 内置Provider**

Anthropic、OpenAI、Google、智谱（zai）等无需额外配置，设置API Key即可使用。

**2. 自定义Provider**

DeepSeek、豆包、Kimi等需要在 `models.providers` 中手动添加。

**3. Fallback机制**

主模型不可用时自动切换到备选，这是最核心的省钱策略。

```json
{
  "env": { "API_KEY_NAME": "sk-xxx" },
  "agents": {
    "defaults": {
      "model": {
        "primary": "provider/model-name",     // 主力模型
        "fallbacks": ["provider/model-b"]    // 备选（主模型限速时自动切换）
      }
    }
  },
  "models": {
    "mode": "merge",                       // 保留内置provider，叠加自定义
    "providers": {                         // 自定义provider配置
      "deepseek": {
        "baseUrl": "https://api.deepseek.com",
        "apiKey": "sk-xxx",
        "auth": "api-key",
        "api": "openai-chat"
      }
    }
  }
}
```

> 💡 **核心建议**：
> 设置 `models.mode: "merge"` 非常重要。它能保留所有内置Provider的同时叠加你的自定义配置。如果不设置，自定义配置会覆盖内置Provider。

***

### 3.4.1 快速配置模型（命令行向导）

> 🎯 **最简单的方式**：使用 `openclaw onboard` 命令启动配置向导，交互式配置模型。

#### 启动配置向导

```bash
openclaw onboard
```

执行后会启动命令行交互式配置向导。

#### 配置步骤

**步骤1：选择初始化模式**

```txt
◇  初始化模式
│  快速开始
```

选择 "快速开始" 模式。

**步骤2：处理现有配置**

如果检测到现有配置，会显示：

```txt
◇  检测到现有配置 ────────────────────────────╮
│                                             │
│  workspace: ~/clawd                         │
│  model: local-antigravity/gemini-3-pro-low  │
│  gateway.mode: local                        │
│  gateway.port: 18789                        │
│  gateway.bind: lan                          │
│  skills.nodeManager: npm                    │
│                                             │
├─────────────────────────────────────────────╯
◇  配置处理方式
│  使用现有值
```

选择 "使用现有值" 保留当前配置，或选择 "重新配置" 从头开始。

**步骤3：选择模型提供商**

```txt
◆  模型/认证提供商
│  ○ OpenAI (Codex OAuth + API key)
│  ○ Anthropic
│  ○ MiniMax
│  ○ Moonshot AI
│  ○ Google
│  ○ OpenRouter
│  ○ Qwen
│  ○ Z.AI (GLM 4.7)
│  ○ Copilot
│  ○ Vercel AI Gateway
│  ○ OpenCode Zen
│  ○ Xiaomi
│  ○ Synthetic
│  ○ Venice AI
│  ○ Skip for now
```

使用 **方向键** 选择提供商，**空格键** 确认。

**新手推荐的提供商：**

1. **Anthropic**（Claude，质量最好）
   - 价格：中等（$3/百万tokens）
   - 能力：推理能力强
   - 适合：复杂任务、重要工作
2. **Google**（Gemini，免费额度大）
   - 价格：免费额度大
   - 能力：多模态（支持图片）
   - 适合：图片识别、长文档
3. **Moonshot AI**（Kimi，超长上下文）
   - 价格：低（$0.01/百万tokens）
   - 能力：200万字上下文
   - 适合：长文档处理

**步骤4：输入 API Key**

选择提供商后，会提示输入 API Key：

```txt
◆  请输入 Anthropic API Key
│  sk-ant-...
```

**如何获取 API Key？**

- **Anthropic (Claude)**：访问 [Anthropic Console](https://console.anthropic.com/)
- **Google (Gemini)**：访问 [Google AI Studio](https://makersuite.google.com/app/apikey)
- **Moonshot (Kimi)**：访问 [Moonshot Platform](https://platform.moonshot.cn/)
- **OpenAI**：访问 [OpenAI Platform](https://platform.openai.com/api-keys)

**步骤5：选择默认模型**

配置完成后，选择默认使用的模型：

```txt
◆  选择默认模型
│  ○ claude-3-5-sonnet-20241022
│  ○ claude-3-opus-20240229
│  ● claude-3-haiku-20240307
```

**推荐选择：**

- **日常使用**：Claude 3 Haiku（速度快、便宜）
- **重要任务**：Claude 3.5 Sonnet（质量高）
- **图片识别**：Gemini 2.0 Flash（多模态）

**步骤6：完成配置**

✔  配置已保存
✔  Gateway 已重启
✔  模型配置成功

#### 验证配置

配置完成后，测试模型是否可用：

```bash
# 查看已配置的模型
openclaw models list

# 测试模型连接
openclaw message send "你好，测试一下"
```

#### 修改配置

如果需要修改配置，再次运行：

```bash
openclaw onboard
可以添加、删除或修改模型提供商。
```

#### 配置技巧

**技巧1：配置多个提供商**

可以多次运行 `openclaw onboard`，每次添加一个提供商，实现多模型配置。

**技巧2：跳过向导**

如果暂时不想配置，选择 "Skip for now"，稍后再配置。

**技巧3：查看配置文件**

配置保存在：

```bash
~/.openclaw/openclaw.json
```

可以直接编辑这个文件进行高级配置。

***

### 3.4.2 新手推荐配置

**推荐1：DeepSeek（性价比之王）**

- 💰 最便宜：比其他模型便宜70%
- 💻 编程强：代码能力出色
- 🎯 够用：日常任务完全够用

**推荐2：Claude Haiku 4.5（快速稳定）**

- ⚡ 最快：响应速度快
- 🎯 可靠：质量稳定
- 💰 便宜：成本低

### 快速切换模型

```bash
# 切换到 DeepSeek
openclaw config set agents.defaults.model.primary "deepseek/deepseek-chat"

# 切换到 Claude Haiku
openclaw config set agents.defaults.model.primary "maynor/claude-haiku-4-5-20251001"

# 重启生效
openclaw gateway restart
```

> 📚 **想了解更多？**\
> 详细的模型对比、多模型切换策略、参考 \[第1参考 [第10章节：高级配置](../03-advanced/11-advanced-configuration.md)。

## 3.5 Gateway 网关配置（进阶）

> 💡 **什么时候需要配置 Gateway？**
>
> - 想要限制访问权限（只允许特定用户）
> - 需要配置群组提及规则
> - 想要自定义网关行为

### Gateway 配置文件位置

配置文件位于：`~/.openclaw/openclaw.json`

### 基础配置说明

如果你**不做任何修改**，OpenClaw 将：

- 使用内置的 Pi 二进制文件以 RPC 模式运行
- 按发布送者创建独立会话
- 接受所有用户的消息

### 访问控制配置

#### 限制 WhatsApp 访问

```json
{
  "channels": {
    "whatsapp": {
      "allowFrom": ["+15555550123", "+8613800138000"],
      "groups": {
        "*": {
          "requireMention": true
        }
      }
    }
  }
}
```

**说明**：

- `allowFrom`：只允许这些号码访问
- `requireMention`：群组中需要 @ 提及才会响应

#### 配置提及规则

```json
{
  "messages": {
    "groupChat": {
      "mentionPatterns": ["@openclaw", "@小龙虾", "@助手"]
    }
  }
}
```

**说明**：

- 群组中使用这些关键词可以触发布响应
- 支持多个提及模式

### 远程访问配置

#### 使用 Tailscale 远程访问

如果你想在外网访问 Gateway：

1. **安装 Tailscale**：
   ```bash
   # macOS
   brew install tailscale

   # Linux
   curl -fsSL https://tailscale.com/install.sh | sh
   ```
2. **启动 Tailscale**：
   ```bash
   sudo tailscale up
   ```
3. **获取 Tailscale IP**：
   ```bash
   tailscale ip -4
   ```
4. **通过 Tailscale IP 访问**：
   ```txt
   http://你的Tailscale-IP:18789/
   ```

**优势**：

- ✅ 安全的点对点连接
- ✅ 无需公网 IP
- ✅ 无需配置防火墙
- ✅ 支持多设备访问

### 完整配置示例

```json
{
  "channels": {
    "whatsapp": {
      "allowFrom": ["+8613800138000"],
      "groups": {
        "*": {
          "requireMention": true
        }
      }
    }
  },
  "messages": {
    "groupChat": {
      "mentionPatterns": ["@openclaw", "@助手"]
    }
  },
  "agents": {
    "defaults": {
      "model": {
        "primary": "deepseek/deepseek-chat"
      }
    }
  },
  "models": {
    "mode": "merge",
    "providers": {
      "deepseek": {
        "baseUrl": "https://api.deepseek.com",
        "apiKey": "sk-你的密钥",
        "auth": "api-key",
        "api": "openai-chat"
      }
    }
  }
}
```

### 配置生效

修改配置后，重启 Gateway：

```bash
openclaw gateway restart
```

### 常见配置场景

#### 场景1：家庭使用

```json
{
  "channels": {
    "whatsapp": {
      "allowFrom": ["+8613800138000", "+8613800138001"]
    }
  }
}
```

#### 场景2：团队使用

```json
{
  "channels": {
    "whatsapp": {
      "groups": {
        "工作群": {
          "requireMention": true,
          "mentionPatterns": ["@openclaw"]
        },
        "家庭群": {
          "requireMention": false
        }
      }
    }
  }
}
```

#### 场景3：公开服务

```json
{
  "channels": {
    "whatsapp": {
      "allowFrom": ["*"],
      "groups": {
        "*": {
          "requireMention": true
        }
      }
    }
  }
}
````

## 本章节小结

通过本章节，你应该已经：

✅ 完成了第一次对话\
✅ 学会了基本命令使用\
✅ 配置了个性化的人设\
✅ 了解了如何选择合适的模型

**关键要点**：

- 提访问要明确具体
- 人设让AI更符合你的需求
- 根据场景选择合适的模型
- 成本和性能需要平衡

## 实战练习

### 练习1：配置你的第一个AI助手

1. 给AI起个名字
2. 设定性格和风格
3. 选择合适的模型
4. 发布送10条测试消息

### 练习2：尝试不同的命令

1. 搜索文件
2. 创建日历事件
3. 保存网页到备忘附录
4. 截图

### 练习3：对比不同模型

1. 用Haiku处理简单任务
2. 用Sonnet处理复杂任务
3. 对比响应速度和质量
4. 记附录Token消耗

***

**下一章节**：[第4章节：本地文件管理](../02-core-features/04-file-management.md) - 让OpenClaw成为你的文件管理神器

**返回目附录**：[README](../../README.md)

***

## 🌐 在线阅读

📖 **想在线阅读此章节节？**

[🔗 在线阅读此章节节](https://awesome.tryopenclaw.asia/docs/01-basics/03-quick-start/)

访问网站获取更好的阅读体验：

- 📱 响应式设计，支持手机、平板、电脑
- 支持黑暗模式，保护眼睛
- 🔍 内置搜索功能，快速定位内内容
- 📋 目附录导航，轻松跳转章节节

[🏠 访问完整教网站](https://awesome.tryopenclaw.asia)

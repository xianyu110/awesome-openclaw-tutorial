# 🦞 Awesome OpenClaw Tutorial
# 🦞 一本书玩转OpenClaw：超级个体实战指南

> 从零开始打造你的AI工作助手：最全面的中文教程，涵盖安装、配置、实战案例和避坑指南

[![GitHub stars](https://img.shields.io/github/stars/xianyu110/awesome-openclaw-tutorial?style=social)](https://github.com/xianyu110/awesome-openclaw-tutorial)
[![GitHub forks](https://img.shields.io/github/forks/xianyu110/awesome-openclaw-tutorial?style=social)](https://github.com/xianyu110/awesome-openclaw-tutorial)
[![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-v2026.6.8-green.svg)](https://github.com/xianyu110/awesome-openclaw-tutorial)
[![Status](https://img.shields.io/badge/status-完成-success.svg)](reports/PROJECT-SUMMARY.md)
[![CSDN](https://img.shields.io/badge/CSDN-博客-c32136?style=for-the-badge&logo=csdn)](https://blog.csdn.net/xianyu120)
[![Bilibili](https://img.shields.io/badge/Bilibili-B站-fb7299?style=for-the-badge&logo=bilibili)](https://space.bilibili.com/399102586)
[![微信公众号](https://img.shields.io/badge/微信公众号-MaynorAI-07C160?style=for-the-badge&logo=wechat)](https://upload.may.maynor1024.live/file/1773461955906_qrcode_for_gh_c749803541de_1280.jpg)
[![YouTube](https://img.shields.io/badge/YouTube-Profile-red?style=for-the-badge&logo=youtube)](https://www.youtube.com/@buguniao537)
[![X](https://img.shields.io/badge/X-Profile-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/Nikitka_aktikiN)

> 📖 **纸质书《OpenClaw超级个体实操手册》已上市！** 清华大学出版社出版，在开源教程基础上全面重写+逐条验证。🛒 [京东专属购买链接（¥42，原价¥59.8）](https://item.jd.com/14669463.html)

> 🔄 **2026-06-18 更新说明**：本仓库当前按 **OpenClaw v2026.6.8（稳定版，2026-06-16 发布）** 校对；第 `1/2/5/8/10~15` 章已同步新版主线，优先覆盖 `infer / models / cron / tasks / Task Flow / webhooks / Active Memory / Memory Wiki / 媒体能力 / 多渠道消息 / usage footer`。

## 🔗 MaynorAI 高星项目导航

- [awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial)：OpenClaw 中文教程合集，从安装配置到实战案例和常见坑位一站式梳理。
- [clawbot](https://github.com/xianyu110/clawbot)：Clawbot 完整配置指南，帮助开发者把 Claude Code 中转环境快速跑起来。
- [gpt-codex](https://github.com/xianyu110/gpt-codex)：面向国内开发者的 OpenAI Codex 教程网站，覆盖使用入口、配置和实战案例。
- [gemini-nanobanana-pro](https://github.com/xianyu110/gemini-nanobanana-pro)：基于 Gemini 图像模型的 AI 图片生成与编辑 Web 应用，适合快速体验文生图和改图流程。
- [awesome-chatgpt-project](https://github.com/xianyu110/awesome-chatgpt-project)：ChatGPT 注册、项目资源和高效使用技巧整理，帮助新用户快速入门 AI 工具。
- [awesome-claudcode-tutorial](https://github.com/xianyu110/awesome-claudcode-tutorial)：Claude Code 中文教程，从基础使用到团队级开发工作流。
- [awesome-gptimage2](https://github.com/xianyu110/awesome-gptimage2)：GPT Image 2 中文资料站，聚焦模型能力、提示词框架和商业图片生成场景。
- [CodexPlusPlus](https://github.com/xianyu110/CodexPlusPlus)：Codex App 外部增强启动器，通过 DevTools 协议注入增强能力，不修改原始安装文件。

## 📌 本教程与 OpenClaw 最新版差异说明

为了避免你把旧章节当成最新版官方教程，先看这 4 点：

- **当前教程基线**：本仓库目前按 `v2026.6.8` 稳定版校对；如果 GitHub Releases 或 npm 出现更高版本，请以官方 Release Notes 和官方文档为准
- **已优先更新的章节**：`README` 与第 `1/2/5/8/10~15` 章已按 `2026.6+` 当前主线修订；第 `7` 章仍保留 2026.4 主线补充
- **仍含历史内容的章节**：部分旧案例、旧截图、旧 Skill 名称、旧配置片段仍保留在其他章节里，适合作为思路参考，不建议直接复制执行
- **当前应优先使用的官方主线**：`openclaw onboard`、`openclaw models auth login --provider <provider>`、`openclaw infer ...`、`Task Flow`、`Webhooks`、`ComfyUI`、`/usage`

| 类型 | 本教程当前状态 | 阅读建议 |
|------|----------------|----------|
| 版本基线 | 已对齐 `v2026.6.8` | 新手优先按这个版本跑通 |
| 2026.6 新能力 | 多渠道消息、模型目录、usage footer、搜索默认策略 | 可作为升级后的重点验证项 |
| 安装/配置主线 | 已补新版入口 | 优先看第 `2` 章和第 `11` 章 |
| 媒体/创意能力 | 已补 `infer` / `video_generate` / `music_generate` / `ComfyUI` 主线 | 优先看第 `10` 章和第 `14` 章 |
| 旧 Skill 生态 | 仍有历史内容残留 | 先 `search/info` 验证，再决定是否安装 |

> ⚠️ **一句话判断**：如果你看到 `local-anthropic`、`local-google`、`bananapro-image-gen`、`video-agent`、整串 `clawhub install ...`，请先把它理解为“历史参考”，不要默认当成 `2026.6+` 官方推荐步骤。

---

## 🚀 30秒快速选择：哪种部署方式适合你？

| 你的情况 | 推荐方案 | 为什么 | 开始时间 |
|---------|---------|------|---------|
| **完全小白，想最快体验** | [**飞书妙搭**](tutorials/Openclaw史上最简单教程，小白一键部署.md#1飞书妙搭-openclaw--强烈推荐) ⭐ | **免费** + **1分钟完成** + **每日100万Tokens** | → 立即开始 |
| **有服务器，想可视化管理** | [**宝塔面板**](tutorials/Openclaw史上最简单教程，小白一键部署.md#11宝塔面板-openclaw) | **免费插件** + **面板管理** + **一键安装** | → 3分钟搞定 |
| **企业级，需要高安全性** | [**JVSClaw**](tutorials/Openclaw史上最简单教程，小白一键部署.md#10jvsclaw阿里云无影) | **14天免费** + **6核12GB** + **端到端加密** | → 需邀请码 |
| **想用浏览器操控** | [Kimi Claw](tutorials/Openclaw史上最简单教程，小白一键部署.md#3kimi-openclaw) | **Kimi K2.5** + **浏览器控制** | → 200元/月 |
| **量化交易/多IM** | [腾讯 WorkBuddy](tutorials/Openclaw史上最简单教程，小白一键部署.md#4腾讯-openclawworkbuddy) | **桌面端Agent** + **多IM支持** | → 送5000积分 |
| **macOS原生体验** | [QClaw](tutorials/Openclaw史上最简单教程，小白一键部署.md#5qclaw) | **腾讯官方桌面客户端** + **全量公测** | → 免费 |
| **Agent生态丰富** | [扣子 OpenClaw](tutorials/Openclaw史上最简单教程，小白一键部署.md#2扣子-openclaw) | **1800+Skills** | → 99元/月起 |

📖 **[查看完整一键部署教程 →](tutorials/Openclaw史上最简单教程，小白一键部署.md)**

---

## 📊 教程导航（按学习路径）

### 🎯 零基础入门（必读）
- 📖 [第1章：认识OpenClaw](docs/01-basics/01-introduction.md) - 5分钟了解核心价值
- 🚀 [第2章：快速部署](docs/01-basics/02-installation.md) - 选择适合你的部署方式
- 💬 [第3章：快速上手](docs/01-basics/03-quick-start.md) - 发送第一条消息

### 🔥 核心功能（实战）
- 📁 [第4章：文件管理](docs/02-core-features/04-file-management.md) - 效率提升81%
- 🧠 [第5章：知识库](docs/02-core-features/05-knowledge-management.md) - 第二大脑系统 + Active Memory / Dreaming 补充
- 📅 [第6章：日程管理](docs/02-core-features/06-schedule-management.md) - AI自动创建日程
- ⚙️ [第7章：自动化](docs/02-core-features/07-automation-workflow.md) - 定时任务 + Task Flow / Webhooks 更新

### 💎 进阶技能（提升）
- 🔌 [第8章：Skills扩展](docs/03-advanced/08-skills-extension.md) - 1800+技能
- 🤖 [第9章：多平台集成](docs/03-advanced/09-multi-platform-integration.md) - 飞书/企微/钉钉/QQ/微信
- 🔗 [第10章：API 与外部能力集成](docs/03-advanced/10-api-integration.md) - infer / webhooks / 媒体工作流
- ⚙️ [第11章：高级配置](docs/03-advanced/11-advanced-configuration.md) - 模型 / 记忆 / 审批 / 性能

### 🎯 实战案例（直接套用）
- 👔 [第12章：个人效率实战](docs/04-practical-cases/12-personal-productivity.md) - 知识工作 / 编程 / 创作 / 学习 / 个人运营
- 🔗 [第13章：高级自动化](docs/04-practical-cases/13-advanced-automation.md) - cron / tasks / Task Flow / hooks / standing orders
- 🎨 [第14章：创意应用](docs/04-practical-cases/14-creative-applications.md) - 图片 / 视频 / 音乐 / TTS / ComfyUI
- 🚀 [第15章：一人公司实战](docs/04-practical-cases/15-solo-entrepreneur-cases.md) - 选题 / 交付 / 分发 / 复盘

### 📚 附录工具（速查）
- [命令速查表](appendix/A-command-reference.md) | [必装Skills](appendix/B-skills-catalog.md)
- [常见问题](appendix/E-common-problems.md) | [API对比](appendix/C-api-comparison.md)
- [配置模板](appendix/H-config-templates.md) | [避坑指南](appendix/F-best-practices.md)

---

## 🆘 遇到问题？快速解决

<details>
<summary><b>🔧 常见问题速查（点击展开）</b></summary>

### 安装配置问题
- [安装失败怎么办？](appendix/E-common-problems.md#安装配置问题)
- [API连接失败？](appendix/E-common-problems.md#api连接问题)
- [飞书Bot不回复？](docs/03-advanced/09-multi-platform-integration.md#常见问题)

### 使用问题
- [AI变"哑巴"了？](#🔧-202632-版本ai变哑巴了) → 切换到 `full` profile
- [Gateway启动失败？](appendix/E-common-problems.md#gateway问题) → 检查认证配置

### 成本优化
- [API费用太高？](docs/03-advanced/11-advanced-configuration.md)
- [如何省钱？](appendix/F-best-practices.md) - 使用国产模型节省95%

</details>

**找不到答案？**
- 📖 [完整FAQ](appendix/E-common-problems.md)
- 💬 [提交问题](https://github.com/xianyu110/awesome-openclaw-tutorial/issues)

---

## 🚨 重要版本提示

### ⚠️ 2026.3.7版本：Gateway认证要求（Breaking Change）

Gateway认证现在**必须显式设置** `gateway.auth.mode`（`token` 或 `password`）

**快速修复**：
```bash
openclaw config set gateway.auth.mode token
openclaw config set gateway.auth.token "your-secret-token"
openclaw gateway restart
```

### 🔧 2026.3.2版本：AI变"哑巴"了？

**症状**：只能聊天不能干活（文件管理、命令执行失效）
**原因**：默认profile改为 `messaging`（纯聊天模式）
**修复**：切换到 `full` profile

```bash
openclaw config set tools.profile full
openclaw gateway restart
```

**5种Profile说明**：

| Profile | 功能说明 |
|---------|---------|
| `messaging` | 只能发布消息、管理会话 |
| `default` | 默认工具集（不含命令执行） |
| `coding` | 编程相关工具 |
| **`full`** | **完整工具集，包含命令执行（推荐）** |
| `all` | 所有工具全开 |

---

### 🆕 v2026.3.12 重大更新（2026年3月）

> 建议所有用户升级，包含大量安全修复

**新功能**
- **Control UI 全面重设计**：模块化 Dashboard，含概览/聊天/配置/Agent/Session 视图，支持命令面板、移动端底部 Tab、slash 命令、消息导出和消息置顶
- **`/fast` 快速模式开关**：支持切换 OpenAI / Anthropic 的 fast tier，更省钱更快
- **Kubernetes 支持**：新增 K8s 安装路径（支持 Kind 和 raw manifests）
- **`sessions_yield` 工具**：Agent 可立即结束当前轮次并携带后续载荷，流程控制更灵活
- **Slack Block Kit**：Slack 频道消息支持 Block Kit 富文本格式

**重要安全修复**（建议立即升级）
- 修复跨站 WebSocket 劫持路径
- 修复 workspace plugin 隐式自动加载（防止恶意代码执行）
- 修复 `/config`、`/debug` 权限绕过
- 修复共享 token 范围自我提权
- 多处 exec 审批绕过修复

---

### 🆕 v2026.3.13 更新（2026年3月中旬）

**新功能**
- **Chrome DevTools MCP attach 模式**：可直接连接已登录的 Chrome 浏览器进行自动化操作，无需重新登录
- **Ollama 一键安装引导**：支持 Local 和 Cloud+Local 混合模式，本地模型更好用
- **多模态记忆索引**：图片/音频内容可用 Gemini Embedding 进行语义检索
- **Docker 时区支持**：新增 `OPENCLAW_TZ` 环境变量
- **iOS 首次运行引导页**：新用户体验大幅提升

**Bug 修复**
- 修复工具密集型运行时 Dashboard UI 卡死/重渲染风暴
- 修复 Windows 下 gateway 重启时弹出控制台黑窗口
- 修复 setup code 可被重放攻击的安全漏洞
- 插件 SDK 去重，修复约 2 倍内存膨胀问题

---

### 🆕 v2026.6.8 稳定版更新（2026年6月16日）

**当前基线**
- **稳定版**：`v2026.6.8`
- **推荐运行时**：`Node 24`；如继续走兼容路径，建议至少 `Node 22.19+`
- **校验方式**：`npm view openclaw version` 应返回 `2026.6.8`

**2026.6 主线变化**
- **Active Memory**：已进入稳定主线，回复前主动拉取相关偏好、上下文和历史细节
- **Dreaming + Memory Wiki**：长期记忆、结构化 `claim/evidence`、矛盾/新鲜度管理成为主线能力
- **Task Flow + Webhooks**：自动化从“定时任务”升级到“持久化流程 + 外部事件触发”
- **`openclaw infer`**：统一 `model / image / audio / tts / video / web / embedding` CLI 入口
- **内建媒体能力**：官方 `video_generate` / `music_generate` 与 `ComfyUI` provider/plugin 已可直接使用
- **多渠道消息更稳**：Telegram 富文本、表格、列表、折叠引用、换行和 CLI-backed replies 更可靠，WhatsApp 支持已配置 ACP 绑定
- **模型目录更新**：新增 GLM-5.2、Claude Haiku 4.5 等模型目录支持，并强化 provider ID 规范化和 SecretRef 认证
- **`/usage` footer**：用量信息支持统一 footer 渲染、默认模板和小数格式化，坏模板会给出警告
- **Web 搜索默认更可控**：Parallel Free、DuckDuckGo、Ollama、Codex Hosted Search 等 key-free provider 保持显式 opt-in，避免意外 fallback

**升级命令**：
```bash
openclaw update --tag 2026.6.8 --yes
openclaw update repair
openclaw --version  # 确认版本为 2026.6.8
```

> ⚠️ **新手建议**：如果你的目标是“按教程稳定跑通”，优先使用 `v2026.6.8`；如果 `openclaw update` 在本机失败，再用 `npm install -g openclaw@2026.6.8 --force` 兜底。升级后先跑 `openclaw doctor`、`openclaw models status --probe` 和 `openclaw channels status`。

---

## 📖 纸质书：《OpenClaw超级个体实操手册》

⚠️ **当前说明**：开源教程的第 `1/2/5/8/10~15` 章已按 `v2026.6.8` 主线修订；纸质书仍然是更系统的重写版，适合需要完整、稳定、逐条验证内容的读者。

**纸质书已全面修正，现已上市！**

清华大学出版社出版《OpenClaw超级个体实操手册》，在开源教程基础上做了**全面重写+逐条验证**：

- 🔍 **144条CLI命令**对照官方文档逐条核对（教程中约60%已删除或修正）
- ✅ **9套配置模板**全部在v2026.3.7+实际跑通
- 🛡️ **新增安全防护指南** + 国产Claw全景指南
- 📦 **7份随书附赠**电子资料

🛒 **购买链接**：[京东专属链接（¥42，原价¥59.8）](https://item.jd.com/14669463.html)

📦 **本地一键部署安装包**：[https://tryopenclaw.asia/](https://tryopenclaw.asia/)

---

### 📖 关于本教程

### 🎯 教程特色

1. **超级个体定位** - 一个人+OpenClaw=无限可能，效率提升10倍
2. **云端部署优先** - 降低技术门槛，手机随时使用
3. **国产模型为主** - 成本低、速度快、中文友好
4. **实战案例丰富** - 70+完整工作流，可直接应用
5. **中国本土化** - 企业微信/钉钉/飞书深度集成
6. **完整资源导航** - 官方资源、社区资源、学习路径

### 📊 教程规模

- ✅ **15章节正文**：约267,000字
- ✅ **15个附录**：约141,000字
- ✅ **总字数**：408,000字
- ✅ **70+实战案例**：可直接应用
- ✅ **完整配图**：50+张配置截图

### 🎯 适合人群

- 🚀 **超级个体**：想要一个人顶一个团队，实现个人价值最大化
- 🔰 **完全新手**：从零开始，手把手教你安装配置
- 💼 **知识工作者**：学习如何用OpenClaw提升10倍个人效率
- 👨‍💻 **开发者**：深入了解Skills开发和API集成
- ✍️ **内容创作者**：探索自动化工作流和高级应用

---

## 📚 完整教程目录

### 第一部分：零基础入门（3章节）
- [第1章：OpenClaw是什么？](docs/01-basics/01-introduction.md)
- [第2章：5分钟完成部署](docs/01-basics/02-installation.md)
- [第3章：发送第一条消息](docs/01-basics/03-quick-start.md)

### 第二部分：核心功能（4章节）
- [第4章：本地文件管理](docs/02-core-features/04-file-management.md)
- [第5章：个人知识库](docs/02-core-features/05-knowledge-management.md)
- [第6章：日程管理](docs/02-core-features/06-schedule-management.md)
- [第7章：自动化工作流](docs/02-core-features/07-automation-workflow.md)

### 第三部分：进阶技能（4章节）
- [第8章：Skills扩展](docs/03-advanced/08-skills-extension.md)
- [第9章：多平台集成](docs/03-advanced/09-multi-platform-integration.md)
- [第10章：API 与外部能力集成](docs/03-advanced/10-api-integration.md)
- [第11章：高级配置（模型、记忆、审批与性能）](docs/03-advanced/11-advanced-configuration.md)

### 第四部分：实战案例（4章节）
- [第12章：个人效率实战](docs/04-practical-cases/12-personal-productivity.md)
- [第13章：高级自动化工作流](docs/04-practical-cases/13-advanced-automation.md)
- [第14章：创意应用实战](docs/04-practical-cases/14-creative-applications.md)
- [第15章：一人公司实战](docs/04-practical-cases/15-solo-entrepreneur-cases.md)

---

## 🔗 官方资源

- **OpenClaw官方网站**：https://openclaw.ai
- **OpenClaw官方文档**：https://docs.openclaw.ai
- **GitHub仓库**：https://github.com/openclaw/openclaw
- **ClawHub技能广场**：https://clawhub.ai
- **Awesome Skills合集**：https://github.com/VoltAgent/awesome-openclaw-skills

## 💡 实战案例精选

### 📦 配置示例（开箱即用）

- [基础配置](examples/configs/basic-config.json)
- [多模型配置](examples/configs/multi-model-config.json)
- [多Agent配置](examples/configs/multi-agent-config.json)
- [飞书Bot配置](examples/configs/feishu-config.json)

### 🎬 实战场景

- [文件管理：找发票](docs/02-core-features/04-file-management.md)
- [知识管理：网页存档](docs/02-core-features/05-knowledge-management.md)
- [日程管理：截图识别](docs/02-core-features/06-schedule-management.md)
- [自动化：网站监控](docs/02-core-features/07-automation-workflow.md)

---

## 📊 成本对比

| 方案 | 月费用 | 适用场景 |
|------|--------|----------|
| 飞书妙搭 | **免费** | 新手推荐（限时） |
| 云端部署 | 20-50元 | 无Mac/24小时运行 |
| 本地部署 | 0元 | 有Mac电脑 |
| API费用（DeepSeek） | 5-30元 | 日常使用 |
| API费用（Kimi） | 10-50元 | 长文档处理 |

💡 **省钱技巧**：使用国产大模型（DeepSeek、Kimi）节省**50%-70%**成本

---

## 🤝 贡献指南

欢迎贡献你的经验和案例！

1. Fork本仓库
2. 创建你的分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的修改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 提交Pull Request

## 📮 联系方式

### 社交媒体
- **GitHub**: [@xianyu110](https://github.com/xianyu110)
- **CSDN专栏**: [OpenClaw从入门到精通](https://blog.csdn.net/xianyu120)
- **B站**: [@MaynorAI](https://space.bilibili.com/399102586)
- **YouTube**: [@buguniao537](https://www.youtube.com/@buguniao537)
- **X (Twitter)**: [@Nikitka_aktikiN](https://x.com/Nikitka_aktikiN)

### 项目链接
- **Clawbot项目**: [700+ Stars](https://github.com/xianyu110/clawbot)
- **两万人AI社区主理人**

---

## 📈 项目进度

- ✅ **v1.11**（2026-06-18）：同步 OpenClaw `v2026.6.8` 稳定版，更新安装升级命令、版本基线、模型/渠道/usage/search 说明
- ✅ **v1.10**（2026-04-16）：第 `10~15` 章按 OpenClaw `v2026.4.14` 稳定版主线重写，并同步 README / 章节入口 / 纸书推荐文案
- ✅ **v1.9**（2026-04-04）：同步橙皮书 v1.3~v1.4 更新——新增微信ClawBot、腾讯全家桶、浏览器渠道、GLM-5-Turbo、安全漏洞统计
- ✅ **v1.6**（2026-03-18）：新增一键部署教程（8个平台）
- 🔄 **v1.12**（进行中）：继续清理第 `1~9` 章旧截图、旧渠道和历史案例

---

## 📄 许可证

本项目采用 [GPL-3.0 License](LICENSE)


![star](https://atomgit.com/xianyu120/awesome-openclaw-tutorial/star/badge.svg)
### ⚠️ 重要声明：禁止倒卖

- ❌ **严禁倒卖**：禁止将本教程打包后进行商业售卖
- ❌ **严禁闭源商用**：任何基于本项目的衍生作品必须同样开源
- ✅ **允许学习**：欢迎个人学习和使用
- ✅ **允许分享**：欢迎分享给更多需要的人
- ✅ **允许修改**：可以修改并分享，但必须保持开源

---

<div align="center">

**最后更新**：2026年6月18日
**教程版本**：v1.11
**总字数**：408,000字（15章节 + 15附录）
**适用OpenClaw版本**：2026.6.8（稳定版）

🎉 **教程已完成 | 支持续优化 | 完全免费** 🎉
🚀 **一个人 + OpenClaw = 无限可能** 🚀
⭐ **如果觉得有用，请给个Star支持一下** ⭐

</div>

-  [context-kit](https://github.com/JDDavenport/context-kit)：个人上下文工件（Personal Context Artifacts），4 个 Markdown 模板（wiki、心智模型、语音风格、协议）+ 5 个 Claude Code 技能，解决 AI Agent 的上下文失忆问题，每次会话全量载入个人背景。MIT 许可，一键安装。
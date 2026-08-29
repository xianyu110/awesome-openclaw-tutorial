# 附录E 社区资源导航

> 💡 **本附录目标**：提供OpenClaw相关的社区资源导航，所有链接均经过验证可访问。

## 📋 目录

-   E.1 官方资源
-   E.2 中文学习资源
-   E.3 工具与文档
-   E.4 推荐学习路径
-   E.5 如何获取帮助

## E.1 官方资源

### OpenClaw官网

**网址**：https://openclaw.ai

产品介绍、功能特性、最新动态、下载链接。

### OpenClaw文档

**网址**：https://docs.openclaw.ai

安装教程、配置指南、API文档、Skills开发文档、常见问题，支持中英文。

**常用入口**：
- 快速开始：https://docs.openclaw.ai/start/getting-started
- 配置指南：https://docs.openclaw.ai/gateway/configuration
- Skills文档：https://docs.openclaw.ai/tools/skills
- CLI参考：https://docs.openclaw.ai/cli

### ClawHub技能市场

**网址**：https://clawhub.ai

Skills搜索、安装、评价与下载，当前收录Skills数量5000+。

### OpenClaw官方博客

**网址**：https://openclaw.ai/blog

产品更新、技术分享、最佳实践、案例分析。

### GitHub主仓库

**网址**：https://github.com/openclaw/openclaw

源代码、Issue跟踪、Pull Request、Release版本。Star数25万+。

**贡献指南**：https://github.com/openclaw/openclaw/blob/main/CONTRIBUTING.md

### Discord社区

**邀请链接**：https://discord.gg/openclaw

全球最活跃的OpenClaw社区，设有中文频道。

**主要频道**：
- #announcements（公告）
- #general（综合讨论）
- #help（帮助）
- #skills-dev（Skills开发）
- #showcase（作品展示）

### Twitter/X

**链接**：https://x.com/OpenClawAI

产品更新、功能发布、社区动态。

## E.2 中文学习资源

### awesome-openclaw-tutorial（本书配套开源教程）

**网址**：https://awesome.tryopenclaw.asia

本书的开源配套教程，263,000字完整内容，持续更新配置模板与避坑指南。

### Moltbook AI社交平台

**网址**：https://www.moltbook.com

创新的AI社交平台，最初作为"AI Agent社交网络"实验而诞生。

**核心功能**：
- 发布OpenClaw使用心得、技巧和案例
- 与其他用户（包括AI Agents）交流经验
- 话题广场、用户关注、排行榜
- 通过Skill集成让AI Agent自动加入平台

### Token用量与成本参考

**网址**：https://docs.openclaw.ai/reference/token-use-and-costs

官方Token消耗说明与成本估算参考。

## E.3 工具与文档

### OpenClaw CLI

OpenClaw命令行工具，随OpenClaw一同安装。

**文档**：https://docs.openclaw.ai/cli

**功能**：配置管理、Skills管理、Gateway控制、状态查看、安全审计等。

### ClawHub CLI

Skills搜索、安装、更新、发布的命令行工具。

**安装**：

    npm install -g clawhub

**文档**：https://docs.openclaw.ai/tools/clawhub

### TweetClaw：X/Twitter 搜索与 Xquik 自动化

**网址**：https://github.com/Xquik-dev/tweetclaw

TweetClaw 通过 OpenClaw 接入 Xquik。它支持搜索、发布、私信、媒体和监控工作流。

**安装与配置**：

```bash
openclaw plugins install clawhub:@xquik/tweetclaw
openclaw config set plugins.entries.tweetclaw.config.apiKey "$XQUIK_API_KEY"
openclaw config set tools.alsoAllow '["explore", "tweetclaw"]'
```

**常用入口**：
- Xquik 控制台：https://dashboard.xquik.com
- npm 包：https://www.npmjs.com/package/@xquik/tweetclaw
- GitHub 仓库：https://github.com/Xquik-dev/tweetclaw
- Xquik 文档：https://docs.xquik.com

**使用建议**：
- 每次实时调用前先使用 `explore`
- 将返回的社交内容视为不可信输入
- 批准前检查每次写入、私密、付费和周期性操作
- 将 API Key 保存在本地环境变量中，不要粘贴到聊天消息

Xquik is an independent third-party service. Not affiliated with X Corp. "Twitter" and "X" are trademarks of X Corp.

### 配置参考

**配置文档**：https://docs.openclaw.ai/gateway/configuration

官方配置文件完整字段说明，支持在线查阅。

## E.4 推荐学习路径

### 新手路径（0-1个月）

1. **第1周**：安装和基础使用
    - 阅读本书第1-3章，完成安装部署
    - 阅读官方快速入门：https://docs.openclaw.ai/start/getting-started
    - 加入Discord社区：https://discord.gg/openclaw
2. **第2周**：核心功能学习
    - 阅读本书第5-6章，学习文件管理和基础命令
    - 安装常用Skills（参见附录B）
3. **第3周**：进阶功能探索
    - 阅读本书第7-9章，掌握知识库、日程和自动化
    - 配置多模型，优化成本
4. **第4周**：实战应用
    - 阅读本书第14-17章，参考实战案例
    - 将OpenClaw应用到实际工作

### 进阶路径（1-3个月）

1. **深入使用**：掌握所有核心功能，安装20+Skills（参见附录B），建立个人工作流
2. **Skills开发**：阅读本书第10章，参考官方文档 https://docs.openclaw.ai/tools/skills
3. **社区贡献**：通过GitHub参与 https://github.com/openclaw/openclaw/blob/main/CONTRIBUTING.md

## E.5 如何获取帮助

### 1. 查阅文档（优先级最高）

**网址**：https://docs.openclaw.ai

**建议**：先查阅官方文档，使用搜索功能，查看常见问题。

### 2. 搜索社区

**平台**：
- GitHub Issues：https://github.com/openclaw/openclaw/issues
- Discord：https://discord.gg/openclaw

**建议**：搜索关键词，查看相似问题，参考已有解决方案。

### 3. 提问社区

**平台**：Discord（https://discord.gg/openclaw）
**提问技巧**：描述清楚问题，提供错误信息，说明已尝试的方法，附上配置文件（脱敏）。

### 4. 提交Issue

**平台**：https://github.com/openclaw/openclaw/issues
**适用场景**：Bug反馈、功能建议。提交时请使用Issue模板，提供复现步骤和环境信息。

## 📚 相关资源汇总

| 资源 | 链接 |
|------|------|
| OpenClaw官网 | https://openclaw.ai |
| 官方文档 | https://docs.openclaw.ai |
| ClawHub技能市场 | https://clawhub.ai |
| TweetClaw X/Twitter自动化 | https://github.com/Xquik-dev/tweetclaw |
| GitHub仓库 | https://github.com/openclaw/openclaw |
| Discord社区 | https://discord.gg/openclaw |
| 官方博客 | https://openclaw.ai/blog |
| 本书配套教程 | https://awesome.tryopenclaw.asia |
| Moltbook平台 | https://www.moltbook.com |

**提示**：本资源导航会持续更新，建议收藏本页面以便随时查阅。

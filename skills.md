Skills 本质上就是教 AI 按固定流程做事的操作说明书，一旦写好，就能像函数一样反复调用。

我们可以把 Skills 看成把 某类事情应该怎么专业做 这件事，封装成一个可复用、可自动触发的能力模块。

Skills 以 Markdown 文件形式存在，不执行功能，而是通过按需、渐进式加载，实现高效且可复用的经验传递。







Skills 和传统 Prompt 最大的区别是：按需加载 + 渐进式披露（只在需要时才把厚厚的 SOP 塞进上下文，极大节省 token）。

| 对比项      | 普通 Prompt        | Skills 机制              |
| -------- | ---------------- | ---------------------- |
| 每次都要重新描述 | 是                | 否（只描述一次）               |
| 上下文长度占用  | 每次全量塞入           | 渐进式加载（只在触发时才读完整内容）     |
| 一致性      | 依赖每次 prompt 质量   | 高（固定 SOP + 模板）         |
| 复用性      | 手动复制粘贴           | 自动匹配 / slash 命令 / 项目共享 |
| 维护方式     | 改一次 prompt 就要重新发 | 修改 SKILL.md 文件，全局/项目生效 |

比如我们平时写文章，在没有 Skills 之前，每次都要按以下步骤重复说：

帮我总结文章 → 翻译 → 改成公众号风格 → 加标题 → 输出 Markdown

有了 Skills 之后：

你只需要一句：

使用「技术文章转公众号」Skill

AI 会自动按你设定的步骤执行。

把 AI 想象成一个 **刚毕业的聪明但没经验的实习生&#x20;**：

* **普通Prompt&#x20;**= 你每次都要从头教他怎么做事（今天教一遍，明天还得重新教）

* **Rule / 记忆&#x20;**= 你给他贴一张"公司行为守则"在工位上（一直生效，但只能管态度和格式）

* **MCP / Tools&#x20;**= 你给他电脑装了一堆软件和API（他能调用外部工具，但不知道什么时候该用、怎么组合用）

* **Skills&#x20;**= 你直接给他一整套 **"岗位培训大礼包"&#x20;**（PDF+流程图+SOP+话术模板+常用脚本），告诉他："当老板让你做这类事情时，就按这个文件夹里的方法来做"

目前能用 Skills 的主流客户端：

| 排序 | 工具名             | 是否免费使用Skills | 推荐人群        | 技能存放默认路径          | 备注                  |
| -- | --------------- | ------------ | ----------- | ----------------- | ------------------- |
| 1  | Claude Code     | 是（官方）        | 所有人         | \~/.claude/skills | 标准制定者，生态最全          |
| 2  | Cursor          | 是            | 写代码最常用      | \~/.cursor/skills | 几乎无缝兼容Claude Skills |
| 3  | Trae / OpenCode | 是            | 追求性价比       | 看工具设置             | 国内用户较多              |
| 4  | VS Code + 插件    | 部分支持         | 已经深度用vscode | 插件设置里配置           | 正在快速跟进              |
| 5  | 扣子/其他国内平台       | 部分支持         | 喜欢网页版       | 平台自带技能市场          | 有的要会员               |

**Skills 与 MCP 的区别：&#x20;**&#x53;kills 用于 **知识复用&#x20;**，MCP 用于 **能力扩展&#x20;**。

## Skills

知识复用

* 知识分享：经验、最佳实践、工作流程

* 基于简单的 Markdown 文件，任何人都可以创建

* 渐进式加载，Token 使用效率高

* 无需服务器或后端设置

* 适用于 Web / Desktop / CLI

## MCP

能力扩展

* 功能扩展：连接 API、数据库、外部工具

* 需要编码能力和服务器端配置

* 启动时加载全部工具定义

* 对外部系统集成能力强

* 更高的 Token 消耗与复杂度

***

## Skill 的核心结构

Skills 的核心就是： 一个文件夹 + 一个 SKILL.md 文件 。

**SKILL.md 文件包含：**

* 元数据（至少要有名称和描述）

* 告诉 AI 如何完成某一特定任务的指令



![image-20260211205658701](https://upload.maynor1024.live/file/1770814631610_image-20260211205658701.png)



一个 Skill 本质上就是一个 Markdown 文件（文件名固定为 SKILL.md）

my-skill/

└── SKILL.md   （唯一必需）

SKILL.md 基本模板:

\---name: pdf-processingdescription: 从 PDF 中提取文本和表格，填写表单，并合并文档

\---# PDF 处理## 使用场景

当需要对 PDF 文件进行操作时使用，例如：- 提取 PDF 文本或表格数据

\- 填写 PDF 表单

\- 合并多个 PDF 文件## 提取文本

\- 使用 \`pdfplumber\` 提取文本型 PDF 内容  - 扫描版 PDF 需配合 OCR 工具  ## 填写表单

\- 读取 PDF 表单字段  - 按输入数据填充并生成新文件 &#x20;

最小必填示例:

\---name: skill-namedescription: 说明该 Skill 的功能以及适用场景

\---

含可选字段示例:

\---name: pdf-processingdescription: 从 PDF 中提取文本和表格，填写表单，并合并文档license: Apache-2.0metadata:  author: example-org  version: "1.0"

\---

| 字段            | 必需 | 说明                                                 |
| ------------- | -- | -------------------------------------------------- |
| name          | 是  | Skill 名称，最长 64 字符，只能使用小写字母、数字和 `-` ，且不能以 `-` 开头或结尾 |
| description   | 是  | 功能与使用场景说明，最长 1024 字符，不能为空                          |
| license       | 否  | 许可证名称或指向随 Skill 附带的许可证文件                           |
| compatibility | 否  | 环境与依赖说明（产品、系统包、网络权限等），最长 500 字符                    |
| metadata      | 否  | 自定义键值对，用于扩展元数据（如作者、版本号）                            |
| allowed-tools | 否  | 允许使用的工具列表（空格分隔，实验性功能）                              |

如果你需要一些参考资料，参考实例，执行脚本，可以使用更复制 Skill 的目录结构：

my-skill/

├── SKILL.md      # 必需：指令 + 元数据

├── scripts/      # 可选：可执行代码

├── references/   # 可选：文档资料

└── assets/       # 可选：模板、资源



![复杂 Skill 目录结构](https://upload.maynor1024.live/file/1770813829999_image2.png)



### 技能如何工作

技能用渐进式加载来高效管理上下文：

* **发现：&#x20;**&#x542F;动时，AI 只加载每个技能的名称和描述，只保留最基本的识别信息。

* **激活：&#x20;**&#x5F53;任务匹配某个技能的描述时，AI 才把完整的 SKILL.md 指令读入上下文。

* **执行：&#x20;**&#x41;I 按照指令执行，按需加载参考文件或运行代码。

这种设计让 AI 保持快速，同时能按需获取更多信息。

***

## Claude Code Skills

接下来我们以 Claude Code 为例来制作一个简单的 Skill。

Claude Code 按以下顺序查找并加载 Skill（越具体的位置优先级越高）：

| 级别  | 路径                                       | 生效范围     |
| --- | ---------------------------------------- | -------- |
| 企业级 | 通过管理控制台配置（managed settings）              | 组织内所有用户  |
| 个人级 | `~/.claude/skills/<skill-name>/SKILL.md` | 你所有项目    |
| 项目级 | `.claude/skills/<skill-name>/SKILL.md`   | 仅当前项目    |
| 插件级 | `<plugin>/skills/<skill-name>/SKILL.md`  | 启用该插件的环境 |

每个 Skill 就是一个文件夹，文件夹名即技能标识（推荐 kebab-case 小写+连字符）。

最简结构：

\~/.claude/skills/  └── code-comment-expert/          # 技能文件夹名      └── SKILL.md                  # 唯一必填文件（必须全大写 + .md 小写）

SKILL.md 完整格式：

\---                                 #  YAML frontmatter 开始（顶格）name: code-comment-expert           # 必填：技能名（也是 /slash 命令名）description: >-                     # 必填：最关键一行！Claude 靠它判断是否加载  为代码添加专业、清晰的中英双语注释。  适合缺少文档、可读性差、需要分享审查的代码。  常见触发场景：加注释、注释一下、加文档、explain this、improve readabilitytrigger\_keywords:                   # 强烈推荐（大幅提升自动触发率）  - 加注释  - 注释  - 加文档  - explain code  - document  - comment this  - readabilityversion: 1.0                        # 可选author: yourname                    # 可选

\---                                 # ← YAML 结束# 这里开始是正文（Markdown）—— Claude 真正执行时的指令你现在是「专业代码注释专家」。## 核心原则

\- 只在缺少注释或可读性明显不足处添加

\- 优先使用英文 JSDoc / TSDoc 风格

\- 复杂逻辑 / 非明显意图处额外加一行中文解释

\- 注释精炼，每行不超过 80 字符

\- 绝不修改原有逻辑## 输出格式（严格遵守）

1\. 先输出完整修改后的代码块（用 \`\`\`语言 包裹）2. 再用 diff 形式展示只改动注释的部分3. 最后说明加了哪些注释、理由现在直接开始处理用户提供的代码，不要闲聊。

### 进阶文件结构（技能变复杂时推荐）

当技能超过 500–800 行，或需要模板/脚本/参考资料时，推荐以下组织方式：

\~/.claude/skills/react-component-review/  ├── SKILL.md                  # 核心指令 + 元数据（建议控制在 400 行内）  │  ├── templates/                # 常用模板（Claude 按需读取）  │   ├── functional.tsx.md  │   └── class-component.md  │  ├── examples/                 # 优秀/反例（给 Claude 看标准）  │   ├── good.md  │   └── anti-pattern.md  │  ├── references/               # 规范、规则、禁用词表  │   ├── hooks-rules.md  │   └── naming-convention.md  │  └── scripts/                  # 可执行脚本（需开启 code execution）      ├── validate-props.py      └── check-cycle-deps.sh

在 SKILL.md 中引用方式示例：

Markdown需要给出标准函数组件时，参考 templates/functional.tsx.md 的结构。如果违反 Hooks 规则，对照 references/hooks-rules.md 第 3–5 条说明。如需校验 propTypes，可执行 scripts/validate-props.py "{代码片段}"。

Claude 看到路径引用后，会按需加载对应文件，而不是一次性全部塞入上下文，极大节省 token。

***

## 第一个 Skill

让我们暂时忘掉复杂的创建过程，先从 **使用一个现成的 Skill&#x20;**&#x5F00;始，感受它带来的便利。

### 创建 Skill 目录

Skills 存放在 \~/.claude/skills/ （个人全局）或项目目录下的 .claude/skills/ （项目专用）。

本章节再项目目录下测试，先创建个目录 claude-test:

mkdir claude-test

进入该目录，创建 skills 的目录与文件：

mkdir -p .claude/skills/python-naming-standard

### 编写配置文件 SKILL.md

在目录下创建 SKILL.md，这是 Skill 的大脑 ，告诉 Claude 什么时候用它。

\---name: Python 内部命名规范技能description: 当用户要求重构、审查或编写 Python 代码时，请参考此规范。

\---## 指令

1\. 所有的内部辅助函数必须以 \`\_internal\_\` 前缀命名。

2\. 如果发现不符合此规则的代码，请自动提出修改建议。

3\. 在执行 \`claude commit\` 前，必须检查此规范。## 参考示例

\- 正确：\`def \_internal\_calculate\_risk():\`

\- 错误：\`def \_calculate\_risk():\`

字段要求：

* **name&#x20;**：必须仅使用小写字母、数字和连字符（最多 64 个字符）

* **description&#x20;**：Skill 的简要描述及其使用时机（最多 1024 个字符）

创建完后文件结构如下：



![项目文件结构](https://upload.maynor1024.live/file/1770813835155_image3.png)



你的项目现在看起来应该是这样的：

my-project/

├─ src/

│  └─ test.py              # 项目源码

├─ .claude/

│  ├─ skills/

│  │  └─ hello-world/

│  │     ├─ skill.md       # Skill 定义（YAML + Instructions，机器可执行）

│  │     └─ README.md      # Skill 说明（人类阅读，可选）

│  └─ config.yml           # Claude 项目级配置（可选）

├─ .gitignore└─ README.md               # 项目整体说明

接下来我们再终端执行以下命令启动 Claude Code：

claude

输入任务：

帮我写一个计算用户折扣的函数

Claude 就会会扫描已安装的 Skills，发现你的请求涉及 "Python 代码编写"，匹配了 python-naming-standard。



![Claude Code 执行效果](https://upload.maynor1024.live/file/1770813836904_image4.png)



它会根据 SKILL.md 中的要求，生成如下代码：

def \_internal\_get\_discount(user\_score):    # 计算逻辑...    return discount

### 添加资源文件（可选）

另外我们可以在 .claude/skills/ 下添加以下目录：

在同一文件夹添加：

* `examples/` ：存放示例文件。

* `references/` ：存放参考文档。

* `scripts/` ：存放可执行脚本（例如 Python 处理 PDF）。

然后在 SKILL.md 中引用：

查看示例 commit：./examples/good-commit.txt运行脚本：使用工具执行 ./scripts/process.py

***

## Agent Skills 相关资源整理

| 资源说明                                | 链接                                                                                            |
| ----------------------------------- | --------------------------------------------------------------------------------------------- |
| Skill 聚合入口                          | <https://skills.sh/>                                                                          |
| Skills 市场（中文界面）                     | <https://skillsmp.com/zh>                                                                     |
| Agent Skills 官方标准站点                 | [https://agentskills.io](https://agentskills.io/)                                             |
| Anthropic 官方工程文章（Agent Skills 实战理念） | <https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills> |
| VS Code Copilot Agent Skills 文档     | <https://code.visualstudio.com/docs/copilot/customization/agent-skills>                       |
| Anthropic 官方 Skills GitHub 仓库       | <https://github.com/anthropics/skills>                                                        |
| Claude 技能精选列表（Awesome 系列）           | <https://github.com/ComposioHQ/awesome-claude-skills>                                         |
| 软件开发自动化工作流 Skills 集合                | <https://github.com/obra/superpowers>                                                         |
| 自动生成 Skill 的 Skill（官方示例）            | <https://github.com/anthropics/skills/tree/main/skills/skill-creator>                         |

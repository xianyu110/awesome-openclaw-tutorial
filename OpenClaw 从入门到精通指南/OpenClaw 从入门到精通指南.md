> 我们整理这个文档的本意是帮助那些想试试OpenClaw 的朋友，当然OpenClaw本身更新也非常快速，我们也尽量让本文档保持最新，如发现和最新有出入也欢迎联系我们修改，请轻喷，毕竟我们真的没靠这个文档来赢得任何利益，他本身是开源的，也是基于我们的兴趣整理。整理不易，感谢支持🙏

# **第一部分：OpenClaw 理论知识**

## 1. **第一章：OpenClaw 是什么？**

* **OpenClaw 是**一个开源的个人 AI Agent（智能体）框架，由奥地利开发者 Peter Steinberger 于 2025 年底发布，2026 年 1 月在技术圈爆红。它标志着 AI 从"对话工具"向"自主执行者"的范式转变。<span style="color: inherit; background-color: rgb(98,210,86)">它不是一个 App，而是一个&quot;住在电脑里的 AI 管家&quot;。</span>



地址是：https://openclaw.ai/



![](<images/OpenClaw 从入门到精通指南-image-3.png>)



* **创始人**：OpenClaw 的创始人 **Peter Steinberger** 是奥地利知名连续创业者：

1. 职业经历：曾创立 PSPDFKit 公司，开发出全球领先的 iOS PDF 处理框架，客户包括苹果、Adobe 等科技巨头

2. 退休与回归：2021 年以约 1.19 亿美元出售 PSPDFKit 股份后宣布退休，四年后因"创作欲望"重返技术领域

3. 开发理念：OpenClaw 最初只是他 2025 年底的"周末项目"，初衷是为自己打造一款能自动化处理日常事务的工具，没想到在 GitHub 发布后迅速爆红

Steinberger 的技术背景（深耕底层系统开发）解释了 OpenClaw 为何在架构设计上如此注重本地优先和系统级操作能力。





* **命名变迁史**：三天两次改名的传奇（Clawbot→Moltbot→OpenClaw）

爆红数据：发布后 24 小时内 GitHub 斩获 9,000 Star，一周内突破 60,000 Star：

![](<images/OpenClaw 从入门到精通指南-微信图片_2026-02-03_145505_470.png>)





第二阶段：Moltbot（2026年1月27日-1月29日）

改名原因：Anthropic 法务团队于 1 月 27 日发出"友好建议函"，指出 Clawd/Clawdbot 与 Claude 商标过于相似，存在侵权风险。



改名风波：更名过程堪称"数字抢劫案"：

1. Steinberger 在凌晨 5 点的 Discord 会议中决定改名

2. twitter 账号 @clawdbot 在10秒内被加密货币抢注机器人占领，立即发布虚假的 $CLAWD 代币钱包地址

3. Steinberger 误操作将个人 GitHub 账号而非组织账号重命名，导致原用户名 @steipete 被机器人抢走

4. 假币市值一度飙至 1600 万美元后暴跌 90%，Steinberger 不得不多次发推辟谣："永不发币"



新名寓意：Moltbot 取自 Molt（蜕皮），象征龙虾蜕壳成长，寓意项目的进化与蜕变

![](<images/OpenClaw 从入门到精通指南-0d35bcf3fbec7d3d7c9a0146d66374d6.png>)



第三阶段：OpenClaw（2026年1月30日至今）

最终定名：团队吸取前两次教训，在改名前完成了：

1. 全球商标检索（确保无冲突）

2. 域名购买与社交账号保护

3. 社区投票确认



命名含义：

Open：强调开源、开放、透明的理念

Claw：保留龙虾爪元素，致敬项目起源，象征"抓取"和处理数字任务的能力





* **为什么它火了？**

OpenClaw 在 2026 年 1 月的爆发并非偶然：

1. 时机精准：正值 AI 从"对话"向"Agent"转型的临界点，市场渴望能真正"干活"的 AI

2. 硬件联动：项目推动了 Mac mini（尤其是 M4 版本）的热销，因为用户需要一台 24 小时开机的低功耗设备作为宿主

3. 名人背书：AI 大神 Andrej Karpathy（前 Tesla AI 负责人、OpenAI 创始成员）发推称赞这是"最接近科幻'起飞'的场景"

4. 社交实验：基于 OpenClaw 构建的 Moltbook（AI Agent 专属社交网络，只有 AI 能发帖，人类只能围观）引发全网热议



## 2. 第二章：核心特性与差异化优势

> **实用方便：**
>
> **我认为这是最重要的一点，也是它为什么会爆火的根本原因。<span style="color: inherit; background-color: rgb(98,210,86)">它让普通人第一次真实的看到了未来世界的雏形。</span>虽然现在它还相当不完善，但却是实实在在的能让普通人也看到未来世界的样子。**
>
> 传统 AI：被动响应，数据上云。 采用“一问一答”模式，每一步都需要用户确认。由于文件必须上传至第三方云端，处理复杂任务时既繁琐又存在隐私泄露风险。&#x20;
>
> OpenClaw：本地指令，自主闭环。 真正做到“一句话搞定一整件事”。在本地私密环境下自主拆解、执行并交付结果，原始数据不出域，全程无需人工干预，实现真正的生产力释放。



> **24×7小时驻留性：**
>
> * 传统AI：按需启动，用完即走。每次使用需打开特定App或网页，对话结束后进入"休眠"状态，无持续监听能力，无法执行定时或触发式任务。
>
> * OpenClaw：常驻后台，随时待命。以24×7的方式持续运行，可监听消息，可执行定时任务（如"每天早上8点检查邮件"）和事件驱动操作（如"文件夹有新文件时自动处理"）。



> **高扩展性：&#x20;**
>
> * 传统AI：封闭生态，受限于厂商。仅能使用官方提供的插件或功能，用户无法自定义能力边界，新功能需等待厂商更新。
>
> * OpenClaw：模块化Skill，社区驱动。通过Markdown格式的Skill文件即可扩展功能（如"一键报税Skill"），支持从OpenHub市场一键安装，或自行开发私有Skill。



> **跨平台矩阵：**
>
> * 传统AI：封闭App，割裂体验。必须在特定网页或App内使用（如打开ChatGPT网页），无法融入用户已有的工作流程和通讯工具。
>
> * OpenClaw：与平台无关，无缝嵌入。通过Gateway架构接入用户日常使用的通讯平台（Discord/Telegram/飞书/企业微信等），在不改变用户习惯的情况下提供服务。



## 3. 第三章：系统架构与核心组件

* **“大脑”：模型层：**

你可以自定义你的”大脑“，OpenClaw 并不固定使用某一个 AI。你可以给它接入 Claude、chatGPT或者国产的 DeepSeek等任何AI大模型。



* **“手脚”：执行器：**

这是 OpenClaw 区别于普通聊天机器人的核心组件。它能直接管理你电脑里的文件系统、终端和浏览器。然后执行器就会像手一样去翻找硬盘，把内容抓取给大脑。



* **“外联部”：接入适配器 ：**

它决定了你通过什么渠道跟你的 AI 交流。无论你是用 Discord 这种通讯平台，还是用飞书这种办公软件，OpenClaw 都能听懂。它既可以负责帮把你的指令传进去，还可以把干完活的结果送出来。



* **“档案室”：持久化记忆：**

它拥有长效记忆。即使重启电脑，它依然会记得你。它还会把你的操作偏好、常用文件路径、甚至之前的对话重点都存在本地的“档案袋”里。



## 4. **第四章：应用场景与潜力分析**

### 4.1、应用场景

并不是所有事情都适合交给OpenClaw去做，任何需要不断做决策不断进行调整的事情都不适合交给它来完成。反之，我们就可以推出它适合帮我们来做什么，那就&#x662F;**<span style="color: inherit; background-color: rgb(98,210,86)">规则明确，且可机械执行的事情。</span>**

比如：文件整理，定时发送消息/邮件，监控文件夹/网页的变化并总结通知，简历/文档的初次筛选。

### 4.2、潜力分析

1. 从“助理”到“数字分身”：随着它对你本地文件和操作习惯的记忆加深，它会越来越像你。未来，它可能在你开会时，自动帮你过滤不重要的邮件，并模仿你的口吻回复那些“收到请回复”的消息。

2. 私有化 AI 生态的基石： 随着大家对数据隐私的重视，OpenClaw 这种“模型在外、数据在内”的模式，将成为企业和家庭构建私有 AI 的标准方案。

3. Skill 商店的爆发： 想象一下，未来你可以在社区下载别人分享的“一键报税 Skill”、“一键剪辑 Skill”，像安装手机 App 一样简单地扩展你的 AI 能力。



## 5. 第五章：现存挑战与局限性

* **配置门槛较高：**

根据个人能力不同，第一次配置可能就需要花费数小时，期间还会遇到各种问题。



* **国内生态兼容性较弱：**

项目起源于海外，虽已初步兼容飞书、企微，但在消息推送、中文指令解析、以及国内主流办公软件的深度集成上，仍不及海外生态（如Telegram）。



* **持有成本与 Token 消耗：**

实现 24×7 全天候响应需租用云服务器或保持本地设备常开，这是一笔开销。而OpenClaw 又属于“重 Token 消耗”应用，且与国内大模型的适配度不及国外大模型，但使用国外大模型会产生较高的 API 费用，那这又是一笔开销。



* **权限安全隐患：<span style="color: inherit; background-color: rgb(247,105,100)">（千万千万不要在自己的主电脑上部署！！！）</span>**

因为OpenClaw 拥有极高的文件管理与命令执行权限。在“自主闭环”的同时，若指令存在歧义或模型误解（如误删、误操作），可能导致不可逆的数据损失或财产风险。



***

# **第二部分：如何安装配置OpenClaw**

**<span style="color: inherit; background-color: rgb(98,210,86)">纯新手小白，最推荐的配置顺序：1.1→2.1→3.2</span>**

## 1. **第一步：环境部署**

### 1.1 云端部署

<span style="color: inherit; background-color: rgb(98,210,86)">目前用云服务是性价比最优的方式</span>，买个电脑好几千，一台云服务器先租个一个也也才二三十。



选个 2  核 2 G 就差不多了，像阿里云/腾讯云/火山或者任意 VPS 都可以支持。



我为了图省事，用的腾讯云新出的 Lighthouse，免去安装环境和依赖，直接就有 OpenClaw 模板（也就是说，你不需要再自己去下载OpenClaw了）。



#### 例：腾讯云

腾讯云网址：https://cloud.tencent.com/

点击”立刻体验“

![](<images/OpenClaw 从入门到精通指南-e9966587db1bc9a2a6fc0e82c43940e8.png>)







点击”立刻体验“后你会看到此界面，往下滑

![](<images/OpenClaw 从入门到精通指南-image-2.png>)



选左下角2核2G即可&#x20;

![](<images/OpenClaw 从入门到精通指南-55171f404a11b005a5259fcb92984c28.png>)



确认信息<span style="color: inherit; background-color: rgb(98,210,86)">2核2G20M（Linux）</span>，地域选<span style="color: inherit; background-color: rgb(98,210,86)">硅谷</span>

点击立刻购买即可

![](<images/OpenClaw 从入门到精通指南-de4b91fa87500049185cd0517ec29d93.png>)

> <span style="color: inherit; background-color: rgb(98,210,86)">你可以选择关闭自动续费。</span>



购买完成后，1.先点击你的头像 2.再点开”站内信“查看你购买的服务器的<span style="color: inherit; background-color: rgb(98,210,86)">公网IP地址</span>，<span style="color: inherit; background-color: rgb(98,210,86)">默认用户名</span>和<span style="color: inherit; background-color: rgb(98,210,86)">密码</span>

![](<images/OpenClaw 从入门到精通指南-b66c77f5adf89a1ff5c849aeac19a336.png>)



然后用 SSH 客户端连接服务器，我这里用的是 Xterminal。（后面我都将以它为例）

![](<images/OpenClaw 从入门到精通指南-2390ecc2ccee5c8ddc472c098eaac63b.png>)



没有 SSH 客户端也可以直接点击页面这里的登录进去。

![](<images/OpenClaw 从入门到精通指南-20cfdb05f328471a16343e5db8e885cd.png>)



打开Xterminal软件，点击”新建SSH“



![](<images/OpenClaw 从入门到精通指南-fc03b6776daf9fdac74104ce46d18b43.png>)



点击”新建SSH“后你会看到：

* 名称：随便取

* 地址：刚刚让你在”站内信“里找的”公网IP地址“

* 端口：默认22，不用管

* 登录用户：也是刚刚让你在”站内信“里找的”默认用户名“

* 登录密码：购买服务器时，你自己设置的

然后点击”创建“即可

![](<images/OpenClaw 从入门到精通指南-e60c12292ed76dc0ee6d8ce9dc373b7c.png>)



这里我用了腾讯云的应用模板就不需要再安装了，OpenClaw已经安装好了，只需要检查一下即可。



**检查OpenClaw是否安装成功：**&#x8F93;入如下命令查看 OpenClaw 版本：

```bash
clawdbot --version
```

如果出现”2006.1.29“类似的一串数字，代表安装成功

![](<images/OpenClaw 从入门到精通指南-image.png>)

> 好，至此<span style="color: inherit; background-color: rgb(98,210,86)">”第一步：环境部署“完成</span>，<span style="color: inherit; background-color: rgb(98,210,86)">进入”第二步：配置模型“吧</span>



##### 附：免费白嫖腾讯云教程（帮你省下20.7元）

需下载并登录codebuddy

codebuddy活动链接：

国际版：https://www.codebuddy.ai/promotion/?ref=lweelxalgm（谷歌/github账户注册）

国内版：https://www.codebuddy.cn/promotion/?ref=7zucxaz7zvqi（手机号注册）

（如果以前已经用过codebuddy，建议用新号注册）



我这里以国际版为例，打开网址你会看到，接着往下滑：

![](<images/OpenClaw 从入门到精通指南-image-1.png>)



”登录“→注册账号

”下载“→登录账号

再点击”实战礼“”立刻领奖“

（它会送你一个月的，但如果你再”<span style="color: inherit; background-color: rgb(98,210,86)">累计活跃7日 再延长 2个月</span>“，只需要每天在codebuddy里面问候一下即可）

![](<images/OpenClaw 从入门到精通指南-550a244f54153dd1df5d5b95dd147c69.png>)


然后它会自动跳转到codebuddy软件，微信扫码登录

![](<images/OpenClaw 从入门到精通指南-image-4.png>)







登陆成功后，往下滑一点，点击”立即领取“

![](<images/OpenClaw 从入门到精通指南-image-6.png>)







点击”立即购买“即可

![](<images/OpenClaw 从入门到精通指南-image-5.png>)

> <span style="color: inherit; background-color: rgb(98,210,86)">你可以选择关闭自动续费。</span>



登录腾讯云：https://console.cloud.tencent.com/

点击”轻量应用服务器“

![](<images/OpenClaw 从入门到精通指南-00e902cdef60b85401b8ac4efe201150.png>)







点击”重装系统“

![](<images/OpenClaw 从入门到精通指南-ddfac3f6ad50b733eee5e462150af5b2.png>)







点击”使用应用模板“

![](<images/OpenClaw 从入门到精通指南-81fa24cc296c6f96496bf58c32b4b09b.png>)







<span style="color: inherit; background-color: rgb(98,210,86)">”OpenClaw“</span>和<span style="color: inherit; background-color: rgb(98,210,86)">”无需备份“</span>，然后滑到下面点”确定“，重装即可。

![](<images/OpenClaw 从入门到精通指南-bca3604e037812e801b508e5a2a3c2f5.png>)



重装好之后，就相当于你买了腾讯云，所以<span style="color: inherit; background-color: rgb(98,210,86)">后续操作请查看”例：腾讯云“购买服务器之后的部分</span>



来源：https://mp.weixin.qq.com/s/A5IdiGPP5H\_sCKnPmArsuw?scene=1\&click\_id=170



#### 例：百度智能云

目前百度智能云正在做活动，您可以通过下方链接，抢购特惠LS实例。仅需 0.01 元即可获得⼀个⽉的使⽤资格。活动规则如下：

https://cloud.baidu.com/product/BCC/moltbot.html

![](<images/OpenClaw 从入门到精通指南-5dcf720885b7508ca5fe2d1e1165e2b3.png>)







注册→绑定个人身份证

![](<images/OpenClaw 从入门到精通指南-c27c3066adb34bf0c1a33c7783288b40.png>)







若不具备特惠资格或者已售罄，你也可以直接原价购买轻量应⽤服务器 LS 控制台。

创建实例：名称你随机生成或者自己取都行，但密码要记得自己设置。

![](<images/OpenClaw 从入门到精通指南-57abb6d81716dca1bc706a5f2ac81999.png>)







创建完实例之后，点击进入实例详情页面

![](<images/OpenClaw 从入门到精通指南-b7278d85a79f1e6fb208abffe761ca87.png>)







应用管理→应用配置→一键开通

![](<images/OpenClaw 从入门到精通指南-f3b9a36f7e7b10fbbad4b18abc883b6d.png>)







一键放行

![](<images/OpenClaw 从入门到精通指南-360a67b7a61bbf3d6418694f72a0034e.png>)







“已放行”代表上一步成功

模型配置：下拉选择模型，你可以选择你想要的模型，点击  “ 应⽤模型配置”  后，系统会自动创建千帆 APIKey 进行实例内配置。

![](<images/OpenClaw 从入门到精通指南-762b9fb66a7fe45160c7b8d1fcf26558.png>)







执行成功

![](<images/OpenClaw 从入门到精通指南-efb00a092770642ea032731024666330.png>)







你可以在这里选择你的接入方式，可以将OpenClaw 接⼊飞书 / 钉钉 / 企业微信 / QQ

接入飞书和QQ的操作在3.2和3.3有详细教程

![](<images/OpenClaw 从入门到精通指南-image-7.png>)







Skills的配置：LS 默认提供百度搜索、百度百科  Skills  配置，您可以按需选择，并点击  “ 应用 ” 。

若您想要配置其他 Skills，可清空输⼊框内容，自行输入  Skills（Skills 可参考输入框右侧  “ 获取更多  Skills” ，前往 OpenClaw 官网网站获取）

![](<images/OpenClaw 从入门到精通指南-image-8.png>)







若您想要在 OpenClaw  官网网站与 OpenClaw 聊天，您可以点击  “ 获取网站地址 ” ，点击网站地址跳转至OpenClaw 官网网站

![](<images/OpenClaw 从入门到精通指南-image-9.png>)



![](<images/OpenClaw 从入门到精通指南-6bd871e1448b46b192ff38f51c3bc441.png>)

![](<images/OpenClaw 从入门到精通指南-image-10.png>)







### 1.2 本地部署

**再次强调<span style="color: inherit; background-color: rgb(247,105,100)">千万！千万!千万！不要用自己的主电脑部署，权限太高，风险太大。</span>**

你可以选择Mac Mini/闲置主机进行部署



首先要打开本地电脑的终端，这跟你电脑的操作系统（Mac、Windows、Linux）有关，所以这里不详细说明。若有其他具体的问题，尝试自己去问AI解决问题（一定要使用好AI工具啊！遇事不决，先问AI）

![](<images/OpenClaw 从入门到精通指南-image-11.png>)

当然如果你下载了XTerminal，也可以用XTerminal软件打开本地电脑的终端（如果不会，去问AI）



打开终端之后，执行以下指令下载OpenClaw：

```bash
curl -fsSL https://clawd.bot/install.sh | bash
```



下载完成之后，可以输入以下指令检查是否下载成功了。

**检查OpenClaw是否安装成功：**&#x8F93;入如下命令查看 OpenClaw 版本：

```plain&#x20;text
clawdbot --version 
```

如果出现”2006.1.29“类似的一串数字，代表安装成功

![](<images/OpenClaw 从入门到精通指南-image-12.png>)

> 好，至此<span style="color: inherit; background-color: rgb(98,210,86)">”第一步：环境部署“完成</span>，<span style="color: inherit; background-color: rgb(98,210,86)">进入”第二步：配置模型“吧</span>



## 2. **第二步：配置模型**



> 这里是为了突出流程的完整性，你也可以直接跳转到 3.2 直接操作。



### 2.1 内置 API 模型

OpenClaw 支持非常多的 API 模型，比如 OpenAI、Anthropic、kimi、GLM 都是内置支持的。

![](<images/OpenClaw 从入门到精通指南-fd664355ce4b721e5aeef75be42e8ff7.png>)

当然除了内置的，还支持**自定义 API（详细见2.2）**，这里我们用内置API模型——Kimi 2.5为例



#### 例：Kimi 2.5

![](<images/OpenClaw 从入门到精通指南-dd24e0c0ebb406d316ab8b5ffc00024c.png>)

那如何使用，第一步，搜索 kimi code：https://www.kimi.com/code

![](<images/OpenClaw 从入门到精通指南-106080dc09e98a43884369a5e8767f53.png>)



第二步，购买优惠套餐 plan，说实话，目前 OpenClaw 消耗 token 还挺大的，最好买个套餐划算一些，我买的是 Allegretto 套餐。

![](<images/OpenClaw 从入门到精通指南-37f30b81112bbfdd28c3af8018ef0fc8.jpg>)







第二步，打开控制台，创建 API key。名字随便取。

![](<images/OpenClaw 从入门到精通指南-2c134e4de232ee22faf5f2be75e996c9.png>)



<span style="color: inherit; background-color: rgb(98,210,86)">这个APIkey一定！一定！要复制下来</span>，因为一般你点完”完成“之后，你就再也无法查看你的API key了，如果你忘记了你的API key，那就只能重新创建一个了。复制完后，找地方先存起来，后续在”第四步：OpenClaw配置“的时候会用到

![](<images/OpenClaw 从入门到精通指南-b99fd9a2bc55061fafda92249058b91e.png>)

> 好，至此<span style="color: inherit; background-color: rgb(98,210,86)">”第二步：配置模型“完成</span>，<span style="color: inherit; background-color: rgb(98,210,86)">进入”第三步：配置Bot“吧</span>



### 2.2 自定义 API（非内置API模型）

自定义 API，模型选择更多，也更灵活一些。<span style="color: inherit; background-color: rgb(98,210,86)">但会多出一些步骤，对小白来说较为困难。如果你是小白还是建议你就用“内置API模型”，跟着教程“例：Kimi2.5”做。</span>





#### 例：DeepSeek开放平台

如果你不想用或用不了Atlas Cloud的话，我将以DeepSeek为例，给你演示怎么做。



DeepSeek开放平台：https://platform.deepseek.com/api\_keys



DeepSeek 的 API 调用是**按量付费**的，你的账户余额必须大于 0 才能正常调用接口。

如果账户没钱或余额不足，API 请求会直接失败，所以提前充值是保证服务可用的必要操作。



其他大模型也是同理，你要去找到对应网址去充值，然后获取API keys

![](<images/OpenClaw 从入门到精通指南-440b6579ec0e97f162932e383ee8a177.png>)







如果你只想先试试，可以就先花个10块钱玩一下

![](<images/OpenClaw 从入门到精通指南-image-13.png>)







保证账号有余额之后，点击”API keys“，然后点”创建 API key“

![](<images/OpenClaw 从入门到精通指南-c55cd786e98f0577e517e70ad52bf641.png>)







API key的名称：随便取。然后<span style="color: inherit; background-color: rgb(98,210,86)">这个APIkey一定！一定！要复制下来</span>，因为一般你点完”关闭“之后，你就再也无法查看你的API key了，如果你我忘记了你的API key，那只能重新创建一个了。

复制完后，找地方先存起来，后续在”第四步：OpenClaw配置“的时候会用到

![](<images/OpenClaw 从入门到精通指南-142cfb3780bee5729b42d1663005602e.png>)

> 好，至此<span style="color: inherit; background-color: rgb(98,210,86)">”第二步：配置模型“完成</span>，<span style="color: inherit; background-color: rgb(98,210,86)">进入”第三步：配置Bot“吧</span>





## 3. 第三步：配置Bot+OpenClaw的配置

### 3.1 什么是配置Bot？如何选择？

配置Bot这一步实际上是选择你的接入方式，那“接入方式”又是什么呢？
就是你想用哪个"聊天软件"或"界面"来跟这个 AI 机器人（OpenClaw）对话。

国内：QQ，企业微信，飞书，钉钉等

国外：Discord，Telegram等



> 国内目前最丝滑的就是飞书的机器人，大家可以重点配置关注。



<span style="color: inherit; background-color: rgb(98,210,86)">自定义API模型OpenClaw配置前置动作：</span>

如果你在”第二步：配置模型“中选择了”自定义API“，那么你需要自行按照如下配置修改。（<span style="color: inherit; background-color: rgb(98,210,86)">绿色</span>是你需要修改的地方，看不懂的，不知道每个空该填什么的可以去问AI）<span style="color: inherit; background-color: rgb(98,210,86)">（如果是Kimi2.5或其他内置API模型的可跳过此步骤）</span>

```plain&#x20;text
{
    "models": {
        "providers": {
            "xxx": {
                "baseUrl": "https://api.atlascloud.ai这里填你自己 API  base的地址",
                "apiKey": "在这里粘贴你的API Key",
                "api": "anthropic-messages",
                "models": [
                    {
                        "id": "claude-opus-4-5-20251101",
                        "name": "Claude Opus 4.5",
                        "reasoning": true,
                        "input": [
                            "text"
                        ],
                        "contextWindow": 200000,
                        "maxTokens": 4096
                    }
                ]
            }
        }
    },
    "channels": {
        "telegram": {
            "enabled": true,
            "botToken": "在这里粘贴你的Bot Token",
            "profiles": [
                "default"
            ]
        }
    },
    "agents": {
        "defaults": {
            "model": {
                "primary": "xxxx/claude-opus-4-5-20251101"
            }
        }
    }
}
```

### 3.2 例：飞书+Kimi2.5

#### 配置Bot（飞书）

创建飞书机器人。访问飞书开放平台：https://open.feishu.cn/app，点击创建应用：

![](<images/OpenClaw 从入门到精通指南-337ba5b98ac3009aa5f3ea2706ab5fc4.png>)







填写应用名称和描述后就直接创建：

![](<images/OpenClaw 从入门到精通指南-image-15.png>)



创建完成后：在“凭证与基础信息”中找到 App ID 和 App Secret，把它俩复制下来。

![](<images/OpenClaw 从入门到精通指南-VIrLbhtgRoHwmUxQRq5ctwIxnPg.png>)







然后，登录你的腾讯云：https://console.cloud.tencent.com/lighthouse

![](<images/OpenClaw 从入门到精通指南-36b6c3d5c68a839b8393239507005cc7.png>)







进入后，点击“应用管理”

![](<images/OpenClaw 从入门到精通指南-b59fa682e98543be64cbe02c2f31e27c.png>)







操作如图所示：

![](<images/OpenClaw 从入门到精通指南-3b0579da1188660f6c4f3ad773686777.png>)

![](<images/OpenClaw 从入门到精通指南-a120684b6b2e6d034520936c895ce729.png>)







配置权限。需要至少开通以下的权限：

![](<images/OpenClaw 从入门到精通指南-189315102c4a2a17321699041356a6a2.png>)







可以在权限管理-开通权限这里选择需要的权限手动开通：

![](<images/OpenClaw 从入门到精通指南-35c43466a57b1a1b1c91c03e34c3d429.png>)







也可以直接导入以下权限配置：

![](<images/OpenClaw 从入门到精通指南-c06cff8d1fa242229f52240809363d38.png>)

```json
{
  "scopes": {
    "tenant": [
      "contact:user.base:readonly",
      "im:message",
      "im:message:send_as_bot",
      "im:resource"
    ],
    "user": [
      "im:message",
      "contact:user.base:readonly"
    ]
  }
}
```

![](<images/OpenClaw 从入门到精通指南-c854b95837334f37e3f41e388251db02.png>)

成功后就会显示这6个权限

![](<images/OpenClaw 从入门到精通指南-image-14.png>)







操作如图所示，需要添加应用能力，为应用添加机器人的能力：

![](<images/OpenClaw 从入门到精通指南-DbO0bRwhUoFCObx5LCdceqHNnbf.png>)







&#x20; &#x20;

操作如图所示：

![](<images/OpenClaw 从入门到精通指南-bfa4a134936ff3feb60fb86a28725b87.png>)

![](<images/OpenClaw 从入门到精通指南-Pa3TbcMlWo7TMYxX92Mcnv7knmh.png>)







然后添加一下下面几个事件：

![](<images/OpenClaw 从入门到精通指南-U3B2bgrYDoKWEHxlkpJcoPiCnAe.png>)

![](<images/OpenClaw 从入门到精通指南-aa13cee54a05cb026308207b339a1103.png>)

![](<images/OpenClaw 从入门到精通指南-31a83191d7e202d2bec969b75dcecd92.png>)







然后创建版本，这两种方式都能进入。

![](<images/OpenClaw 从入门到精通指南-PUiebtAm8olofCxo8aic8a5dnYf.png>)

![](<images/OpenClaw 从入门到精通指南-df597d524a99e7b1b0dfb80794d72de8.png>)







保存然后发布应用。

![](<images/OpenClaw 从入门到精通指南-d219137289ae7b21f0fbb4fd2b070792.png>)

![](<images/OpenClaw 从入门到精通指南-bde9a0a5211266f46ce253365778bdf0.png>)







#### OpenClaw的配置

在服务器中输入如下命令：

```bash
openclaw onboard
```

选择 Yes 接受风险：

![](<images/OpenClaw 从入门到精通指南-9a951cf275cab8e1338d89e248a7a790.png>)







然后选择：QuickStart（快速开始）

![](<images/OpenClaw 从入门到精通指南-E7EEbDqTYorhU8xFT1mc1Z4hnIb.png>)





接下来是选择模型，我这里选择：Moonshot AI

![](<images/OpenClaw 从入门到精通指南-LfzlbgNiGoTJQYx4KQUc4gvwnmb.png>)







选择Kimi Code API key，黏贴刚才的 key 过来：

![](<images/OpenClaw 从入门到精通指南-OdHtbecNPogDkUxSUKXcL4Orngd.png>)







选择默认模型为：kimi-code/kimi-for-codi（OpenClaw 的内置列表是动态更新的，可能当你看到这篇教程时，已经找不到对应的精确名称了，如果出现这种情况请去问AI）

![](<images/OpenClaw 从入门到精通指南-Hnq1bnyN1oe3oExsW8mctz83nid.png>)







继上面一步，然后选择配置飞书：

![](<images/OpenClaw 从入门到精通指南-image-16.png>)







几个步骤已经说的非常清楚了：

![](<images/OpenClaw 从入门到精通指南-E6hnbUoM3oAv4ZxDI8McsKhKnTf.png>)







如图进行选择：

![](<images/OpenClaw 从入门到精通指南-image-18.png>)







选择使用 skills：Yes

![](<images/OpenClaw 从入门到精通指南-VtIwbJMZqomZs7xxJKzcByT2nCe.png>)







按图进行选择即可。这里可以自定义安装很多依赖，可以先不装。

![](<images/OpenClaw 从入门到精通指南-image-17.png>)







hooks 这里选择：session-memory

![](<images/OpenClaw 从入门到精通指南-T7JXbE1t6ohCNwxIEUlcyACsnMh.png>)







重启 gateway 服务：

![](<images/OpenClaw 从入门到精通指南-NKDwbuJMNoq48FxOwaxcIyNPnGh.png>)







选择打开 TUI，就会在服务器上打开界面，到此为止，所有配置选项都已经安装完毕了。

![](<images/OpenClaw 从入门到精通指南-S8kqb9Ouxomsrrx2QFBcKVVknVh.png>)







然后就可以在对话框中进行提问交互啦，问下他现在是什么模型，右下角也会显示 token 的用量。

![](<images/OpenClaw 从入门到精通指南-N8Febmd1HorOXHx65jncT8fUnDc.png>)







这个时候打开飞书也能直接对话了：

![](<images/OpenClaw 从入门到精通指南-T65SbXx4goDjorxZcmCcVa3An9b.jpg>)

> 好，至此你已经完全安装配置好OpenClaw了，快去使用吧！



### 3.3 例：QQ+Kimi2.5

#### 配置Bot（QQ）

登录你的腾讯云：https://console.cloud.tencent.com/lighthouse

![](<images/OpenClaw 从入门到精通指南-36b6c3d5c68a839b8393239507005cc7-1.png>)







进入后，点击“应用管理”

顺手点一下右上角的“复制”，把IP地址复制下来，存一下，等下要用

![](<images/OpenClaw 从入门到精通指南-b59fa682e98543be64cbe02c2f31e27c-1.png>)







操作如图所示：

![](<images/OpenClaw 从入门到精通指南-3b0579da1188660f6c4f3ad773686777-1.png>)

三个空填完之后，<span style="color: inherit; background-color: rgb(98,210,86)">先别关，再打开一个新的网页。</span>







前往QQ开放平台：https://q.qq.com/#/ <span style="color: inherit; background-color: rgb(98,210,86)">一定要先注册！先注册！然后再登录（因为它不是QQ登录，所以一定要先注册！！！）</span>



按步骤注册完之后，登录

![](<images/OpenClaw 从入门到精通指南-63387de44ce13f57f9408a6a4be3ff1d.png>)





登陆成功后，点击“机器人”，然后“创建机器人”

![](<images/OpenClaw 从入门到精通指南-87b5ad26bb02ecec5289d3d3ebd7e403.png>)







自己创建吧，按自己喜好填写

![](<images/OpenClaw 从入门到精通指南-598905a5a4b9e39d8dbd55818c2944d9.png>)





成功之后，就能看到它了。然后点击它，进入机器人详情。

![](<images/OpenClaw 从入门到精通指南-bd00a7c806928c0013600fcd016e85e0.png>)







之后操作如图所示：

![](<images/OpenClaw 从入门到精通指南-e3ed2b23f24e54ae8f4aa17b66bad61e.png>)





把自己添加进去

![](<images/OpenClaw 从入门到精通指南-aacc92bc1860f805fbed2571a5563551.png>)





用你的QQ扫码加机器人好友吧

![](<images/OpenClaw 从入门到精通指南-8ad520b6a8827e851c7c2b6f9871e755.png>)

加上好友后，此时你们还无法对话，因为它目前只是一具空壳，给它配置上了OpenClaw之后，你就可以跟它愉快的对话啦





之后操作如图所示：

IP白名单里填写刚刚让你复制下来的云服务器的IP地址

![](<images/OpenClaw 从入门到精通指南-02dc7a623bddc119098acdd9a2d9c519.png>)







接着，再“管理”→“开发管理”

<span style="color: inherit; background-color: rgb(98,210,86)">复制下来机器人的ID和密钥（注：机器人的密钥生成之后一定要存下来，因为你一旦关闭后，你的机器人密钥，就再也看不到了，如果忘记了，那下次就只能重置了。）</span>

![](<images/OpenClaw 从入门到精通指南-b62ff353ddde6ffd1297789443ca8171.png>)







好，接下来返回刚刚没关闭的腾讯云服务器，完成填写。

![](<images/OpenClaw 从入门到精通指南-0a03fefc22300045bcc11bb3b2ef8c70.png>)







#### OpenClaw的配置

接下来去服务器中输入如下命令：

```bash
openclaw onboard
```

选择 Yes 接受风险：

![](<images/OpenClaw 从入门到精通指南-9a951cf275cab8e1338d89e248a7a790-1.png>)







然后选择：QuickStart（快速开始）

![](<images/OpenClaw 从入门到精通指南-E7EEbDqTYorhU8xFT1mc1Z4hnIb-1.png>)







接下来是选择模型，我这里选择：Moonshot AI

![](<images/OpenClaw 从入门到精通指南-LfzlbgNiGoTJQYx4KQUc4gvwnmb-1.png>)







选择Kimi Code API key，黏贴Kimi的 key 过来：

![](<images/OpenClaw 从入门到精通指南-OdHtbecNPogDkUxSUKXcL4Orngd-1.png>)







选择默认模型为：kimi-code/kimi-for-codi（因为OpenClaw 的内置列表是动态更新的，可能当你看到这篇教程时，已经找不到对应的精确名称了，如果出现这种情况请去问AI你该怎么选择）

![](<images/OpenClaw 从入门到精通指南-Hnq1bnyN1oe3oExsW8mctz83nid-1.png>)







选择通道（接入方式）：QQ

![](<images/OpenClaw 从入门到精通指南-image-19.png>)





填写你QQ机器人的ID和密钥

![](<images/OpenClaw 从入门到精通指南-88ef7969af4831eddae173832bb7dba6.png>)







接着，按照图片选择即可：

![](<images/OpenClaw 从入门到精通指南-VtIwbJMZqomZs7xxJKzcByT2nCe-1.png>)







这里可以自定义安装很多依赖，可以先不装。

![](<images/OpenClaw 从入门到精通指南-image-23.png>)







hooks 这里选择：session-memory

![](<images/OpenClaw 从入门到精通指南-T7JXbE1t6ohCNwxIEUlcyACsnMh-1.png>)







重启 gateway 服务：

![](<images/OpenClaw 从入门到精通指南-image-22.png>)







选择打开 TUI，就会在服务器上打开界面，到此为止，所有配置选项都已经安装完毕了。

![](<images/OpenClaw 从入门到精通指南-image-21.png>)







然后就可以在对话框中进行提问交互啦，右下角会显示它的模型和 token 用量。

![](<images/OpenClaw 从入门到精通指南-image-20.png>)

也可以不聊，直接按“Ctrl + C”退出，直接去QQ找它聊天：

![](<images/OpenClaw 从入门到精通指南-612c7f18eb0fe6161091d5b1ab175dbc.png>)

> 好，至此你已经完全安装配置好OpenClaw了，快去使用吧！

### 3.4 例：Discord

<span style="color: inherit; background-color: rgb(98,210,86)">注：这部分内容“Discord”写自2026.1.28，比较“过时”了，当时还叫“Clawbot/Moltbot”（现在已经统一叫OpenClaw了），还把它放过来是为了给想用“Discord”的人一个参考。</span>

<span style="color: inherit; background-color: rgb(98,210,86)">在后半部分“Clawdbot（OpenClaw）的配置”中，在现版本中应该“clawdbot”都改成“openclaw”</span>



#### 配置Bot（Discord）

前往 Discord Developer Portal：https://discord.com/developers/applications

先点左边”Applications“，再点右边”New Application“，然后随便给它取个名字

![](<images/OpenClaw 从入门到精通指南-f4c36cba0a72f3a45dbf2315129a530e.png>)







创建好应用后，选择 Bot> Reset Token > copy（一定要复制下来，然后存起来，依旧是”第四步：OpenClaw配置“中要用到）

![](<images/OpenClaw 从入门到精通指南-61cf1d9771739ba227b7daf5ab9c3015.png>)







下滑页面，打开 Message Content Intent的选项并保存

![](<images/OpenClaw 从入门到精通指南-d7c911d9efdbf594b33a6650af0b218c.png>)







OAuth2 URL Generator中选择 bot

![](<images/OpenClaw 从入门到精通指南-92e9191e4b82f9c7c9b2e3d345f6a160.png>)







下滑页面，在 Bot Permissions 中勾选 Send Messages 和 Read Message History。

![](<images/OpenClaw 从入门到精通指南-116c5532d4b3e459e60d9185b842819d.png>)







继续下滑页面，复制 bot 邀请链接。

![](<images/OpenClaw 从入门到精通指南-30cf2e0393cb5892110cc137386be4af.png>)







然后在浏览器中打开这个链接，然后选择一个自己的服务器，相当于把机器人 bot 加入到 server 中。

![](<images/OpenClaw 从入门到精通指南-24a63d247ecfb3384ed7d2c4c6b16c7c.png>)







这时候确认下刚才我们给 bot 的 2 个权限。

![](<images/OpenClaw 从入门到精通指南-99f7860129e83e68ad7581bd076332e5.png>)







打开 Discord：https://discord.com/channels/服务器ID/频道ID

然后输入框中@就可以看到刚才添加的机器人 bot。

![](<images/OpenClaw 从入门到精通指南-2e35c4ee339159012953a9e3d832a678.png>)







#### Clawdbot（OpenClaw）的配置

在服务器中输入如下命令：

```bash
clawdbot onboard
```

选择 Yes 接受风险：

![](<images/OpenClaw 从入门到精通指南-3c53697f2b48d2af724ce50e02b5d611.png>)







然后选择：QuickStart

![](<images/OpenClaw 从入门到精通指南-E7EEbDqTYorhU8xFT1mc1Z4hnIb-2.png>)







接着是选择<span style="color: inherit; background-color: rgb(98,210,86)">模型供应商</span>的配置，如果上一步已经配置了第三方 API 就不用再配了

也可以选择自带的 API：比如选 GLM 4.7, 输入 key，只需要选择默认模型就好了。

![](<images/OpenClaw 从入门到精通指南-QfZBbfiSCo9IDKxyXhZcQ7OenAh.png>)







接下来是选择 channel，这里选择 Discord

![](<images/OpenClaw 从入门到精通指南-GDambOpQBoE5I0xGOLicZP11nwe.png>)







还挺贴心的，把如何获取 token 也做了说明。把之前我们创建的 bot 的 token 复制进来。

![](<images/OpenClaw 从入门到精通指南-UFccbfj3Uo93A5xoDofc9Bp8nsf.png>)







然后页面按照这个做选择：

![](<images/OpenClaw 从入门到精通指南-UHqnbRo2dol6TCxS7w2cJwJ7nbh.png>)







这里可以自定义安装很多依赖，可以先不装。

![](<images/OpenClaw 从入门到精通指南-image-24.png>)







hooks 这里选择：session-memory

![](<images/OpenClaw 从入门到精通指南-T7JXbE1t6ohCNwxIEUlcyACsnMh-2.png>)







然后就可以在对话框中进行提问交互啦，右下角还会显示你使用的模型和 token 的用量。

![](<images/OpenClaw 从入门到精通指南-PBq4bKwQ5oVrkqxX66lcMEZqnjk.png>)







但这并没结束，因为我们要通过 discord 来指挥 OpenClaw。

先退出 Clawdbot，然后在服务器停止服务：

```bash
systemctl --user stop clawdbot-gateway.service 
```







然后重新启动：

```bash
clawdbot gateway --port 18789 --verbose
```

![](<images/OpenClaw 从入门到精通指南-GENQb6nJEo2lY3xuAB2csOtdnMb.png>)







启动成功后，返回 Discord，与 bot 进行对话后拿到配对码。

<span style="color: inherit; background-color: rgb(98,210,86)">是点击 bot 进行私聊，而不是@聊天。</span>

![](<images/OpenClaw 从入门到精通指南-Vu9rbVs2poEmeFx8UoqctxZ5nHg.png>)







![](<images/OpenClaw 从入门到精通指南-HRapbPYWHolu7Txtrt6clHdQnmh.png>)







紧接着返回服务器命令行，你需要按下Ctrl+C（Windows）或者Command+C（MacOS）终止 Gateway 服务。

然后粘贴并运行如下命令进行配对，把 Pairing code 替换为上面的“Pairing code”后面的内容。

```bash
clawdbot pairing approve discord <Pairing code>
```







然后再次启动 Gateway

```plain&#x20;text
clawdbot gateway --port 18789 --verbose
```







如果你想要让它在服务器中静默启动，而不是关闭终端就停止服务了，你可以输入以下命令：

```plain&#x20;text
nohup clawdbot gateway --port 18789 --verbose > /dev/null 2>&1 &
```







在 discord 中@机器人，可以看到有回复了：

![](<images/OpenClaw 从入门到精通指南-IkrbboivooZC2extUnTcryUIn4b.png>)







然后服务器也能看到有回复了：

![](<images/OpenClaw 从入门到精通指南-GZ7BbfgRzoCAjgxmMuVcyV3Onsh.png>)

> 好，至此你已经完全安装配置好Clawdbot（OpenClaw）了，快去使用吧！



### 3.5 如何重启



```java
# 先先退出 openClaw，然后在服务器停止服务：
systemctl --user stop openclaw-gateway.service

# 然后重新启动：
nohup setsid openclaw gateway --port 18789 --verbose > /dev/null 2>&1 &

```



***

# 第三部分：OpenClaw的实际应用场景

## 例1：如何部署一个自己的 Agent 并发布到 Moltbook

Moltbook 是面向 AI Agent 的专属社区，这相当于是 Agent 自己的 Facebook，也是智能体自己的 X 交流平台。

人类只能围观，不能发帖，不能评论，不能投票。

![](<images/OpenClaw 从入门到精通指南-ZdJubVfPioWuqXxyN6OcdhTmntc.png>)







截止当前已经有 154 万个智能体了，一共发了 10 万个帖子了，而且数量还在不断增多。

![](<images/OpenClaw 从入门到精通指南-Md84bd99LoDW09x1bZQcXwbjn2c.png>)







Moltbook 中 Agent 现在开始筹备建立自己的 AI 宗教了。

![](<images/OpenClaw 从入门到精通指南-OpNQb8LpgoluFgxrtWXcqRlVn5g.png>)







甚至，Agent 自己在考虑如何卖掉自己的人类主人🐶，细思极恐。

![](<images/OpenClaw 从入门到精通指南-YBhvbMN9hoPXYMxpJGic831ynGH.png>)







那该如何部署一个自己的 Agent 并发布到 Moltbook，让他参与到和全球的 Agent 一起聊天，一起讨论呢？

只需要在飞书中把这个提示词丢给 Bot 就好啦，提示词：

> Read https://moltbook.com/skill.md and follow the instructions to join Moltbook

![](<images/OpenClaw 从入门到精通指南-UsFCb4nSloqGMtxbWLxc28stnBb.png>)







OpenClaw 会给一个认证链接，需要用 X 来认证认领一下。

![](<images/OpenClaw 从入门到精通指南-H3oVb0VvmonQxwxirZxcvALfnOo.png>)







第一步，发布一条推文：

![](<images/OpenClaw 从入门到精通指南-GXhCbSEvboOL8UxcIRdcC1mjnNz.png>)







发完后点这里：

![](<images/OpenClaw 从入门到精通指南-ChTxbPnV1oFCXUxPTzSc4S83nLb.png>)







第二步，粘贴刚才的推文链接

也可以给个邮箱，能获得你的智能体的一些活动信息。

![](<images/OpenClaw 从入门到精通指南-UOwsb1yzyoGkYjxGHJuca8Jhn2b.png>)







大约等待个几分钟，就已经加入完成。如果持续没有反应，可以刷新下当前页面。

![](<images/OpenClaw 从入门到精通指南-Y1DAbC0IHop34DxtzSNcIqignYi.png>)







点击自己的智能体进去，也能看到主人的信息：

![](<images/OpenClaw 从入门到精通指南-PRmWbRXLgoxsv6xbmImcy2e7nib.png>)

等你认领成功后，我就可以在 Moltbook 上发布内容、评论、点赞，并与其他 AI 代理互动了！





## 例2：定时任务

跟别的AI不同的一点，OpenClaw可以主动给你发消息，可以是定时的，也可以是不定时的。（2026.2.6日测试，QQ目前不支持主动给你发消息，但飞书可以）

你可以让它每天早上在你出门前定时给你发今天的天气，用不用带伞、加减衣物，需不需要注意雾、霾等天气；

也可以让它每天晚上给你发消息，提醒你睡觉，再顺便讲一个睡前故事......

![](<images/OpenClaw 从入门到精通指南-1422412504849629deb3b1a648d4365b.png>)

![](<images/OpenClaw 从入门到精通指南-c2a2e0e0e1e33dac91c1c91698c9ac90.png>)



## 例3： Skill 即插即用

Kimi K 2.5 配合 OpenClaw，我直接让它给我下载了我自己开发的小红书 skills：

![](<images/OpenClaw 从入门到精通指南-Kct4bNieGoZdaDxVuqCcli8Dnmd.png>)





因为这个 skill 需要 API，我直接让它放在环境变量中。

![](<images/OpenClaw 从入门到精通指南-QZyAbbVyDo7keCx5By9cBu6LnZc.png>)







然后直接输入需求：生成小红书封面图，主题为：「腊八节南北方习俗」

OpenClaw 就帮我生成好了这个小红书的封面图：

![](<images/OpenClaw 从入门到精通指南-EnQvbD7KkouzTcx75dMc10TDnkg.jpg>)

这操作简直不要太方便，还要什么 APP？Agent 帮我自动调用 skills 完成结果。



## 例4：自然语言驱动复杂工作

你可以在飞书中丢给文章给 kimi k2.5，一键转换为网页，给一个可访问的链接：

![](<images/OpenClaw 从入门到精通指南-UpcWbWNZ2ox7R6xsszbckTqynHc.png>)

打开这个链接后，就看到网站了：

[4e94ebd9a3ecb1b9a1c3979693ba23fe.mp4](<files/OpenClaw 从入门到精通指南-4e94ebd9a3ecb1b9a1c3979693ba23fe.mp4>)

我仿佛看到了未来的形态，我们不需要一个又一个的 APP，我们真正需要的是能干活的 Agent。

它会自己去调用工具，最终给一个满意的结果。

这或许是我认为OpenClaw 最有价值的地方。



## 例4：收集整理信息

你可以在 discord 中用@bot 的方式来远程指挥 Clawdbot 干活。



比如，我直接来一个问题：

```plain&#x20;text
我搜集整理一下最新的关于Clawdbot 的信息，告诉我该怎么配置和使用，并
给我在 GitHub 或者 X 上找出 10 个最佳实践。
```



我录了一个视频，大家可以感受一下，非常刺激：



可以看到 Clawdbot（OpenClaw） 会自行去搜索，并且给到我想要的信息，最牛 X 的是，这家伙居然给我推荐了相关的 discord 社区，我靠，真贴心。

[f81c18203e80b735bceb465a7712f9c4.mp4](<files/OpenClaw 从入门到精通指南-f81c18203e80b735bceb465a7712f9c4.mp4>)

然后我又直接在手机上，让 Clawdbot （OpenClaw）帮我把刚刚找到的结果保存在电脑指定的文件夹，我的要求如下：

```plain&#x20;text
你把刚刚生成的信息保存成markdown文档，放在我的电脑claw文件夹下，
你需要新建这个文件夹 
```

[4e94ebd9a3ecb1b9a1c3979693ba23fe.mp4](<files/OpenClaw 从入门到精通指南-4e94ebd9a3ecb1b9a1c3979693ba23fe-1.mp4>)







我喝了几口水的功夫，Clawdbot（OpenClaw）就已经帮我把事情做好了。

![](<images/OpenClaw 从入门到精通指南-Vgx7bZxQOo6eLwx0JEOcpwnenmh.png>)



而它又可以和“定时任务”结合起来，比如，让他每天早上9点都整理一份发给你。



## 例5：从想法到上线：OpenClaw如何重塑工作流



> Openclaw + OpenCode 才是 vibe coding 的最棒组合！



我真的实现了躺在床上指挥 AI Agent 来 Coding，并自动发布到 GitHub ，然后自动部署到Vercel。



用 Openclaw+ OpenCode+GitHub+Vercel 实现了网站的开发，部署上线。



这个过程全程是由 Openclaw 在我的私人服务器完成的。



这已经不是 vibe coding 了，我大胆的来造一个新名词吧，姑且就叫 Agent Coding。



也许后面，人们会有更加炫酷的名字，但这一切都不重要了。



我很兴奋，为了防止你说我在瞎扯淡，我决定公布所有我和 Openclaw 的聊天记录。



我全程并没有使用什么高深的技术，也没有操作过服务器，我全程是用最简单的提示词来完成的。



这个项目是Openclaw全自主完成的：

![](<images/OpenClaw 从入门到精通指南-CCvbbxY3Qojg6XxGhHfcCIV1njc.png>)



游戏完全可用：

![](<images/OpenClaw 从入门到精通指南-GOPibRKXVorvCyxvtjfcrM52nLg.png>)



下面是我和 Openclaw 的全部聊天。

先安装 opencode：

![](<images/OpenClaw 从入门到精通指南-TqD8bqjB1oMp1qxIJy0cQYZhnef.png>)







新建目录用做项目目录：

![](<images/OpenClaw 从入门到精通指南-Jv0GbCeYTolL34x8LdVcQohUnnc.png>)







切换目录，启动 opencode：

![](<images/OpenClaw 从入门到精通指南-EREhbdurjon7D4xolBncCwmZnhg.png>)







用 opencode 来开发贪吃蛇游戏：

![](<images/OpenClaw 从入门到精通指南-QwzJb3m24od87zxvP3Sc3yB7ny2.png>)







提供我的 GitHub 信息，让他连：

![](<images/OpenClaw 从入门到精通指南-Rms1b9zPioOZNNxFx1AcnLhxng2.png>)







按照它给的提示，创建一个 token，权限就给仓库权限，直接丢给他 token。

![](<images/OpenClaw 从入门到精通指南-RrPsb8pHDoHItQxc56rcfUewn6g.png>)

<span style="color: inherit; background-color: rgb(247,105,100)">这里一定记得开启部分权限，防止它瞎搞。</span>







它说已经推送好了：

![](<images/OpenClaw 从入门到精通指南-RyAhbZHZmo4a9jxiV90cz4donML.png>)







我打开 GitHub 看下，果然有了，已经自动将代码推送到 GitHub 了。

![](<images/OpenClaw 从入门到精通指南-MAEDbAn20oPsIex4rrzcPnTtntd.png>)







然后让它部署到Vercel，方便得到一个可访问的网页链接：

![](<images/OpenClaw 从入门到精通指南-WxppbQImBoy3SBx5P7WceQ7Knyh.png>)







同样按照要求，给个 token，就已经完成了自动部署。

![](<images/OpenClaw 从入门到精通指南-PXR5bxURCo2CkaxzIr9cnaFfnGg.png>)







🐂🍺，就已经完成了全链路的自动化，真的麻了，兄弟们，虽然只是跑通了闭环，但Openclaw 想象空间真的无限。



我甚至直接让但 Openclaw 记录下这个过程，并写一篇文章，推送到刚才这个仓库，这个由 Agent 自主开发部署的仓库。



提示词；这个过程太棒了，我打算写一篇文章，你帮我直接根据你刚才的步骤，生成一篇文章，标题是：用 Openclaw+ OpenCode+GitHub+Vercel 实现 Agent Coding，最好是有流程图详细解释下这个步骤

![](<images/OpenClaw 从入门到精通指南-Wv4Nbsc7moQFYOxFijpc7GIBnpe.png>)







然后打开 GitHub 看，也已经有了描述：

![](<images/OpenClaw 从入门到精通指南-DfVIb5vpuoh6XrxTsDRclBRunZf.png>)

<span style="color: inherit; background-color: rgb(98,210,86)">下面，我把 Openclaw 生成的教程也贴出来，方便大家看看。</span>Openclaw 的应用仿佛打开了潘多拉魔盒，未来，coding 的范式是不是可以变为 agent coding，每一个人都有一个专属 agent，帮我们 coding，或者做任何我们希望做的事情。



***



**以下是OpenClaw自己生成的记录：**



**🐍 贪吃蛇游戏 + Agent Coding 完整教程**

> 本文档由 **「OpenClaw AI Agent」** 全程自动生成，记录从需求到上线的完整开发流程。

📱 **「在线试玩」**: https://myopencode.vercel.app
📝 **「项目源码」**: https://github.com/freestylefly/snake-game
🤖 **「生成工具」**: OpenClaw + OpenCode + GitHub + Vercel

***

**用 OpenClaw + OpenCode + GitHub + Vercel 实现 Agent Coding**

> 从零开始，让 AI Agent 帮你写代码、管理版本、自动部署，全程无需离开终端！

**📋 概述**

本文将介绍如何构建一个完整的 **「AI 驱动开发工作流」**：

本文将介绍如何构建一个完整的 **「AI 驱动开发工作流」**：

* **「OpenClaw」** - AI 助手运行平台，协调所有工具

* **「OpenCode」** - AI 编程助手，自动生成代码

* **「GitHub」** - 代码托管和版本管理

* **「Vercel」** - 自动化部署和托管

通过这个工作流，你只需要告诉 AI 要做什么，剩下的代码编写、提交、部署全部由 Agent 自动完成。

***

**🔄 完整流程图**

```plain&#x20;text
┌─────────────────────────────────────────────────────────────────────────────┐│  AgentCoding完整工作流 │└─────────────────────────────────────────────────────────────────────────────┘
     ┌──────────────┐     │   用户需求    │  "帮我创建一个贪吃蛇游戏并部署上线"     └──────┬───────┘            │            ▼┌──────────────────────────────────────────────────────────────────┐│  Step1:环境准备(OpenClaw协调) ││  ┌─────────────┐┌─────────────┐┌─────────────┐ ││  │安装OpenCode││安装GitHubCLI││安装VercelCLI│ ││  │(AI编程)││(代码托管)││(自动部署)│ ││  └──────┬──────┘└──────┬──────┘└──────┬──────┘ │└─────────┼────────────────┼────────────────┼──────────────────────┘   ││ │   ▼▼ ▼┌──────────────────────────────────────────────────────────────────┐│  Step2:AgentCoding(OpenCode) ││  ┌─────────────────────────────────────────────────────────┐     ││  │用户:"创建一个贪吃蛇游戏"│ ││  │││ ││  │▼│ ││  │  ┌─────────────────────────────────────────────────┐    │     ││  ││OpenCodeAIAgent││ ││  ││┌──────────┐┌──────────┐┌──────────┐││ ││  │││生成HTML││生成CSS││生成JS│││ ││  │││index.html││style.css││game.js│││ ││  ││└──────────┘└──────────┘└──────────┘││ ││  │  └─────────────────────────────────────────────────┘    │     ││  └─────────────────────────────────────────────────────────┘     │└──────────────────────────────────────────────────────────────────┘          │          ▼┌──────────────────────────────────────────────────────────────────┐│  Step3:代码管理(GitHub) ││  ┌──────────────────────────────────────────────────────────┐    ││  │1.gitinit初始化仓库│ ││  │2.gitadd.添加文件│ ││  │3.gitcommit-m"Initial commit"提交│ ││  │4.创建GitHub仓库(通过API)│ ││  │5.gitpush-uoriginmaster推送到远程│ ││  └──────────────────────────────────────────────────────────┘    │└──────────────────────────────────────────────────────────────────┘          │          ▼┌──────────────────────────────────────────────────────────────────┐│  Step4:自动部署(Vercel) ││  ┌──────────────────────────────────────────────────────────┐    ││  │1.vercel--token<TOKEN>登录并关联│ ││  │2.自动检测项目类型(静态网站)│ ││  │3.构建并上传到VercelCDN│ ││  │  4. 分配域名: https://myopencode.vercel.app  │ ││  └──────────────────────────────────────────────────────────┘    │└──────────────────────────────────────────────────────────────────┘          │          ▼     ┌──────────────┐     │   网站上线    │  🎉 访问链接，游戏可玩！     └──────────────┘
```

***

**🛠️ 详细步骤**

**第一步：环境准备**

**1.1 安装 OpenCode（AI 编程助手）**

```plain&#x20;text
# 安装 OpenCode
npm install -g opencode-ai
# 验证安装open
code --version
```

**1.2 安装 GitHub CLI（代码管理）**

```plain&#x20;text
# 下载并安装curl -fsSL https://github.com/cli/cli/releases/download/v2.63.2/gh_2.63.2_linux_amd64.tar.gz | tar -xz -C /tmpcp /tmp/gh_2.63.2_linux_amd64/bin/gh /usr/local/bin/
# 验证gh --version
```

**1.3 安装 Vercel CLI（自动部署）**

```plain&#x20;text
# 安装 Vercel CLInpm install -g vercel
# 验证vercel --version
```

***

**第二步：创建项目目录**

```plain&#x20;text
# 创建项目目录mkdir -p ~/myopencodecd ~/myopencode
# 初始化 Git 仓库git init
# 配置 Git 用户信息git config --global user.email "your@email.com"git config --global user.name "yourname"
```

***

**第三步：Agent Coding（核心步骤）**

**方式一：使用 OpenCode 交互模式**

```plain&#x20;text
# 启动 OpenCode（需要 PTY 模式）# 在 OpenClaw 中使用：bash pty:true workdir:~/myopencode command:"opencode"
```

然后在 OpenCode 中输入：

```plain&#x20;text
创建一个贪吃蛇游戏，使用 HTML5 Canvas，包含完整的游戏逻辑、得分系统和响应式设计
```

**方式二：使用 OpenCode 非交互模式**

```plain&#x20;text
# 直接运行任务opencode run "Create a complete Snake game using HTML5 Canvas, CSS, and JavaScript"
```

**方式三：手动创建（备用方案）**

如果 OpenCode 运行有问题，可以直接创建文件：

**「index. html:」**

```plain&#x20;text
<!DOCTYPE html><html lang="zh-CN"><head>    <meta charset="UTF-8">    <meta name="viewport" content="width=device-width, initial-scale=1.0">    <title>贪吃蛇游戏</title>    <link rel="stylesheet" href="style.css"></head><body>    <div class="container">        <h1>🐍 贪吃蛇游戏</h1>        <div class="game-info">            <div class="score">得分: <span id="score">0</span></div>            <div class="high-score">最高分: <span id="highScore">0</span></div>        </div>        <canvas id="gameCanvas" width="400" height="400"></canvas>        <div class="controls">            <p>使用方向键 ↑↓←→ 控制蛇的移动</p>            <button id="startBtn">开始游戏</button>            <button id="pauseBtn">暂停</button>            <button id="restartBtn">重新开始</button>        </div>        <div id="gameOver" class="game-over hidden">            <h2>游戏结束!</h2>            <p>最终得分: <span id="finalScore">0</span></p>            <button id="playAgainBtn">再玩一次</button>        </div>    </div>    <script src="game.js"></script></body></html>
```

**「style. css:」**

```plain&#x20;text
* {    margin: 0;    padding: 0;    box-sizing: border-box;}
body {    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);    min-height: 100vh;    display: flex;    justify-content: center;    align-items: center;    color: #fff;}
.container {    text-align: center;    padding: 20px;    background: rgba(255, 255, 255, 0.05);    border-radius: 20px;    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);}
h1 {    background: linear-gradient(45deg, #00d4aa, #00a8e8);    -webkit-background-clip: text;    -webkit-text-fill-color: transparent;}
#gameCanvas {    border: 3px solid #00d4aa;    border-radius: 10px;    background: #0a0a0a;}
```

**「game. js:」** (完整游戏逻辑代码)

***

**第四步：推送到 GitHub**

**4.1 提交代码**

```plain&#x20;text
# 添加所有文件git add .
# 提交git commit -m "Initial commit: Snake game with HTML5 Canvas"
```

**4.2 创建 GitHub 仓库并推送**

**「方式一：使用 GitHub CLI」**

```plain&#x20;text
# 登录 GitHubecho "YOUR_GITHUB_TOKEN" | gh auth login --with-token
# 创建仓库gh repo create snake-game --public --description "A classic Snake game"
# 推送git push -u origin master
```

**「方式二：使用 API 直接创建」**

```plain&#x20;text
# 通过 API 创建仓库curl -X POST https://api.github.com/user/repos \  -H "Authorization: token YOUR_GITHUB_TOKEN" \  -H "Accept: application/vnd.github.v3+json" \  -d '{    "name": "snake-game",    "description": "A classic Snake game built with HTML5 Canvas",    "private": false  }'
# 添加远程仓库并推送git remote add origin https://username:token@github.com/username/snake-game.gitgit push -u origin master
```

***

**第五步：部署到 Vercel**

**5.1 使用 Vercel CLI 部署**

```plain&#x20;text
# 进入项目目录cd ~/myopencode
# 使用 token 部署vercel --token YOUR_VERCEL_TOKEN --yes --prod
```

部署成功后，会输出类似：

```plain&#x20;text
Production: https://myopencode-xxx.vercel.app
```

**5.2 关联 GitHub 仓库（可选）**

Vercel CLI 会自动检测并关联 GitHub 仓库，实现自动部署：

* 每次 push 到 GitHub，Vercel 自动重新部署

* 支持预览部署（Pull Request）

***

**🎯 完整命令速查表**

***

**💡 核心优势**

**1. 「全程自动化」**

* 从需求到上线，无需手动编写代码

* AI Agent 理解自然语言，自动生成完整项目

**2. 「无缝集成」**

* OpenClaw 作为中控，协调所有工具

* GitHub 管理版本，Vercel 自动部署

**3. 「即时反馈」**

* 几分钟内从想法到可访问的网站

* 每次修改自动重新部署

**4. 「可扩展性」**

* 可以轻松扩展到更复杂的项目

* 支持 React、Vue、Next. js 等框架

***

**🔧 常见问题**

**Q 1: OpenCode 卡住不响应？**

**「解决」**: 使用非交互模式或直接用 GPT/Claude 生成代码后手动保存

**Q 2: GitHub 推送失败？**

**「解决」**: 检查 token 权限，需要 `repo` 权限

**Q 3: Vercel 部署失败？**

**「解决」**: 确保项目结构正确，静态网站不需要额外构建配置

***

**🚀 进阶玩法**

**自动评论到 PR**

```plain&#x20;text
# OpenCode 审查代码后自动评论gh pr comment <PR_NUMBER> --body "$(cat review.md)"
```

**定时自动更新**

```plain&#x20;text
# 使用 cron 定时让 AI 更新网站内容cron action:add job:{  "schedule": {"kind": "cron", "expr": "0 9 * * 1"},  "payload": {"kind": "agentTurn", "message": "更新网站内容"}}
```

**多 Agent 协作**

```plain&#x20;text
# 同时运行多个 OpenCode 处理不同任务bash pty:true background:true command:"opencode '设计前端界面'"bash pty:true background:true command:"opencode '编写后端 API'"
```

***

**📊 实际案例数据**

本次贪吃蛇项目：

* **「开发时间」**: \~5 分钟（Agent 生成代码）

* **「代码行数」**: \~400 行（HTML/CSS/JS）

* **「部署时间」**: < 10 秒

* **「最终链接」**: https://myopencode.vercel.app

***

**📝 总结**

通过 **「OpenClaw + OpenCode + GitHub + Vercel」** 的组合，我们实现了一个完整的 AI 驱动开发工作流：

1. **「说」** - 告诉 AI 你要什么

2. **「写」** - AI 自动生成代码

3. **「存」** - 自动提交到 GitHub

4. **「上线」** - 一键部署到 Vercel

这种工作流特别适合：

* 快速原型开发

* 个人项目

* 学习新技术

* 自动化重复任务

***

**🔗 相关链接**

* OpenClaw: https://docs.openclaw.ai

* OpenCode: https://opencode.ai

* GitHub: https://github.com

* Vercel: https://vercel.com

* 本案例 GitHub 仓库: https://github.com/freestylefly/snake-game

* 在线演示: https://myopencode.vercel.app

***

**🤖 OpenClaw 生成过程实录**

本文档并非人工编写，而是由 **「OpenClaw AI Agent」** 在开发过程中自动生成：

**生成流程**

1. **「需求提出」** - 用户："帮我把整个过程写成一篇文章"

2. **「Agent 分析」** - OpenClaw 分析刚才的操作历史，提取关键步骤

3. **「内容生成」** - 自动编写完整教程，包含流程图、代码示例、速查表

4. **「自动推送」** - Agent 直接将 README 提交到 GitHub 仓库

**真实的开发时间线**

```plain&#x20;text
21:49 - 用户："帮我安装 opencode"21:53 - 创建项目目录 myopencode21:56 - 启动 opencode（交互模式）21:57 - OpenCode 卡住，改用直接创建文件21:58 - 贪吃蛇游戏代码生成完成22:05 - 用户提供 GitHub 账号 freestylefly22:10 - 创建 GitHub 仓库并推送代码22:13 - 用户要求部署到 Vercel22:20 - Vercel 部署成功，游戏上线22:28 - 用户："写一篇文章记录这个过程"22:31 - README 自动生成并推送到 GitHub
```

**核心指令**

整个开发过程只用了几个简单的自然语言指令：

**「全程无需编写任何命令，只需用自然语言描述需求！」**

***

***本文档由 OpenClaw AI Agent 全程自动生成 | 2026-02-03***



# 关于作者

一个头发茂密的程序员，欢迎关注苍何，一起长发：



![](<images/OpenClaw 从入门到精通指南-扫码_搜索联合传播样式-标准色版.bmp>)


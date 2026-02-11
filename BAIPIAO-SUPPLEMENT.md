# 百度智能云部署补充内容

> 基于"OpenClaw白嫖云部署"文章整理，可直接补充到教程第2章

## 2.4 百度智能云部署（推荐白嫖方案）⭐

### 为什么选择百度智能云？

百度智能云最近推出了针对OpenClaw的特别优惠方案，是目前**性价比最高**的云端部署选择：

| 对比项 | 百度智能云 | 腾讯云 | 阿里云 |
|--------|-----------|--------|--------|
| 月费用 | **0.01元** | 20元起 | 20元起 |
| 配置 | 2H4G | 2H4G | 2H4G |
| 部署方式 | 一键部署 | 一键部署 | 一键部署 |
| 配置方式 | **界面化** | 命令行为主 | 命令行为主 |
| 香港节点 | ✅ 支持 | ✅ 支持 | ✅ 支持 |
| 适合人群 | 新手/白嫖党 | 有预算用户 | 有预算用户 |

**核心优势**：
- 💰 **超低成本**：0.01元/月，几乎免费（每天限量500台）
- 🎯 **界面化操作**：无需命令行，小白友好
- ⚡ **一键开通**：千帆大模型、云助手、运维编排OOS
- 🌍 **支持香港**：可连接国外服务
- 🖥️ **Web管理**：可视化配置模型、消息平台、Skills

### 部署步骤

#### 第一步：购买服务器

1. 访问百度智能云OpenClaw部署页面：
   ```
   https://cloud.baidu.com/product/BCC/moltbot.html
   ```

![百度智能云OpenClaw部署页面](https://upload.maynor1024.live/file/1770782669321_image_1.jpg)

2. 选择配置：
   - **地域**：如需连接国外服务，选择「香港」；否则选择离你最近的地域
   - **配置**：默认2H4G即可
   - **价格**：0.01元/月

![选择地域](https://upload.maynor1024.live/file/1770782678617_image_10.jpg)

3. 点击购买，完成支付

#### 第二步：进入管理控制台

1. 购买成功后，进入「管理控制台」

![管理控制台](https://upload.maynor1024.live/file/1770782685578_image_11.jpg)

2. 选择对应的地域（与购买时选择的一致）

3. 找到刚创建的服务器实例

![服务器实例](https://upload.maynor1024.live/file/1770782688793_image_12.jpg)

#### 第三步：一键开通相关服务

1. 点击进入服务器详情页

2. 选择「应用管理 -> 模型配置」

3. 点击「一键开通」以下服务：
   - 千帆大模型
   - 云助手
   - 运维编排OOS服务

![一键开通服务](https://upload.maynor1024.live/file/1770782692412_image_13.jpg)

> 💡 **提示**：这个一键开通功能很方便，不然这些云平台各种权限要找半天才能配置好。

#### 第四步：配置模型

1. 在「模型配置」页面，选择要使用的模型：
   - **性价比优先**：DeepSeek V3.2
   - **Agent能力优先**：Kimi-K2

![模型配置](https://upload.maynor1024.live/file/1770782691983_image_14.jpg)

2. 配置完成后，点击「应用」按钮

> ⚠️ **注意**：每次配置修改后都要点击「应用」才能生效

#### 第五步：配置消息平台

百度智能云支持以下消息平台：
- 飞书
- 企业微信
- 钉钉
- QQ

以飞书为例：

1. 在飞书开放平台获取 App ID 和 App Secret
   - 参考官方文档：[飞书接入指南](https://cloud.baidu.com/doc/qianfan/s/Mmlda41a2)

2. 在「消息平台配置」页面填入相关信息

![消息平台配置](https://upload.maynor1024.live/file/1770782698314_image_15.jpg)

3. 点击「应用」

#### 第六步：配置Skills

1. 在「Skills配置」页面，可以：
   - 使用默认推荐的Skills
   - 清空输入框，自行添加Skills

2. Skills来源：
   - OpenClaw官方：https://clawhub.ai/skills
   - 百度千帆官方Skills：https://cloud.baidu.com/doc/qianfan/s/Mmlda41a2

![Skills配置](https://upload.maynor1024.live/file/1770782700795_image_16.jpg)

3. 配置完成后，点击「应用」

**推荐Skills**：
- 百度搜索
- 百度百科
- 百度学术
- 百度智能PPT

**获取API Key**（部分Skills需要）：
```
https://console.bce.baidu.com/iam/#/iam/apikey/list
```

![获取API Key](https://upload.maynor1024.live/file/1770782712874_image_17.jpg)

#### 第七步：访问Web界面

1. 点击「获取网站地址」

![获取网站地址](https://upload.maynor1024.live/file/1770782712074_image_18.jpg)

2. 复制得到的网址，在浏览器中打开

![Web界面](https://upload.maynor1024.live/file/1770782715841_image_19.jpg)

3. 现在可以通过Web界面使用OpenClaw了！

**Web界面功能**：
- 对话交互
- Skills管理
- 配置修改

![Skills管理](https://upload.maynor1024.live/file/1770782720761_image_2.jpg)

### 高级技巧

#### 1. 让OpenClaw自动安装Skills

最简单的方式是直接告诉OpenClaw：

```
帮我安装这个Skill：https://clawhub.ai/skills/xxx
```

或者：

```
帮我安装百度搜索Skill
```

OpenClaw会自动帮你安装！

![自动安装Skills](https://upload.maynor1024.live/file/1770782726525_image_20.jpg)

#### 2. 命令行访问（高级用户）

如果你熟悉命令行，也可以点击「远程登录」，通过SSH连接服务器：

![远程登录](https://upload.maynor1024.live/file/1770782728511_image_21.jpg)

配置文件位置：
```bash
/root/.openclaw/openclaw.json
```

### 常见问题

#### Q1：每天限量500台是什么意思？

A：百度智能云的0.01元/月优惠每天只有500个名额，建议早上抢购。

#### Q2：0.01元/月能用多久？

A：首月0.01元，后续价格以百度智能云官方为准。建议关注官方活动。

#### Q3：香港节点和国内节点有什么区别？

A：
- **香港节点**：可以访问国外服务（如Claude、GPT等），但访问国内服务可能稍慢
- **国内节点**：访问国内服务快，但无法直接访问国外服务

#### Q4：界面化配置和命令行配置有什么区别？

A：
- **界面化配置**：适合新手，可视化操作，不需要懂命令行
- **命令行配置**：适合高级用户，更灵活，可以做更复杂的配置

### 下一步

部署完成后，建议：
1. 阅读 [第3章：快速上手](03-quick-start.md) 开始使用
2. 阅读 [第8章：Skills扩展](../03-advanced/08-skills-extension.md) 了解更多Skills
3. 阅读 [第11章：高级配置](../03-advanced/11-advanced-configuration.md) 进行深度定制

---

## 相关资源

- 百度智能云OpenClaw部署：https://cloud.baidu.com/product/BCC/moltbot.html
- 百度千帆官方Skills：https://cloud.baidu.com/doc/qianfan/s/Mmlda41a2
- 百度千帆MCP广场：https://cloud.baidu.com/product/qianfan_mcp.html
- OpenClaw官方文档：https://docs.openclaw.ai

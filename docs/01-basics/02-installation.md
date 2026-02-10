# 第2章：环境搭建

> 本章将手把手教你安装OpenClaw，推荐新手使用**云端一键部署**，5分钟即可完成。

## 快速导航

- 🚀 [云端一键部署（推荐新手）](#云端一键部署)
- 💻 [本地安装教程](#本地安装教程)
- 🔑 [API配置指南](#api配置指南)
- ❓ [常见问题解决](#常见问题解决)

## 2.1 系统要求与准备

### 云端部署要求

如果选择云端部署，**无需任何本地环境**，只需要：
- ✅ 一个浏览器
- ✅ 20元/月预算
- ✅ 10分钟时间

### 本地部署要求

如果选择本地部署，需要：

**硬件要求**：
- CPU：2核以上
- 内存：4GB以上
- 硬盘：10GB以上空闲空间

**操作系统**：
- macOS 12+（推荐）
- Windows 10/11
- Linux（Ubuntu 20.04+）

**前置软件**：
- Node.js 22.0.0+
- pnpm（推荐）或 npm

**网络要求**：
- 稳定的网络连接
- 能访问GitHub（用于下载）

### 为什么推荐Mac系统？

OpenClaw在Mac上体验最好，因为：
- ✅ 原生支持最完善
- ✅ 可以操作Mac日历、备忘录
- ✅ 截图功能完美支持
- ✅ 与iPhone无缝同步

但Windows和Linux也完全可用！

## 云端一键部署

> 🔥 **强烈推荐新手使用云端部署**：无需配置环境，点几下鼠标就完成！

### 为什么推荐云端部署？

| 优势 | 说明 |
|------|------|
| ⚡ **秒级部署** | 点几下鼠标就完成，无需配置环境 |
| 💰 **成本低** | 20元/月起，比买Mac Mini便宜太多 |
| 📱 **手机可用** | 通过QQ、企微、飞书随时随地访问 |
| 🔒 **稳定可靠** | 24小时运行，不用担心电脑关机 |
| 🎥 **视频教程** | 官方视频手把手教学 |

### 方案对比

| 方案 | 价格 | 带宽 | 推荐场景 |
|------|------|------|----------|
| 腾讯云Lighthouse | 20元/月，99元/年 | 20M | QQ、企微用户 |
| 火山引擎 | 9.9元/月，58元/年 | 5M | 飞书用户 |

### 腾讯云Lighthouse部署（推荐）

#### 第一步：购买服务器

1. **访问活动页面**：
   ```
   https://cloud.tencent.com/act/pro/lighthouse-moltbot
   ```

2. **选择配置**：
   - 配置：2核2G
   - 带宽：20M
   - 价格：20元/月 或 99元/年

![飞书界面](https://upload.maynor1024.live/file/1770176084594_640.png)

3. **实名认证**：
   - 首次使用需要实名认证
   - 选择个人认证即可
   - 按提示完成认证

4. **完成购买**：
   - 点击"立即购买"
   - 支付20元（建议先买1个月试用）
   - 等待服务器创建完成

#### 第二步：一键部署OpenClaw

1. **进入控制台**：
   - 购买成功后，点击"查看实例"
   - 进入轻量应用服务器控制台

2. **选择OpenClaw镜像**：
   - 系统会自动选择OpenClaw应用镜像
   - 无需手动配置

3. **等待部署完成**：
   - 部署过程约1-2分钟
   - 完成后会显示访问地址

#### 第三步：配置大模型

1. **进入应用管理**：
   - 点击服务器卡片
   - 切换到"应用管理"标签

2. **选择模型**：
   - 推荐使用 **Kimi k2.5**（性价比最高）
   - 也可以选择其他国产大模型

3. **获取API Key**：
   
   **Kimi k2.5配置**（推荐）：
   ```
   1. 访问：https://platform.moonshot.cn/
   2. 注册账号并登录
   3. 进入"API管理"
   4. 点击"创建API Key"
   5. 复制API Key（格式：sk-xxx）
   ```

4. **填入配置**：
   - 将API Key粘贴到配置框
   - 点击"保存"
   - 等待配置生效

#### 第四步：测试连接

1. **访问WebUI**：
   - 使用控制台提供的访问地址
   - 格式：`http://你的服务器IP:18789/?token=xxx`

2. **发送测试消息**：
   ```
   你好，能听到我说话吗？
   ```

3. **验证成功**：
   - 如果收到AI回复，说明配置成功
   - 右上角会显示使用的模型名称

### 火山引擎部署（更便宜）

如果你是飞书重度用户，推荐使用火山引擎：

1. **访问活动页面**：
   ```
   https://www.volcengine.com/activity/clawdbot
   ```

2. **价格优势**：
   - 9.9元/月
   - 58元/年
   - 比腾讯云便宜10元

3. **配置对比**：
   - 2核2G（相同）
   - 5M带宽（腾讯云20M）
   - 适合飞书用户

4. **部署流程**：
   - 与腾讯云类似
   - 按照页面提示操作即可

### 官方视频教程（强烈推荐）

腾讯云提供了详细的视频教程，跟着视频操作更简单：

1. **云上OpenClaw一键部署并接入企微和QQ**
   - 视频地址：https://cloud.tencent.com/developer/video/85003
   - 时长：约10分钟
   - 内容：从购买到配置完成

2. **云上OpenClaw一键部署并接入飞书和钉钉**
   - 视频地址：https://cloud.tencent.com/developer/video/85055
   - 时长：约10分钟
   - 内容：飞书和钉钉接入全流程

### 存量服务器部署

如果你已经有轻量服务器，可以使用AI助手对话式部署：

- **官方教程**：https://cloud.tencent.com/developer/article/2625605
- **适用场景**：已有轻量服务器
- **部署方式**：通过AI对话完成配置
- **优势**：更灵活，可自定义

### 云端部署常见问题

**Q1: 云端部署安全吗？**
- ✅ 数据存储在你的服务器上
- ✅ 只有你能访问
- ✅ 可以设置访问密码

**Q2: 可以随时停止吗？**
- ✅ 可以随时删除服务器
- ✅ 按使用时长计费
- ✅ 不用了就删除，不浪费钱

**Q3: 手机怎么访问？**
- 通过QQ、企微、飞书等平台
- 详见[第9章：多平台集成](../03-advanced/09-platform-integration.md)

## 本地安装教程

> 如果你有Mac电脑，或者想完全本地部署，可以选择本地安装。

### macOS安装步骤

#### 第一步：升级Node.js

OpenClaw要求Node.js 22+，使用nvm管理版本：

```bash
# 安装nvm（如果还没安装）
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash

# 重启终端，然后安装Node.js 22
nvm install 22

# 设置为默认版本
nvm use 22
nvm alias default 22

# 验证版本
node --version  # 应显示 v22.x.x
```

#### 第二步：使用官方安装脚本

```bash
# 一键安装
curl -fsSL https://clawd.bot/install.sh | bash
```

安装过程说明：
- 自动检测系统环境
- 安装依赖包（约1010个包）
- 构建TypeScript代码
- 构建Web UI
- 安装命令行工具

#### 第三步：初始化配置

```bash
# 运行配置向导
clawdbot onboard
```

配置向导流程：

1. **选择AI模型**：
   - 默认：`anthropic/claude-opus-4-5`
   - 可选：Claude Haiku、Sonnet、Opus系列

2. **配置技能（Skills）**：
   - 跳过可选依赖安装
   - 跳过API key配置（稍后手动配置）

3. **启用Hooks**：
   - 推荐启用`session-memory`（会话记忆）

4. **Gateway运行时**：
   - 自动选择Node.js 22+
   - 安装为系统服务（macOS: LaunchAgent）

5. **消息通道**：
   - 可选配置Telegram、Discord等
   - 建议先跳过，使用Web UI测试

6. **完成配置**：
   - Gateway服务自动启动
   - 获取Web UI访问链接

#### 第四步：验证安装

```bash
# 检查Gateway状态
clawdbot channels status

# 应该显示：
# Gateway reachable.
```

### Windows安装步骤

#### 第一步：安装Node.js

1. 访问Node.js官网：https://nodejs.org/
2. 下载Windows安装包（22.x LTS版本）
3. 运行安装程序
4. 验证安装：
   ```cmd
   node --version
   ```

#### 第二步：安装OpenClaw

```cmd
# 使用PowerShell运行
irm https://clawd.bot/install.ps1 | iex
```

#### 第三步：初始化配置

```cmd
clawdbot onboard
```

按照提示完成配置（与macOS相同）。

### Linux安装步骤

#### 第一步：安装Node.js

```bash
# Ubuntu/Debian
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt-get install -y nodejs

# 验证安装
node --version
```

#### 第二步：安装OpenClaw

```bash
curl -fsSL https://clawd.bot/install.sh | bash
```

#### 第三步：初始化配置

```bash
clawdbot onboard
```

## API配置指南

> OpenClaw需要连接AI模型才能工作，推荐使用**国产大模型**，性价比高。

### 为什么需要API？

OpenClaw本身不包含AI模型，需要连接第三方API：
- 官方API：价格贵、国内访问困难
- 第三方API：价格便宜、国内直连

### 国产大模型配置（推荐）

#### 1. DeepSeek配置（性价比之王）

**特点**：
- 💰 **最便宜**：输入0.001元/千tokens
- 🧠 **推理能力强**：适合复杂任务
- 💻 **编程能力出色**：代码生成质量高

**配置步骤**：

1. **注册账号**：
   ```
   访问：https://platform.deepseek.com/
   注册并登录
   ```

2. **获取API Key**：
   ```
   进入"API管理"
   点击"创建API Key"
   复制API Key（格式：sk-xxx）
   ```

3. **配置到OpenClaw**：
   ```bash
   # 编辑配置文件
   nano ~/.clawdbot/clawdbot.json
   ```

   添加配置：
   ```json
   {
     "models": {
       "mode": "merge",
       "providers": {
         "deepseek": {
           "baseUrl": "https://api.deepseek.com",
           "apiKey": "sk-你的API密钥",
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
         }
       }
     },
     "agents": {
       "defaults": {
         "model": {
           "primary": "deepseek/deepseek-chat"
         }
       }
     }
   }
   ```

4. **重启Gateway**：
   ```bash
   clawdbot gateway restart
   ```

**成本估算**：
- 日常使用：5-10元/月
- 中度使用：10-30元/月
- 重度使用：30-50元/月

#### 2. Kimi配置（长文本专家）

**特点**：
- 📚 **超长上下文**：支持200万字
- 📄 **长文档处理**：论文、报告分析专家
- 🎯 **中文理解好**：适合中文场景

**配置步骤**：

1. **注册账号**：
   ```
   访问：https://platform.moonshot.cn/
   注册并登录
   ```

2. **获取API Key**：
   ```
   进入"API管理"
   点击"创建API Key"
   复制API Key
   ```

3. **配置到OpenClaw**：
   ```json
   {
     "models": {
       "mode": "merge",
       "providers": {
         "moonshot": {
           "baseUrl": "https://api.moonshot.cn/v1",
           "apiKey": "sk-你的API密钥",
           "auth": "api-key",
           "api": "openai-chat",
           "models": [
             {
               "id": "moonshot-v1-8k",
               "name": "Kimi k2.5",
               "contextWindow": 8000,
               "maxTokens": 4096
             }
           ]
         }
       }
     },
     "agents": {
       "defaults": {
         "model": {
           "primary": "moonshot/moonshot-v1-8k"
         }
       }
     }
   }
   ```

**成本估算**：
- 日常使用：10-20元/月
- 中度使用：20-50元/月
- 重度使用：50-100元/月

#### 3. 其他国产大模型

| 模型 | 特点 | 价格 | 官网 |
|------|------|------|------|
| GLM-4 | 多模态能力强 | 中等 | https://open.bigmodel.cn/ |
| 文心一言 | 百度生态 | 中高 | https://cloud.baidu.com/ |
| 通义千问 | 阿里生态 | 中等 | https://dashscope.aliyun.com/ |

### 国际模型配置（可选）

如果需要使用Claude、GPT等国际模型：

1. **直接使用官方API**（需要魔法）
2. **使用第三方API服务**（国内直连）

**推荐第三方API**：
- 价格便宜50%-70%
- 国内直连，无需魔法
- 支持支付宝、微信支付

### 成本对比

| 模型 | 输入价格 | 输出价格 | 月费用估算 |
|------|----------|----------|-----------|
| DeepSeek | 0.001元/千tokens | 0.002元/千tokens | 5-30元 |
| Kimi | 0.012元/千tokens | 0.012元/千tokens | 10-50元 |
| GLM-4 | 0.005元/千tokens | 0.005元/千tokens | 10-40元 |
| Claude（第三方） | 0.015元/千tokens | 0.075元/千tokens | 50-200元 |
| GPT-4（第三方） | 0.03元/千tokens | 0.06元/千tokens | 100-300元 |

💡 **省钱技巧**：
- 日常对话用DeepSeek（最便宜）
- 长文档用Kimi（长上下文）
- 复杂任务用Claude（质量最高）

## 常见问题解决

### 安装问题

**Q1: Node.js版本不对**
```bash
# 检查版本
node --version

# 如果低于22，升级
nvm install 22
nvm use 22
```

**Q2: 权限错误**
```bash
# macOS/Linux
sudo chown -R $USER ~/.clawdbot

# Windows
# 以管理员身份运行PowerShell
```

**Q3: 网络连接失败**
- 检查网络连接
- 尝试使用代理
- 或使用云端部署

### API配置问题

**Q1: API Key无效**
- 检查是否完整复制（包括sk-前缀）
- 检查是否有多余空格
- 检查账户余额是否充足

**Q2: 模型不可用**
- 检查模型ID是否正确
- 检查API服务是否正常
- 尝试切换其他模型

**Q3: Token消耗太快**
- 使用更便宜的模型（DeepSeek）
- 优化提示词
- 定期清理会话历史

### Gateway问题

**Q1: Gateway无法启动**
```bash
# 查看日志
tail -f ~/.clawdbot/logs/gateway.log

# 重启Gateway
clawdbot gateway restart
```

**Q2: 端口被占用**
```bash
# 查看端口占用
lsof -i :18789

# 修改端口
clawdbot config set gateway.port 18790
```

## 本章小结

通过本章，你应该已经：

✅ 了解了云端部署和本地部署的区别  
✅ 完成了OpenClaw的安装（云端或本地）  
✅ 配置了API（推荐国产大模型）  
✅ 验证了安装是否成功  

## 实战练习

1. 完成OpenClaw安装（云端或本地）
2. 配置至少一个API（推荐DeepSeek或Kimi）
3. 发送第一条测试消息
4. 验证AI是否正常回复

---

**下一章**：[第3章：快速上手](03-quick-start.md) - 开始使用OpenClaw

**返回目录**：[README](../../README.md)

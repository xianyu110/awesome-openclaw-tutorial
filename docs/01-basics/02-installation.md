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

3. **实名认证**：
   - 首次使用需要实名认证
   - 选择个人认证即可
   - 按提示完成认证

4. **完成购买**：
   - 点击"立即购买"
   - 支付20元（建议先买1个月试用）
   - 等待服务器创建完成

![腾讯云轻量服务器](https://upload.maynor1024.live/file/1770742212222_01-tencent-cloud-server.png)

#### 第二步：一键部署OpenClaw

1. **进入控制台**：
   - 购买成功后，点击"查看实例"
   - 进入轻量应用服务器控制台

2. **选择OpenClaw镜像**：
   - 系统会自动选择OpenClaw应用镜像
   - 无需手动配置

![OpenClaw镜像](https://upload.maynor1024.live/file/1770742213992_02-openclaw-image.png)

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

![选择AI供应商](https://upload.maynor1024.live/file/1770742221938_03-select-ai-provider.png)

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

![测试对话](https://upload.maynor1024.live/file/1770742223389_04-test-chat.png)

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

### 阿里云部署（可选）

阿里云也提供了OpenClaw一键部署方案：

1. **访问活动页面**：
   ```
   https://www.aliyun.com/activity/ecs/clawdbot
   ```

2. **选择轻量应用服务器**：
   - 使用OpenClaw镜像
   - 一键安装配置

![阿里云轻量服务器](https://upload.maynor1024.live/file/1770742237148_05-aliyun-server.png)

3. **价格参考**：
   - 与腾讯云类似
   - 具体以活动页面为准

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

## Docker 部署

> 🐳 **推荐开发者使用**：Docker 部署简单、隔离性好、易于管理。

### 为什么选择 Docker？

| 优势 | 说明 |
|------|------|
| 🔒 **环境隔离** | 不影响系统环境，干净整洁 |
| 📦 **一键部署** | 无需配置依赖，开箱即用 |
| 🔄 **易于更新** | 一条命令完成更新 |
| 🌐 **跨平台** | Windows/macOS/Linux 统一方案 |
| 🚀 **快速启动** | 5分钟完成部署 |

### 前置要求

**安装 Docker**：

**macOS**：
```bash
# 下载 Docker Desktop
# 访问：https://www.docker.com/products/docker-desktop

# 或使用 Homebrew
brew install --cask docker
```

**Windows**：
```bash
# 下载 Docker Desktop
# 访问：https://www.docker.com/products/docker-desktop

# 安装 WSL2（如果还没安装）
wsl --install
```

**Linux (Ubuntu)**：
```bash
# 安装 Docker
curl -fsSL https://get.docker.com | sh

# 启动 Docker 服务
sudo systemctl start docker
sudo systemctl enable docker

# 添加当前用户到 docker 组
sudo usermod -aG docker $USER
```

**验证安装**：
```bash
docker --version
# 应显示：Docker version 24.x.x
```

### 快速开始

#### 方式一：一键脚本部署（推荐新手）

最简单的方式，一条命令搞定所有配置！

```bash
curl -fsSL https://clawd.org.cn/install.sh | bash
```

**这个脚本会自动：**
- ✅ 检查 Docker 环境
- ✅ 下载镜像（使用国内镜像：`jiulingyun803/openclaw-cn:latest`）
- ✅ 配置环境变量
- ✅ 启动容器
- ✅ 运行配置向导
- ✅ 生成网关令牌

完成后，在浏览器打开 `http://127.0.0.1:18789/` 即可使用。

**脚本后续操作**：
- 按照提示输入渠道信息（可选）
- 将生成的令牌复制到 Web UI 登录

#### 方式二：手动 Docker Compose 部署（适合进阶用户）

如果一键脚本不适用，或需要自定义配置，按以下步骤操作。

**步骤 1：创建工作目录**

```bash
mkdir -p ~/openclaw-docker
cd ~/openclaw-docker
```

**步骤 2：创建 `.env` 环境文件**

```bash
cat > .env << 'EOF'
# 镜像配置（使用国内镜像）
OPENCLAW_IMAGE=jiulingyun803/openclaw-cn:latest

# 数据目录
OPENCLAW_CONFIG_DIR=./data/.openclaw
OPENCLAW_WORKSPACE_DIR=./data/clawd

# 网关配置
OPENCLAW_GATEWAY_PORT=18789
OPENCLAW_BRIDGE_PORT=18790
OPENCLAW_GATEWAY_BIND=lan
OPENCLAW_GATEWAY_TOKEN=your-secure-token-here

# Claude 集成（可选）
CLAUDE_AI_SESSION_KEY=
CLAUDE_WEB_SESSION_KEY=
CLAUDE_WEB_COOKIE=
EOF
```

**步骤 3：创建 `docker-compose.yml` 文件**

```yaml
services:
  openclaw-cn-gateway:
    image: ${OPENCLAW_IMAGE:-jiulingyun803/openclaw-cn:latest}
    user: node:node
    environment:
      HOME: /home/node
      TERM: xterm-256color
      OPENCLAW_GATEWAY_TOKEN: ${OPENCLAW_GATEWAY_TOKEN}
      CLAUDE_AI_SESSION_KEY: ${CLAUDE_AI_SESSION_KEY}
      CLAUDE_WEB_SESSION_KEY: ${CLAUDE_WEB_SESSION_KEY}
      CLAUDE_WEB_COOKIE: ${CLAUDE_WEB_COOKIE}
    volumes:
      - ${OPENCLAW_CONFIG_DIR:-./data/.openclaw}:/home/node/.openclaw
      - ${OPENCLAW_WORKSPACE_DIR:-./data/clawd}:/home/node/clawd
    ports:
      - "${OPENCLAW_GATEWAY_PORT:-18789}:18789"
      - "${OPENCLAW_BRIDGE_PORT:-18790}:18790"
    init: true
    restart: unless-stopped
    command:
      [
        "node",
        "dist/index.js",
        "gateway",
        "--bind",
        "${OPENCLAW_GATEWAY_BIND:-lan}",
        "--port",
        "${OPENCLAW_GATEWAY_PORT:-18789}"
      ]

  openclaw-cn-cli:
    image: ${OPENCLAW_IMAGE:-jiulingyun803/openclaw-cn:latest}
    user: node:node
    environment:
      HOME: /home/node
      TERM: xterm-256color
      BROWSER: echo
      CLAUDE_AI_SESSION_KEY: ${CLAUDE_AI_SESSION_KEY}
      CLAUDE_WEB_SESSION_KEY: ${CLAUDE_WEB_SESSION_KEY}
      CLAUDE_WEB_COOKIE: ${CLAUDE_WEB_COOKIE}
    volumes:
      - ${OPENCLAW_CONFIG_DIR:-./data/.openclaw}:/home/node/.openclaw
      - ${OPENCLAW_WORKSPACE_DIR:-./data/clawd}:/home/node/clawd
    stdin_open: true
    tty: true
    init: true
    entrypoint: ["node", "dist/index.js"]
```

**步骤 4：启动容器**

```bash
# 拉取最新镜像
docker compose pull

# 启动网关（后台运行）
docker compose up -d openclaw-cn-gateway

# 查看日志（可选）
docker compose logs -f openclaw-cn-gateway
```

**步骤 5：运行配置向导**

```bash
docker compose run --rm openclaw-cn-cli onboard
```

配置向导会提示你：
- 选择网关后端（Claude、Gemini 等）
- 配置 Feishu、Telegram 等渠道
- 生成和保存配置

**步骤 6：访问 Web UI**

打开浏览器访问：`http://127.0.0.1:18789/`

将配置向导生成的令牌复制到登录页面即可。

### 环境变量详解

| 变量 | 含义 | 默认值 | 必需 | 说明 |
|------|------|--------|------|------|
| OPENCLAW_IMAGE | Docker 镜像名称 | jiulingyun803/openclaw-cn:latest | ❌ | 使用国内镜像，也可指定版本号 |
| OPENCLAW_CONFIG_DIR | 配置文件目录 | ./data/.openclaw | ❌ | OpenClaw 配置和凭证存储位置 |
| OPENCLAW_WORKSPACE_DIR | 工作空间目录 | ./data/clawd | ❌ | 代理工作文件存储位置 |
| OPENCLAW_GATEWAY_PORT | 网关端口号 | 18789 | ❌ | 访问 Web UI 的端口 |
| OPENCLAW_BRIDGE_PORT | 桥接端口号 | 18790 | ❌ | 用于客户端连接的端口 |
| OPENCLAW_GATEWAY_BIND | 网关绑定地址 | lan | ❌ | localhost（仅本机）/ lan（局域网）/ 0.0.0.0（公网，⚠️ 谨慎使用） |
| OPENCLAW_GATEWAY_TOKEN | 网关认证令牌 | 自动生成 | ❌ | Web UI 登录令牌（可自定义或留空自动生成） |
| CLAUDE_AI_SESSION_KEY | Claude.ai 会话密钥 | 空 | ❌ | ⚠️ 仅使用 Claude AI 作为后端时填写 |
| CLAUDE_WEB_SESSION_KEY | Claude Web 会话密钥 | 空 | ❌ | ⚠️ 仅使用 Claude Web 版时填写 |
| CLAUDE_WEB_COOKIE | Claude Web Cookie | 空 | ❌ | ⚠️ 仅使用 Claude Web 版时填写 |

**环境变量设置方式**：

**方式 A：编辑 `.env` 文件（推荐）**
```bash
# 编辑 .env 文件
nano .env

# docker compose 会自动读取
docker compose up -d
```

**方式 B：命令行设置**
```bash
export OPENCLAW_GATEWAY_PORT=18789
docker compose up -d
```

**方式 C：命令行临时覆盖**
```bash
docker compose -e OPENCLAW_GATEWAY_PORT=8080 up -d
```

### 常用操作

#### 查看网关状态

```bash
# 检查容器是否运行
docker compose ps

# 查看网关日志
docker compose logs openclaw-cn-gateway

# 实时查看日志（持续跟踪）
docker compose logs -f openclaw-cn-gateway
```

#### 配置渠道

通过 CLI 容器配置各类渠道：

**Telegram（需要机器人令牌）**：
```bash
docker compose run --rm openclaw-cn-cli channels add \
  --channel telegram \
  --token "YOUR_BOT_TOKEN"
```

**Discord（需要机器人令牌）**：
```bash
docker compose run --rm openclaw-cn-cli channels add \
  --channel discord \
  --token "YOUR_BOT_TOKEN"
```

**WhatsApp（QR 扫码）**：
```bash
docker compose run --rm openclaw-cn-cli channels login
```

**Feishu（需要 App ID 和 Secret）**：
```bash
docker compose run --rm openclaw-cn-cli onboard
# 按提示输入信息
```

#### 重新配置

```bash
# 重新运行配置向导
docker compose run --rm openclaw-cn-cli onboard

# 查看当前配置
docker compose run --rm openclaw-cn-cli config get
```

#### 重启网关

```bash
# 重启网关容器
docker compose restart openclaw-cn-gateway

# 停止网关
docker compose down

# 重新启动
docker compose up -d openclaw-cn-gateway
```

#### 更新到最新版本

```bash
# 拉取最新镜像
docker compose pull

# 重启容器（自动使用新镜像）
docker compose up -d openclaw-cn-gateway
```

#### 清理数据（谨慎操作）

```bash
# 停止并删除容器
docker compose down

# 删除本地数据目录
rm -rf ./data/

# 删除本地镜像（可选）
docker rmi jiulingyun803/openclaw-cn:latest
```

### 数据持久化

Docker 容器的数据存储在工作目录的 `data` 文件夹：

```bash
~/openclaw-docker/data/
├── .openclaw/         # 配置文件
│   ├── openclaw.json  # 主配置
│   └── logs/          # 日志文件
└── clawd/             # 工作空间
    └── workspace/     # 代理工作文件
```

**备份数据**：
```bash
# 备份配置和数据
tar -czf openclaw-backup-$(date +%Y%m%d).tar.gz ./data

# 恢复数据
tar -xzf openclaw-backup-20260210.tar.gz
```

### Docker 部署常见问题

#### 问题 1：容器无法启动

**症状**：`docker compose up` 后容器立即退出

**解决方案**：
```bash
# 查看详细错误日志
docker compose logs openclaw-cn-gateway

# 检查端口是否被占用
sudo netstat -ltnp | grep 18789
# macOS 使用：lsof -i :18789

# 如果被占用，修改 OPENCLAW_GATEWAY_PORT
# 编辑 .env，将端口改为其他（如 18790）
nano .env
```

#### 问题 2：权限拒绝（Permission Denied）

**症状**：`Error: EACCES: permission denied, mkdir ...`

**解决方案**：
```bash
# 确保数据目录存在且权限正确
mkdir -p ./data/.openclaw ./data/clawd
chmod 755 ./data/.openclaw ./data/clawd

# 如果使用了宿主机路径，确保目录可写
chmod 777 ./data
```

#### 问题 3：无法访问 Web UI

**症状**：浏览器访问 `http://127.0.0.1:18789` 无响应

**解决方案**：
```bash
# 检查容器是否运行
docker compose ps

# 检查网关日志
docker compose logs openclaw-cn-gateway

# 验证端口是否正确
# 如果 OPENCLAW_GATEWAY_PORT=18789，则访问 :18789
# 如果改了端口，访问对应的新端口

# 检查防火墙设置
# macOS
sudo pfctl -d  # 临时关闭防火墙测试

# Linux
sudo ufw status
sudo ufw allow 18789
```

#### 问题 4：配置向导卡住

**症状**：`docker compose run --rm openclaw-cn-cli onboard` 无反应

**解决方案**：
```bash
# 按 Ctrl+C 中断

# 检查网关是否运行
docker compose logs openclaw-cn-gateway

# 重新启动网关并重试
docker compose restart openclaw-cn-gateway
docker compose run --rm openclaw-cn-cli onboard
```

#### 问题 5：镜像拉取失败（403 错误）

**症状**：`docker pull openclaw/openclaw:latest` 返回 403 错误

**解决方案**：
```bash
# 使用国内镜像（推荐）
docker pull jiulingyun803/openclaw-cn:latest

# 或在 .env 文件中指定国内镜像
echo "OPENCLAW_IMAGE=jiulingyun803/openclaw-cn:latest" >> .env

# 重新拉取
docker compose pull
```

#### 问题 6：网络超时

**症状**：拉取镜像或访问 API 时网络超时

**解决方案**：
```bash
# 配置 Docker 镜像加速（国内用户）
# 编辑 Docker 配置
sudo nano /etc/docker/daemon.json

# 添加镜像加速器
{
  "registry-mirrors": [
    "https://docker.mirrors.ustc.edu.cn",
    "https://hub-mirror.c.163.com"
  ]
}

# 重启 Docker
sudo systemctl restart docker

# macOS 用户在 Docker Desktop 设置中添加镜像加速器
```

#### 问题 7：数据丢失

**症状**：重启容器后配置和数据丢失

**解决方案**：
```bash
# 确保使用了数据卷挂载
# 检查 docker-compose.yml 中的 volumes 配置

# 查看数据是否存在
ls -la ./data/.openclaw
ls -la ./data/clawd

# 如果数据丢失，从备份恢复
tar -xzf openclaw-backup-20260210.tar.gz
```

#### 问题 8：性能问题

**症状**：容器运行缓慢或占用资源过高

**解决方案**：
```bash
# 限制资源使用（编辑 docker-compose.yml）
services:
  openclaw-cn-gateway:
    # ... 其他配置
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 2G
        reservations:
          cpus: '1'
          memory: 1G

# 重启容器
docker compose up -d openclaw-cn-gateway
```

### 从一键脚本迁移到手动配置

如果想从一键脚本切换到手动配置（或反之）：

```bash
# 停止现有容器
docker compose down

# 备份现有配置
cp -r ~/.openclaw ~/.openclaw.backup

# 更新 .env 和 docker-compose.yml

# 重新启动
docker compose up -d openclaw-cn-gateway
```

配置会自动保留在数据目录中，无需重新设置。

### Docker 部署优势总结

✅ **环境隔离**：不影响系统环境  
✅ **快速部署**：5分钟完成  
✅ **易于管理**：一条命令更新  
✅ **跨平台**：统一部署方案  
✅ **可扩展**：支持多实例部署  
✅ **国内优化**：使用国内镜像，下载速度快

**推荐使用场景**：
- 开发者本地测试
- 服务器部署
- 多环境隔离
- 快速体验 OpenClaw

**下一步**：
- 配置 API 模型（见下文"API配置指南"）
- 配置通讯渠道（见[第9章：多平台集成](../03-advanced/09-multi-platform-integration.md)）
- 安装 Skills（见[第8章：Skills扩展](../03-advanced/08-skills-extension.md)）

---

## Fly.io 云端部署

> ☁️ **推荐开发者使用**：Fly.io 提供免费额度，全球 CDN，部署简单。

### 为什么选择 Fly.io？

| 优势 | 说明 |
|------|------|
| 💰 **免费额度** | 每月免费 3 个小型应用 |
| 🌍 **全球 CDN** | 自动选择最近节点 |
| 🚀 **快速部署** | 一条命令完成部署 |
| 📊 **自动扩展** | 根据负载自动扩容 |
| 🔒 **HTTPS 免费** | 自动配置 SSL 证书 |

### 前置要求

**安装 Fly CLI**：

**macOS/Linux**：
```bash
curl -L https://fly.io/install.sh | sh
```

**Windows**：
```powershell
iwr https://fly.io/install.ps1 -useb | iex
```

**验证安装**：
```bash
flyctl version
```

### 快速开始

#### 1. 注册并登录

```bash
# 注册账号（会打开浏览器）
flyctl auth signup

# 或登录已有账号
flyctl auth login
```

#### 2. 创建应用

```bash
# 创建新应用
flyctl apps create openclaw-app

# 或使用随机名称
flyctl apps create
```

#### 3. 配置应用

创建 `fly.toml` 文件：

```toml
app = "openclaw-app"
primary_region = "hkg"  # 香港节点，国内访问快

[build]
  image = "openclaw/openclaw:latest"

[env]
  OPENCLAW_PORT = "8080"
  NODE_ENV = "production"

[http_service]
  internal_port = 18789
  force_https = true
  auto_stop_machines = true
  auto_start_machines = true
  min_machines_running = 0

[[vm]]
  cpu_kind = "shared"
  cpus = 1
  memory_mb = 512

[[mounts]]
  source = "openclaw_data"
  destination = "/root/.openclaw"
```

#### 4. 创建存储卷

```bash
# 创建 1GB 存储卷
flyctl volumes create openclaw_data \
  --region hkg \
  --size 1
```

#### 5. 部署应用

```bash
# 部署
flyctl deploy

# 查看状态
flyctl status

# 查看日志
flyctl logs
```

#### 6. 配置 API

```bash
# 设置环境变量
flyctl secrets set DEEPSEEK_API_KEY=sk-your-api-key

# 或编辑配置文件
flyctl ssh console
nano ~/.openclaw/openclaw.json
```

### 访问应用

```bash
# 获取应用 URL
flyctl info

# 打开应用
flyctl open
```

应用地址格式：`https://openclaw-app.fly.dev`

### 自定义域名

```bash
# 添加自定义域名
flyctl certs add your-domain.com

# 配置 DNS
# 添加 CNAME 记录：your-domain.com -> openclaw-app.fly.dev
```

### 扩容和缩容

```bash
# 增加内存
flyctl scale memory 1024

# 增加 CPU
flyctl scale vm shared-cpu-2x

# 增加实例数量
flyctl scale count 2

# 查看当前配置
flyctl scale show
```

### 常用命令

```bash
# 查看应用列表
flyctl apps list

# 查看应用状态
flyctl status

# 查看日志
flyctl logs

# 重启应用
flyctl apps restart

# SSH 连接
flyctl ssh console

# 删除应用
flyctl apps destroy openclaw-app
```

### 成本估算

**免费额度**：
- 3 个共享 CPU 应用
- 每个应用 256MB 内存
- 3GB 存储
- 160GB 出站流量

**付费价格**（超出免费额度）：
- CPU：$0.02/小时
- 内存：$0.0000022/MB/小时
- 存储：$0.15/GB/月
- 流量：$0.02/GB

**月成本估算**：
- 轻度使用：$0（免费额度内）
- 中度使用：$5-10/月
- 重度使用：$10-20/月

### Fly.io 部署常见问题

**Q1: 部署失败**
```bash
# 查看详细日志
flyctl logs

# 检查配置
flyctl config validate
```

**Q2: 应用无法访问**
```bash
# 检查健康状态
flyctl checks list

# 重启应用
flyctl apps restart
```

**Q3: 数据丢失**
- 确保创建了存储卷
- 定期备份数据

**Q4: 国内访问慢**
- 选择香港节点（hkg）
- 或使用自定义域名 + CDN

---

## Railway 云端部署

> 🚂 **推荐新手使用**：Railway 界面友好，一键部署，免费额度充足。

### 为什么选择 Railway？

| 优势 | 说明 |
|------|------|
| 🎨 **界面友好** | 可视化操作，无需命令行 |
| 💰 **免费额度** | 每月 $5 免费额度 |
| 🚀 **一键部署** | 从 GitHub 直接部署 |
| 📊 **自动构建** | Git push 自动部署 |
| 🔗 **数据库集成** | 一键添加 PostgreSQL/Redis |

### 快速开始

#### 方式一：从模板部署（最简单）

1. **访问 Railway**：
   ```
   https://railway.app/
   ```

2. **登录账号**：
   - 使用 GitHub 账号登录
   - 授权 Railway 访问

3. **创建项目**：
   - 点击 "New Project"
   - 选择 "Deploy from Docker Image"
   - 输入镜像：`openclaw/openclaw:latest`

4. **配置环境变量**：
   ```
   OPENCLAW_PORT=18789
   NODE_ENV=production
   DEEPSEEK_API_KEY=sk-your-api-key
   ```

5. **部署**：
   - 点击 "Deploy"
   - 等待部署完成（约 2-3 分钟）

6. **访问应用**：
   - 点击 "Generate Domain"
   - 获得公网地址：`https://openclaw-app.up.railway.app`

#### 方式二：从 GitHub 部署

1. **Fork 仓库**：
   ```
   https://github.com/openclaw/openclaw
   ```

2. **连接 Railway**：
   - 在 Railway 中选择 "Deploy from GitHub"
   - 选择你 fork 的仓库

3. **自动部署**：
   - Railway 自动检测配置
   - 自动构建和部署

4. **配置环境变量**：
   - 在 Railway 控制台添加环境变量
   - 保存后自动重新部署

### 添加数据库

如果需要持久化存储：

```bash
# 在 Railway 控制台
1. 点击 "New" -> "Database"
2. 选择 "PostgreSQL"
3. 自动创建并连接
```

Railway 会自动设置环境变量：
- `DATABASE_URL`
- `POSTGRES_HOST`
- `POSTGRES_PORT`
- `POSTGRES_USER`
- `POSTGRES_PASSWORD`

### 自定义域名

```bash
# 在 Railway 控制台
1. 进入项目设置
2. 点击 "Domains"
3. 点击 "Add Domain"
4. 输入你的域名
5. 配置 DNS CNAME 记录
```

### 查看日志

```bash
# 在 Railway 控制台
1. 进入项目
2. 点击 "Deployments"
3. 选择最新部署
4. 查看实时日志
```

### 环境变量管理

```bash
# 在 Railway 控制台
1. 进入项目设置
2. 点击 "Variables"
3. 添加/编辑变量
4. 保存后自动重新部署
```

常用环境变量：
```
OPENCLAW_PORT=18789
NODE_ENV=production
DEEPSEEK_API_KEY=sk-xxx
MOONSHOT_API_KEY=sk-xxx
LOG_LEVEL=info
```

### 成本估算

**免费额度**：
- $5/月免费额度
- 512MB 内存
- 1GB 存储
- 100GB 出站流量

**付费价格**（超出免费额度）：
- 按使用量计费
- 约 $0.000463/GB-秒

**月成本估算**：
- 轻度使用：$0（免费额度内）
- 中度使用：$5-10/月
- 重度使用：$10-20/月

### Railway CLI（可选）

**安装 CLI**：
```bash
# macOS/Linux
npm install -g @railway/cli

# 或使用 Homebrew
brew install railway
```

**使用 CLI**：
```bash
# 登录
railway login

# 初始化项目
railway init

# 部署
railway up

# 查看日志
railway logs

# 打开控制台
railway open
```

### Railway 部署常见问题

**Q1: 部署失败**
- 检查 Dockerfile 或 railway.json 配置
- 查看构建日志
- 确认环境变量正确

**Q2: 应用无法访问**
- 检查端口配置（必须使用 Railway 提供的 PORT 环境变量）
- 检查健康检查配置

**Q3: 超出免费额度**
- 查看使用量统计
- 优化资源使用
- 考虑升级付费计划

**Q4: 数据丢失**
- 使用 Railway 提供的数据库服务
- 定期备份数据

---

## 更新和维护

> 🔄 **保持最新**：定期更新 OpenClaw 以获得新功能和安全修复。

### 检查更新

```bash
# 检查当前版本
openclaw --version

# 检查最新版本
curl -s https://api.github.com/repos/openclaw/openclaw/releases/latest | grep tag_name
```

### 本地安装更新

```bash
# 方式一：使用安装脚本
curl -fsSL https://openclaw.ai/install.sh | bash

# 方式二：手动更新
cd ~/openclaw
git pull origin main
pnpm install
pnpm build
```

### Docker 更新

```bash
# 拉取最新镜像
docker pull openclaw/openclaw:latest

# 停止并删除旧容器
docker stop openclaw
docker rm openclaw

# 启动新容器
docker run -d \
  --name openclaw \
  -p 18789:18789 \
  -v ~/.openclaw:/root/.openclaw \
  --restart unless-stopped \
  openclaw/openclaw:latest
```

### Fly.io 更新

```bash
# 更新应用
flyctl deploy

# 或指定新镜像
flyctl deploy --image openclaw/openclaw:latest
```

### Railway 更新

**自动更新**：
- Railway 会自动检测 GitHub 仓库更新
- 自动触发重新部署

**手动更新**：
```bash
# 在 Railway 控制台
1. 进入项目
2. 点击 "Deployments"
3. 点击 "Redeploy"
```

### 备份数据

**本地安装备份**：
```bash
# 备份配置和数据
tar -czf openclaw-backup-$(date +%Y%m%d).tar.gz ~/.openclaw

# 恢复数据
tar -xzf openclaw-backup-20260210.tar.gz -C ~/
```

**Docker 备份**：
```bash
# 备份数据卷
docker run --rm \
  -v ~/.openclaw:/data \
  -v $(pwd):/backup \
  alpine tar czf /backup/openclaw-backup-$(date +%Y%m%d).tar.gz /data

# 恢复数据
docker run --rm \
  -v ~/.openclaw:/data \
  -v $(pwd):/backup \
  alpine tar xzf /backup/openclaw-backup-20260210.tar.gz -C /
```

**云端备份**：
```bash
# Fly.io 备份存储卷
flyctl volumes snapshots create openclaw_data

# Railway 备份数据库
# 在控制台导出数据库
```

### 回滚版本

**本地安装回滚**：
```bash
# 查看历史版本
git tag

# 回滚到指定版本
git checkout v2026.2.8
pnpm install
pnpm build
```

**Docker 回滚**：
```bash
# 使用指定版本镜像
docker run -d \
  --name openclaw \
  -p 18789:18789 \
  -v ~/.openclaw:/root/.openclaw \
  openclaw/openclaw:v2026.2.8
```

### 监控和日志

**查看日志**：
```bash
# 本地安装
tail -f ~/.openclaw/logs/gateway.log

# Docker
docker logs -f openclaw

# Fly.io
flyctl logs

# Railway
# 在控制台查看
```

**监控指标**：
```bash
# 查看系统状态
openclaw gateway status

# 查看资源使用
openclaw stats

# 查看 API 消耗
openclaw stats api
```

### 故障排查

**常见问题**：

1. **Gateway 无法启动**
   ```bash
   # 查看日志
   openclaw logs
   
   # 检查端口占用
   lsof -i :18789
   
   # 重启 Gateway
   openclaw gateway restart
   ```

2. **API 连接失败**
   ```bash
   # 测试 API 连接
   openclaw test api
   
   # 检查 API Key
   openclaw config get models.providers
   ```

3. **性能问题**
   ```bash
   # 清理缓存
   openclaw cache clear
   
   # 重启服务
   openclaw gateway restart
   ```

### 卸载

**本地安装卸载**：
```bash
# 停止服务
openclaw gateway stop

# 删除文件
rm -rf ~/.openclaw
rm -rf ~/openclaw

# 删除命令
npm uninstall -g openclaw
```

**Docker 卸载**：
```bash
# 停止并删除容器
docker stop openclaw
docker rm openclaw

# 删除镜像
docker rmi openclaw/openclaw

# 删除数据
rm -rf ~/.openclaw
```

**云端卸载**：
```bash
# Fly.io
flyctl apps destroy openclaw-app

# Railway
# 在控制台删除项目
```

---

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

#### 第二步：使用官方一键安装脚本

OpenClaw官方提供了一行代码的一键安装脚本，它会自动帮你把环境依赖都搞定：

```bash
# 一键安装
curl -fsSL https://openclaw.ai/install.sh | bash
```

安装过程说明：
- 自动检测系统环境
- 安装依赖包
- 构建TypeScript代码
- 构建Web UI
- 安装命令行工具

#### 第三步：验证安装

安装完后，输入下面这行命令，看看OpenClaw是否已经成功安装：

```bash
# 检查版本
openclaw --version
```

如果显示版本号，说明安装成功！

#### 第四步：初始化配置

```bash
# 运行配置向导
openclaw onboard
```

配置向导流程：

**1. 风险提示**：

OpenClaw 能力很强，但也有风险。选择 `yes` 继续安装：

![风险提示](https://upload.maynor1024.live/file/1770742236672_06-risk-warning.png)

**2. 选择启动模式**：

推荐选择 `QuickStart` 快速启动：

![选择QuickStart](https://upload.maynor1024.live/file/1770742238798_07-select-quickstart.png)

**3. 选择AI模型**：

选择你的AI供应商（支持国内外主流模型）：

![选择AI供应商](https://upload.maynor1024.live/file/1770742221938_03-select-ai-provider.png)

国内推荐：Qwen（通义千问）、MiniMax、智谱GLM

**4. 选择聊天工具**：

如果没有海外账号，选择最后一个 `None`：

![选择聊天工具](https://upload.maynor1024.live/file/1770742247561_08-select-chat-tool.png)

**5. Gateway端口设置**：

默认 `18789` 即可：

![端口设置](https://upload.maynor1024.live/file/1770742247410_09-port-setting.png)

**6. 选择Skills**：

使用空格键选择你需要的技能，也可以直接跳过：

![选择Skills](https://upload.maynor1024.live/file/1770742255849_10-select-skills.png)

**7. API Key配置**：

没有的可以选择 `no` 跳过：

![API Key配置](https://upload.maynor1024.live/file/1770742264976_11-api-key-config.png)

**8. 启用Hooks**：

推荐启用这三个钩子（用于内容引导、日志和会话记录）：

![启用Hooks](https://upload.maynor1024.live/file/1770742261487_12-enable-hooks.png)

**9. 完成配置**：

配置完成后，会自动启动Gateway服务并打开Web UI（`http://127.0.0.1:18789/chat`）

#### 第五步：验证安装

```bash
# 检查Gateway状态
openclaw channels status

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
irm https://openclaw.ai/install.ps1 | iex
```

#### 第三步：验证安装

```cmd
# 检查版本
openclaw --version
```

#### 第四步：初始化配置

```cmd
openclaw onboard
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
curl -fsSL https://openclaw.ai/install.sh | bash
```

#### 第三步：验证安装

```bash
# 检查版本
openclaw --version
```

#### 第四步：初始化配置

```bash
openclaw onboard
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
   nano ~/.openclaw/openclaw.json
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
   openclaw gateway restart
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
sudo chown -R $USER ~/.openclaw

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
tail -f ~/.openclaw/logs/gateway.log

# 重启Gateway
openclaw gateway restart
```

**Q2: 端口被占用**
```bash
# 查看端口占用
lsof -i :18789

# 修改端口
openclaw config set gateway.port 18790
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

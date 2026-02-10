# 附录A 命令速查表

> 💡 **本附录目标**：提供OpenClaw常用命令的快速参考，方便日常使用时查阅。

## 📋 目录

- A.1 基础命令
- A.2 文件操作命令
- A.3 系统操作命令
- A.4 Skills管理命令
- A.5 高级命令

---

## A.1 基础命令

### A.1.1 启动与停止

```bash
# 启动OpenClaw
openclaw start

# 停止OpenClaw
openclaw stop

# 重启OpenClaw
openclaw restart

# 查看运行状态
openclaw status

# 启动TUI界面
openclaw tui

# 启动Gateway
openclaw gateway start

# 停止Gateway
openclaw gateway stop

# 重启Gateway
openclaw gateway restart
```

### A.1.2 版本与帮助

```bash
# 查看版本
openclaw --version
openclaw -v

# 查看帮助
openclaw --help
openclaw -h

# 查看子命令帮助
openclaw config --help
openclaw models --help
openclaw skills --help
```

### A.1.3 配置管理

```bash
# 查看所有配置
openclaw config list

# 查看特定配置
openclaw config get model.apiKey
openclaw config get model.name

# 设置配置
openclaw config set model.apiKey "sk-xxx"
openclaw config set model.name "claude-sonnet-4"

# 删除配置
openclaw config delete model.apiKey

# 重置配置
openclaw config reset

# 导出配置
openclaw config export > config-backup.json

# 导入配置
openclaw config import config-backup.json
```

### A.1.4 对话管理

```bash
# 发送消息
openclaw chat "你好"
openclaw message send "你好"

# 查看对话历史
openclaw conversation list

# 清空对话历史
openclaw conversation clear

# 清理旧对话（保留最近N条）
openclaw conversation clean --keep 20

# 导出对话历史
openclaw conversation export > conversation.json

# 导入对话历史
openclaw conversation import conversation.json
```

---

## A.2 文件操作命令

### A.2.1 文件搜索

```bash
# 搜索文件（按名称）
"帮我找一下名为'报告.pdf'的文件"

# 搜索文件（按内容）
"帮我找一下包含'OpenClaw'的文件"

# 搜索文件（按类型）
"帮我找一下所有的PDF文件"

# 搜索文件（按时间）
"帮我找一下最近7天修改的文件"

# 搜索文件（按大小）
"帮我找一下大于100MB的文件"

# 组合搜索
"帮我找一下最近7天修改的、包含'OpenClaw'的PDF文件"
```

### A.2.2 文件处理

```bash
# 读取文件
"帮我读一下这个文件：~/Documents/report.pdf"

# 总结文件
"帮我总结一下这个文件：~/Documents/report.pdf"

# 提取信息
"帮我从这个文件中提取所有的日期和金额：~/Documents/invoice.pdf"

# 转换格式
"帮我把这个Word文档转成PDF：~/Documents/report.docx"

# 合并文件
"帮我把这个文件夹里的所有PDF合并成一个：~/Documents/reports/"

# 压缩文件
"帮我把这个文件夹压缩成zip：~/Documents/project/"
```

### A.2.3 文件整理

```bash
# 批量重命名
"帮我把这个文件夹里的所有文件，按照'日期-文件名'的格式重命名"

# 按类型分类
"帮我把桌面上的文件按类型分类到不同的文件夹"

# 按日期分类
"帮我把这个文件夹里的文件按月份分类"

# 删除重复文件
"帮我找出并删除这个文件夹里的重复文件"

# 清理临时文件
"帮我清理系统临时文件"

# 整理下载文件夹
"帮我整理下载文件夹，按类型分类"
```

---

## A.3 系统操作命令

### A.3.1 应用程序控制

```bash
# 打开应用
"帮我打开Chrome"
"帮我打开微信"

# 关闭应用
"帮我关闭Chrome"

# 切换应用
"帮我切换到Chrome"

# 查看运行的应用
"帮我看一下现在运行了哪些应用"

# 强制退出应用
"帮我强制退出Chrome"
```

### A.3.2 系统信息

```bash
# 查看系统信息
"帮我看一下系统信息"

# 查看CPU使用率
"帮我看一下CPU使用率"

# 查看内存使用
"帮我看一下内存使用情况"

# 查看硬盘空间
"帮我看一下硬盘空间"

# 查看网络状态
"帮我看一下网络连接状态"

# 查看电池状态（笔记本）
"帮我看一下电池状态"
```

### A.3.3 截图与录屏

```bash
# 截取全屏
"帮我截个全屏"

# 截取窗口
"帮我截取Chrome窗口"

# 截取区域
"帮我截取屏幕左上角的区域"

# 延迟截图
"帮我5秒后截个图"

# 录制屏幕
"帮我录制屏幕"

# 停止录制
"帮我停止录制"
```

---

## A.4 Skills管理命令

### A.4.1 Skills安装

```bash
# 列出可用Skills
openclaw skills list

# 搜索Skills
openclaw skills search "文件管理"

# 安装Skills
openclaw skills install peekaboo
openclaw skills install @openclaw/feishu

# 安装指定版本
openclaw skills install peekaboo@1.0.0

# 从URL安装
openclaw skills install https://github.com/user/skill.git

# 从本地安装
openclaw skills install ./my-skill/
```

### A.4.2 Skills管理

```bash
# 查看已安装Skills
openclaw skills list --installed

# 查看Skills详情
openclaw skills info peekaboo

# 更新Skills
openclaw skills update peekaboo

# 更新所有Skills
openclaw skills update --all

# 卸载Skills
openclaw skills uninstall peekaboo

# 启用Skills
openclaw skills enable peekaboo

# 禁用Skills
openclaw skills disable peekaboo
```

### A.4.3 Skills配置

```bash
# 查看Skills配置
openclaw skills config peekaboo

# 设置Skills配置
openclaw skills config peekaboo --set key=value

# 重置Skills配置
openclaw skills config peekaboo --reset

# 导出Skills配置
openclaw skills config peekaboo --export > peekaboo-config.json

# 导入Skills配置
openclaw skills config peekaboo --import peekaboo-config.json
```

---

## A.5 高级命令

### A.5.1 模型管理

```bash
# 列出可用模型
openclaw models list

# 列出已配置模型
openclaw models list --configured

# 添加模型
openclaw models add \
  --provider anthropic \
  --name claude-sonnet-4 \
  --apiKey sk-xxx

# 删除模型
openclaw models remove claude-sonnet-4

# 设置默认模型
openclaw models set-default claude-sonnet-4

# 测试模型连接
openclaw models test claude-sonnet-4

# 查看模型使用统计
openclaw models stats
```

### A.5.2 日志管理

```bash
# 查看日志
openclaw logs

# 查看最近N行日志
openclaw logs --tail 100

# 实时查看日志
openclaw logs --follow

# 查看错误日志
openclaw logs --level error

# 清空日志
openclaw logs clear

# 导出日志
openclaw logs export > logs.txt
```

### A.5.3 性能优化

```bash
# 清理缓存
openclaw cache clear

# 查看缓存大小
openclaw cache size

# 优化数据库
openclaw db optimize

# 重建索引
openclaw db reindex

# 检查健康状态
openclaw health check

# 性能诊断
openclaw diagnose
```

### A.5.4 备份与恢复

```bash
# 备份配置
openclaw backup create

# 列出备份
openclaw backup list

# 恢复备份
openclaw backup restore backup-20260210.tar.gz

# 删除备份
openclaw backup delete backup-20260210.tar.gz

# 自动备份设置
openclaw backup auto --enable
openclaw backup auto --disable
```

---

## 📝 常用命令组合

### 场景1：初次安装后的配置

```bash
# 1. 配置API Key
openclaw config set model.apiKey "sk-xxx"

# 2. 设置默认模型
openclaw config set model.name "claude-sonnet-4"

# 3. 启用自动清理
openclaw config set conversation.autoClean true

# 4. 重启Gateway
openclaw gateway restart

# 5. 测试连接
openclaw chat "你好"
```

### 场景2：切换模型

```bash
# 1. 查看可用模型
openclaw models list

# 2. 切换模型
openclaw config set model.name "deepseek-chat"

# 3. 重启Gateway
openclaw gateway restart

# 4. 测试新模型
openclaw chat "测试"
```

### 场景3：安装新Skills

```bash
# 1. 搜索Skills
openclaw skills search "截图"

# 2. 安装Skills
openclaw skills install peekaboo

# 3. 查看Skills配置
openclaw skills config peekaboo

# 4. 重启Gateway
openclaw gateway restart

# 5. 测试Skills
"帮我截个图"
```

### 场景4：性能优化

```bash
# 1. 清理对话历史
openclaw conversation clean --keep 20

# 2. 清理缓存
openclaw cache clear

# 3. 优化数据库
openclaw db optimize

# 4. 重启Gateway
openclaw gateway restart

# 5. 检查性能
openclaw health check
```

### 场景5：故障排查

```bash
# 1. 查看运行状态
openclaw status

# 2. 查看日志
openclaw logs --tail 100

# 3. 检查配置
openclaw config list

# 4. 测试模型连接
openclaw models test

# 5. 性能诊断
openclaw diagnose
```

---

## 🔧 配置文件路径

```bash
# 主配置文件
~/.openclaw/openclaw.json

# Skills目录
~/.openclaw/extensions/

# 日志目录
~/.openclaw/logs/

# 缓存目录
~/.openclaw/cache/

# 备份目录
~/.openclaw/backups/

# 对话历史
~/.openclaw/conversations/
```

---

## 💡 使用技巧

### 技巧1：使用别名

```bash
# 在 ~/.zshrc 或 ~/.bashrc 中添加
alias oc="openclaw"
alias ocg="openclaw gateway"
alias occ="openclaw config"
alias ocs="openclaw skills"

# 使用别名
oc chat "你好"
ocg restart
occ get model.name
ocs list
```

### 技巧2：使用管道

```bash
# 从文件读取内容发送
cat report.txt | openclaw chat

# 保存输出到文件
openclaw chat "总结一下OpenClaw的优势" > summary.txt

# 组合使用
cat input.txt | openclaw chat | tee output.txt
```

### 技巧3：使用环境变量

```bash
# 设置环境变量
export OPENCLAW_API_KEY="sk-xxx"
export OPENCLAW_MODEL="claude-sonnet-4"

# OpenClaw会自动读取这些环境变量
openclaw start
```

### 技巧4：批量操作

```bash
# 批量安装Skills
for skill in peekaboo feishu telegram; do
  openclaw skills install $skill
done

# 批量更新Skills
openclaw skills list --installed | xargs -I {} openclaw skills update {}

# 批量测试模型
openclaw models list | xargs -I {} openclaw models test {}
```

---

## 📚 相关资源

- OpenClaw官方文档：https://docs.openclaw.ai/
- 命令行参考：https://docs.openclaw.ai/cli
- Skills市场：https://hub.openclaw.ai/
- 社区论坛：https://community.openclaw.ai/

---

**提示**：本速查表会随OpenClaw版本更新而更新，建议收藏本页面以便随时查阅。


# CSDN 自动发文工具

基于 Selenium 的 CSDN 自动发文工具，支持单篇和批量发布。

## 📋 功能特性

- ✅ **自动登录**: 扫码登录，安全可靠
- ✅ **自动填写**: 标题、正文、分类、标签
- ✅ **Markdown 支持**: 自动切换到 Markdown 编辑模式
- ✅ **批量发布**: 一键发布所有 15 篇文章
- ✅ **人工确认**: 填写完成后人工检查再发布

## 🔧 环境要求

1. Python 3.7+
2. Chrome 浏览器
3. ChromeDriver（与 Chrome 版本匹配）

## 📦 安装步骤

### 1. 安装 Python 依赖

```bash
cd scripts
pip install -r requirements.txt
```

### 2. 安装 ChromeDriver

**方法 A: 自动安装（推荐）**

```bash
pip install webdriver-manager
```

脚本会自动下载匹配的 ChromeDriver。

**方法 B: 手动安装**

1. 检查 Chrome 版本: `chrome://version/`
2. 下载对应版本: https://chromedriver.chromium.org/
3. 将 ChromeDriver 放到 PATH 中

## 🚀 使用方法

### 方式 1: 单篇发布

```bash
cd scripts
python csdn_auto_publisher.py ../csdn_articles/01-introduction_csdn.md
```

### 方式 2: 批量发布（推荐）

```bash
cd scripts
python batch_publish_csdn.py
```

## 📝 使用流程

### 1. 启动脚本

```bash
python batch_publish_csdn.py
```

### 2. 扫码登录

1. 脚本会自动打开 Chrome 浏览器
2. 显示 CSDN 登录二维码
3. 使用 CSDN App 扫码登录
4. 登录成功后脚本自动继续

### 3. 自动填写文章

脚本会自动：
- 打开文章编辑页面
- 切换到 Markdown 模式
- 填写标题和正文
- 选择分类
- 添加标签

### 4. 人工确认发布

1. 检查文章内容是否正确
2. 手动点击"发布"按钮
3. 按回车继续下一篇

## ⚙️ 配置选项

### 修改分类和标签

编辑 `batch_publish_csdn.py`:

```python
publisher.publish_article(
    title=title,
    content=content,
    category="OpenClaw从入门到精通",  # 修改分类
    tags=["OpenClaw", "AI助手", "人工智能", "Agent"]  # 修改标签
)
```

### 无头模式（后台运行）

编辑 `csdn_auto_publisher.py`:

```python
publisher = CSDNAutoPublisher(headless=True)  # 改为 True
```

⚠️ **注意**: 无头模式下无法扫码登录，建议先在有头模式下登录，保存 cookies 后再使用无头模式。

## 📂 文章列表

脚本会自动读取 `csdn_articles/` 目录下的所有文章：

1. 01-introduction_csdn.md - OpenClaw 是什么？
2. 02-installation_csdn.md - 安装教程
3. 03-quick-start_csdn.md - 快速上手
4. 04-file-management_csdn.md - 本地文件管理
5. 05-knowledge-management_csdn.md - 个人知识库
6. 06-schedule-management_csdn.md - 日程管理
7. 07-automation-workflow_csdn.md - 自动化工作流
8. 08-skills-extension_csdn.md - Skills 扩展
9. 09-multi-platform-integration_csdn.md - 多平台集成
10. 10-api-integration_csdn.md - API 服务集成
11. 11-advanced-configuration_csdn.md - 高级配置
12. 12-personal-productivity_csdn.md - 效率提升实战
13. 13-advanced-automation_csdn.md - 高级自动化工作流
14. 14-creative-applications_csdn.md - 创意应用探索
15. 15-solo-entrepreneur-cases_csdn.md - 超级个体实战

## ❓ 常见问题

### Q1: ChromeDriver 版本不匹配

**错误**: `This version of ChromeDriver only supports Chrome version XX`

**解决**:
```bash
pip install --upgrade webdriver-manager
```

或手动下载匹配版本的 ChromeDriver。

### Q2: 登录超时

**错误**: `✗ 登录超时，请重试`

**解决**:
- 确保网络连接正常
- 快速扫码（二维码有效期 2 分钟）
- 修改等待时间（代码中的 `WebDriverWait` 参数）

### Q3: 找不到元素

**错误**: `NoSuchElementException`

**解决**:
- 等待页面加载完成
- 检查 CSDN 页面结构是否更新
- 使用浏览器开发者工具检查元素选择器

### Q4: 内容未同步

**现象**: 填写后内容显示为空

**解决**:
- 增加等待时间（修改 `time.sleep(3)`）
- 检查是否成功切换到 Markdown 模式
- 手动复制粘贴内容作为备选方案

## 🎯 发布建议

### 发布时间

- **工作日**: 9:00-10:00 或 20:00-21:00
- **周末**: 10:00-11:00
- **避免**: 深夜 23:00-7:00

### 发布频率

- 每天发布 2-3 篇
- 避免一次性发布全部（可能被限流）
- 建议分 5-7 天发布完

### 互动运营

- 发布后及时回复评论
- 在文末添加"点赞、收藏、关注"引导
- 分享到朋友圈、微信群

## 🔐 安全说明

- Cookie 和登录信息仅保存在本地浏览器
- 不会上传任何账号密码
- 建议使用专用账号进行自动化操作

## 📊 进阶功能

### 保存 Cookies 避免重复登录

修改脚本保存 cookies 到文件：

```python
import json

# 保存 cookies
with open("cookies.json", "w") as f:
    json.dump(driver.get_cookies(), f)

# 加载 cookies
with open("cookies.json", "r") as f:
    cookies = json.load(f)
    for cookie in cookies:
        driver.add_cookie(cookie)
```

### 定时发布

使用 cron 或任务计划程序定时运行脚本：

```bash
# 每天上午 9 点运行
0 9 * * * cd /path/to/scripts && python batch_publish_csdn.py
```

## 📞 技术支持

遇到问题请在 GitHub 提交 Issue：
https://github.com/xianyu110/awesome-openclaw-tutorial/issues

## 🔍 搜索索引

使用统一入口生成两个搜索索引文件：

```bash
bash scripts/generate-search-index.sh
```

运行回归测试：

```bash
bash scripts/test-generate-search-index.sh
```

## 📄 许可证

GPL-3.0 License

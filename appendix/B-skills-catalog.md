# 附录B 常用Skills清单

> 💡 **本附录目标**：提供OpenClaw常用Skills的详细清单，包括官方Skills和社区热门Skills，帮助你快速找到需要的功能。

## 📋 目录

- B.1 官方Skills
- B.2 社区热门Skills
- B.3 Skills评价和推荐

---

## B.1 官方Skills

### B.1.1 系统集成类

#### 📸 peekaboo（截图工具）

**功能**：
- 截取全屏
- 截取窗口
- 截取区域
- 延迟截图

**安装**：
```bash
openclaw skills install peekaboo
```

**使用示例**：
```
"帮我截个全屏"
"帮我截取Chrome窗口"
"帮我5秒后截个图"
```

**推荐指数**：⭐⭐⭐⭐⭐

**适用场景**：
- 需要验证OpenClaw的操作
- 需要记录屏幕内容
- 需要调试问题

---

#### 📝 notes（备忘录集成）

**功能**：
- 创建备忘录
- 搜索备忘录
- 更新备忘录
- 删除备忘录

**安装**：
```bash
openclaw skills install notes
```

**使用示例**：
```
"帮我创建一个备忘录：明天开会"
"帮我搜索包含'OpenClaw'的备忘录"
"帮我更新这个备忘录"
```

**推荐指数**：⭐⭐⭐⭐⭐

**适用场景**：
- 需要快速记录信息
- 需要跨设备同步
- 需要搜索历史记录

---

#### 📅 calendar（日历集成）

**功能**：
- 创建日历事件
- 查询日程安排
- 更新事件
- 删除事件

**安装**：
```bash
openclaw skills install calendar
```

**使用示例**：
```
"帮我创建一个日历事件：明天下午3点开会"
"帮我看一下今天的日程"
"帮我取消明天的会议"
```

**推荐指数**：⭐⭐⭐⭐⭐

**适用场景**：
- 需要管理日程
- 需要设置提醒
- 需要跨设备同步

---

#### 📧 mail（邮件集成）

**功能**：
- 发送邮件
- 读取邮件
- 搜索邮件
- 管理邮件

**安装**：
```bash
openclaw skills install mail
```

**使用示例**：
```
"帮我发一封邮件给张三"
"帮我看一下最新的邮件"
"帮我搜索包含'OpenClaw'的邮件"
```

**推荐指数**：⭐⭐⭐⭐

**适用场景**：
- 需要快速发送邮件
- 需要搜索邮件
- 需要自动化邮件处理

---

### B.1.2 文件处理类

#### 📁 file-manager（文件管理）

**功能**：
- 搜索文件
- 读取文件
- 移动文件
- 删除文件
- 重命名文件

**安装**：
```bash
openclaw skills install file-manager
```

**使用示例**：
```
"帮我找一下包含'报告'的文件"
"帮我把这个文件移动到桌面"
"帮我删除这个文件"
```

**推荐指数**：⭐⭐⭐⭐⭐

**适用场景**：
- 需要搜索文件
- 需要整理文件
- 需要批量处理文件

---

#### 📄 pdf-tools（PDF工具）

**功能**：
- 读取PDF
- 提取文本
- 合并PDF
- 分割PDF
- 压缩PDF

**安装**：
```bash
openclaw skills install pdf-tools
```

**使用示例**：
```
"帮我读一下这个PDF"
"帮我把这两个PDF合并"
"帮我把这个PDF的第1-10页提取出来"
```

**推荐指数**：⭐⭐⭐⭐⭐

**适用场景**：
- 需要处理PDF文件
- 需要提取PDF内容
- 需要合并或分割PDF

---

#### 🖼️ image-tools（图片工具）

**功能**：
- 压缩图片
- 转换格式
- 调整大小
- 批量处理

**安装**：
```bash
openclaw skills install image-tools
```

**使用示例**：
```
"帮我压缩这张图片"
"帮我把这张图片转成PNG格式"
"帮我把这张图片调整到800x600"
```

**推荐指数**：⭐⭐⭐⭐

**适用场景**：
- 需要处理图片
- 需要批量转换格式
- 需要压缩图片

---

### B.1.3 网络服务类

#### 🌐 web-search（网页搜索）

**功能**：
- 搜索网页
- 提取内容
- 总结网页
- 保存网页

**安装**：
```bash
openclaw skills install web-search
```

**使用示例**：
```
"帮我搜索一下OpenClaw的最新消息"
"帮我总结一下这个网页"
"帮我保存这个网页到备忘录"
```

**推荐指数**：⭐⭐⭐⭐⭐

**适用场景**：
- 需要搜索信息
- 需要总结网页
- 需要保存网页内容

---

#### 📰 rss-reader（RSS阅读器）

**功能**：
- 订阅RSS
- 读取文章
- 搜索文章
- 推送更新

**安装**：
```bash
openclaw skills install rss-reader
```

**使用示例**：
```
"帮我订阅这个RSS源"
"帮我看一下最新的文章"
"帮我搜索包含'AI'的文章"
```

**推荐指数**：⭐⭐⭐⭐

**适用场景**：
- 需要订阅博客
- 需要获取最新资讯
- 需要自动推送更新

---

### B.1.4 开发工具类

#### 💻 code-assistant（代码助手）

**功能**：
- 代码生成
- 代码审查
- 代码解释
- 代码优化

**安装**：
```bash
openclaw skills install code-assistant
```

**使用示例**：
```
"帮我写一个Python函数，计算斐波那契数列"
"帮我审查一下这段代码"
"帮我解释一下这段代码的作用"
```

**推荐指数**：⭐⭐⭐⭐⭐

**适用场景**：
- 需要生成代码
- 需要审查代码
- 需要学习代码

---

#### 🐛 debug-helper（调试助手）

**功能**：
- 分析错误
- 提供解决方案
- 搜索文档
- 生成测试用例

**安装**：
```bash
openclaw skills install debug-helper
```

**使用示例**：
```
"帮我分析一下这个错误"
"帮我搜索一下这个错误的解决方案"
"帮我生成测试用例"
```

**推荐指数**：⭐⭐⭐⭐

**适用场景**：
- 需要调试代码
- 需要解决错误
- 需要生成测试

---

## B.2 社区热门Skills

### B.2.1 通讯工具类

#### 💬 feishu（飞书集成）

**功能**：
- 发送消息
- 创建文档
- 管理日历
- 发送通知

**安装**：
```bash
openclaw skills install @openclaw/feishu
```

**使用示例**：
```
"帮我在飞书上发个消息给张三"
"帮我创建一个飞书文档"
"帮我在飞书上创建一个日历事件"
```

**推荐指数**：⭐⭐⭐⭐⭐

**适用场景**：
- 使用飞书办公
- 需要团队协作
- 需要自动化通知

---

#### 💼 dingtalk（钉钉集成）

**功能**：
- 发送消息
- 创建待办
- 管理审批
- 发送通知

**安装**：
```bash
openclaw skills install @openclaw/dingtalk
```

**使用示例**：
```
"帮我在钉钉上发个消息"
"帮我创建一个钉钉待办"
"帮我查看钉钉审批"
```

**推荐指数**：⭐⭐⭐⭐⭐

**适用场景**：
- 使用钉钉办公
- 需要管理待办
- 需要处理审批

---

#### 🏢 wecom（企业微信集成）

**功能**：
- 发送消息
- 创建群聊
- 管理通讯录
- 发送通知

**安装**：
```bash
openclaw skills install @openclaw/wecom
```

**使用示例**：
```
"帮我在企业微信上发个消息"
"帮我创建一个企业微信群"
"帮我查看企业微信通讯录"
```

**推荐指数**：⭐⭐⭐⭐⭐

**适用场景**：
- 使用企业微信办公
- 需要团队沟通
- 需要自动化通知

---

### B.2.2 AI服务类

#### 🎨 banana（AI绘画）

**功能**：
- 生成图片
- 修改图片
- 图片风格转换
- 图片增强

**安装**：
```bash
openclaw skills install @openclaw/banana
```

**使用示例**：
```
"帮我画一个可爱的小龙虾"
"帮我把这张图片转成卡通风格"
"帮我增强这张图片的清晰度"
```

**推荐指数**：⭐⭐⭐⭐⭐

**适用场景**：
- 需要生成图片
- 需要修改图片
- 需要创意设计

---

#### 🎬 video-gen（视频生成）

**功能**：
- 生成视频
- 视频剪辑
- 添加字幕
- 添加音乐

**安装**：
```bash
openclaw skills install @openclaw/video-gen
```

**使用示例**：
```
"帮我生成一段视频：小龙虾在海底跳舞"
"帮我给这个视频添加字幕"
"帮我给这个视频添加背景音乐"
```

**推荐指数**：⭐⭐⭐⭐

**适用场景**：
- 需要生成视频
- 需要剪辑视频
- 需要制作短视频

---

#### 🔊 tts（语音合成）

**功能**：
- 文字转语音
- 多语言支持
- 多种音色
- 调整语速

**安装**：
```bash
openclaw skills install @openclaw/tts
```

**使用示例**：
```
"帮我把这段文字转成语音"
"帮我用女声读这段文字"
"帮我把语速调快一点"
```

**推荐指数**：⭐⭐⭐⭐

**适用场景**：
- 需要语音播报
- 需要制作音频
- 需要多语言支持

---

### B.2.3 数据处理类

#### 📊 data-analysis（数据分析）

**功能**：
- 数据清洗
- 数据分析
- 生成图表
- 导出报告

**安装**：
```bash
openclaw skills install @openclaw/data-analysis
```

**使用示例**：
```
"帮我分析一下这个Excel文件"
"帮我生成一个销售趋势图"
"帮我导出分析报告"
```

**推荐指数**：⭐⭐⭐⭐

**适用场景**：
- 需要分析数据
- 需要生成图表
- 需要制作报告

---

#### 📈 excel-tools（Excel工具）

**功能**：
- 读取Excel
- 写入Excel
- 数据透视
- 公式计算

**安装**：
```bash
openclaw skills install @openclaw/excel-tools
```

**使用示例**：
```
"帮我读一下这个Excel文件"
"帮我把这些数据写入Excel"
"帮我创建一个数据透视表"
```

**推荐指数**：⭐⭐⭐⭐

**适用场景**：
- 需要处理Excel
- 需要数据分析
- 需要自动化报表

---

## B.3 Skills评价和推荐

### B.3.1 必装Skills（Top 10）

1. **peekaboo**（截图工具）⭐⭐⭐⭐⭐
   - 验证操作必备
   - 调试问题必备
   - 使用频率：极高

2. **notes**（备忘录集成）⭐⭐⭐⭐⭐
   - 知识管理必备
   - 跨设备同步
   - 使用频率：极高

3. **calendar**（日历集成）⭐⭐⭐⭐⭐
   - 日程管理必备
   - 提醒功能强大
   - 使用频率：高

4. **file-manager**（文件管理）⭐⭐⭐⭐⭐
   - 文件搜索必备
   - 批量处理强大
   - 使用频率：极高

5. **web-search**（网页搜索）⭐⭐⭐⭐⭐
   - 信息搜索必备
   - 网页总结强大
   - 使用频率：高

6. **code-assistant**（代码助手）⭐⭐⭐⭐⭐
   - 开发者必备
   - 代码生成强大
   - 使用频率：高（开发者）

7. **feishu**（飞书集成）⭐⭐⭐⭐⭐
   - 飞书用户必备
   - 团队协作强大
   - 使用频率：高（飞书用户）

8. **banana**（AI绘画）⭐⭐⭐⭐⭐
   - 创意工作必备
   - 图片生成强大
   - 使用频率：中

9. **pdf-tools**（PDF工具）⭐⭐⭐⭐⭐
   - PDF处理必备
   - 功能全面
   - 使用频率：高

10. **mail**（邮件集成）⭐⭐⭐⭐
    - 邮件管理必备
    - 自动化强大
    - 使用频率：中

### B.3.2 按场景推荐

**个人效率提升**：
- notes（备忘录）
- calendar（日历）
- file-manager（文件管理）
- web-search（网页搜索）
- mail（邮件）

**团队协作**：
- feishu（飞书）
- dingtalk（钉钉）
- wecom（企业微信）
- calendar（日历）
- mail（邮件）

**开发者**：
- code-assistant（代码助手）
- debug-helper（调试助手）
- file-manager（文件管理）
- web-search（网页搜索）
- peekaboo（截图）

**内容创作**：
- banana（AI绘画）
- video-gen（视频生成）
- tts（语音合成）
- image-tools（图片工具）
- web-search（网页搜索）

**数据分析**：
- data-analysis（数据分析）
- excel-tools（Excel工具）
- pdf-tools（PDF工具）
- file-manager（文件管理）
- web-search（网页搜索）

### B.3.3 Skills组合推荐

**组合1：知识管理套装**
```bash
openclaw skills install notes
openclaw skills install web-search
openclaw skills install pdf-tools
openclaw skills install file-manager
```

**组合2：团队协作套装**
```bash
openclaw skills install feishu
openclaw skills install calendar
openclaw skills install mail
openclaw skills install file-manager
```

**组合3：开发者套装**
```bash
openclaw skills install code-assistant
openclaw skills install debug-helper
openclaw skills install peekaboo
openclaw skills install file-manager
```

**组合4：创意工作套装**
```bash
openclaw skills install banana
openclaw skills install video-gen
openclaw skills install tts
openclaw skills install image-tools
```

---

## 📚 相关资源

- ClawHub市场：https://hub.openclaw.ai/
- Skills开发文档：https://docs.openclaw.ai/skills
- 社区论坛：https://community.openclaw.ai/
- GitHub仓库：https://github.com/openclaw/skills

---

**提示**：本清单会随着新Skills的发布而更新，建议定期查看以获取最新信息。


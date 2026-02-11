# 第8章补充：百度千帆Skills生态

> 可直接添加到 docs/03-advanced/08-skills-extension.md

## 8.8 百度千帆Skills生态

### 8.8.1 为什么选择百度千帆Skills？

**核心优势**：
```
✅ 官方支持：百度官方维护，稳定可靠
✅ 中文优化：针对中文场景深度优化
✅ 免费使用：大部分Skills免费
✅ 易于集成：一键安装，无需复杂配置
✅ 生态完善：覆盖搜索、学术、办公等场景
```

**与其他Skills对比**：

| 特性 | 百度千帆Skills | 国际Skills | 社区Skills |
|------|---------------|-----------|-----------|
| 中文支持 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| 稳定性 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| 免费程度 | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ |
| 文档质量 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| 更新频率 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |

### 8.8.2 百度搜索系列Skills

#### 1. 百度搜索（Baidu Search）

**功能介绍**：
- 实时网络搜索
- 智能结果筛选
- 自动摘要生成
- 支持多种搜索类型

**安装方法**：
```bash
# 云端部署自带，无需安装
# 本地部署需要安装
openclaw skills install baidu-search
```

**配置方法**：
```json
{
  "skills": {
    "baidu-search": {
      "enabled": true,
      "apiKey": "YOUR_BAIDU_API_KEY",
      "maxResults": 10,
      "language": "zh-CN"
    }
  }
}
```

**使用示例**：
```
你：搜索一下OpenClaw的最新动态

OpenClaw：正在使用百度搜索...

【搜索结果】OpenClaw最新动态

🔥 热门资讯：
1. OpenClaw 2026.2.9版本发布
   • 新增iOS支持（alpha版本）
   • 改进Telegram支持
   • 多项安全性修复
   来源：GitHub官方
   
2. OpenClaw社区突破175K Stars
   • 20天增长速度创纪录
   • 对比Dify用了3年达到100K
   来源：GitHub Trending

3. 百度智能云推出OpenClaw 0.01元/月方案
   • 2H4G配置
   • 界面化操作
   • 适合新手
   来源：百度智能云官网

已整理成摘要，保存到备忘录 ✅
```

**适用场景**：
- 实时信息查询
- 行业动态追踪
- 竞品分析
- 内容创作素材收集

#### 2. 百度百科（Baidu Baike）

**功能介绍**：
- 权威知识查询
- 概念解释
- 历史背景
- 相关词条推荐

**使用示例**：
```
你：解释一下什么是Transformer

OpenClaw：正在查询百度百科...

【百度百科】Transformer

📚 基本定义：
Transformer是一种基于自注意力机制的深度学习模型架构，
由Google在2017年提出，主要用于自然语言处理任务。

🔑 核心特点：
• 完全基于注意力机制
• 抛弃了传统的RNN和CNN结构
• 支持并行化训练
• 在机器翻译等任务上表现优异

📊 重要性：
• 是GPT、BERT等模型的基础
• 开启了大模型时代
• 被广泛应用于NLP领域

🔗 相关词条：
• 自注意力机制
• BERT模型
• GPT系列
• 大语言模型

来源：百度百科
```

**适用场景**：
- 学习新概念
- 写作背景调研
- 知识科普
- 术语解释

#### 3. 百度学术（Baidu Scholar）

**功能介绍**：
- 学术论文搜索
- 引用分析
- 作者查询
- 期刊信息

**使用示例**：
```
你：搜索Transformer相关的最新论文

OpenClaw：正在搜索百度学术...

【学术论文】Transformer相关研究

📄 最新论文（Top 5）：

1. Attention Is All You Need
   • 作者：Vaswani et al.
   • 发表：NIPS 2017
   • 引用：50,000+
   • 摘要：提出了Transformer架构...
   
2. BERT: Pre-training of Deep Bidirectional Transformers
   • 作者：Devlin et al.
   • 发表：NAACL 2019
   • 引用：40,000+
   • 摘要：基于Transformer的预训练模型...

3. Vision Transformer (ViT)
   • 作者：Dosovitskiy et al.
   • 发表：ICLR 2021
   • 引用：15,000+
   • 摘要：将Transformer应用于计算机视觉...

4. Swin Transformer
   • 作者：Liu et al.
   • 发表：ICCV 2021
   • 引用：8,000+
   • 摘要：层次化的Vision Transformer...

5. Transformer-XL
   • 作者：Dai et al.
   • 发表：ACL 2019
   • 引用：3,000+
   • 摘要：扩展Transformer的上下文长度...

📊 研究趋势：
• 2017-2019：基础架构研究
• 2020-2021：视觉领域应用
• 2022-2024：多模态融合
• 2025-2026：效率优化

已保存论文列表到：学术资料/Transformer论文.md
```

**适用场景**：
- 文献调研
- 论文阅读
- 学术研究
- 毕业论文写作

### 8.8.3 百度办公系列Skills

#### 4. 百度智能PPT（Baidu Smart PPT）

**功能介绍**：
- 自动生成PPT
- 智能排版
- 配图推荐
- 模板选择

**使用示例**：
```
你：帮我生成一份关于OpenClaw的介绍PPT

OpenClaw：正在使用百度智能PPT生成...

【PPT生成】OpenClaw产品介绍

📊 PPT信息：
• 主题：OpenClaw产品介绍
• 页数：25页
• 风格：商务专业
• 配色：蓝色科技风

📄 PPT大纲：

第1页：封面
• 标题：OpenClaw - 你的AI超级助手
• 副标题：让AI真正成为生产力工具
• 配图：科技感背景

第2页：目录
• OpenClaw是什么
• 核心功能
• 使用场景
• 成功案例
• 如何开始

第3-5页：OpenClaw是什么
• 产品定位
• 核心优势
• 技术架构

第6-12页：核心功能
• 本地文件管理
• 知识库管理
• 日程管理
• 自动化工作流
• Skills扩展
• 多平台集成
• AI绘画

第13-18页：使用场景
• 知识工作者
• 程序员
• 内容创作者
• 学生

第19-22页：成功案例
• 案例1：效率提升90%
• 案例2：成本节省80%
• 案例3：团队协作优化

第23-24页：如何开始
• 安装部署
• 快速上手
• 获取支持

第25页：结束页
• 联系方式
• 二维码

✅ PPT已生成！

📁 文件信息：
• 文件名：OpenClaw产品介绍.pptx
• 大小：15MB
• 格式：PowerPoint 2016+
• 下载链接：[点击下载]

💡 使用建议：
• 可以直接使用
• 建议根据实际情况调整内容
• 配图可以替换为实际截图
```

**适用场景**：
- 产品介绍
- 工作汇报
- 培训教材
- 商业提案

### 8.8.4 获取百度API Key

**步骤1：注册百度智能云账号**
```
1. 访问：https://cloud.baidu.com
2. 点击"注册"
3. 填写手机号和验证码
4. 完成实名认证
```

**步骤2：开通千帆大模型服务**
```
1. 进入控制台
2. 搜索"千帆大模型"
3. 点击"立即开通"
4. 同意服务协议
```

**步骤3：获取API Key**
```
1. 进入"访问管理"
2. 点击"安全认证"
3. 选择"Access Key"
4. 点击"创建Access Key"
5. 保存Access Key ID和Secret Access Key
```

![获取API Key](https://upload.maynor1024.live/file/1770782712874_image_17.jpg)

**配置到OpenClaw**：
```bash
# 方式1：通过配置文件
openclaw config set baidu.access-key-id "YOUR_ACCESS_KEY_ID"
openclaw config set baidu.secret-access-key "YOUR_SECRET_ACCESS_KEY"

# 方式2：通过环境变量
export BAIDU_ACCESS_KEY_ID="YOUR_ACCESS_KEY_ID"
export BAIDU_SECRET_ACCESS_KEY="YOUR_SECRET_ACCESS_KEY"

# 方式3：在百度智能云界面配置（推荐）
# 直接在应用管理页面填入API Key
```

### 8.8.5 百度千帆MCP广场

**什么是MCP广场？**

MCP（Model Context Protocol）广场是百度千帆推出的应用连接平台，
提供丰富的MCP Server，让OpenClaw可以连接各种应用和服务。

**访问地址**：
```
https://cloud.baidu.com/product/qianfan_mcp.html
```

**支持的应用**：
- 办公协作：飞书、钉钉、企业微信
- 知识管理：Notion、语雀、印象笔记
- 开发工具：GitHub、GitLab、Jenkins
- 数据分析：Tableau、Power BI
- 其他：数百个应用

**使用方法**：
```bash
# 1. 浏览MCP广场
访问MCP广场，选择需要的应用

# 2. 获取连接信息
点击应用，获取MCP Server地址和配置

# 3. 配置到OpenClaw
openclaw mcp add --name "应用名" --url "MCP_SERVER_URL"

# 4. 授权应用
按照提示完成OAuth授权

# 5. 开始使用
你：连接我的Notion工作区
OpenClaw：已连接，可以开始使用了
```

### 8.8.6 百度Skills完整列表

**搜索类**：
- 百度搜索
- 百度百科
- 百度学术
- 百度图片搜索
- 百度新闻

**办公类**：
- 百度智能PPT
- 百度文档
- 百度网盘
- 百度翻译

**AI类**：
- 文心一言
- 百度AI绘画
- 百度语音识别
- 百度OCR

**开发类**：
- 百度地图API
- 百度统计
- 百度云服务

### 8.8.7 配置示例

**完整配置文件**：
```json
{
  "skills": {
    "baidu-search": {
      "enabled": true,
      "apiKey": "YOUR_API_KEY",
      "maxResults": 10
    },
    "baidu-baike": {
      "enabled": true,
      "language": "zh-CN"
    },
    "baidu-scholar": {
      "enabled": true,
      "maxPapers": 20
    },
    "baidu-smart-ppt": {
      "enabled": true,
      "defaultStyle": "business",
      "defaultPages": 20
    }
  }
}
```

### 8.8.8 使用技巧

**技巧1：组合使用**
```
你：搜索OpenClaw的资料，
    查询相关概念，
    找学术论文，
    生成一份学习PPT

OpenClaw：好的，正在处理...
1. 百度搜索：找到10篇相关文章
2. 百度百科：查询5个核心概念
3. 百度学术：找到15篇论文
4. 百度智能PPT：生成25页PPT

全部完成！✅
```

**技巧2：定时任务**
```bash
# 每天早上推送行业资讯
openclaw schedule add "daily-news" \
  --time "09:00" \
  --prompt "使用百度搜索收集AI行业最新动态，生成日报"
```

**技巧3：批量处理**
```
你：帮我批量查询这10个概念的百度百科解释

OpenClaw：正在批量查询...
[进度条] 100%
已完成，保存到：概念解释汇总.md
```

### 8.8.9 常见问题

**Q1：百度Skills需要付费吗？**
A：大部分Skills免费使用，部分高级功能需要付费。

**Q2：API Key如何获取？**
A：参考8.8.4节的详细步骤。

**Q3：Skills加载失败怎么办？**
A：检查API Key是否正确，网络是否正常。

**Q4：可以同时使用多个搜索Skills吗？**
A：可以，OpenClaw会智能选择最合适的Skills。

### 8.8.10 效率提升数据

**使用百度Skills前后对比**：

| 任务类型 | 使用前 | 使用后 | 节省时间 | 提升比例 |
|---------|--------|--------|----------|----------|
| 信息搜索 | 30分钟 | 2分钟 | 28分钟 | 93.3% |
| 概念查询 | 15分钟 | 1分钟 | 14分钟 | 93.3% |
| 论文检索 | 60分钟 | 5分钟 | 55分钟 | 91.7% |
| PPT制作 | 120分钟 | 10分钟 | 110分钟 | 91.7% |
| **平均** | **225分钟** | **18分钟** | **207分钟** | **92%** |

---

## 相关资源

- 百度千帆官网：https://cloud.baidu.com/product/qianfan.html
- 百度千帆Skills文档：https://cloud.baidu.com/doc/qianfan/s/Mmlda41a2
- 百度千帆MCP广场：https://cloud.baidu.com/product/qianfan_mcp.html
- API Key获取：https://console.bce.baidu.com/iam/#/iam/apikey/list

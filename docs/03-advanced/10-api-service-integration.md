# 第10章 API服务封装

> 💡 **本章目标**：学会将第三方API服务封装到OpenClaw中，实现Banana绘图、Notion同步、视频生成、语音合成等功能。

## 🔌 本章内容

- 10.1 Banana绘图集成
- 10.2 Notion数据同步
- 10.3 视频生成服务
- 10.4 语音合成接入

---

## 10.1 Banana绘图集成

### 10.1.1 什么是Banana

**Banana介绍**：
- Nano Banana Pro是一款AI绘图工具
- 支持文生图、图生图、图片编辑
- 质量高、速度快、价格便宜
- 适合手机端使用

**为什么选择Banana**：
```
✅ 质量优秀：媲美Midjourney
✅ 速度快：10秒出图
✅ 价格低：比其他工具便宜50%
✅ 易集成：API简单易用
```

### 10.1.2 获取Banana API

**步骤1：注册Banana账号**
```
访问：https://banana.dev
注册账号并登录
```

**步骤2：获取API Key**
```
1. 进入控制台
2. 点击"API Keys"
3. 创建新的API Key
4. 复制保存
```

**步骤3：充值（可选）**
```
- 新用户有免费额度
- 可以先测试再充值
- 支持多种支付方式
```


### 10.1.3 配置OpenClaw

**方式1：使用现成的Skills**
```bash
# 安装Banana Skills
openclaw skill install banana-draw

# 配置API Key
openclaw config set banana.apiKey "your-api-key"

# 测试
你：用Banana画一只可爱的猫
OpenClaw：正在生成图片...
[图片]
```

**方式2：自己封装API**
```typescript
// src/banana-skill.ts
import { Skill } from '@openclaw/sdk';
import axios from 'axios';

export default class BananaSkill extends Skill {
  private apiKey = process.env.BANANA_API_KEY;
  private apiUrl = 'https://api.banana.dev/v1';

  async onMessage(message: string) {
    // 检测绘图请求
    const match = message.match(/画(.+)/);
    if (!match) return null;

    const prompt = match[1];
    
    try {
      // 调用Banana API
      const response = await axios.post(
        `${this.apiUrl}/generate`,
        {
          prompt: prompt,
          model: 'nano-banana-pro',
          size: '1024x1024'
        },
        {
          headers: {
            'Authorization': `Bearer ${this.apiKey}`
          }
        }
      );

      const imageUrl = response.data.image_url;
      return `图片已生成：${imageUrl}`;
      
    } catch (error) {
      return '生成失败，请稍后重试';
    }
  }
}
```

### 10.1.4 实战案例

**案例1：手机上画图**
```
场景：在飞书上用OpenClaw画图

步骤：
1. 打开飞书
2. 找到OpenClaw
3. 发送：画一个赛博朋克风格的城市
4. 等待10秒
5. 收到图片

优势：
- 无需打开电脑
- 随时随地画图
- 自动保存到相册
```

**案例2：批量生成图片**
```
场景：为文章生成配图

步骤：
你：帮我生成3张图片：
1. 科技感的办公室
2. 未来城市
3. AI机器人

OpenClaw：正在生成...
[图片1]
[图片2]
[图片3]

全部完成 ✅
```

**案例3：图片编辑**
```
场景：修改已有图片

步骤：
你：[发送图片]
把这张图改成卡通风格

OpenClaw：正在处理...
[修改后的图片]

完成 ✅
```


### 10.1.5 提示词优化技巧

**基本原则**：
```
1. 描述清晰具体
2. 包含风格关键词
3. 指定画面元素
4. 控制画面比例
```

**优秀提示词示例**：
```
❌ 差：画一只猫
✅ 好：一只可爱的橘猫，坐在窗台上，
      阳光洒在身上，温暖的色调，
      高清摄影，景深效果

❌ 差：画个城市
✅ 好：赛博朋克风格的未来城市，
      霓虹灯闪烁，高楼林立，
      夜景，雨后街道，
      电影级画质，广角镜头
```

**风格关键词**：
```
- 写实风格：photorealistic, 4K, detailed
- 卡通风格：cartoon, cute, colorful
- 赛博朋克：cyberpunk, neon, futuristic
- 水彩画：watercolor, soft, artistic
- 油画：oil painting, classical, textured
```

### 10.1.6 成本控制

**Banana定价**：
```
- 标准图片：$0.02/张
- 高清图片：$0.05/张
- 图片编辑：$0.03/张
```

**省钱技巧**：
```
1. 使用标准分辨率
2. 批量生成
3. 优化提示词（减少重试）
4. 使用免费额度
```

**成本对比**：
```
| 工具 | 价格 | 质量 | 速度 |
|------|------|------|------|
| Banana | $0.02 | ⭐⭐⭐⭐ | 10秒 |
| Midjourney | $0.08 | ⭐⭐⭐⭐⭐ | 30秒 |
| DALL-E | $0.04 | ⭐⭐⭐⭐ | 15秒 |
| Stable Diffusion | 免费 | ⭐⭐⭐ | 20秒 |
```

---

## 10.2 Notion数据同步

### 10.2.1 Notion介绍

**Notion的优势**：
```
✅ 功能强大：笔记、数据库、项目管理
✅ 跨平台：Web、Mac、Windows、iOS、Android
✅ 协作友好：团队共享、权限管理
✅ API完善：易于集成
```

### 10.2.2 获取Notion API

**步骤1：创建Integration**
```
1. 访问：https://www.notion.so/my-integrations
2. 点击"New integration"
3. 填写信息：
   - Name：OpenClaw
   - Associated workspace：选择工作区
   - Capabilities：勾选需要的权限
4. 提交并获取Token
```

**步骤2：分享数据库**
```
1. 打开要同步的Notion页面
2. 点击右上角"Share"
3. 搜索并添加你的Integration
4. 确认权限
```

**步骤3：获取Database ID**
```
从Notion页面URL中获取：
https://notion.so/workspace/[database-id]?v=...
```


### 10.2.3 配置OpenClaw

```bash
# 安装Notion Skills
openclaw skill install notion-sync

# 配置Token
openclaw config set notion.token "your-notion-token"

# 配置Database ID
openclaw config set notion.databaseId "your-database-id"

# 测试
你：把这段内容保存到Notion
OpenClaw：已保存到Notion ✅
```

### 10.2.4 实战案例

**案例1：笔记同步**
```
功能：自动同步笔记到Notion

使用：
你：保存这段笔记到Notion：
[笔记内容]

OpenClaw：已保存 ✅
标题：[自动生成]
标签：#笔记
链接：https://notion.so/...
```

**案例2：任务管理**
```
功能：同步任务到Notion数据库

使用：
你：添加任务：完成项目报告
截止日期：明天
优先级：高

OpenClaw：任务已添加 ✅
```

**案例3：知识库构建**
```
功能：自动整理知识到Notion

使用：
你：把这篇文章保存到知识库
[文章链接]

OpenClaw：正在处理...
- 提取内容 ✅
- 生成摘要 ✅
- 添加标签 ✅
- 保存到Notion ✅

完成！
```

---

## 10.3 视频生成服务

### 10.3.1 视频生成工具介绍

**SeeDream**：
```
- 文生视频
- 图生视频
- 视频编辑
- 价格：$0.1/秒
```

**可灵（Kling）**：
```
- 国产视频生成
- 质量优秀
- 价格实惠
- 支持中文
```

### 10.3.2 配置视频生成

```bash
# 安装视频生成Skills
openclaw skill install video-gen

# 配置SeeDream
openclaw config set seedream.apiKey "your-api-key"

# 配置可灵
openclaw config set kling.apiKey "your-api-key"
```

### 10.3.3 实战案例

**案例1：短视频制作**
```
你：生成一个5秒的视频：
海浪拍打沙滩，日落时分

OpenClaw：正在生成...
预计时间：2分钟

[视频生成完成]
时长：5秒
分辨率：1080p
大小：15MB
```

---

## 10.4 语音合成接入

### 10.4.1 语音合成工具

**海螺TTS**：
```
- 多种音色
- 自然流畅
- 支持中英文
- 价格：$0.01/千字
```

**MiniMax Music**：
```
- AI音乐生成
- 多种风格
- 高质量输出
```

### 10.4.2 配置语音合成

```bash
# 安装TTS Skills
openclaw skill install tts

# 配置海螺TTS
openclaw config set heluo.apiKey "your-api-key"

# 测试
你：把这段文字转成语音：
[文字内容]

OpenClaw：正在生成...
[语音文件]
```

---

## 📝 本章小结

学习了API服务封装：
1. Banana绘图集成
2. Notion数据同步
3. 视频生成服务
4. 语音合成接入

下一章学习高级配置。

---

**下一章预告**：第11章将学习高级配置，包括Antigravity Manager配置、多模型切换策略、成本优化方案、性能调优技巧等内容。

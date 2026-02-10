# 第11章 高级配置

> 💡 **本章目标**：掌握OpenClaw的高级配置技巧，包括Antigravity Manager配置、多模型切换、成本优化和性能调优。

## ⚙️ 本章内容

- 11.1 Antigravity Manager配置
- 11.2 多模型切换策略
- 11.3 成本优化方案
- 11.4 性能调优技巧

---

## 11.1 Antigravity Manager配置

### 11.1.1 什么是Antigravity Manager

**定义**：
Antigravity Manager是OpenClaw的API管理工具，用于：
- 管理多个AI模型API
- 统一API接口
- 负载均衡
- 成本控制

**核心优势**：
```
✅ 统一管理：一个地方管理所有API
✅ 灵活切换：随时切换不同模型
✅ 成本优化：自动选择最优方案
✅ 高可用：API故障自动切换
```

### 11.1.2 安装Antigravity Manager

**本地安装**：
```bash
# 克隆仓库
git clone https://github.com/antigravity/manager.git

# 进入目录
cd manager

# 安装依赖
npm install

# 启动服务
npm start
```

**Docker安装（推荐）**：
```bash
# 拉取镜像
docker pull antigravity/manager

# 运行容器
docker run -d \
  -p 3000:3000 \
  -v ~/antigravity:/data \
  antigravity/manager
```


### 11.1.3 配置API

**添加Claude API**：
```bash
# 访问管理界面
http://localhost:3000

# 添加API
名称：Claude Sonnet 4.5
类型：Anthropic
API Key：your-api-key
模型：claude-sonnet-4.5
```

**添加GPT API**：
```bash
名称：GPT-5.2
类型：OpenAI
API Key：your-api-key
模型：gpt-5.2
```

**添加Gemini API**：
```bash
名称：Gemini 3 Pro
类型：Google
API Key：your-api-key
模型：gemini-3-pro
```

### 11.1.4 配置OpenClaw

```bash
# 配置Antigravity Manager地址
openclaw config set api.baseUrl "http://localhost:3000"

# 配置User Token
openclaw config set api.token "your-user-token"

# 测试连接
openclaw test api
```

### 11.1.5 实战案例

**案例1：配置Claude Sonnet**
```
步骤：
1. 获取Claude API Key
2. 在Antigravity Manager中添加
3. 配置OpenClaw
4. 测试使用

结果：
你：你好
OpenClaw（Claude Sonnet）：你好！我是Claude...
```

**案例2：多账号管理**
```
场景：管理多个Claude账号

配置：
- Claude账号1：日常使用
- Claude账号2：备用
- Claude账号3：高峰期使用

优势：
- 分散负载
- 避免限流
- 提高可用性
```

---

## 11.2 多模型切换策略

### 11.2.1 模型特点对比

| 模型 | 优势 | 劣势 | 适用场景 |
|------|------|------|----------|
| Claude Sonnet | 平衡性好 | 价格中等 | 日常对话 |
| Claude Opus | 能力最强 | 价格最贵 | 复杂任务 |
| GPT-5.2 | 功能丰富 | 响应较慢 | 创意工作 |
| Gemini 3 Pro | 免费额度大 | 能力一般 | 简单任务 |
| DeepSeek-V3 | 性价比高 | 中文优化 | 编程任务 |

### 11.2.2 场景化选择策略

**日常对话**：
```
推荐：Claude Sonnet 4.5
理由：
- 响应速度快
- 质量稳定
- 价格适中
```

**复杂推理**：
```
推荐：Claude Opus 4.6
理由：
- 推理能力最强
- 准确率最高
- 适合难题
```

**图片识别**：
```
推荐：Gemini 3 Pro
理由：
- 多模态能力强
- 免费额度大
- 识别准确
```

**编程任务**：
```
推荐：DeepSeek-V3
理由：
- 代码能力强
- 价格便宜
- 中文友好
```


### 11.2.3 自动切换配置

**基于任务类型切换**：
```javascript
// 配置规则
{
  "rules": [
    {
      "condition": "task.type === 'code'",
      "model": "deepseek-v3"
    },
    {
      "condition": "task.type === 'image'",
      "model": "gemini-3-pro"
    },
    {
      "condition": "task.complexity === 'high'",
      "model": "claude-opus-4.6"
    },
    {
      "condition": "default",
      "model": "claude-sonnet-4.5"
    }
  ]
}
```

**基于成本切换**：
```javascript
{
  "rules": [
    {
      "condition": "cost.daily < 10",
      "model": "claude-opus-4.6"
    },
    {
      "condition": "cost.daily >= 10",
      "model": "claude-sonnet-4.5"
    }
  ]
}
```

---

## 11.3 成本优化方案

### 11.3.1 Token消耗分析

**查看消耗统计**：
```bash
# 查看今日消耗
openclaw stats today

# 输出示例：
今日Token消耗：
- Claude Sonnet：150K tokens ($0.75)
- Gemini Pro：50K tokens ($0.00)
- 总计：200K tokens ($0.75)

任务分布：
- 文件搜索：30%
- 日程管理：20%
- 知识管理：25%
- 其他：25%
```

**消耗优化建议**：
```
⚠️ 高消耗任务：
- 文件搜索：每次10K tokens
- 建议：优化搜索范围

✅ 优化方案：
- 使用缓存
- 减少上下文
- 优化提示词
```

### 11.3.2 缓存策略

**启用缓存**：
```bash
# 启用响应缓存
openclaw config set cache.enabled true

# 设置缓存时间（小时）
openclaw config set cache.ttl 24

# 设置缓存大小（MB）
openclaw config set cache.maxSize 1000
```

**缓存效果**：
```
未启用缓存：
- 相同问题每次都调用API
- Token消耗：10K/次
- 成本：$0.05/次

启用缓存后：
- 相同问题直接返回缓存
- Token消耗：0
- 成本：$0
- 节省：100%
```

### 11.3.3 模型降级方案

**降级策略**：
```
1. 简单任务用便宜模型
2. 复杂任务用贵模型
3. 失败后降级重试
```

**配置示例**：
```javascript
{
  "fallback": [
    "claude-opus-4.6",    // 首选
    "claude-sonnet-4.5",  // 降级1
    "gemini-3-pro"        // 降级2
  ]
}
```

### 11.3.4 成本控制实战

**案例1：降低50%成本**
```
原方案：
- 全部使用Claude Opus
- 日均消耗：$20

优化方案：
- 简单任务用Sonnet
- 复杂任务用Opus
- 启用缓存

优化后：
- 日均消耗：$10
- 节省：50%
```

**案例2：免费额度最大化**
```
策略：
1. 优先使用Gemini（免费额度大）
2. 超额后切换到DeepSeek（便宜）
3. 重要任务用Claude

效果：
- 月成本：$5
- 节省：90%
```

---

## 11.4 性能调优技巧

### 11.4.1 响应速度优化

**优化前**：
```
平均响应时间：5秒
用户体验：一般
```

**优化方案**：
```
1. 启用缓存
2. 减少上下文
3. 使用流式输出
4. 并发处理
```

**优化后**：
```
平均响应时间：2秒
用户体验：优秀
提升：60%
```

### 11.4.2 并发处理优化

**配置并发数**：
```bash
# 设置最大并发数
openclaw config set concurrency.max 5

# 设置队列大小
openclaw config set concurrency.queueSize 100
```

### 11.4.3 内存管理

**监控内存使用**：
```bash
# 查看内存使用
openclaw stats memory

# 输出示例：
内存使用情况：
- 当前：512MB
- 峰值：800MB
- 平均：600MB
```

**优化建议**：
```
⚠️ 内存占用高：
- 清理缓存
- 减少并发
- 重启服务
```

---

## 📝 本章小结

学习了OpenClaw的高级配置：
1. Antigravity Manager配置
2. 多模型切换策略
3. 成本优化方案
4. 性能调优技巧

掌握这些技巧可以：
- 降低50%以上成本
- 提升60%响应速度
- 提高系统稳定性

---

**下一章预告**：第12章将进入实战案例部分，学习个人效率提升的完整工作流。

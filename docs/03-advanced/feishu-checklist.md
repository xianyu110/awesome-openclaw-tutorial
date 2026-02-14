# 飞书Bot配置检查清单

> ✅ 使用本清单确保飞书Bot配置完整，避免常见问题

---

## 📋 配置前准备

- [ ] 已安装 OpenClaw（版本 2026.2.9+）
- [ ] 已注册飞书开放平台账号
- [ ] 已创建企业/团队（个人也可以）
- [ ] 网络可以访问飞书开放平台

---

## 🔧 应用创建（飞书开放平台）

### 1. 创建应用

- [ ] 登录飞书开放平台：https://open.feishu.cn
- [ ] 点击"创建企业自建应用"
- [ ] 填写应用信息：
  - [ ] 应用名称（如：OpenClaw助手）
  - [ ] 应用描述
  - [ ] 应用图标
- [ ] 记录 App ID 和 App Secret

### 2. 配置机器人

- [ ] 进入"应用功能" → "机器人"
- [ ] 启用机器人功能
- [ ] 设置机器人名称
- [ ] 设置机器人描述
- [ ] 上传机器人头像

### 3. 配置权限（⭐ 重要）

在"权限管理"页面，添加以下权限：

#### 必需权限（缺一不可）

- [ ] `im:message` - 获取与发送单聊、群组消息
- [ ] `im:message:send_as_bot` - 以应用身份发消息
- [ ] `contact:contact.base:readonly` - 获取通讯录基本信息 ⭐

> ⚠️ **特别注意**：`contact:contact.base:readonly` 是最容易遗漏的权限！
> 
> 如果缺少此权限：
> - ❌ 机器人无法识别用户
> - ❌ 无法响应任何消息
> - ❌ 日志中会出现 "User not found" 错误

#### 可选权限（根据需要添加）

- [ ] `im:message:group_at_msg:readonly` - 获取群组中@机器人的消息
- [ ] `im:message:group_msg:readonly` - 获取群组消息
- [ ] `im:chat` - 获取群组信息
- [ ] `contact:user.base:readonly` - 获取用户详细信息

### 4. 配置事件订阅

在"事件订阅"页面：

- [ ] 选择"使用长连接接收事件"（WebSocket 模式）
- [ ] 添加事件：`im.message.receive_v1`（接收消息）
- [ ] 确认长连接状态显示"已连接"

> 💡 **提示**：如果长连接无法建立，请先完成下面的 OpenClaw 配置步骤

### 5. 发布应用

- [ ] 点击"版本管理与发布"
- [ ] 创建版本
- [ ] 填写版本说明
- [ ] 提交审核（企业自建应用通常自动通过）
- [ ] 确认应用状态为"已发布"

### 6. 设置可用范围

- [ ] 在"可用性"页面设置可用范围
- [ ] 添加可使用的部门或成员
- [ ] 或选择"全员可用"

---

## 💻 OpenClaw 配置

### 1. 添加飞书渠道

```bash
# 运行添加渠道命令
openclaw channels add

# 选择 Feishu
# 输入 App ID
# 输入 App Secret
```text
**检查配置**：
```bash
# 查看渠道列表
openclaw channels list

# 应该看到 feishu 渠道
```text
### 2. 启动网关

```bash
# 启动网关
openclaw gateway start

# 检查状态
openclaw gateway status

# 应该显示 "running"
```text
### 3. 验证配置

```bash
# 测试飞书连接
openclaw channels test feishu

# 应该显示连接成功
```text
---

## 🧪 测试验证

### 1. 基础测试

- [ ] 在飞书中搜索并添加机器人
- [ ] 发送消息："你好"
- [ ] 机器人应该回复

### 2. 功能测试

- [ ] 测试文本消息
- [ ] 测试文件发送（如果需要）
- [ ] 测试图片发送（如果需要）
- [ ] 测试群组消息（需要@机器人）

### 3. 权限测试

- [ ] 机器人能识别用户名
- [ ] 机器人能正常回复
- [ ] 访问控制正常工作（如果配置了）

---

## 🔍 故障排查

### 机器人不回复？

按以下顺序检查：

1. **检查权限（最常见问题）**
   ```text
   ✅ im:message
   ✅ im:message:send_as_bot
   ✅ contact:contact.base:readonly ⭐ 必需
   ```

2. **检查事件订阅**
   ```text
   ✅ 已选择"长连接"模式
   ✅ 已添加 im.message.receive_v1
   ✅ 长连接状态"已连接"
   ```

3. **检查应用状态**
   ```text
   ✅ 应用已发布
   ✅ 应用已通过审核
   ✅ 用户在可用范围内
   ```

4. **检查 OpenClaw**
   ```bash
   # 检查网关状态
   openclaw gateway status
   
   # 查看日志
   openclaw logs --follow
   
   # 检查渠道配置
   openclaw channels list
   ```

### 查看详细日志

```bash
# 实时查看日志
openclaw logs --follow

# 过滤飞书相关日志
openclaw logs --follow | grep feishu

# 查看最近100行日志
openclaw logs --tail 100
```

### 常见错误及解决

| 错误信息 | 原因 | 解决方案 |
|---------|------|---------|
| `Permission denied` | 缺少权限 | 添加所有必需权限 |
| `User not found` | 缺少通讯录权限 | 添加 `contact:contact.base:readonly` |
| `Connection failed` | 网关未启动 | 运行 `openclaw gateway start` |
| `Invalid app_id` | AppID错误 | 检查配置 |
| `Long connection failed` | 长连接失败 | 确保网关已启动再配置事件订阅 |

---

## 📚 相关文档

- [第9章：多平台集成](09-multi-platform-integration.md)
- [附录E：常见问题速查](../../appendix/E-common-problems.md#问题14飞书bot不回复)
- [飞书开放平台文档](https://open.feishu.cn/document/)

---

## 💡 最佳实践

### 开发建议

1. **先测试后发布**
   - 在测试环境完成配置
   - 充分测试后再发布到生产环境

2. **权限最小化**
   - 只添加必需的权限
   - 定期审查权限使用情况

3. **日志监控**
   - 定期查看日志
   - 及时发现和解决问题

4. **备份配置**
   - 定期备份 OpenClaw 配置
   - 记录飞书应用的配置信息

### 安全建议

1. **保护密钥**
   - 不要将 App Secret 提交到代码仓库
   - 使用环境变量存储敏感信息

2. **访问控制**
   - 配置 allowlist 限制可访问用户
   - 定期审查访问日志

3. **定期更新**
   - 保持 OpenClaw 版本最新
   - 关注飞书平台的更新公告

---

**最后更新**：2026年2月14日  
**适用版本**：OpenClaw 2026.2.9+

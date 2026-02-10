# 📚 官方文档同步指南

> 本指南说明如何保持教程与 OpenClaw 官方文档同步

## 🤖 自动同步（推荐）

### GitHub Actions 自动检查

项目已配置 GitHub Actions，会自动执行以下操作：

1. **每天自动检查**
   - 北京时间每天上午 10 点自动运行
   - 检查 OpenClaw 是否有新版本发布
   - 检查官方文档是否有更新

2. **自动创建 Issue**
   - 发现新版本时自动创建提醒 Issue
   - Issue 包含 Release Notes 和待办清单
   - 标签：`sync`, `auto-generated`, `documentation`

3. **手动触发**
   - 访问 Actions 页面
   - 选择 "同步官方文档" 工作流
   - 点击 "Run workflow"

## 🔧 手动同步

### 使用同步脚本

```bash
# 运行同步检查脚本
./scripts/sync-check.sh
```

脚本会检查：
- ✅ 最新版本号
- ✅ 官方文档更新
- ✅ 关键链接可访问性
- ✅ 生成同步建议

### 手动检查清单

#### 1. 版本更新检查

**检查频率**: 每周一次

**检查内容**:
- [ ] 访问 [OpenClaw Releases](https://github.com/openclaw/openclaw/releases)
- [ ] 对比当前教程版本号
- [ ] 阅读 Release Notes
- [ ] 记录新功能和变更

**需要更新的文件**:
```
README.md                           # 版本号、新功能
docs/01-basics/02-installation.md   # 安装说明
appendix/A-command-reference.md     # 新命令
```

#### 2. 官方文档检查

**检查频率**: 每两周一次

**关键页面**:
- [官方文档首页](https://docs.openclaw.ai/)
- [快速开始](https://docs.openclaw.ai/start/getting-started)
- [配置参考](https://docs.openclaw.ai/gateway/configuration)
- [命令行工具](https://docs.openclaw.ai/cli)

**检查方法**:
```bash
# 查看官方文档最新提交
curl -s "https://api.github.com/repos/openclaw/openclaw/commits?path=docs&per_page=5" | \
  jq -r '.[] | "\(.commit.author.date) - \(.commit.message | split("\n")[0])"'
```

#### 3. GitHub 仓库检查

**检查频率**: 每周一次

**关注内容**:
- [ ] [Issues](https://github.com/openclaw/openclaw/issues) - 常见问题
- [ ] [Discussions](https://github.com/openclaw/openclaw/discussions) - 社区讨论
- [ ] [Pull Requests](https://github.com/openclaw/openclaw/pulls) - 新功能预览
- [ ] README.md 变更

## 📋 同步工作流程

### 发现新版本时

1. **评估影响**
   ```bash
   # 查看 Release Notes
   curl -s https://api.github.com/repos/openclaw/openclaw/releases/latest | jq -r .body
   ```

2. **创建同步分支**
   ```bash
   git checkout -b sync/v2026.2.9
   ```

3. **更新内容**
   - 更新版本号
   - 补充新功能说明
   - 更新命令参考
   - 添加配置示例
   - 更新截图（如需要）

4. **测试验证**
   - 检查所有链接
   - 验证命令示例
   - 确认配置正确

5. **提交更新**
   ```bash
   git add .
   git commit -m "sync: 同步 OpenClaw v2026.2.9"
   git push origin sync/v2026.2.9
   ```

6. **创建 Pull Request**
   - 标题：`sync: 同步 OpenClaw v2026.2.9`
   - 描述：列出主要变更
   - 标签：`sync`, `documentation`

### 发现文档更新时

1. **对比变更**
   ```bash
   # 查看具体变更
   open "https://github.com/openclaw/openclaw/commits/main/docs"
   ```

2. **识别影响范围**
   - 新增页面 → 考虑是否补充到教程
   - 修改说明 → 更新对应章节
   - 删除内容 → 检查教程是否需要调整

3. **更新教程**
   - 保持教程的中文特色
   - 补充实战案例
   - 添加避坑指南

## 🎯 同步优先级

### 高优先级（必须同步）

- ✅ 版本号更新
- ✅ 安装方式变更
- ✅ 重大功能变更
- ✅ 安全相关更新
- ✅ 命令行变更

### 中优先级（建议同步）

- 📝 新功能说明
- 📝 配置项变更
- 📝 最佳实践更新
- 📝 故障排查指南

### 低优先级（可选同步）

- 📌 文档格式调整
- 📌 示例代码优化
- 📌 链接更新

## 📊 同步记录

### 最近同步记录

| 日期 | 版本 | 主要变更 | 负责人 |
|------|------|---------|--------|
| 2026-02-10 | v2026.2.9 | 初始版本，补充50+配置截图 | @xianyu110 |

### 待同步内容

- [ ] iOS 支持（alpha）
- [ ] Grok (xAI) 集成
- [ ] Agent 管理 RPC 方法

## 🔗 重要链接

### 官方资源
- [OpenClaw 官网](https://openclaw.ai/)
- [官方文档](https://docs.openclaw.ai/)
- [GitHub 仓库](https://github.com/openclaw/openclaw)
- [Release 页面](https://github.com/openclaw/openclaw/releases)
- [ClawHub](https://clawhub.com/)

### 监控工具
- [GitHub Actions](../../actions)
- [Issues 列表](../../issues?q=is%3Aissue+label%3Async)

## 💡 最佳实践

1. **定期检查**
   - 设置日历提醒
   - 订阅 GitHub Release 通知
   - 关注官方 Discord/Twitter

2. **保持特色**
   - 中文本土化
   - 实战案例丰富
   - 避坑指南详细

3. **快速响应**
   - 重大更新 24 小时内响应
   - 一般更新 1 周内同步
   - 小调整可批量处理

4. **质量保证**
   - 所有命令都要测试
   - 链接都要验证
   - 截图保持最新

## 🤝 贡献指南

如果你发现官方文档有更新，欢迎：

1. 创建 Issue 提醒
2. 提交 Pull Request
3. 在 Discussions 讨论

---

**最后更新**: 2026-02-10  
**维护者**: [@xianyu110](https://github.com/xianyu110)

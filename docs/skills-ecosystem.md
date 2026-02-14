# OpenClaw Skills 生态说明

## 📊 Skills 分类统计（2026年2月）

### 📦 内置 Skills（预装）

**数量**: 49个  
**位置**: OpenClaw 安装包自带  
**特点**: 开箱即用，无需安装  
**类型**: 文件管理、知识管理、日程管理、自动化等

**说明**: 这些 Skills 在安装 OpenClaw 时就已经包含，可以直接使用，无需额外安装。

**查看命令**:
```bash
openclaw skills list --builtin
```text
---

### 🏪 ClawHub 官方 Skills

**数量**: 93个（包含49个内置）  
**位置**: ClawHub 官方仓库  
**特点**: 官方维护，质量保证  
**安装**: `clawhub install <skill-name>`

**说明**: ClawHub 是 OpenClaw 官方的 Skills 市场，提供经过官方审核和维护的高质量 Skills。

**访问方式**:
```bash
# 搜索 Skills
clawhub search <关键词>

# 安装 Skills
clawhub install <skill-name>

# 查看已安装
openclaw skills list
```text
---

### 🌐 社区 Skills（扩展）

**数量**: 1715+个  
**位置**: GitHub 社区贡献  
**特点**: 功能丰富，需要筛选  
**安装**: 手动安装或通过 GitHub

**说明**: 社区开发者贡献的 Skills，涵盖各种场景和需求。质量参差不齐，使用前建议查看评价和文档。

**安装方式**:
```bash
# 从 GitHub 克隆
git clone https://github.com/user/skill-name ~/.openclaw/skills/skill-name

# 或使用 clawhub（如果已发布）
clawhub install community/skill-name
```

---

### 🏢 企业级 Skills（百度千帆）

**数量**: 1715个  
**位置**: 百度千帆平台  
**特点**: 企业级质量，覆盖20+行业  
**适用**: 企业用户、行业应用

**说明**: 百度千帆提供的企业级 Skills 生态，专为企业场景设计，包含行业解决方案。

**行业覆盖**:
- 金融、医疗、教育、零售
- 制造、物流、客服、营销
- 等 20+ 行业

---

## 📈 总计

| 类型 | 数量 | 质量 | 推荐度 |
|------|------|------|--------|
| 内置 Skills | 49个 | ⭐⭐⭐⭐⭐ | 必用 |
| ClawHub 官方 | 93个 | ⭐⭐⭐⭐⭐ | 强烈推荐 |
| 社区 Skills | 1715+个 | ⭐⭐⭐ | 按需选择 |
| 企业级 Skills | 1715个 | ⭐⭐⭐⭐⭐ | 企业推荐 |
| **总计** | **1800+个** | - | - |

---

## 🎯 推荐安装

### Top 20 必装 Skills

详见 [第8章：Skills扩展](03-advanced/08-skills-extension.md)

### 新手推荐

1. **从内置 Skills 开始** - 熟悉基本功能
2. **安装 Top 5 核心 Skills** - 扩展核心能力
3. **根据需求选择社区 Skills** - 满足特定场景

---

## 💡 使用建议

### 选择 Skills 的原则

1. **优先使用内置 Skills** - 稳定可靠
2. **官方 Skills 次之** - 质量保证
3. **社区 Skills 谨慎选择** - 查看评价和文档
4. **企业用户考虑企业级 Skills** - 专业支持

### 避免过度安装

- ❌ 不要一次性安装太多 Skills
- ✅ 按需安装，逐步扩展
- ✅ 定期清理不用的 Skills
- ✅ 关注 Skills 更新

---

## 🔗 相关链接

- [第8章：Skills扩展](03-advanced/08-skills-extension.md) - 详细的 Skills 使用指南
- [ClawHub 市场](https://clawhub.com) - 官方 Skills 市场
- [Skills 开发文档](https://docs.openclaw.ai/skills) - 开发自己的 Skills

---

**最后更新**: 2026-02-14  
**数据来源**: OpenClaw 官方统计

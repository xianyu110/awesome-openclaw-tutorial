#!/bin/bash

# OpenClaw 官方文档同步检查脚本
# 用法: ./scripts/sync-check.sh

set -e

echo "🦞 OpenClaw 教程同步检查工具"
echo "================================"
echo ""

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 1. 检查最新版本
echo "📦 检查最新版本..."
LATEST_VERSION=$(curl -s https://api.github.com/repos/openclaw/openclaw/releases/latest | jq -r .tag_name)
CURRENT_VERSION=$(grep '适用OpenClaw版本' README.md | head -1 | sed 's/.*：//' | sed 's/+.*//' | sed 's/（.*//')

echo "   当前教程版本: v${CURRENT_VERSION}"
echo "   最新官方版本: ${LATEST_VERSION}"

if [ "$LATEST_VERSION" != "v$CURRENT_VERSION" ]; then
    echo -e "${YELLOW}⚠️  发现新版本！${NC}"
    echo ""
    echo "📝 Release Notes:"
    curl -s https://api.github.com/repos/openclaw/openclaw/releases/latest | jq -r .body | head -20
    echo ""
else
    echo -e "${GREEN}✅ 已是最新版本${NC}"
fi

echo ""
echo "================================"

# 2. 检查官方文档更新
echo "📚 检查官方文档更新..."
DOCS_LATEST_COMMIT=$(curl -s "https://api.github.com/repos/openclaw/openclaw/commits?path=docs&per_page=1" | jq -r '.[0].sha')
DOCS_LATEST_DATE=$(curl -s "https://api.github.com/repos/openclaw/openclaw/commits?path=docs&per_page=1" | jq -r '.[0].commit.author.date')

echo "   最新文档提交: ${DOCS_LATEST_COMMIT:0:7}"
echo "   提交时间: $DOCS_LATEST_DATE"

# 检查是否有记录
if [ -f ".last-docs-commit" ]; then
    LAST_COMMIT=$(cat .last-docs-commit)
    if [ "$DOCS_LATEST_COMMIT" != "$LAST_COMMIT" ]; then
        echo -e "${YELLOW}⚠️  官方文档有更新！${NC}"
        echo ""
        echo "📝 最近的文档变更:"
        curl -s "https://api.github.com/repos/openclaw/openclaw/commits?path=docs&per_page=5" | \
            jq -r '.[] | "  - [\(.sha[0:7])] \(.commit.message | split("\n")[0])"'
        echo ""
    else
        echo -e "${GREEN}✅ 文档无更新${NC}"
    fi
else
    echo "   首次检查，保存当前提交..."
    echo "$DOCS_LATEST_COMMIT" > .last-docs-commit
fi

echo ""
echo "================================"

# 3. 检查关键 URL 是否可访问
echo "🔗 检查关键链接..."

check_url() {
    local url=$1
    local name=$2
    if curl -s -o /dev/null -w "%{http_code}" "$url" | grep -q "200"; then
        echo -e "   ${GREEN}✅${NC} $name"
    else
        echo -e "   ${RED}❌${NC} $name"
    fi
}

check_url "https://openclaw.ai/" "官方网站"
check_url "https://docs.openclaw.ai/" "官方文档"
check_url "https://github.com/openclaw/openclaw" "GitHub 仓库"
check_url "https://clawhub.com/" "ClawHub"

echo ""
echo "================================"

# 4. 生成同步建议
echo "💡 同步建议:"
echo ""

if [ "$LATEST_VERSION" != "v$CURRENT_VERSION" ]; then
    echo "1. 更新版本号:"
    echo "   - README.md"
    echo "   - docs/01-basics/02-installation.md"
    echo ""
    echo "2. 检查新功能:"
    echo "   访问: https://github.com/openclaw/openclaw/releases/latest"
    echo ""
    echo "3. 更新命令参考:"
    echo "   - appendix/A-command-reference.md"
    echo ""
fi

echo "4. 定期检查官方文档:"
echo "   https://docs.openclaw.ai/"
echo ""
echo "5. 关注 GitHub Discussions:"
echo "   https://github.com/openclaw/openclaw/discussions"
echo ""

echo "================================"
echo "✨ 检查完成！"
echo ""
echo "💡 提示: 运行 'git add .last-docs-commit && git commit -m \"chore: 更新文档同步记录\"' 保存检查记录"

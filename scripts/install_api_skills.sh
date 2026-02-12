#!/bin/bash

# OpenClaw API集成Skills批量安装脚本
# 使用方法：./install_api_skills.sh [场景名称]
# 场景选项：all, content, video, knowledge, marketing, education

set -e

# 颜色定义
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 打印带颜色的消息
print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${YELLOW}ℹ️  $1${NC}"
}

# 安装单个Skill
install_skill() {
    local skill=$1
    print_info "正在安装: $skill"
    
    if npx clawhub@latest install "$skill"; then
        print_success "$skill 安装成功"
        return 0
    else
        print_error "$skill 安装失败"
        return 1
    fi
}

# 安装Skills列表
install_skills() {
    local skills=("$@")
    local success=0
    local failed=0
    
    for skill in "${skills[@]}"; do
        if install_skill "$skill"; then
            ((success++))
        else
            ((failed++))
        fi
        echo "---"
    done
    
    echo ""
    print_info "安装完成！成功: $success, 失败: $failed"
}

# 显示使用帮助
show_help() {
    cat << EOF
OpenClaw API集成Skills批量安装脚本

使用方法：
  $0 [场景名称]

场景选项：
  all         - 安装所有Skills（推荐高级用户）
  content     - 内容创作者场景（fal-ai, notion, elevenlabs）
  video       - 视频UP主场景（video-agent, tube-cog, elevenlabs）
  knowledge   - 知识工作者场景（notion, notion-mcp, openai-tts）
  marketing   - 营销人员场景（fal-ai, video-agent, elevenlabs）
  education   - 教育工作者场景（fal-ai, video-cog, openai-tts）

示例：
  $0 content    # 安装内容创作者场景的Skills
  $0 all        # 安装所有Skills

EOF
}

# 主函数
main() {
    local scenario=${1:-}
    
    if [ -z "$scenario" ]; then
        show_help
        exit 1
    fi
    
    case "$scenario" in
        all)
            print_info "开始安装所有API集成Skills..."
            print_info "注意：某些Skills可能不存在，将跳过"
            install_skills \
                "fal-ai" "nvidia-image-gen" "pollinations" "venice-ai" "recraft" \
                "video-agent" "sora-video-gen" "veo3-video-gen" "tube-cog" "video-cog" \
                "elevenlabs" "azure-tts" "google-tts" "openai-tts"
            print_info "Notion集成建议使用官方API（见文档10.2.2节）"
            ;;
        content)
            print_info "安装内容创作者场景Skills..."
            install_skills "fal-ai" "elevenlabs"
            print_info "Notion集成建议使用官方API（见文档10.2.2节）"
            ;;
        video)
            print_info "安装视频UP主场景Skills..."
            install_skills "video-agent" "tube-cog" "elevenlabs"
            ;;
        knowledge)
            print_info "安装知识工作者场景Skills..."
            install_skills "openai-tts"
            print_info "Notion集成建议使用官方API（见文档10.2.2节）"
            ;;
        marketing)
            print_info "安装营销人员场景Skills..."
            install_skills "fal-ai" "video-agent" "elevenlabs"
            ;;
        education)
            print_info "安装教育工作者场景Skills..."
            install_skills "fal-ai" "video-cog" "openai-tts"
            ;;
        -h|--help|help)
            show_help
            exit 0
            ;;
        *)
            print_error "未知场景: $scenario"
            echo ""
            show_help
            exit 1
            ;;
    esac
}

main "$@"

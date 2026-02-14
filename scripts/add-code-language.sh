#!/bin/bash

# 为代码块自动添加语言标注
# 根据代码块内容智能判断语言类型

set -e

DOCS_DIR="docs"
BACKUP_DIR=".backup-$(date +%Y%m%d-%H%M%S)"

echo "🔍 开始为代码块添加语言标注..."
echo ""

# 创建备份
echo "📦 创建备份到 $BACKUP_DIR..."
mkdir -p "$BACKUP_DIR"
cp -r "$DOCS_DIR" "$BACKUP_DIR/"
echo "✅ 备份完成"
echo ""

# 统计信息
total_files=0
total_blocks=0
bash_blocks=0
json_blocks=0
text_blocks=0
yaml_blocks=0
python_blocks=0
javascript_blocks=0
typescript_blocks=0

# 处理单个文件
process_file() {
    local file="$1"
    local temp_file="${file}.tmp"
    local in_code_block=0
    local code_content=""
    local modified=0
    
    while IFS= read -r line || [ -n "$line" ]; do
        # 检测代码块开始
        if [[ "$line" =~ ^\`\`\`[[:space:]]*$ ]]; then
            if [ $in_code_block -eq 0 ]; then
                # 开始新的代码块
                in_code_block=1
                code_content=""
                echo "$line" >> "$temp_file"
            else
                # 代码块结束，判断语言类型
                in_code_block=0
                local lang=$(detect_language "$code_content")
                
                if [ -n "$lang" ]; then
                    # 回到文件开头，替换最后一个 ```
                    local last_line=$(tail -1 "$temp_file")
                    if [[ "$last_line" =~ ^\`\`\`[[:space:]]*$ ]]; then
                        # 删除最后一行
                        sed -i '' -e '$ d' "$temp_file"
                        # 添加带语言标注的代码块开始
                        echo "\`\`\`$lang" >> "$temp_file"
                        # 添加代码内容（已经在之前添加过了）
                        modified=1
                        
                        case "$lang" in
                            bash) ((bash_blocks++)) ;;
                            json) ((json_blocks++)) ;;
                            text) ((text_blocks++)) ;;
                            yaml) ((yaml_blocks++)) ;;
                            python) ((python_blocks++)) ;;
                            javascript) ((javascript_blocks++)) ;;
                            typescript) ((typescript_blocks++)) ;;
                        esac
                    fi
                fi
                
                echo "$line" >> "$temp_file"
                code_content=""
            fi
        elif [ $in_code_block -eq 1 ]; then
            # 收集代码块内容
            code_content+="$line"$'\n'
            echo "$line" >> "$temp_file"
        else
            # 普通行
            echo "$line" >> "$temp_file"
        fi
    done < "$file"
    
    if [ $modified -eq 1 ]; then
        mv "$temp_file" "$file"
        return 0
    else
        rm -f "$temp_file"
        return 1
    fi
}

# 智能检测代码块语言
detect_language() {
    local content="$1"
    
    # 移除空白行
    content=$(echo "$content" | sed '/^[[:space:]]*$/d')
    
    # 如果内容为空，返回 text
    if [ -z "$content" ]; then
        echo "text"
        return
    fi
    
    # 检测 Bash/Shell 命令
    if echo "$content" | grep -qE '^(openclaw|clawhub|npm|pnpm|yarn|git|docker|curl|wget|ssh|cd|ls|mkdir|rm|cp|mv|cat|echo|export|source|\$)'; then
        echo "bash"
        return
    fi
    
    # 检测 JSON
    if echo "$content" | grep -qE '^\s*\{' && echo "$content" | grep -qE '\}\s*$'; then
        echo "json"
        return
    fi
    if echo "$content" | grep -qE '^\s*\[' && echo "$content" | grep -qE '\]\s*$'; then
        echo "json"
        return
    fi
    if echo "$content" | grep -qE '"[^"]+"\s*:\s*'; then
        echo "json"
        return
    fi
    
    # 检测 YAML
    if echo "$content" | grep -qE '^[a-zA-Z_][a-zA-Z0-9_]*:\s*'; then
        if ! echo "$content" | grep -qE '\{|\}'; then
            echo "yaml"
            return
        fi
    fi
    
    # 检测 Python
    if echo "$content" | grep -qE '^(def |class |import |from |if __name__|print\(|return )'; then
        echo "python"
        return
    fi
    
    # 检测 JavaScript
    if echo "$content" | grep -qE '^(const |let |var |function |class |import |export |require\(|module\.exports)'; then
        echo "javascript"
        return
    fi
    
    # 检测 TypeScript
    if echo "$content" | grep -qE '^(interface |type |enum |namespace |declare )'; then
        echo "typescript"
        return
    fi
    if echo "$content" | grep -qE ':\s*(string|number|boolean|any|void|never)'; then
        echo "typescript"
        return
    fi
    
    # 检测输出内容（包含特定关键词）
    if echo "$content" | grep -qE '(Output:|Error:|Success:|Warning:|INFO|DEBUG|✅|❌|⚠️)'; then
        echo "text"
        return
    fi
    
    # 检测配置文件路径
    if echo "$content" | grep -qE '^(~\/|\/|\.\/|[A-Z]:\\)'; then
        echo "text"
        return
    fi
    
    # 默认返回 text
    echo "text"
}

# 导出函数供子进程使用
export -f detect_language

# 遍历所有 Markdown 文件
echo "📝 处理 Markdown 文件..."
while IFS= read -r -d '' file; do
    echo "处理: $file"
    if process_file "$file"; then
        ((total_files++))
    fi
done < <(find "$DOCS_DIR" -name "*.md" -type f -print0)

echo ""
echo "✅ 处理完成！"
echo ""
echo "📊 统计信息："
echo "  - 修改文件数: $total_files"
echo "  - 添加语言标注:"
echo "    - bash: $bash_blocks"
echo "    - json: $json_blocks"
echo "    - text: $text_blocks"
echo "    - yaml: $yaml_blocks"
echo "    - python: $python_blocks"
echo "    - javascript: $javascript_blocks"
echo "    - typescript: $typescript_blocks"
echo ""
echo "💡 提示："
echo "  - 备份位置: $BACKUP_DIR"
echo "  - 如需恢复: cp -r $BACKUP_DIR/docs/* docs/"
echo ""

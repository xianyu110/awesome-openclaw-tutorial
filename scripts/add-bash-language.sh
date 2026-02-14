#!/bin/bash

# 为明显的 Bash 命令代码块添加语言标注
# 只处理以 openclaw/clawhub 等命令开头的代码块

set -e

DOCS_DIR="docs"

echo "🔍 为 Bash 命令代码块添加语言标注..."
echo ""

# 统计
total_added=0

# 查找所有 Markdown 文件
find "$DOCS_DIR" -name "*.md" -type f | while read -r file; do
    # 使用 awk 处理文件
    awk '
    BEGIN {
        in_empty_block = 0
        block_start_line = 0
        block_content = ""
    }
    
    # 检测空代码块开始
    /^```[[:space:]]*$/ {
        if (in_empty_block == 0) {
            in_empty_block = 1
            block_start_line = NR
            block_content = ""
            print $0
            next
        } else {
            # 代码块结束
            in_empty_block = 0
            
            # 判断是否是 bash 命令
            if (block_content ~ /^(openclaw|clawhub|npm|pnpm|yarn|git|docker|curl|wget|ssh|cd |ls |mkdir|rm |cp |mv |cat |echo |export |source|\$ )/) {
                # 需要添加 bash 标注
                # 输出修改标记
                print "# NEED_BASH_TAG_AT_LINE_" block_start_line > "/dev/stderr"
            }
            
            print $0
            block_content = ""
        }
        next
    }
    
    # 收集代码块内容
    in_empty_block == 1 {
        if (block_content == "") {
            block_content = $0
        }
        print $0
        next
    }
    
    # 普通行
    {
        print $0
    }
    ' "$file" > "${file}.tmp" 2> "${file}.markers"
    
    # 检查是否有需要修改的标记
    if [ -s "${file}.markers" ]; then
        # 有需要修改的行，使用 sed 添加 bash 标注
        while IFS= read -r marker; do
            if [[ "$marker" =~ NEED_BASH_TAG_AT_LINE_([0-9]+) ]]; then
                line_num="${BASH_REMATCH[1]}"
                # 在指定行添加 bash
                sed -i '' "${line_num}s/^\`\`\`[[:space:]]*$/\`\`\`bash/" "${file}.tmp"
                ((total_added++))
            fi
        done < "${file}.markers"
        
        # 替换原文件
        mv "${file}.tmp" "$file"
        echo "✅ $file (添加了 bash 标注)"
    else
        # 没有修改，删除临时文件
        rm -f "${file}.tmp"
    fi
    
    # 清理标记文件
    rm -f "${file}.markers"
done

echo ""
echo "✅ 完成！共添加 $total_added 个 bash 语言标注"
echo ""

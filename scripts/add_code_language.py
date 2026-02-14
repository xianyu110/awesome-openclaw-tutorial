#!/usr/bin/env python3
"""
为代码块自动添加语言标注
根据代码块内容智能判断语言类型
"""

import re
import os
from pathlib import Path

def detect_language(content):
    """根据代码块内容检测语言类型"""
    if not content.strip():
        return 'text'
    
    first_line = content.strip().split('\n')[0].strip()
    
    # 检测 Bash/Shell 命令
    bash_patterns = [
        r'^(openclaw|clawhub|npm|pnpm|yarn|bun|git|docker|curl|wget|ssh)\s',
        r'^(cd|ls|mkdir|rm|cp|mv|cat|echo|export|source|chmod|chown)\s',
        r'^\$\s',
        r'^#\s*!/bin/(bash|sh)',
    ]
    for pattern in bash_patterns:
        if re.search(pattern, first_line):
            return 'bash'
    
    # 检测 JSON
    if content.strip().startswith('{') or content.strip().startswith('['):
        if '"' in content and ':' in content:
            return 'json'
    
    # 检测 YAML
    if re.search(r'^[a-zA-Z_][\w-]*:\s*\S', content, re.MULTILINE):
        if '{' not in content[:50]:  # 不是 JSON
            return 'yaml'
    
    # 检测 Python
    python_patterns = [
        r'^(def|class|import|from|if __name__|print\(|return)\s',
        r'^\s*(def|class)\s+\w+',
    ]
    for pattern in python_patterns:
        if re.search(pattern, content, re.MULTILINE):
            return 'python'
    
    # 检测 JavaScript/TypeScript
    js_patterns = [
        r'^(const|let|var|function|class|import|export|require\(|module\.exports)\s',
    ]
    ts_patterns = [
        r'^(interface|type|enum|namespace|declare)\s',
        r':\s*(string|number|boolean|any|void|never)\s*[;=]',
    ]
    
    for pattern in ts_patterns:
        if re.search(pattern, content, re.MULTILINE):
            return 'typescript'
    
    for pattern in js_patterns:
        if re.search(pattern, content, re.MULTILINE):
            return 'javascript'
    
    # 检测输出内容
    output_patterns = [
        r'(Output:|Error:|Success:|Warning:|INFO|DEBUG)',
        r'[✅❌⚠️]',
        r'Exit Code:',
    ]
    for pattern in output_patterns:
        if re.search(pattern, content):
            return 'text'
    
    # 默认返回 text
    return 'text'

def process_file(filepath):
    """处理单个 Markdown 文件"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 查找所有未标注语言的代码块
    pattern = r'```\s*\n(.*?)\n```'
    
    modified = False
    stats = {'bash': 0, 'json': 0, 'text': 0, 'yaml': 0, 'python': 0, 'javascript': 0, 'typescript': 0}
    
    def replace_code_block(match):
        nonlocal modified, stats
        code_content = match.group(1)
        lang = detect_language(code_content)
        
        if lang:
            modified = True
            stats[lang] = stats.get(lang, 0) + 1
            return f'```{lang}\n{code_content}\n```'
        return match.group(0)
    
    new_content = re.sub(pattern, replace_code_block, content, flags=re.DOTALL)
    
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True, stats
    
    return False, stats

def main():
    docs_dir = Path('docs')
    
    print("🔍 开始为代码块添加语言标注...")
    print()
    
    total_files = 0
    total_stats = {'bash': 0, 'json': 0, 'text': 0, 'yaml': 0, 'python': 0, 'javascript': 0, 'typescript': 0}
    
    # 遍历所有 Markdown 文件
    for md_file in docs_dir.rglob('*.md'):
        modified, stats = process_file(md_file)
        if modified:
            total_files += 1
            print(f"✅ {md_file}")
            for lang, count in stats.items():
                if count > 0:
                    total_stats[lang] += count
    
    print()
    print("✅ 处理完成！")
    print()
    print("📊 统计信息：")
    print(f"  - 修改文件数: {total_files}")
    print("  - 添加语言标注:")
    for lang, count in sorted(total_stats.items(), key=lambda x: x[1], reverse=True):
        if count > 0:
            print(f"    - {lang}: {count}")
    print()

if __name__ == '__main__':
    main()

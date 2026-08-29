#!/usr/bin/env python3
"""
搜索索引生成脚本
从所有 markdown 文件中提取内容，生成完整的搜索索引 JSON
"""

import os
import re
import json
from pathlib import Path

def extract_title(content):
    """从 markdown 内容中提取标题"""
    # 尝试提取第一个 # 标题
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if match:
        title = match.group(1)
        # 移除章节号（如 "第1章："）
        title = re.sub(r'^第[\dIVX]+章[：:]\s*', '', title)
        return title.strip()
    return "未命名文档"

def extract_excerpt(content, max_length=200):
    """提取摘要（引用块和第一个段落）"""
    # 提取引用块
    quotes = re.findall(r'^>\s+(.+)$', content, re.MULTILINE)
    if quotes:
        excerpt = ' '.join(quotes[:3])
    else:
        # 提取第一个段落
        match = re.search(r'^[^#\s].+', content, re.MULTILINE)
        excerpt = match.group(0) if match else ""

    # 清理和截断
    excerpt = re.sub(r'\*\*([^*]+)\*\*', r'\1', excerpt)  # 移除加粗标记
    excerpt = re.sub(r'[`*\[\]]', '', excerpt)  # 移除其他 markdown 标记
    excerpt = excerpt.strip()

    if len(excerpt) > max_length:
        excerpt = excerpt[:max_length] + '...'
    return excerpt

def extract_keywords(content):
    """提取关键词（标题、重要术语）"""
    keywords = []

    # 提取所有标题
    headings = re.findall(r'^#+\s+(.+)$', content, re.MULTILINE)
    keywords.extend(headings)

    # 提取加粗文本（通常是关键词）
    bold_texts = re.findall(r'\*\*([^*]+)\*\*', content)
    keywords.extend(bold_texts)

    # 提取列表项中的关键词
    list_items = re.findall(r'^[\s]*[-*]\s+\*\*([^*]+)\*\*', content, re.MULTILINE)
    keywords.extend(list_items)

    # 清理并按首次出现顺序去重，确保索引可重复生成
    keywords = [k.strip() for k in keywords if k.strip()]
    keywords = list(dict.fromkeys(keywords))

    return ' '.join(keywords[:20])  # 限制数量

def extract_content_summary(content, max_length=500):
    """提取内容摘要（主要文本内容）"""
    # 移除代码块
    content = re.sub(r'```[\s\S]*?```', '', content)
    # 移除图片链接
    content = re.sub(r'!\[.*?\]\(.*?\)', '', content)
    # 移除普通链接
    content = re.sub(r'\[.*?\]\(.*?\)', '', content)
    # 移除 markdown 标记
    content = re.sub(r'[#*`\[\]]', '', content)
    # 移除特殊字符，保留中文、英文、数字
    content = re.sub(r'[^\u4e00-\u9fa5a-zA-Z0-9\s]', ' ', content)
    # 压缩空白
    content = re.sub(r'\s+', ' ', content).strip()

    if len(content) > max_length:
        content = content[:max_length] + '...'
    return content

def process_markdown_file(file_path):
    """处理单个 markdown 文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 获取相对路径
        rel_path = str(file_path)
        if rel_path.startswith('./'):
            rel_path = rel_path[2:]

        # 转换为 HTML URL
        url_path = '/' + rel_path.replace('.md', '.html')

        # 提取各类信息
        title = extract_title(content)
        excerpt = extract_excerpt(content)
        keywords = extract_keywords(content)
        content_summary = extract_content_summary(content)

        # 确定分类
        if rel_path.startswith('docs/'):
            category = 'docs'
        elif rel_path.startswith('appendix/'):
            category = 'appendix'
        elif rel_path.startswith('examples/'):
            category = 'examples'
        else:
            category = 'other'

        return {
            'title': title,
            'url': url_path,
            'excerpt': excerpt,
            'content': f"{keywords} {content_summary}",
            'category': category
        }
    except Exception as e:
        print(f"❌ 处理文件出错 {file_path}: {e}")
        return None

def main():
    print("🔍 生成搜索索引...")

    search_index = []

    # 遍历所有 markdown 文件
    directories = ['docs', 'appendix', 'examples']
    for directory in directories:
        if not os.path.exists(directory):
            continue

        for root, dirs, files in os.walk(directory):
            # 排除隐藏目录
            dirs[:] = [d for d in dirs if not d.startswith('.')]

            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    doc = process_markdown_file(file_path)
                    if doc:
                        search_index.append(doc)
                        print(f"✓ 已索引: {doc['title']}")

    # 添加首页
    search_index.insert(0, {
        'title': '首页',
        'url': '/',
        'excerpt': '从零开始打造你的AI工作助手：最全面的中文教程',
        'content': 'OpenClaw 一本书玩转 OpenClaw：超级个体实战指南 从零开始打造你的 AI 工作助手 最全面的中文教程 涵盖安装 配置 实战案例 避坑指南',
        'category': 'root'
    })

    # 保存为 JSON
    output_file = 'search-index-expanded.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(search_index, f, ensure_ascii=False, indent=2)

    print(f"\n✅ 搜索索引已生成: {output_file}")
    print(f"📊 总计文档数: {len(search_index)}")

    # 同时更新 search-index.json（备份）
    backup_file = 'search-index.json'
    with open(backup_file, 'w', encoding='utf-8') as f:
        json.dump(search_index, f, ensure_ascii=False, indent=2)
    print(f"📋 备份已更新: {backup_file}")

if __name__ == '__main__':
    main()

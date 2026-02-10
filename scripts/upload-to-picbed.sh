#!/bin/bash

# 上传图片到图床脚本
API_URL="https://upload.maynor1024.live/upload"
IMAGE_DIR="images/wechat"
OUTPUT_FILE="images/wechat/uploaded-urls.txt"

echo "开始上传图片到图床..."
echo "" > "$OUTPUT_FILE"

# 遍历所有图片
for img in "$IMAGE_DIR"/*.png; do
    filename=$(basename "$img")
    echo "上传: $filename"
    
    # 使用 curl 上传
    response=$(curl -s -X POST "$API_URL" -F "file=@$img")
    
    # 提取 URL（根据你的图床返回格式调整）
    # 假设返回格式是 JSON: [{"src": "https://..."}]
    url=$(echo "$response" | grep -o '"src":"[^"]*"' | sed 's/"src":"//;s/"//')
    
    if [ -n "$url" ]; then
        echo "✓ 成功: $url"
        echo "$filename|$url" >> "$OUTPUT_FILE"
    else
        echo "✗ 失败: $filename"
        echo "响应: $response"
    fi
    
    # 避免请求过快
    sleep 1
done

echo ""
echo "上传完成！"
echo "URL 列表保存在: $OUTPUT_FILE"
cat "$OUTPUT_FILE"

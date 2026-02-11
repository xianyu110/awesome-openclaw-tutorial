#!/bin/bash

# 上传白嫖文章的图片到图床

TEMP_DIR="images/baipiao-temp"
OUTPUT_FILE="images/baipiao-uploaded-urls.txt"
MAPPING_FILE="images/baipiao-url-mapping.txt"

# 清空输出文件
> "$OUTPUT_FILE"
> "$MAPPING_FILE"

echo "开始上传图片到图床..."

COUNTER=1
for img in "$TEMP_DIR"/image_*.jpg; do
    if [ -f "$img" ]; then
        echo "[$COUNTER/40] 上传: $(basename "$img")"
        
        RESPONSE=$(curl -s -X POST "https://upload.maynor1024.live/upload" \
            -H "Authorization: Bearer maynor1024" \
            -F "file=@$img")
        
        # 提取上传后的URL路径（从JSON响应中）
        URL_PATH=$(echo "$RESPONSE" | grep -o '"/file/[^"]*"' | tr -d '"')
        
        if [ -n "$URL_PATH" ]; then
            FULL_URL="https://upload.maynor1024.live${URL_PATH}"
            echo "$FULL_URL" >> "$OUTPUT_FILE"
            echo "image_${COUNTER} -> $FULL_URL" >> "$MAPPING_FILE"
            echo "  ✓ $FULL_URL"
        else
            echo "  ✗ 上传失败: $RESPONSE"
        fi
        
        COUNTER=$((COUNTER + 1))
        sleep 0.5
    fi
done

echo ""
echo "完成！"
echo "上传的URL保存在: $OUTPUT_FILE"
echo "URL映射保存在: $MAPPING_FILE"
echo "总共上传: $(wc -l < "$OUTPUT_FILE") 张图片"

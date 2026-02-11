#!/bin/bash

# Upload images to image hosting service
echo "Uploading images to https://upload.maynor1024.live..."

# Upload image 1
echo "Uploading image 1..."
response1=$(curl -s -F "file=@/tmp/skills_images/image1.png" https://upload.maynor1024.live/upload)
url1=$(echo $response1 | grep -o 'https://[^"]*' | head -1)
echo "Image 1 URL: $url1"

# Upload image 2
echo "Uploading image 2..."
response2=$(curl -s -F "file=@/tmp/skills_images/image2.png" https://upload.maynor1024.live/upload)
url2=$(echo $response2 | grep -o 'https://[^"]*' | head -1)
echo "Image 2 URL: $url2"

# Upload image 3
echo "Uploading image 3..."
response3=$(curl -s -F "file=@/tmp/skills_images/image3.png" https://upload.maynor1024.live/upload)
url3=$(echo $response3 | grep -o 'https://[^"]*' | head -1)
echo "Image 3 URL: $url3"

# Upload image 4
echo "Uploading image 4..."
response4=$(curl -s -F "file=@/tmp/skills_images/image4.png" https://upload.maynor1024.live/upload)
url4=$(echo $response4 | grep -o 'https://[^"]*' | head -1)
echo "Image 4 URL: $url4"

echo ""
echo "All uploads complete!"
echo "Image 1: $url1"
echo "Image 2: $url2"
echo "Image 3: $url3"
echo "Image 4: $url4"

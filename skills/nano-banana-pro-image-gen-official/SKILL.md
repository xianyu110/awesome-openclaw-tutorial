---
name: nano-banana-pro-image-gen
description: 图片生成技能，当用户需要生成图片、创建图像、编辑/修改/调整已有图片时使用此技能。支持10种图片比例（1:1、16:9、9:16等）和3种分辨率（1K、2K、4K），支持文生图和图生图编辑。
---

# 图片生成与编辑

图片生成技能，可以通过自然语言帮助用户生成图片，通过API易国内代理服务访问，支持Node.js和Python两种运行环境。

## 使用指引

遵循以下步骤：

### 第1步：分析需求与参数提取
1. **明确意图**：区分用户是需要【文生图】（生成新图片）还是【图生图】（编辑/修改现有图片）。
2. **提示词（Prompt）分析**：
   - **使用用户原始完整输入**：把用户输入的原始完整问题需求描述（原文）直接作为 `-p` 提示词的主体，避免自行改写、总结或二次创作，防止细节丢失。
   - **需要补充时先确认**：如果信息不足（例如缺少风格、主体数量、镜头语言、场景细节、文字内容、禁止元素等），先向用户提问确认；用户确认后，再把补充内容**以“追加”的方式**拼接到原始提示词后。
   - 样例：
       - 用户输入：“帮我生成一张猫的图片，风格要可爱一点。”
       - 正例说明：直接使用用户输入作为提示词：`-p "帮我生成一张猫的图片，风格要可爱一点。"`
       - 反例说明：擅自改写为“生成一张可爱风格的猫的图片”会丢失用户原始输入的细节和语气。
       - 如果需要补充细节（例如颜色、背景等），先提问确认：“你希望猫是什么颜色的？背景有什么要求吗？”用户回答后，再追加到提示词中：`-p "帮我生成一张猫的图片，风格要可爱一点。猫是橘色的，背景是草地。"`

3. **关键参数整理**：
   - **Prompt（必需）**：提示词分析后的最终提示词（默认=用户原始完整且一致的输入；仅在用户确认后才追加补充信息）。
   - **Filename（可选）**：输出图片文件名/路径(需包含文件随机标识，避免重复)。不传则脚本会自动生成带时间戳的文件名。建议根据内容生成合理文件名（例如 `cat_in_garden.png`），避免使用通用名。
   - **Aspect Ratio（可选）**：根据用户描述推断比例。例如：
     - "手机壁纸" -> `9:16`
     - "电脑壁纸/视频封面" -> `16:9`
     - "头像" -> `1:1`
     - 默认若用户未明确不指定图片比例，保持图片比例为空。
   - **Resolution（可选）**：
     - 默认图片比例使用 `2K`。
     - 仅在极端高清需求或用户指定时使用 `4K`，并通过友好性提示，提示用户生成较慢，耐心等待。
     - **注意**：参数值必须大写（`1K`, `2K`, `4K`）。

### 第2步：环境检查与命令执行
1. **检查环境**：确认 `APIYI_API_KEY` 环境变量是否已设置（通常假定已设置，若运行失败再提示用户）。
2. **构建并运行命令**：
   - **优先尝试 Node.js 版本**：如果环境有 Node（`node` 命令可用），优先使用 `scripts/generate_image.js`（零依赖，参数与 Python 保持一致）。
   - **Node 不可用再用 Python 版本**：使用 `scripts/generate_image.py`。
   
   **文生图命令模板（优先 Node.js）：**
   ```bash
   node scripts/generate_image.js -p "{prompt}" -f "{filename}" [-a {ratio}] [-r {res}]
   ```

   **图生图命令模板（优先 Node.js）：**
   ```bash
   node scripts/generate_image.js -p "{edit_instruction}" -i "{input_path}" -f "{output_filename}" [-r {res}]
   ```

   **（可选）Python 版本命令模板（Node 不可用时）**：
   ```bash
   python scripts/generate_image.py -p "{prompt}" -f "{filename}" [-a {ratio}] [-r {res}]
   python scripts/generate_image.py -p "{edit_instruction}" -i "{input_path}" -f "{output_filename}" [-r {res}]
   ```

## ⏱️ 长时间任务处理策略

### 1. 任务前提示

**执行前必须告知用户**：
- "图片生成已启动，预计需要25秒到5分钟"

### 2. 🎨 最佳实践示例

1. 快速生成场景（1K分辨率）

> "快速模式：1K分辨率生成，预计30秒内完成"

2. 高质量生成场景（2K/4K分辨率）

> "高质量模式：2K分辨率生成，预计1-4分钟\n⏳ 开始生成... 🔄"

### 第3步：结果反馈
1. **执行反馈**：等待终端命令执行完毕。
2. **成功**：告知用户图片已生成，并指出保存路径。
3. **失败**：
   - 若提示 API Key 缺失，请指导用户设置环境变量。
   - 若提示网络错误，建议用户检查网络或稍后重试。

## 命令行使用样例

### 生成新图片

```bash
python scripts/generate_image.py -p "图片描述文本" -f "output.png" [-a 1:1] [-r 1K]
```

**示例：**
```bash
# 基础生成
python scripts/generate_image.py -p "一只可爱的橘猫在草地上玩耍" -f "cat.png"

# 指定比例和分辨率
python scripts/generate_image.py -p "日落山脉风景" -f "sunset.png" -a 16:9 -r 4K

# 竖版高清图片（适合手机壁纸）
python scripts/generate_image.py -p "城市夜景" -f "city.png" -a 9:16 -r 2K
```

**（可选）Node.js 版本示例：**
```bash
# 基础生成
node scripts/generate_image.js -p "一只可爱的橘猫在草地上玩耍" -f "cat.png"

# 指定比例和分辨率
node scripts/generate_image.js -p "日落山脉风景" -f "sunset.png" -a 16:9 -r 4K
```

### 编辑已有图片

```bash
python scripts/generate_image.py -p "编辑指令" -f "output.png" -i "path/to/input.png" [-a 1:1] [-r 1K]
```

**示例：**
```bash
# 修改风格
python scripts/generate_image.py -p "将图片转换成水彩画风格" -f "watercolor.png" -i "original.png"

# 添加元素
python scripts/generate_image.py -p "在天空添加彩虹" -f "rainbow.png" -i "landscape.png" -r 2K

# 替换背景
python scripts/generate_image.py -p "将背景换成海滩" -f "beach-bg.png" -i "portrait.png" -a 3:4
```

**（可选）Node.js 版本示例：**
```bash
# 修改风格
node scripts/generate_image.js -p "将图片转换成水彩画风格" -f "watercolor.png" -i "original.png"

# 多张参考图（最多14张）
node scripts/generate_image.js -p "参考多张图片融合风格" -i ref1.png ref2.png ref3.png -f "merged.png"
```

## 附加资源
- 常见使用场景文档：references/scene.md

## 命令行参数说明

> Python 与 Node.js 版本参数保持一致（短参数与长参数等价）。

| 参数 | 必填 | 说明 |
|------|------|------|
| `-p` / `--prompt` | 是 | 图片描述（文生图）或编辑指令（图生图）。保留用户原始完整输入。 |
| `-f` / `--filename` | 否 | 输出图片路径/文件名；不传则自动生成带时间戳的 PNG 文件名，并写入当前目录。 |
| `-a` / `--aspect-ratio` | 否 | 图片比例：`1:1`、`16:9`、`9:16`、`4:3`、`3:4`、`3:2`、`2:3`、`5:4`、`4:5`、`21:9`。 |
| `-r` / `--resolution` | 否 | 图片分辨率：`1K` / `2K` / `4K`（必须大写）。不传则不在请求中指定，由 API 侧决定。 |
| `-i` / `--input-image` | 否 | 图生图输入图片路径；可传多张（最多 14 张）。传入该参数即进入编辑模式。 |

## 图片参数说明

### aspect_ratio - 图片比例

支持以下10种比例：

| 比例 | 方向 | 适用场景 |
|------|------|----------|
| 1:1 | 正方形 | 头像、Instagram帖子 |
| 16:9 | 横版 | YouTube缩略图、桌面壁纸、演示文稿 |
| 9:16 | 竖版 | 抖音/TikTok、Instagram Stories、手机壁纸 |
| 4:3 | 横版 | 经典照片、演示文稿 |
| 3:4 | 竖版 | Pinterest、人像摄影 |
| 3:2 | 横版 | 单反相机标准、印刷媒体 |
| 2:3 | 竖版 | 人像海报 |
| 5:4 | 横版 | 大幅面打印、艺术印刷 |
| 4:5 | 竖版 | Instagram帖子、社交媒体 |
| 21:9 | 超宽 | 电影感、横幅、全景 |

### resolution - 图片分辨率

1K、2K、4K三种分辨率选项
**注意：** 分辨率值必须大写（1K、2K、4K）
**默认：** 2K

## 注意事项

- API密钥必须设置，可通过环境变量或命令行参数提供
- 分辨率参数必须大写（1K/2K/4K），小写会默认使用1K
- 图片生成时间：25秒到5分钟不等，取决于分辨率和服务器负载
- 编辑图片时，输入图片会自动转换为base64编码
- 确保输出目录有写入权限

### API Key设置与获取

#### 如何获取API Key

如果你还没有API密钥，请前往 **https://api.apiyi.com** 注册账号并申请API Key。

获取步骤：
1. 访问 https://api.apiyi.com
2. 注册/登录你的账号
3. 在控制台中创建API密钥
4. 复制密钥并设置环境变量或在命令行中使用

#### 设置API Key

脚本按以下顺序查找API密钥：
1. `--api-key` 命令行参数（临时使用）
2. `APIYI_API_KEY` 环境变量（推荐）

**设置环境变量（推荐）：**
```bash
# Linux/Mac
export APIYI_API_KEY="your-api-key-here"

# Windows CMD
我的电脑高级设置中设置环境变量或者执行set APIYI_API_KEY=your-api-key-here

# Windows PowerShell
在我的电脑中设置环境变量:$env:APIYI_API_KEY="your-api-key-here"
```

**命令行参数方式（临时）：**
```bash
python scripts/generate_image.py -p "一只猫" -k "your-api-key-here"
```

## 作者介绍

- 爱海贼的无处不在
- 我的微信公众号：无处不在的技术
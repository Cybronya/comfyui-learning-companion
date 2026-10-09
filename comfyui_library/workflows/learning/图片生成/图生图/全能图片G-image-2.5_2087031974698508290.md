---
key: 图片生成/图生图/全能图片G-image-2.5_2087031974698508290.json
name: 全能图片G-image-2.5_2087031974698508290.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/全能图片G-image-2.5_2087031974698508290.json
hash: 48d0b7b17d0ab425
coverage: 0.526316
learned_at: 2026-10-09 22:36:22
nodes: [RH_RhartImageG25FlareTextToImage, SaveImage, JjkText, JjkText, SaveImage, LoadImage, JjkText, SaveImage, SaveImage, LoadImage, RH_RhartImageG25FlareImageToImage, 孤海注释, 孤海注释, 孤海注释, 孤海注释, RH_RhartImageG25SunburstTextToImage, RH_RhartImageG25SunburstImageToImage, 忽略多组孤海, JjkText]
patterns: []
missing: [忽略多组孤海]
discoveries: [次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识]
---

# 图片生成/图生图/全能图片G-image-2.5_2087031974698508290.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2087031974698508290.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（19 个）：
- `RH_RhartImageG25FlareTextToImage`
- `SaveImage`
- `JjkText`
- `JjkText`
- `SaveImage`
- `LoadImage`
- `JjkText`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `RH_RhartImageG25FlareImageToImage`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `RH_RhartImageG25SunburstTextToImage`
- `RH_RhartImageG25SunburstImageToImage`
- `忽略多组孤海`
- `JjkText`

## 知识

覆盖率 **53%**（10/19）

**有卡**：`RH_RhartImageG25FlareTextToImage`、`SaveImage`、`LoadImage`、`RH_RhartImageG25FlareImageToImage`、`RH_RhartImageG25SunburstTextToImage`、`RH_RhartImageG25SunburstImageToImage`

**缺卡**（1）：`忽略多组孤海`

**用到的条目**：LoadImage、SaveImage、RH_RhartImageG25FlareImageToImage、RH_RhartImageG25SunburstImageToImage、RH_RhartImageG25SunburstTextToImage、RH_RhartImageG25FlareTextToImage、sd15-t2i-basic、sd15-t2i-lora

## 学习发现

- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识

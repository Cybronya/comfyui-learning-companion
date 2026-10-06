---
key: 图片生成/反推提示词/换光线_光影迁移_重打光_氛围光_Image2.5_2102673422240276482.json
name: 换光线_光影迁移_重打光_氛围光_Image2.5_2102673422240276482
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/换光线_光影迁移_重打光_氛围光_Image2.5_2102673422240276482.json
hash: b6c54d4fffff4a42
coverage: 0.5
learned_at: 2026-10-06 21:39:00
nodes: [LoadImage, LoadImage, SaveImage, RH_RhartImageG25FlareImageToImage, Note, Note, Note, Note, LoadImage, LoadImage]
patterns: []
missing: [RH_RhartImageG25FlareImageToImage]
discoveries: [次要节点 `RH_RhartImageG25FlareImageToImage` 知识库中没有该节点类型的任何知识]
---

# 图片生成/反推提示词/换光线_光影迁移_重打光_氛围光_Image2.5_2102673422240276482.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/换光线_光影迁移_重打光_氛围光_Image2.5_2102673422240276482.json`

## 结构

**生成流程**：Output → Other

**节点**（10 个）：
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `RH_RhartImageG25FlareImageToImage`
- `Note`
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **50%**（5/10）

**有卡**：`LoadImage`、`SaveImage`

**缺卡**（1）：`RH_RhartImageG25FlareImageToImage`

**用到的条目**：LoadImage、SaveImage、sd15-t2i-basic、sd15-t2i-lora

## 学习发现

- 次要节点 `RH_RhartImageG25FlareImageToImage` 知识库中没有该节点类型的任何知识

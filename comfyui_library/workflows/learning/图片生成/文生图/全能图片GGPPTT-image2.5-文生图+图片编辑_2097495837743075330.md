---
key: 图片生成/文生图/全能图片GGPPTT-image2.5-文生图+图片编辑_2097495837743075330.json
name: 全能图片GGPPTT-image2.5-文生图+图片编辑_2097495837743075330
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/全能图片GGPPTT-image2.5-文生图+图片编辑_2097495837743075330.json
hash: aa0b68b90c94dc8c
coverage: 0.777778
learned_at: 2026-10-20 01:35:23
nodes: [PreviewImage, RH_RhartImageG2ImageToImage, LayerUtility: TextBox, PreviewImage, LoadImage, SaveImage, SaveImage, LayerUtility: TextBox, RH_RhartImageG2TextToImage]
patterns: []
missing: []
---

# 图片生成/文生图/全能图片GGPPTT-image2.5-文生图+图片编辑_2097495837743075330.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/全能图片GGPPTT-image2.5-文生图+图片编辑_2097495837743075330.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（9 个）：
- `PreviewImage`
- `RH_RhartImageG2ImageToImage`
- `LayerUtility: TextBox`
- `PreviewImage`
- `LoadImage`
- `SaveImage`
- `SaveImage`
- `LayerUtility: TextBox`
- `RH_RhartImageG2TextToImage`

## 知识

覆盖率 **78%**（7/9）

**有卡**：`RH_RhartImageG2ImageToImage`、`LayerUtility: TextBox`、`LoadImage`、`SaveImage`、`RH_RhartImageG2TextToImage`

**用到的条目**：LoadImage、SaveImage、RH_RhartImageG2ImageToImage、RH_RhartImageG2TextToImage、LayerUtility: TextBox、sd15-t2i-basic、sd15-t2i-lora、sd1_5_text2image_sampler_clip_checkpoint

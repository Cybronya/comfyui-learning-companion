---
key: 图片生成/图生图/sam3.1精准抠像_2059564744566206466.json
name: sam3.1精准抠像_2059564744566206466
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/sam3.1精准抠像_2059564744566206466.json
hash: dca366272fbdcd37
coverage: 1
learned_at: 2026-10-23 11:44:51
nodes: [RH_Translator, CLIPTextEncode, SAM3_Detect, Text, INPAINT_ExpandMask, MaskPreview, CheckpointLoaderSimple, LoadImage, Image Blank, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageBlend V2]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
---

# 图片生成/图生图/sam3.1精准抠像_2059564744566206466.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/sam3.1精准抠像_2059564744566206466.json`

## 结构

**生成流程**：Model → Condition → Process → Output → Other

**节点**（12 个）：
- `RH_Translator`
- `CLIPTextEncode` ★核心
- `SAM3_Detect`
- `Text`
- `INPAINT_ExpandMask`
- `MaskPreview`
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `Image Blank`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageBlend V2`

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`RH_Translator`、`CLIPTextEncode`、`SAM3_Detect`、`Text`、`INPAINT_ExpandMask`、`MaskPreview`、`CheckpointLoaderSimple`、`LoadImage`、`Image Blank`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageBlend V2`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、SaveImage、MaskPreview、RH_Translator、Text、INPAINT_ExpandMask

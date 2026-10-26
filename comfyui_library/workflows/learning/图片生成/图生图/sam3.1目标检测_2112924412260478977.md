---
key: 图片生成/图生图/sam3.1目标检测_2112924412260478977.json
name: sam3.1目标检测_2112924412260478977
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/sam3.1目标检测_2112924412260478977.json
hash: b844666049d632b5
coverage: 0.8
learned_at: 2026-10-26 22:04:22
nodes: [LayerUtility: ColorImage, PreviewImage, CLIPTextEncode, LayerUtility: ImageBlend V2, PreviewImage, MaskToImage, CheckpointLoaderSimple, GetImageSize, PreviewImage, MaskPreview, DrawBBoxes, SAM3_Detect, LoadImage, Text, SaveImage]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
---

# 图片生成/图生图/sam3.1目标检测_2112924412260478977.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/sam3.1目标检测_2112924412260478977.json`

## 结构

**生成流程**：Model → Condition → Process → Output → Other

**节点**（15 个）：
- `LayerUtility: ColorImage`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageBlend V2`
- `PreviewImage`
- `MaskToImage`
- `CheckpointLoaderSimple` ★核心
- `GetImageSize`
- `PreviewImage`
- `MaskPreview`
- `DrawBBoxes`
- `SAM3_Detect`
- `LoadImage`
- `Text`
- `SaveImage`

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **80%**（12/15）

**有卡**：`LayerUtility: ColorImage`、`CLIPTextEncode`、`LayerUtility: ImageBlend V2`、`MaskToImage`、`CheckpointLoaderSimple`、`GetImageSize`、`MaskPreview`、`DrawBBoxes`、`SAM3_Detect`、`LoadImage`、`Text`、`SaveImage`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、GetImageSize、GetImageSize、SaveImage、MaskPreview、Text

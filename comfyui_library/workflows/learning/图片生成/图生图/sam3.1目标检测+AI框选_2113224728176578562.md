---
key: 图片生成/图生图/sam3.1目标检测+AI框选_2113224728176578562.json
name: sam3.1目标检测+AI框选_2113224728176578562
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/sam3.1目标检测+AI框选_2113224728176578562.json
hash: 861efd92efb10289
coverage: 0.764706
learned_at: 2026-10-26 22:04:22
nodes: [LayerUtility: ColorImage, PreviewImage, LayerUtility: ImageBlend V2, PreviewImage, MaskToImage, CheckpointLoaderSimple, GetImageSize, PreviewImage, MaskPreview, DrawBBoxes, SaveImage, SAM3_Detect, CreateBoundingBoxes, CLIPTextEncode, Text, PrimitiveStringMultiline, LoadImage]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
---

# 图片生成/图生图/sam3.1目标检测+AI框选_2113224728176578562.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/sam3.1目标检测+AI框选_2113224728176578562.json`

## 结构

**生成流程**：Model → Condition → Process → Output → Other

**节点**（17 个）：
- `LayerUtility: ColorImage`
- `PreviewImage`
- `LayerUtility: ImageBlend V2`
- `PreviewImage`
- `MaskToImage`
- `CheckpointLoaderSimple` ★核心
- `GetImageSize`
- `PreviewImage`
- `MaskPreview`
- `DrawBBoxes`
- `SaveImage`
- `SAM3_Detect`
- `CreateBoundingBoxes`
- `CLIPTextEncode` ★核心
- `Text`
- `PrimitiveStringMultiline`
- `LoadImage`

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **76%**（13/17）

**有卡**：`LayerUtility: ColorImage`、`LayerUtility: ImageBlend V2`、`MaskToImage`、`CheckpointLoaderSimple`、`GetImageSize`、`MaskPreview`、`DrawBBoxes`、`SaveImage`、`SAM3_Detect`、`CreateBoundingBoxes`、`CLIPTextEncode`、`Text`、`LoadImage`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、GetImageSize、GetImageSize、SaveImage、MaskPreview、Text

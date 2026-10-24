---
key: 图片生成/图生图/Sam3.1 高质量语义分割_2054425411542634497.json
name: Sam3.1 高质量语义分割_2054425411542634497
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Sam3.1 高质量语义分割_2054425411542634497.json
hash: 342fcfe587cd28cb
coverage: 0.882353
learned_at: 2026-10-23 11:24:15
nodes: [LoadImage, DeepTranslatorTextNode, SAM3_Detect, MaskComposite, CLIPTextEncode, PrimitiveStringMultiline, ImageAndMaskPreview, easy showAnything, CheckpointLoaderSimple, SaveImage, MaskToImage, ImageCompositeMasked, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, INPAINT_ExpandMask, 1hew_ImageMaskCrop]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1-multiplex-fp16.safetensors"}
---

# 图片生成/图生图/Sam3.1 高质量语义分割_2054425411542634497.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Sam3.1 高质量语义分割_2054425411542634497.json`

## 结构

**生成流程**：Model → Condition → Process → Output → Other

**节点**（17 个）：
- `LoadImage`
- `DeepTranslatorTextNode`
- `SAM3_Detect`
- `MaskComposite`
- `CLIPTextEncode` ★核心
- `PrimitiveStringMultiline`
- `ImageAndMaskPreview`
- `easy showAnything`
- `CheckpointLoaderSimple` ★核心
- `SaveImage`
- `MaskToImage`
- `ImageCompositeMasked`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `INPAINT_ExpandMask`
- `1hew_ImageMaskCrop`

## 关键参数

- `checkpoint` = `sam3.1-multiplex-fp16.safetensors`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`LoadImage`、`DeepTranslatorTextNode`、`SAM3_Detect`、`MaskComposite`、`CLIPTextEncode`、`ImageAndMaskPreview`、`CheckpointLoaderSimple`、`SaveImage`、`MaskToImage`、`ImageCompositeMasked`、`LayerUtility: ImageScaleByAspectRatio V2`、`INPAINT_ExpandMask`、`1hew_ImageMaskCrop`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、SaveImage、ImageAndMaskPreview、ImageCompositeMasked、MaskToImage、INPAINT_ExpandMask

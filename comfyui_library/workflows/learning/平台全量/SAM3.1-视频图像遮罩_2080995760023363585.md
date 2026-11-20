---
key: 平台全量/SAM3.1-视频图像遮罩_2080995760023363585.json
name: SAM3.1-视频图像遮罩_2080995760023363585
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/SAM3.1-视频图像遮罩_2080995760023363585.json
hash: 6e81224a0eb2e956
coverage: 0.885714
learned_at: 2026-11-14 00:55:02
nodes: [Int, VHS_VideoCombine, Convert Masks to Images, VHS_VideoCombine, ImageConcanate, CheckpointLoaderSimple, VHS_VideoCombine, BlockifyMask, GrowMask, CLIPTextEncode, CheckpointLoaderSimple, LoadImage, CLIPTextEncode, easy showAnything, Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), RH_Translator, SAM3_Detect, easy showAnything, PreviewImage, DrawMaskOnImage, LayerMask: MaskPreview, ImageAndMaskPreview, Fast Bypasser (rgthree), Fast Bypasser (rgthree), VHS_LoadVideo, RH_Translator, Note, DrawMaskOnImage, InvertMask, CM_IntToFloat, SAM3_Detect, Int, SimpleMath+, LayerUtility: ImageScaleByAspectRatio V2]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
---

# 平台全量/SAM3.1-视频图像遮罩_2080995760023363585.json

> 来源文件 `comfyui_library/workflows/平台全量/SAM3.1-视频图像遮罩_2080995760023363585.json`

## 结构

**生成流程**：Model → Condition → Process → Output → Other

**节点**（35 个）：
- `Int`
- `VHS_VideoCombine`
- `Convert Masks to Images`
- `VHS_VideoCombine`
- `ImageConcanate`
- `CheckpointLoaderSimple` ★核心
- `VHS_VideoCombine`
- `BlockifyMask`
- `GrowMask`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `RH_Translator`
- `SAM3_Detect`
- `easy showAnything`
- `PreviewImage`
- `DrawMaskOnImage`
- `LayerMask: MaskPreview`
- `ImageAndMaskPreview`
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `VHS_LoadVideo`
- `RH_Translator`
- `Note`
- `DrawMaskOnImage`
- `InvertMask`
- `CM_IntToFloat`
- `SAM3_Detect`
- `Int`
- `SimpleMath+`
- `LayerUtility: ImageScaleByAspectRatio V2`

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **89%**（31/35）

**有卡**：`Int`、`VHS_VideoCombine`、`Convert Masks to Images`、`ImageConcanate`、`CheckpointLoaderSimple`、`BlockifyMask`、`GrowMask`、`CLIPTextEncode`、`LoadImage`、`Mute / Bypass Repeater (rgthree)`、`RH_Translator`、`SAM3_Detect`、`DrawMaskOnImage`、`LayerMask: MaskPreview`、`ImageAndMaskPreview`、`Fast Bypasser (rgthree)`、`VHS_LoadVideo`、`InvertMask`、`CM_IntToFloat`、`SimpleMath+`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ImageAndMaskPreview、LayerMask: MaskPreview、BlockifyMask、CM_IntToFloat、Convert Masks to Images

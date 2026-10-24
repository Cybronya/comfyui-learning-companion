---
key: 图片生成/图生图/Flux Kontext+Union Pro2.0姿势控制及修复V1_1961122601273901058.json
name: Flux Kontext+Union Pro2.0姿势控制及修复V1_1961122601273901058
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux Kontext+Union Pro2.0姿势控制及修复V1_1961122601273901058.json
hash: 912f04d2860e13d3
coverage: 0.805556
learned_at: 2026-10-23 10:57:38
nodes: [CLIPTextEncode, VAEEncode, ConditioningZeroOut, ReferenceLatent, EmptySD3LatentImage, CLIPTextEncode, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, ControlNetLoader, LoadImage, LoadImage, JWInteger, DualCLIPLoader, VAELoader, PreviewImage, KSampler, SaveLatent, Note, FluxGuidance, VAEDecode, UNETLoader, SaveImage, CR Prompt Text, FluxKontextImageScale, AIO_Preprocessor, SaveImage, SaveImage, PreviewImage, ImageConcatMulti, PDIMAGE_LongerSize, SeedVR2GGUF, PreviewImage, easy showAnything, easy showAnything, DF_Get_image_size, ControlNetApplySD3]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "controlnet_strength": 1.8000000000000003, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 445142284599763, "steps": 20}
---

# 图片生成/图生图/Flux Kontext+Union Pro2.0姿势控制及修复V1_1961122601273901058.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux Kontext+Union Pro2.0姿势控制及修复V1_1961122601273901058.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `ReferenceLatent`
- `EmptySD3LatentImage`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ControlNetLoader`
- `LoadImage`
- `LoadImage`
- `JWInteger`
- `DualCLIPLoader`
- `VAELoader`
- `PreviewImage`
- `KSampler` ★核心
- `SaveLatent`
- `Note`
- `FluxGuidance`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `SaveImage`
- `CR Prompt Text`
- `FluxKontextImageScale`
- `AIO_Preprocessor`
- `SaveImage`
- `SaveImage`
- `PreviewImage`
- `ImageConcatMulti`
- `PDIMAGE_LongerSize`
- `SeedVR2GGUF`
- `PreviewImage`
- `easy showAnything`
- `easy showAnything`
- `DF_Get_image_size`
- `ControlNetApplySD3` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `445142284599763`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `1.8000000000000003`

## 知识

覆盖率 **81%**（29/36）

**有卡**：`CLIPTextEncode`、`VAEEncode`、`ConditioningZeroOut`、`ReferenceLatent`、`EmptySD3LatentImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`ControlNetLoader`、`LoadImage`、`JWInteger`、`DualCLIPLoader`、`VAELoader`、`KSampler`、`SaveLatent`、`FluxGuidance`、`VAEDecode`、`UNETLoader`、`SaveImage`、`CR Prompt Text`、`FluxKontextImageScale`、`AIO_Preprocessor`、`ImageConcatMulti`、`PDIMAGE_LongerSize`、`SeedVR2GGUF`、`DF_Get_image_size`、`ControlNetApplySD3`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、ControlNetLoader

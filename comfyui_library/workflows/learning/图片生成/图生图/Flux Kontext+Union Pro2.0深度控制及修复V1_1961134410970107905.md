---
key: 图片生成/图生图/Flux Kontext+Union Pro2.0深度控制及修复V1_1961134410970107905.json
name: Flux Kontext+Union Pro2.0深度控制及修复V1_1961134410970107905
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux Kontext+Union Pro2.0深度控制及修复V1_1961134410970107905.json
hash: a4a712854b9626ba
coverage: 0.810811
learned_at: 2026-10-23 10:57:39
nodes: [CLIPTextEncode, VAEEncode, ConditioningZeroOut, ReferenceLatent, EmptySD3LatentImage, CLIPTextEncode, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, ControlNetLoader, LoadImage, JWInteger, DualCLIPLoader, VAELoader, PreviewImage, KSampler, SaveLatent, Note, FluxGuidance, VAEDecode, UNETLoader, CR Prompt Text, FluxKontextImageScale, SaveImage, SaveImage, PreviewImage, ImageConcatMulti, PDIMAGE_LongerSize, SeedVR2GGUF, PreviewImage, easy showAnything, DF_Get_image_size, easy showAnything, LoadImage, DownloadAndLoadDepthAnythingV2Model, DepthAnything_V2, ControlNetApplySD3, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "controlnet_strength": 1.0000000000000002, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1033500873493113, "steps": 20}
---

# 图片生成/图生图/Flux Kontext+Union Pro2.0深度控制及修复V1_1961134410970107905.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux Kontext+Union Pro2.0深度控制及修复V1_1961134410970107905.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
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
- `CR Prompt Text`
- `FluxKontextImageScale`
- `SaveImage`
- `SaveImage`
- `PreviewImage`
- `ImageConcatMulti`
- `PDIMAGE_LongerSize`
- `SeedVR2GGUF`
- `PreviewImage`
- `easy showAnything`
- `DF_Get_image_size`
- `easy showAnything`
- `LoadImage`
- `DownloadAndLoadDepthAnythingV2Model`
- `DepthAnything_V2`
- `ControlNetApplySD3` ★核心
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1033500873493113`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `1.0000000000000002`

## 知识

覆盖率 **81%**（30/37）

**有卡**：`CLIPTextEncode`、`VAEEncode`、`ConditioningZeroOut`、`ReferenceLatent`、`EmptySD3LatentImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`ControlNetLoader`、`LoadImage`、`JWInteger`、`DualCLIPLoader`、`VAELoader`、`KSampler`、`SaveLatent`、`FluxGuidance`、`VAEDecode`、`UNETLoader`、`CR Prompt Text`、`FluxKontextImageScale`、`SaveImage`、`ImageConcatMulti`、`PDIMAGE_LongerSize`、`SeedVR2GGUF`、`DF_Get_image_size`、`DownloadAndLoadDepthAnythingV2Model`、`DepthAnything_V2`、`ControlNetApplySD3`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、ControlNetLoader

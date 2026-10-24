---
key: 图片生成/图生图/FLUX.Klein-9B一致性lora单图编辑_2033155455794548737.json
name: FLUX.Klein-9B一致性lora单图编辑_2033155455794548737
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.Klein-9B一致性lora单图编辑_2033155455794548737.json
hash: eaf7fbabadfc6703
coverage: 0.888889
learned_at: 2026-10-23 10:54:16
nodes: [ConditioningZeroOut, ReferenceLatent, SamplerCustomAdvanced, EmptyFlux2LatentImage, VAELoader, VAEEncode, ReferenceLatent, ReferenceLatent, ReferenceLatent, GetImageSize, ImageScaleToTotalPixels, KSamplerSelect, ConditioningZeroOut, ReferenceLatent, SamplerCustomAdvanced, Image Comparer (rgthree), PreviewImage, EmptyFlux2LatentImage, VAELoader, LoadTextEncoderShared //Inspire, LoadDiffusionModelShared //Inspire, VAEEncode, ReferenceLatent, ReferenceLatent, ReferenceLatent, GetImageSize, ImageScaleToTotalPixels, VAEDecode, CFGGuider, Flux2Scheduler, Flux2Scheduler, PreviewImage, VAEDecode, Note, LoadDiffusionModelShared //Inspire, LoadTextEncoderShared //Inspire, LayerUtility: ImageReelComposit, RandomNoise, CFGGuider, KSamplerSelect, LoraLoaderModelOnly, CLIPTextEncode, SaveImage, PreviewImage, Image Comparer (rgthree), CLIPTextEncode, ImageScaleToTotalPixels, LayerUtility: ImageReel, ImageStitch, CR Text, VAEEncode, LoadImage, VAEEncode, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/FLUX.Klein-9B一致性lora单图编辑_2033155455794548737.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.Klein-9B一致性lora单图编辑_2033155455794548737.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `ConditioningZeroOut`
- `ReferenceLatent`
- `SamplerCustomAdvanced` ★核心
- `EmptyFlux2LatentImage`
- `VAELoader`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `KSamplerSelect` ★核心
- `ConditioningZeroOut`
- `ReferenceLatent`
- `SamplerCustomAdvanced` ★核心
- `Image Comparer (rgthree)`
- `PreviewImage`
- `EmptyFlux2LatentImage`
- `VAELoader`
- `LoadTextEncoderShared //Inspire`
- `LoadDiffusionModelShared //Inspire`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `VAEDecode` ★核心
- `CFGGuider`
- `Flux2Scheduler`
- `Flux2Scheduler`
- `PreviewImage`
- `VAEDecode` ★核心
- `Note`
- `LoadDiffusionModelShared //Inspire`
- `LoadTextEncoderShared //Inspire`
- `LayerUtility: ImageReelComposit`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `CLIPTextEncode` ★核心
- `ImageScaleToTotalPixels`
- `LayerUtility: ImageReel`
- `ImageStitch`
- `CR Text`
- `VAEEncode` ★核心
- `LoadImage`
- `VAEEncode` ★核心
- `LoadImage`

## 知识

覆盖率 **89%**（48/54）

**有卡**：`ConditioningZeroOut`、`ReferenceLatent`、`SamplerCustomAdvanced`、`EmptyFlux2LatentImage`、`VAELoader`、`VAEEncode`、`GetImageSize`、`ImageScaleToTotalPixels`、`KSamplerSelect`、`LoadTextEncoderShared //Inspire`、`LoadDiffusionModelShared //Inspire`、`VAEDecode`、`CFGGuider`、`Flux2Scheduler`、`LayerUtility: ImageReelComposit`、`RandomNoise`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`SaveImage`、`LayerUtility: ImageReel`、`ImageStitch`、`CR Text`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、LoadImage、CFGGuider、KSamplerSelect

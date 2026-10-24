---
key: 图片生成/图生图/角色换头-单人版-图生图-FLUX.2-klein-换脸_2036297825587306498.json
name: 角色换头-单人版-图生图-FLUX.2-klein-换脸_2036297825587306498
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/角色换头-单人版-图生图-FLUX.2-klein-换脸_2036297825587306498.json
hash: d725dc2a51be0ebc
coverage: 0.972973
learned_at: 2026-10-23 13:27:10
nodes: [RandomNoise, Flux2Scheduler, KSamplerSelect, CFGGuider, ConditioningZeroOut, SaveImage, PathchSageAttentionKJ, Image Comparer (rgthree), LoadImage, ReferenceLatent, ModelPatchTorchSettings, CLIPLoader, VAEDecode, LoraLoaderModelOnly, VAELoader, ReferenceLatent, ReferenceLatent, SamplerCustomAdvanced, EmptyFlux2LatentImage, ImageScaleToTotalPixels, CR Text, CLIPTextEncode, VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, GetImageSize, VAEEncode, LayerUtility: CropByMask V2, easy int, UNETLoader, LoraLoaderModelOnly, ClothesSegment, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel]
patterns: []
missing: []
---

# 图片生成/图生图/角色换头-单人版-图生图-FLUX.2-klein-换脸_2036297825587306498.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/角色换头-单人版-图生图-FLUX.2-klein-换脸_2036297825587306498.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `RandomNoise`
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `ConditioningZeroOut`
- `SaveImage`
- `PathchSageAttentionKJ`
- `Image Comparer (rgthree)`
- `LoadImage`
- `ReferenceLatent`
- `ModelPatchTorchSettings`
- `CLIPLoader`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `ReferenceLatent`
- `ReferenceLatent`
- `SamplerCustomAdvanced` ★核心
- `EmptyFlux2LatentImage`
- `ImageScaleToTotalPixels`
- `CR Text`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `GetImageSize`
- `VAEEncode` ★核心
- `LayerUtility: CropByMask V2`
- `easy int`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ClothesSegment`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`

## 知识

覆盖率 **97%**（36/37）

**有卡**：`RandomNoise`、`Flux2Scheduler`、`KSamplerSelect`、`CFGGuider`、`ConditioningZeroOut`、`SaveImage`、`PathchSageAttentionKJ`、`LoadImage`、`ReferenceLatent`、`ModelPatchTorchSettings`、`CLIPLoader`、`VAEDecode`、`LoraLoaderModelOnly`、`VAELoader`、`SamplerCustomAdvanced`、`EmptyFlux2LatentImage`、`ImageScaleToTotalPixels`、`CR Text`、`CLIPTextEncode`、`VAEEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM V2`、`GetImageSize`、`LayerUtility: CropByMask V2`、`easy int`、`UNETLoader`、`ClothesSegment`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

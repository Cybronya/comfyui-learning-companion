---
key: 图片生成/图生图/角色换脸-单人版-FLUX.2-klein-_2034978304230428674.json
name: 角色换脸-单人版-FLUX.2-klein-_2034978304230428674
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/角色换脸-单人版-FLUX.2-klein-_2034978304230428674.json
hash: f71563cf5931bd11
coverage: 0.975
learned_at: 2026-10-23 13:27:11
nodes: [RandomNoise, KSamplerSelect, ConditioningZeroOut, SaveImage, PathchSageAttentionKJ, Image Comparer (rgthree), LoadImage, ReferenceLatent, ModelPatchTorchSettings, CLIPLoader, VAELoader, ReferenceLatent, ReferenceLatent, CLIPTextEncode, VAEEncode, VAEEncode, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, GetImageSize, Flux2Scheduler, VAEDecode, CFGGuider, SamplerCustomAdvanced, LayerUtility: PurgeVRAM V2, EmptyFlux2LatentImage, LayerUtility: ImageScaleByAspectRatio V2, CR Text, ImageCompositeMasked, LayerUtility: ColorImage V2, BlockifyMask, LayerUtility: CropByMask V2, LoadImage, ClothesSegment, easy int, LayerUtility: ImageScaleByAspectRatio V2, ImageScaleToTotalPixels, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel]
patterns: []
missing: []
---

# 图片生成/图生图/角色换脸-单人版-FLUX.2-klein-_2034978304230428674.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/角色换脸-单人版-FLUX.2-klein-_2034978304230428674.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ConditioningZeroOut`
- `SaveImage`
- `PathchSageAttentionKJ`
- `Image Comparer (rgthree)`
- `LoadImage`
- `ReferenceLatent`
- `ModelPatchTorchSettings`
- `CLIPLoader`
- `VAELoader`
- `ReferenceLatent`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetImageSize`
- `Flux2Scheduler`
- `VAEDecode` ★核心
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LayerUtility: PurgeVRAM V2`
- `EmptyFlux2LatentImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CR Text`
- `ImageCompositeMasked`
- `LayerUtility: ColorImage V2`
- `BlockifyMask`
- `LayerUtility: CropByMask V2`
- `LoadImage`
- `ClothesSegment`
- `easy int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageScaleToTotalPixels`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`

## 知识

覆盖率 **98%**（39/40）

**有卡**：`RandomNoise`、`KSamplerSelect`、`ConditioningZeroOut`、`SaveImage`、`PathchSageAttentionKJ`、`LoadImage`、`ReferenceLatent`、`ModelPatchTorchSettings`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`VAEEncode`、`LoraLoaderModelOnly`、`UNETLoader`、`GetImageSize`、`Flux2Scheduler`、`VAEDecode`、`CFGGuider`、`SamplerCustomAdvanced`、`LayerUtility: PurgeVRAM V2`、`EmptyFlux2LatentImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`CR Text`、`ImageCompositeMasked`、`LayerUtility: ColorImage V2`、`BlockifyMask`、`LayerUtility: CropByMask V2`、`ClothesSegment`、`easy int`、`ImageScaleToTotalPixels`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

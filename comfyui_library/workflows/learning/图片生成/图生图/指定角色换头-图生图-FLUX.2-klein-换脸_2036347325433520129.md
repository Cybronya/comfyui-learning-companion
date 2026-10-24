---
key: 图片生成/图生图/指定角色换头-图生图-FLUX.2-klein-换脸_2036347325433520129.json
name: 指定角色换头-图生图-FLUX.2-klein-换脸_2036347325433520129
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/指定角色换头-图生图-FLUX.2-klein-换脸_2036347325433520129.json
hash: fc6ecf52f4c7ef2d
coverage: 0.977778
learned_at: 2026-10-23 12:55:52
nodes: [RandomNoise, Flux2Scheduler, KSamplerSelect, SaveImage, PathchSageAttentionKJ, Image Comparer (rgthree), LoadImage, ReferenceLatent, ModelPatchTorchSettings, CLIPLoader, VAEDecode, LoraLoaderModelOnly, ReferenceLatent, SamplerCustomAdvanced, ImageScaleToTotalPixels, CR Text, CLIPTextEncode, VAEEncode, GetImageSize, VAEEncode, LayerUtility: CropByMask V2, UNETLoader, LoraLoaderModelOnly, ClothesSegment, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, ReferenceLatent, ConditioningZeroOut, VAELoader, LayerUtility: PurgeVRAM V2, CFGGuider, easy int, InpaintModelConditioning, LayerUtility: PurgeVRAM V2, easy sam3ModelLoader, BlockifyMask, GrowMaskWithBlur, easy sam3ImageSegmentation, RH_Translator, CR Text, LayerMask: MaskPreview, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel]
patterns: []
missing: []
---

# 图片生成/图生图/指定角色换头-图生图-FLUX.2-klein-换脸_2036347325433520129.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/指定角色换头-图生图-FLUX.2-klein-换脸_2036347325433520129.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `RandomNoise`
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `SaveImage`
- `PathchSageAttentionKJ`
- `Image Comparer (rgthree)`
- `LoadImage`
- `ReferenceLatent`
- `ModelPatchTorchSettings`
- `CLIPLoader`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `ReferenceLatent`
- `SamplerCustomAdvanced` ★核心
- `ImageScaleToTotalPixels`
- `CR Text`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `GetImageSize`
- `VAEEncode` ★核心
- `LayerUtility: CropByMask V2`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ClothesSegment`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `VAELoader`
- `LayerUtility: PurgeVRAM V2`
- `CFGGuider`
- `easy int`
- `InpaintModelConditioning`
- `LayerUtility: PurgeVRAM V2`
- `easy sam3ModelLoader`
- `BlockifyMask`
- `GrowMaskWithBlur`
- `easy sam3ImageSegmentation`
- `RH_Translator`
- `CR Text`
- `LayerMask: MaskPreview`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`

## 知识

覆盖率 **98%**（44/45）

**有卡**：`RandomNoise`、`Flux2Scheduler`、`KSamplerSelect`、`SaveImage`、`PathchSageAttentionKJ`、`LoadImage`、`ReferenceLatent`、`ModelPatchTorchSettings`、`CLIPLoader`、`VAEDecode`、`LoraLoaderModelOnly`、`SamplerCustomAdvanced`、`ImageScaleToTotalPixels`、`CR Text`、`CLIPTextEncode`、`VAEEncode`、`GetImageSize`、`LayerUtility: CropByMask V2`、`UNETLoader`、`ClothesSegment`、`LayerUtility: ImageScaleByAspectRatio V2`、`ConditioningZeroOut`、`VAELoader`、`LayerUtility: PurgeVRAM V2`、`CFGGuider`、`easy int`、`InpaintModelConditioning`、`easy sam3ModelLoader`、`BlockifyMask`、`GrowMaskWithBlur`、`easy sam3ImageSegmentation`、`RH_Translator`、`LayerMask: MaskPreview`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

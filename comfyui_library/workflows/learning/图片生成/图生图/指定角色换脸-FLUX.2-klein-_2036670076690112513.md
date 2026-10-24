---
key: 图片生成/图生图/指定角色换脸-FLUX.2-klein-_2036670076690112513.json
name: 指定角色换脸-FLUX.2-klein-_2036670076690112513
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/指定角色换脸-FLUX.2-klein-_2036670076690112513.json
hash: 01eb0e897f177af1
coverage: 0.978723
learned_at: 2026-10-23 12:55:53
nodes: [RandomNoise, KSamplerSelect, ConditioningZeroOut, PathchSageAttentionKJ, Image Comparer (rgthree), ReferenceLatent, ModelPatchTorchSettings, CLIPLoader, VAELoader, CLIPTextEncode, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, GetImageSize, Flux2Scheduler, LayerUtility: PurgeVRAM V2, ImageCompositeMasked, LayerUtility: ColorImage V2, ClothesSegment, LayerUtility: ImageScaleByAspectRatio V2, BlockifyMask, easy sam3ImageSegmentation, easy sam3ModelLoader, RH_Translator, LoadImage, CR Text, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: CropByMask V2, ImageScaleToTotalPixels, VAEEncode, SamplerCustomAdvanced, VAEEncode, ReferenceLatent, ReferenceLatent, InpaintModelConditioning, CR Text, BlockifyMask, GrowMaskWithBlur, LayerMask: MaskPreview, CFGGuider, SaveImage, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, easy int, VAEDecode]
patterns: []
missing: []
---

# 图片生成/图生图/指定角色换脸-FLUX.2-klein-_2036670076690112513.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/指定角色换脸-FLUX.2-klein-_2036670076690112513.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ConditioningZeroOut`
- `PathchSageAttentionKJ`
- `Image Comparer (rgthree)`
- `ReferenceLatent`
- `ModelPatchTorchSettings`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetImageSize`
- `Flux2Scheduler`
- `LayerUtility: PurgeVRAM V2`
- `ImageCompositeMasked`
- `LayerUtility: ColorImage V2`
- `ClothesSegment`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `BlockifyMask`
- `easy sam3ImageSegmentation`
- `easy sam3ModelLoader`
- `RH_Translator`
- `LoadImage`
- `CR Text`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: CropByMask V2`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `InpaintModelConditioning`
- `CR Text`
- `BlockifyMask`
- `GrowMaskWithBlur`
- `LayerMask: MaskPreview`
- `CFGGuider`
- `SaveImage`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`
- `easy int`
- `VAEDecode` ★核心

## 知识

覆盖率 **98%**（46/47）

**有卡**：`RandomNoise`、`KSamplerSelect`、`ConditioningZeroOut`、`PathchSageAttentionKJ`、`ReferenceLatent`、`ModelPatchTorchSettings`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`UNETLoader`、`GetImageSize`、`Flux2Scheduler`、`LayerUtility: PurgeVRAM V2`、`ImageCompositeMasked`、`LayerUtility: ColorImage V2`、`ClothesSegment`、`LayerUtility: ImageScaleByAspectRatio V2`、`BlockifyMask`、`easy sam3ImageSegmentation`、`easy sam3ModelLoader`、`RH_Translator`、`LoadImage`、`CR Text`、`LayerUtility: CropByMask V2`、`ImageScaleToTotalPixels`、`VAEEncode`、`SamplerCustomAdvanced`、`InpaintModelConditioning`、`GrowMaskWithBlur`、`LayerMask: MaskPreview`、`CFGGuider`、`SaveImage`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`easy int`、`VAEDecode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

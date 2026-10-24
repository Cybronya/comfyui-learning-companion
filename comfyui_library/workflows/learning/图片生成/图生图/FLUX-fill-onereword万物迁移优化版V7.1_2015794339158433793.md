---
key: 图片生成/图生图/FLUX-fill-onereword万物迁移优化版V7.1_2015794339158433793.json
name: FLUX-fill-onereword万物迁移优化版V7.1_2015794339158433793
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX-fill-onereword万物迁移优化版V7.1_2015794339158433793.json
hash: 1f11f183881b1ab4
coverage: 0.936709
learned_at: 2026-10-23 10:53:54
nodes: [LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, GrowMask, LayerUtility: ImageScaleByAspectRatio V2, GrowMask, MaskToImage, EmptyImage, ImageConcanate, ImageConcanate, Images to RGB, PreviewImage, ImageConcanate, Images to RGB, GetImageSize, LayerUtility: ImageBlendAdvance, Mask Invert, GetImageSize, CR Color Panel, Image To Mask, LayerUtility: CropBoxResolve, CropMask, GrowMask, ImageConcanate, EmptyImage, ImageToMask, SaveImage, InspyrenetRembgAdvanced, MaskPreview+, InpaintStitch, PreviewImage, InpaintCrop, ImageToMask, LayerUtility: CropByMask V2, ImageScale, LayerMask: MaskGrow, Switch any [Crystools], LoadImage, LoadImage, UNETLoader, VAELoader, LoraLoaderModelOnly, Anything Everywhere, InpaintModelConditioning, Seed (rgthree), StyleModelApply, CLIPVisionEncode, AdvancedVisionLoader, StyleModelLoader, GetImageSize, CR Color Panel, ConditioningZeroOut, DualCLIPLoader, Anything Everywhere, Anything Everywhere, ChinesePrompt_Mix, CLIPTextEncode, GetImageSize, VAEDecode, LayerUtility: PurgeVRAM, LayerUtility: CropByMask V2, ImageToMask, Mask Fill Holes, MaskToImage, LayerUtility: CropByMask, DF_Get_image_size, ImageComposite+, ImageScale, LayerUtility: ImageBlendAdvance, ImageToMask, DifferentialDiffusion, FluxGuidance, KSamplerSelect, RandomNoise, ModelSamplingFlux, BasicGuider, SamplerCustomAdvanced, BasicScheduler, MaskToImage]
patterns: []
missing: []
---

# 图片生成/图生图/FLUX-fill-onereword万物迁移优化版V7.1_2015794339158433793.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX-fill-onereword万物迁移优化版V7.1_2015794339158433793.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（79 个）：
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `GrowMask`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GrowMask`
- `MaskToImage`
- `EmptyImage`
- `ImageConcanate`
- `ImageConcanate`
- `Images to RGB`
- `PreviewImage`
- `ImageConcanate`
- `Images to RGB`
- `GetImageSize`
- `LayerUtility: ImageBlendAdvance`
- `Mask Invert`
- `GetImageSize`
- `CR Color Panel`
- `Image To Mask`
- `LayerUtility: CropBoxResolve`
- `CropMask`
- `GrowMask`
- `ImageConcanate`
- `EmptyImage`
- `ImageToMask`
- `SaveImage`
- `InspyrenetRembgAdvanced`
- `MaskPreview+`
- `InpaintStitch`
- `PreviewImage`
- `InpaintCrop`
- `ImageToMask`
- `LayerUtility: CropByMask V2`
- `ImageScale`
- `LayerMask: MaskGrow`
- `Switch any [Crystools]`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `Anything Everywhere`
- `InpaintModelConditioning`
- `Seed (rgthree)`
- `StyleModelApply`
- `CLIPVisionEncode`
- `AdvancedVisionLoader`
- `StyleModelLoader`
- `GetImageSize`
- `CR Color Panel`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `Anything Everywhere`
- `Anything Everywhere`
- `ChinesePrompt_Mix`
- `CLIPTextEncode` ★核心
- `GetImageSize`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `LayerUtility: CropByMask V2`
- `ImageToMask`
- `Mask Fill Holes`
- `MaskToImage`
- `LayerUtility: CropByMask`
- `DF_Get_image_size`
- `ImageComposite+`
- `ImageScale`
- `LayerUtility: ImageBlendAdvance`
- `ImageToMask`
- `DifferentialDiffusion`
- `FluxGuidance`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `ModelSamplingFlux`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `BasicScheduler`
- `MaskToImage`

## 知识

覆盖率 **94%**（74/79）

**有卡**：`LayerUtility: CropByMask V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM`、`GrowMask`、`MaskToImage`、`EmptyImage`、`ImageConcanate`、`Images to RGB`、`GetImageSize`、`LayerUtility: ImageBlendAdvance`、`Mask Invert`、`CR Color Panel`、`Image To Mask`、`LayerUtility: CropBoxResolve`、`CropMask`、`ImageToMask`、`SaveImage`、`InspyrenetRembgAdvanced`、`MaskPreview+`、`InpaintStitch`、`InpaintCrop`、`ImageScale`、`LayerMask: MaskGrow`、`Switch any [Crystools]`、`LoadImage`、`UNETLoader`、`VAELoader`、`LoraLoaderModelOnly`、`InpaintModelConditioning`、`Seed (rgthree)`、`StyleModelApply`、`CLIPVisionEncode`、`AdvancedVisionLoader`、`StyleModelLoader`、`ConditioningZeroOut`、`DualCLIPLoader`、`ChinesePrompt_Mix`、`CLIPTextEncode`、`VAEDecode`、`Mask Fill Holes`、`LayerUtility: CropByMask`、`DF_Get_image_size`、`ImageComposite+`、`DifferentialDiffusion`、`FluxGuidance`、`KSamplerSelect`、`RandomNoise`、`ModelSamplingFlux`、`BasicGuider`、`SamplerCustomAdvanced`、`BasicScheduler`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance

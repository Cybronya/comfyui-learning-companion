---
key: 平台全量/YH换头完美版V2.0_1950127622279880705.json
name: YH换头完美版V2.0_1950127622279880705
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/YH换头完美版V2.0_1950127622279880705.json
hash: ef65910c85df82a5
coverage: 0.903226
learned_at: 2026-11-14 01:07:45
nodes: [StyleModelApply, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPVisionLoader, StyleModelLoader, InpaintModelConditioning, DualCLIPLoader, VAEDecode, CLIPVisionEncode, easy ifElse, LayerMask: MaskPreview, MaskToImage, ImageTransformPaddingRelative, ImageTransformPaddingRelative, easy ifElse, ImageToMask, GrowMaskWithBlur, ImpactSEGSOrderedFilter, ImpactDecomposeSEGS, SEGSPreview, MaskToSEGS, ImpactFrom_SEG_ELT, ImageConcanate, ImageConcanate, EmptyImage, ImageAndMaskPreview, ImpactSEGSOrderedFilter, ToBinaryMask, GrowMask, LayerMask: MaskPreview, LayerUtility: ImageScaleByAspectRatio, ToBinaryMask, InvertMask, LayerUtility: ImageScaleRestore, SimpleMath+, GetImageSize, GetImageSize, ImageResize+, FluxGuidance, DifferentialDiffusion, LoraLoaderModelOnly, LoraLoaderModelOnly, FloatConstant, PreviewImage, ImpactDecomposeSEGS, easy imageSize, UNETLoader, VAELoader, LayerUtility: ColorImage, ImageToMask, PreviewImage, MaskToImage, GrowMaskWithBlur, ImpactFrom_SEG_ELT_crop_region, LayerMask: MaskPreview, CLIPTextEncode, ImageAndMaskPreview, ImageToMask, MaskToImage, GrowMask, Reroute, LayerMask: MaskPreview, SubtractMask, ImageComposite+, PreviewImage, ImpactFrom_SEG_ELT, MaskToSEGS, easy imageSize, ImageAndMaskPreview, GetImageSize, ImageCrop, SaveImage, DWPreprocessor, ControlNetApplyAdvanced, ControlNetLoader, PreviewImage, SEGSPreview, LayerMask: MaskPreview, Reroute, PreviewImage, ImageComposite+, ImageToMask, InpaintModelConditioning, KSampler, VAEDecode, SaveImage, SaveImage, LoadImage, LayerMask: PersonMaskUltra V2, LoadImage, LayerMask: PersonMaskUltra V2, LayerMask: SegformerB2ClothesUltra]
patterns: []
missing: []
parameters: {"cfg": 8, "controlnet_strength": 1.0000000000000002, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 280265123492163, "steps": 20}
---

# 平台全量/YH换头完美版V2.0_1950127622279880705.json

> 来源文件 `comfyui_library/workflows/平台全量/YH换头完美版V2.0_1950127622279880705.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（93 个）：
- `StyleModelApply`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPVisionLoader`
- `StyleModelLoader`
- `InpaintModelConditioning`
- `DualCLIPLoader`
- `VAEDecode` ★核心
- `CLIPVisionEncode`
- `easy ifElse`
- `LayerMask: MaskPreview`
- `MaskToImage`
- `ImageTransformPaddingRelative`
- `ImageTransformPaddingRelative`
- `easy ifElse`
- `ImageToMask`
- `GrowMaskWithBlur`
- `ImpactSEGSOrderedFilter`
- `ImpactDecomposeSEGS`
- `SEGSPreview`
- `MaskToSEGS`
- `ImpactFrom_SEG_ELT`
- `ImageConcanate`
- `ImageConcanate`
- `EmptyImage`
- `ImageAndMaskPreview`
- `ImpactSEGSOrderedFilter`
- `ToBinaryMask`
- `GrowMask`
- `LayerMask: MaskPreview`
- `LayerUtility: ImageScaleByAspectRatio`
- `ToBinaryMask`
- `InvertMask`
- `LayerUtility: ImageScaleRestore`
- `SimpleMath+`
- `GetImageSize`
- `GetImageSize`
- `ImageResize+`
- `FluxGuidance`
- `DifferentialDiffusion`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `FloatConstant`
- `PreviewImage`
- `ImpactDecomposeSEGS`
- `easy imageSize`
- `UNETLoader` ★核心
- `VAELoader`
- `LayerUtility: ColorImage`
- `ImageToMask`
- `PreviewImage`
- `MaskToImage`
- `GrowMaskWithBlur`
- `ImpactFrom_SEG_ELT_crop_region`
- `LayerMask: MaskPreview`
- `CLIPTextEncode` ★核心
- `ImageAndMaskPreview`
- `ImageToMask`
- `MaskToImage`
- `GrowMask`
- `Reroute`
- `LayerMask: MaskPreview`
- `SubtractMask`
- `ImageComposite+`
- `PreviewImage`
- `ImpactFrom_SEG_ELT`
- `MaskToSEGS`
- `easy imageSize`
- `ImageAndMaskPreview`
- `GetImageSize`
- `ImageCrop`
- `SaveImage`
- `DWPreprocessor`
- `ControlNetApplyAdvanced` ★核心
- `ControlNetLoader`
- `PreviewImage`
- `SEGSPreview`
- `LayerMask: MaskPreview`
- `Reroute`
- `PreviewImage`
- `ImageComposite+`
- `ImageToMask`
- `InpaintModelConditioning`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `LayerMask: PersonMaskUltra V2`
- `LoadImage`
- `LayerMask: PersonMaskUltra V2`
- `LayerMask: SegformerB2ClothesUltra`

## 关键参数

- `seed` = `280265123492163`
- `steps` = `20`
- `cfg` = `8`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `1.0000000000000002`

## 知识

覆盖率 **90%**（84/93）

**有卡**：`StyleModelApply`、`KSampler`、`CLIPTextEncode`、`CLIPVisionLoader`、`StyleModelLoader`、`InpaintModelConditioning`、`DualCLIPLoader`、`VAEDecode`、`CLIPVisionEncode`、`LayerMask: MaskPreview`、`MaskToImage`、`ImageTransformPaddingRelative`、`ImageToMask`、`GrowMaskWithBlur`、`ImpactSEGSOrderedFilter`、`ImpactDecomposeSEGS`、`SEGSPreview`、`MaskToSEGS`、`ImpactFrom_SEG_ELT`、`ImageConcanate`、`EmptyImage`、`ImageAndMaskPreview`、`ToBinaryMask`、`GrowMask`、`LayerUtility: ImageScaleByAspectRatio`、`InvertMask`、`LayerUtility: ImageScaleRestore`、`SimpleMath+`、`GetImageSize`、`ImageResize+`、`FluxGuidance`、`DifferentialDiffusion`、`LoraLoaderModelOnly`、`FloatConstant`、`easy imageSize`、`UNETLoader`、`VAELoader`、`LayerUtility: ColorImage`、`ImpactFrom_SEG_ELT_crop_region`、`SubtractMask`、`ImageComposite+`、`ImageCrop`、`SaveImage`、`DWPreprocessor`、`ControlNetApplyAdvanced`、`ControlNetLoader`、`LoadImage`、`LayerMask: PersonMaskUltra V2`、`LayerMask: SegformerB2ClothesUltra`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、ControlNetApplyAdvanced

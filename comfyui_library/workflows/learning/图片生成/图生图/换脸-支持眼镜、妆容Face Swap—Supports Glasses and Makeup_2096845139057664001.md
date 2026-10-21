---
key: 图片生成/图生图/换脸-支持眼镜、妆容Face Swap—Supports Glasses and Makeup_2096845139057664001.json
name: 换脸-支持眼镜、妆容Face Swap—Supports Glasses and Makeup_2096845139057664001
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/换脸-支持眼镜、妆容Face Swap—Supports Glasses and Makeup_2096845139057664001.json
hash: dc8f63b13d18e793
coverage: 0.91954
learned_at: 2026-10-21 00:53:04
nodes: [Note, Note, Int Literal, Note, Int Literal, PreviewImage, KSampler, DownloadAndLoadFlorence2Model, GrowMaskWithBlur, RHHiddenNodes, StyleModelLoader, GrowMaskWithBlur, CLIPVisionLoader, LayerUtility: ColorImage V2, LayerUtility: ImageScaleRestore V2, Get Image Size, Florence2Run, LayerUtility: ImageBlend, AddMask, ImageToMask, CM_IntBinaryOperation, RepeatLatentBatch, CachePreviewBridge, CachePreviewBridge, CachePreviewBridge, CachePreviewBridge, SaveImage, UNETLoader, ImageMaskSwitch, LayerUtility: CropByMask V2, LayerUtility: CropByMask V2, CLIPVisionEncode, SubtractMask, AddMask, ImageConcanate, ImageConcanate, Get Image Size, CM_NumberToInt, CM_IntBinaryOperation, ImpactInt, VAEDecode, ImageAndMaskPreview, MaskToImage, SubtractMask, ImageConcanate, VAELoader, Mask Fill Holes, BlendInpaint, workflow>123, CutForInpaint, InpaintModelConditioning, IsMaskEmpty, ImageToMask, RHHiddenNodes, easy mathInt, ImageAndMaskPreview, ImageToMask, MaskToImage, ConditioningZeroOut, IsMaskEmpty, StyleModelApply, DifferentialDiffusion, Mask Fill Holes, CM_NumberToInt, MaskToImage, LayerUtility: ImageScaleByAspectRatio V2, ImageCrop+, easy imageSize, ImageScale, workflow>zz, ImageMaskSwitch, LayerUtility: ImageScaleByAspectRatio V2, FluxGuidance, ImageAndMaskPreview, GrowMaskWithBlur, easy cleanGpuUsed, CLIPTextEncode, LoraLoaderModelOnly, ColorMatch, LayerMask: PersonMaskUltra V2, LayerMask: PersonMaskUltra V2, Int Literal, Note, Note, Note, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 25851539885487, "steps": 25}
---

# 图片生成/图生图/换脸-支持眼镜、妆容Face Swap—Supports Glasses and Makeup_2096845139057664001.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/换脸-支持眼镜、妆容Face Swap—Supports Glasses and Makeup_2096845139057664001.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（87 个）：
- `Note`
- `Note`
- `Int Literal`
- `Note`
- `Int Literal`
- `PreviewImage`
- `KSampler` ★核心
- `DownloadAndLoadFlorence2Model`
- `GrowMaskWithBlur`
- `RHHiddenNodes`
- `StyleModelLoader`
- `GrowMaskWithBlur`
- `CLIPVisionLoader`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ImageScaleRestore V2`
- `Get Image Size`
- `Florence2Run`
- `LayerUtility: ImageBlend`
- `AddMask`
- `ImageToMask`
- `CM_IntBinaryOperation`
- `RepeatLatentBatch`
- `CachePreviewBridge`
- `CachePreviewBridge`
- `CachePreviewBridge`
- `CachePreviewBridge`
- `SaveImage`
- `UNETLoader` ★核心
- `ImageMaskSwitch`
- `LayerUtility: CropByMask V2`
- `LayerUtility: CropByMask V2`
- `CLIPVisionEncode`
- `SubtractMask`
- `AddMask`
- `ImageConcanate`
- `ImageConcanate`
- `Get Image Size`
- `CM_NumberToInt`
- `CM_IntBinaryOperation`
- `ImpactInt`
- `VAEDecode` ★核心
- `ImageAndMaskPreview`
- `MaskToImage`
- `SubtractMask`
- `ImageConcanate`
- `VAELoader`
- `Mask Fill Holes`
- `BlendInpaint`
- `workflow>123`
- `CutForInpaint`
- `InpaintModelConditioning`
- `IsMaskEmpty`
- `ImageToMask`
- `RHHiddenNodes`
- `easy mathInt`
- `ImageAndMaskPreview`
- `ImageToMask`
- `MaskToImage`
- `ConditioningZeroOut`
- `IsMaskEmpty`
- `StyleModelApply`
- `DifferentialDiffusion`
- `Mask Fill Holes`
- `CM_NumberToInt`
- `MaskToImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageCrop+`
- `easy imageSize`
- `ImageScale`
- `workflow>zz`
- `ImageMaskSwitch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `FluxGuidance`
- `ImageAndMaskPreview`
- `GrowMaskWithBlur`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `ColorMatch`
- `LayerMask: PersonMaskUltra V2`
- `LayerMask: PersonMaskUltra V2`
- `Int Literal`
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `25851539885487`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **92%**（80/87）

**有卡**：`Int Literal`、`KSampler`、`DownloadAndLoadFlorence2Model`、`GrowMaskWithBlur`、`RHHiddenNodes`、`StyleModelLoader`、`CLIPVisionLoader`、`LayerUtility: ColorImage V2`、`LayerUtility: ImageScaleRestore V2`、`Get Image Size`、`Florence2Run`、`LayerUtility: ImageBlend`、`AddMask`、`ImageToMask`、`CM_IntBinaryOperation`、`RepeatLatentBatch`、`CachePreviewBridge`、`SaveImage`、`UNETLoader`、`ImageMaskSwitch`、`LayerUtility: CropByMask V2`、`CLIPVisionEncode`、`SubtractMask`、`ImageConcanate`、`CM_NumberToInt`、`ImpactInt`、`VAEDecode`、`ImageAndMaskPreview`、`MaskToImage`、`VAELoader`、`Mask Fill Holes`、`BlendInpaint`、`workflow>123`、`CutForInpaint`、`InpaintModelConditioning`、`IsMaskEmpty`、`easy mathInt`、`ConditioningZeroOut`、`StyleModelApply`、`DifferentialDiffusion`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageCrop+`、`easy imageSize`、`ImageScale`、`workflow>zz`、`FluxGuidance`、`easy cleanGpuUsed`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`ColorMatch`、`LayerMask: PersonMaskUltra V2`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage

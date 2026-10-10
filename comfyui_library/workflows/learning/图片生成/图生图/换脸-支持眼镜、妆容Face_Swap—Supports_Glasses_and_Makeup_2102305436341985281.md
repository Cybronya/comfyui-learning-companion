---
key: 图片生成/图生图/换脸-支持眼镜、妆容Face_Swap—Supports_Glasses_and_Makeup_2102305436341985281.json
name: 换脸-支持眼镜、妆容Face_Swap—Supports_Glasses_and_Makeup_2102305436341985281
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/换脸-支持眼镜、妆容Face_Swap—Supports_Glasses_and_Makeup_2102305436341985281.json
hash: fd2287f27b68823f
coverage: 0.666667
learned_at: 2026-10-10 20:48:17
nodes: [Note, Note, Int Literal, Note, Int Literal, KSampler, DownloadAndLoadFlorence2Model, GrowMaskWithBlur, RHHiddenNodes, StyleModelLoader, GrowMaskWithBlur, CLIPVisionLoader, LayerUtility: ColorImage V2, LayerUtility: ImageScaleRestore V2, Get Image Size, Florence2Run, LayerUtility: ImageBlend, AddMask, ImageToMask, CM_IntBinaryOperation, RepeatLatentBatch, CachePreviewBridge, CachePreviewBridge, CachePreviewBridge, CachePreviewBridge, SaveImage, UNETLoader, ImageMaskSwitch, LayerUtility: CropByMask V2, LayerUtility: CropByMask V2, CLIPVisionEncode, SubtractMask, AddMask, ImageConcanate, ImageConcanate, Get Image Size, CM_NumberToInt, CM_IntBinaryOperation, ImpactInt, VAEDecode, ImageAndMaskPreview, MaskToImage, SubtractMask, ImageConcanate, VAELoader, Mask Fill Holes, BlendInpaint, workflow>123, CutForInpaint, InpaintModelConditioning, IsMaskEmpty, ImageToMask, RHHiddenNodes, easy mathInt, ImageAndMaskPreview, ImageToMask, MaskToImage, ConditioningZeroOut, IsMaskEmpty, StyleModelApply, DifferentialDiffusion, Mask Fill Holes, CM_NumberToInt, MaskToImage, LayerUtility: ImageScaleByAspectRatio V2, ImageCrop+, easy imageSize, ImageScale, workflow>zz, ImageMaskSwitch, LayerUtility: ImageScaleByAspectRatio V2, FluxGuidance, ImageAndMaskPreview, GrowMaskWithBlur, easy cleanGpuUsed, CLIPTextEncode, LoraLoaderModelOnly, ColorMatch, LayerMask: PersonMaskUltra V2, LoadImage, Int Literal, Note, Note, LoadImage, Note, LayerMask: PersonMaskUltra V2, PreviewImage]
patterns: []
missing: [ImageCrop+, Int Literal, Int Literal, Int Literal, LayerMask: PersonMaskUltra V2, LayerMask: PersonMaskUltra V2, LayerUtility: ColorImage V2, LayerUtility: CropByMask V2, LayerUtility: CropByMask V2, LayerUtility: ImageBlend, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleRestore V2, Mask Fill Holes, Mask Fill Holes, easy cleanGpuUsed, easy mathInt, workflow>123, workflow>zz, Get Image Size, Get Image Size, easy imageSize]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 993823162769939, "steps": 25}
discoveries: [次要节点 `ImageCrop+` 知识库中没有该节点类型的任何知识, 次要节点 `Int Literal` 知识库中没有该节点类型的任何知识, 次要节点 `Int Literal` 知识库中没有该节点类型的任何知识, 次要节点 `Int Literal` 知识库中没有该节点类型的任何知识, 次要节点 `LayerMask: PersonMaskUltra V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerMask: PersonMaskUltra V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ColorImage V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: CropByMask V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: CropByMask V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageBlend` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleRestore V2` 知识库中没有该节点类型的任何知识, 次要节点 `Mask Fill Holes` 知识库中没有该节点类型的任何知识, 次要节点 `Mask Fill Holes` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识, 次要节点 `workflow>123` 知识库中没有该节点类型的任何知识, 次要节点 `workflow>zz` 知识库中没有该节点类型的任何知识, 次要节点 `Get Image Size` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `Get Image Size` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/换脸-支持眼镜、妆容Face_Swap—Supports_Glasses_and_Makeup_2102305436341985281.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/换脸-支持眼镜、妆容Face_Swap—Supports_Glasses_and_Makeup_2102305436341985281.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（87 个）：
- `Note`
- `Note`
- `Int Literal`
- `Note`
- `Int Literal`
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
- `LoadImage`
- `Int Literal`
- `Note`
- `Note`
- `LoadImage`
- `Note`
- `LayerMask: PersonMaskUltra V2`
- `PreviewImage`

## 关键参数

- `seed` = `993823162769939`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **67%**（58/87）

**有卡**：`KSampler`、`DownloadAndLoadFlorence2Model`、`GrowMaskWithBlur`、`RHHiddenNodes`、`StyleModelLoader`、`CLIPVisionLoader`、`Florence2Run`、`AddMask`、`ImageToMask`、`CM_IntBinaryOperation`、`RepeatLatentBatch`、`CachePreviewBridge`、`SaveImage`、`UNETLoader`、`ImageMaskSwitch`、`CLIPVisionEncode`、`SubtractMask`、`ImageConcanate`、`CM_NumberToInt`、`ImpactInt`、`VAEDecode`、`ImageAndMaskPreview`、`MaskToImage`、`VAELoader`、`BlendInpaint`、`CutForInpaint`、`InpaintModelConditioning`、`IsMaskEmpty`、`ConditioningZeroOut`、`StyleModelApply`、`DifferentialDiffusion`、`ImageScale`、`FluxGuidance`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`ColorMatch`、`LoadImage`

**缺卡**（22）：`ImageCrop+`、`Int Literal`、`Int Literal`、`Int Literal`、`LayerMask: PersonMaskUltra V2`、`LayerMask: PersonMaskUltra V2`、`LayerUtility: ColorImage V2`、`LayerUtility: CropByMask V2`、`LayerUtility: CropByMask V2`、`LayerUtility: ImageBlend`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleRestore V2`、`Mask Fill Holes`、`Mask Fill Holes`、`easy cleanGpuUsed`、`easy mathInt`、`workflow>123`、`workflow>zz`、`Get Image Size`、`Get Image Size`、`easy imageSize`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage

## 学习发现

- 次要节点 `ImageCrop+` 知识库中没有该节点类型的任何知识
- 次要节点 `Int Literal` 知识库中没有该节点类型的任何知识
- 次要节点 `Int Literal` 知识库中没有该节点类型的任何知识
- 次要节点 `Int Literal` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerMask: PersonMaskUltra V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerMask: PersonMaskUltra V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ColorImage V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: CropByMask V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: CropByMask V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageBlend` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleRestore V2` 知识库中没有该节点类型的任何知识
- 次要节点 `Mask Fill Holes` 知识库中没有该节点类型的任何知识
- 次要节点 `Mask Fill Holes` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识
- 次要节点 `workflow>123` 知识库中没有该节点类型的任何知识
- 次要节点 `workflow>zz` 知识库中没有该节点类型的任何知识
- 次要节点 `Get Image Size` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `Get Image Size` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明

---
key: 图片生成/图生图/Flux.2 klein 扩图,外扩展图像尺寸-色块填充_2013700265437827073.json
name: Flux.2 klein 扩图,外扩展图像尺寸-色块填充_2013700265437827073
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.2 klein 扩图,外扩展图像尺寸-色块填充_2013700265437827073.json
hash: 7ce7a99d798ee464
coverage: 0.411765
learned_at: 2026-10-23 10:58:48
nodes: [SetNode, SetNode, GetNode, GetNode, LoadImage, Anything Everywhere, VAELoader, CLIPLoader, SetNode, CLIPLoader, UNETLoader, GetNode, FluxGuidance, SetNode, UNETLoader, CLIPTextEncode, SetNode, RepeatLatentBatch, GetNode, SetNode, VAEDecode, RebatchLatents, ConditioningZeroOut, VAEEncode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, ReferenceLatent, GetNode, Float, GetNode, PreviewImage, InpaintCropImproved, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, LayerMask: MaskPreview, PreviewImage, DrawMaskOnImage, PreviewImage, PreviewImage, ImagePadForOutpaint, PreviewImage, GetNode, SetNode, SetNode, LayerMask: MaskPreview, SetNode, LayerMask: MaskGrow, Reroute, LayerUtility: CropByMask V2, Reroute, Reroute, LayerUtility: ImageScaleRestore V2, GetNode, GetNode, LayerMask: MaskGrow, LayerUtility: ImageScaleByAspectRatio V2, LayerMask: MaskGrow, LayerUtility: RestoreCropBox, PreviewImage, Reroute, JoinImageWithAlpha, LayerUtility: ImageScaleByAspectRatio V2, LayerMask: MaskPreview, GetNode, ImpactSwitch, Int, GetNode, Bjornulf_ShowInt, Bjornulf_ShowInt, GetNode, LayerMask: MaskPreview, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, GetNode, GetNode, ImageCompositeMasked, GetNode, PreviewImage, PreviewImage, PreviewImage, LayerMask: MaskGrow, SetNode, InpaintStitchImproved, LayerMask: MaskGrow, SetNode, SetNode, InpaintCropImproved, ImpactSwitch, DifferentialDiffusion, Anything Everywhere, Int, GetNode, GetNode, InpaintModelConditioning, Image Comparer (rgthree), CR Text, SaveImage, SaveImage, KSampler, ImagePadForOutpaintTargetSize, GetNode, GetNode, GetNode]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1065027593162251, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Flux.2 klein 扩图,外扩展图像尺寸-色块填充_2013700265437827073.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.2 klein 扩图,外扩展图像尺寸-色块填充_2013700265437827073.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（119 个）：
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `Anything Everywhere`
- `VAELoader`
- `CLIPLoader`
- `SetNode`
- `CLIPLoader`
- `UNETLoader` ★核心
- `GetNode`
- `FluxGuidance`
- `SetNode`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `RepeatLatentBatch`
- `GetNode`
- `SetNode`
- `VAEDecode` ★核心
- `RebatchLatents`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ReferenceLatent`
- `GetNode`
- `Float`
- `GetNode`
- `PreviewImage`
- `InpaintCropImproved`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `LayerMask: MaskPreview`
- `PreviewImage`
- `DrawMaskOnImage`
- `PreviewImage`
- `PreviewImage`
- `ImagePadForOutpaint`
- `PreviewImage`
- `GetNode`
- `SetNode`
- `SetNode`
- `LayerMask: MaskPreview`
- `SetNode`
- `LayerMask: MaskGrow`
- `Reroute`
- `LayerUtility: CropByMask V2`
- `Reroute`
- `Reroute`
- `LayerUtility: ImageScaleRestore V2`
- `GetNode`
- `GetNode`
- `LayerMask: MaskGrow`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerMask: MaskGrow`
- `LayerUtility: RestoreCropBox`
- `PreviewImage`
- `Reroute`
- `JoinImageWithAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerMask: MaskPreview`
- `GetNode`
- `ImpactSwitch`
- `Int`
- `GetNode`
- `Bjornulf_ShowInt`
- `Bjornulf_ShowInt`
- `GetNode`
- `LayerMask: MaskPreview`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `GetNode`
- `GetNode`
- `ImageCompositeMasked`
- `GetNode`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `LayerMask: MaskGrow`
- `SetNode`
- `InpaintStitchImproved`
- `LayerMask: MaskGrow`
- `SetNode`
- `SetNode`
- `InpaintCropImproved`
- `ImpactSwitch`
- `DifferentialDiffusion`
- `Anything Everywhere`
- `Int`
- `GetNode`
- `GetNode`
- `InpaintModelConditioning`
- `Image Comparer (rgthree)`
- `CR Text`
- `SaveImage`
- `SaveImage`
- `KSampler` ★核心
- `ImagePadForOutpaintTargetSize`
- `GetNode`
- `GetNode`
- `GetNode`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1065027593162251`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **41%**（49/119）

**有卡**：`LoadImage`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`FluxGuidance`、`CLIPTextEncode`、`RepeatLatentBatch`、`VAEDecode`、`RebatchLatents`、`ConditioningZeroOut`、`VAEEncode`、`ReferenceLatent`、`Float`、`InpaintCropImproved`、`LayerMask: MaskPreview`、`DrawMaskOnImage`、`ImagePadForOutpaint`、`LayerMask: MaskGrow`、`LayerUtility: CropByMask V2`、`LayerUtility: ImageScaleRestore V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: RestoreCropBox`、`JoinImageWithAlpha`、`Int`、`Bjornulf_ShowInt`、`SaveImage`、`ImageCompositeMasked`、`InpaintStitchImproved`、`DifferentialDiffusion`、`InpaintModelConditioning`、`CR Text`、`KSampler`、`ImagePadForOutpaintTargetSize`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

---
key: 图片生成/图生图/InstantX Qwen-lmage-ControlNet-Inpainting扩图工作流_1967786028587188226.json
name: InstantX Qwen-lmage-ControlNet-Inpainting扩图工作流_1967786028587188226
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/InstantX Qwen-lmage-ControlNet-Inpainting扩图工作流_1967786028587188226.json
hash: ff7569dc431cb123
coverage: 0.735294
learned_at: 2026-10-23 11:03:46
nodes: [LayerMask: MaskInvert, LoadImage, MarkdownNote, PrimitiveInt, LoraLoaderModelOnly, Anything Everywhere3, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, PreviewImage, PreviewImage, GrowMaskWithBlur, LayerUtility: ImageScaleByAspectRatio V2, SolidMask, GetImageSize, Any Switch (rgthree), Any Switch (rgthree), VAEEncode, LayerMask: MaskPreview, Fast Groups Muter (rgthree), ImagePadForOutpaintMasked, LayerUtility: ImageScaleByAspectRatio V2, UNETLoader, ControlNetLoader, InpaintPreprocessor, ControlNetInpaintingAliMamaApply, VAELoader, Image Comparer (rgthree), ModelSamplingAuraFlow, SetLatentNoiseMask, KSampler, SaveImage, VAEDecode, LayerUtility: ImageBlend V2]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1025673557863317, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/InstantX Qwen-lmage-ControlNet-Inpainting扩图工作流_1967786028587188226.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/InstantX Qwen-lmage-ControlNet-Inpainting扩图工作流_1967786028587188226.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `LayerMask: MaskInvert`
- `LoadImage`
- `MarkdownNote`
- `PrimitiveInt`
- `LoraLoaderModelOnly` ★核心
- `Anything Everywhere3`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `PreviewImage`
- `PreviewImage`
- `GrowMaskWithBlur`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SolidMask`
- `GetImageSize`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `VAEEncode` ★核心
- `LayerMask: MaskPreview`
- `Fast Groups Muter (rgthree)`
- `ImagePadForOutpaintMasked`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UNETLoader` ★核心
- `ControlNetLoader`
- `InpaintPreprocessor`
- `ControlNetInpaintingAliMamaApply`
- `VAELoader`
- `Image Comparer (rgthree)`
- `ModelSamplingAuraFlow`
- `SetLatentNoiseMask`
- `KSampler` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `LayerUtility: ImageBlend V2`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1025673557863317`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **74%**（25/34）

**有卡**：`LayerMask: MaskInvert`、`LoadImage`、`LoraLoaderModelOnly`、`CLIPLoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`GrowMaskWithBlur`、`LayerUtility: ImageScaleByAspectRatio V2`、`SolidMask`、`GetImageSize`、`VAEEncode`、`LayerMask: MaskPreview`、`ImagePadForOutpaintMasked`、`UNETLoader`、`ControlNetLoader`、`InpaintPreprocessor`、`ControlNetInpaintingAliMamaApply`、`VAELoader`、`ModelSamplingAuraFlow`、`SetLatentNoiseMask`、`KSampler`、`SaveImage`、`VAEDecode`、`LayerUtility: ImageBlend V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

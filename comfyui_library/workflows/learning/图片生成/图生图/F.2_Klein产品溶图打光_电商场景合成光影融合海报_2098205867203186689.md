---
key: 图片生成/图生图/F.2_Klein产品溶图打光_电商场景合成光影融合海报_2098205867203186689.json
name: F.2_Klein产品溶图打光_电商场景合成光影融合海报_2098205867203186689
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.2_Klein产品溶图打光_电商场景合成光影融合海报_2098205867203186689.json
hash: 4f789d7e008f6a14
coverage: 0.910256
learned_at: 2026-10-21 00:38:59
nodes: [Fast Groups Bypasser (rgthree), UNETLoader, LayerMask: LoadBiRefNetModelV2, Image Comparer (rgthree), CLIPLoader, LoraLoaderModelOnly, CLIPTextEncode, ImpactInt, ConditioningZeroOut, KSampler, VAELoader, VAEDecode, ReferenceLatent, VAEEncode, LayerMask: LoadBiRefNetModelV2, LayerMask: BiRefNetUltraV2, UNETLoader, FastCanvasTool, ImageCropper, LoadImage, easy imageRemBg, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, FastCanvas, SaveImage, LayerUtility: ImageMaskScaleAs, LayerMask: MaskGrow, LayerUtility: HLFrequencyDetailRestore, LayerUtility: HLFrequencyDetailRestore, LayerUtility: ImageMaskScaleAs, LayerMask: MaskGrow, VAELoader, VAEDecode, ReferenceLatent, VAEEncode, KSampler, LoraLoaderModelOnly, LayerMask: BiRefNetUltraV2, LayerUtility: ImageScaleByAspectRatio V2, ImpactInt, ConditioningZeroOut, CLIPTextEncode, MultiTextConcatenate, MuyeTextEditOutput, GLM_Translation_Text, LoadImage, CLIPLoader, Image Comparer (rgthree), SaveImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, JjkText, EmptyLatentImage, solarL_SaveImagesToZip, VAEDecode, VAELoader, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/F.2_Klein产品溶图打光_电商场景合成光影融合海报_2098205867203186689.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.2_Klein产品溶图打光_电商场景合成光影融合海报_2098205867203186689.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（78 个）：
- `Fast Groups Bypasser (rgthree)`
- `UNETLoader` ★核心
- `LayerMask: LoadBiRefNetModelV2`
- `Image Comparer (rgthree)`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `ImpactInt`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `ReferenceLatent`
- `VAEEncode` ★核心
- `LayerMask: LoadBiRefNetModelV2`
- `LayerMask: BiRefNetUltraV2`
- `UNETLoader` ★核心
- `FastCanvasTool`
- `ImageCropper`
- `LoadImage`
- `easy imageRemBg`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `FastCanvas`
- `SaveImage`
- `LayerUtility: ImageMaskScaleAs`
- `LayerMask: MaskGrow`
- `LayerUtility: HLFrequencyDetailRestore`
- `LayerUtility: HLFrequencyDetailRestore`
- `LayerUtility: ImageMaskScaleAs`
- `LayerMask: MaskGrow`
- `VAELoader`
- `VAEDecode` ★核心
- `ReferenceLatent`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerMask: BiRefNetUltraV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImpactInt`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `MultiTextConcatenate`
- `MuyeTextEditOutput`
- `GLM_Translation_Text`
- `LoadImage`
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `SaveImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `JjkText`
- `EmptyLatentImage` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **91%**（71/78）

**有卡**：`UNETLoader`、`LayerMask: LoadBiRefNetModelV2`、`CLIPLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`ImpactInt`、`ConditioningZeroOut`、`KSampler`、`VAELoader`、`VAEDecode`、`ReferenceLatent`、`VAEEncode`、`LayerMask: BiRefNetUltraV2`、`FastCanvasTool`、`ImageCropper`、`LoadImage`、`easy imageRemBg`、`LayerUtility: ImageScaleByAspectRatio V2`、`FastCanvas`、`SaveImage`、`LayerUtility: ImageMaskScaleAs`、`LayerMask: MaskGrow`、`LayerUtility: HLFrequencyDetailRestore`、`MultiTextConcatenate`、`MuyeTextEditOutput`、`GLM_Translation_Text`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、SaveImage

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

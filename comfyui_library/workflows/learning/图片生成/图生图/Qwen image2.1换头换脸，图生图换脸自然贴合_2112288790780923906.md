---
key: 图片生成/图生图/Qwen image2.1换头换脸，图生图换脸自然贴合_2112288790780923906.json
name: Qwen image2.1换头换脸，图生图换脸自然贴合_2112288790780923906
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image2.1换头换脸，图生图换脸自然贴合_2112288790780923906.json
hash: e2842040f89d3674
coverage: 0.84507
learned_at: 2026-10-23 11:14:24
nodes: [LoraLoaderModelOnly, CLIPLoader, VAELoader, Anything Everywhere3, UNETLoader, SeedVR2Preprocess, VAEEncodeTiled, SeedVR2Conditioning, GetImageSize, SplitImageToTileList, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ResizeImageMaskNode, KSampler, SeedVR2PostProcessing, VAEDecodeTiled, ImageMergeTileList, Image Comparer (rgthree), RH_DLSS5Enhance, LayerUtility: HLFrequencyDetailRestore, ImageBlend, SaveImage, SaveImage, UNETLoader, Image Comparer (rgthree), TextEncodeQwenImage21, EmptyLatentImage, LoraLoaderModelOnly, LoadImage, LoadImage, VAELoader, PrimitiveInt, PrimitiveInt, PrimitiveFloat, SaveImage, LayerUtility: ImageReelComposit, KSampler, VAEDecode, ComfySwitchNode, LayerUtility: ImageReel, ResolutionSelector, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen image2.1换头换脸，图生图换脸自然贴合_2112288790780923906.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image2.1换头换脸，图生图换脸自然贴合_2112288790780923906.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（71 个）：
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `Anything Everywhere3`
- `UNETLoader` ★核心
- `SeedVR2Preprocess`
- `VAEEncodeTiled` ★核心
- `SeedVR2Conditioning`
- `GetImageSize`
- `SplitImageToTileList`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ResizeImageMaskNode`
- `KSampler` ★核心
- `SeedVR2PostProcessing`
- `VAEDecodeTiled` ★核心
- `ImageMergeTileList`
- `Image Comparer (rgthree)`
- `RH_DLSS5Enhance`
- `LayerUtility: HLFrequencyDetailRestore`
- `ImageBlend`
- `SaveImage`
- `SaveImage`
- `UNETLoader` ★核心
- `Image Comparer (rgthree)`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `VAELoader`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveFloat`
- `SaveImage`
- `LayerUtility: ImageReelComposit`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ComfySwitchNode`
- `LayerUtility: ImageReel`
- `ResolutionSelector`
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
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
- `Note`

**识别到的模式**：text_to_image

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

覆盖率 **85%**（60/71）

**有卡**：`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`SeedVR2Preprocess`、`VAEEncodeTiled`、`SeedVR2Conditioning`、`GetImageSize`、`SplitImageToTileList`、`ComfyMathExpression`、`ResizeImageMaskNode`、`KSampler`、`SeedVR2PostProcessing`、`VAEDecodeTiled`、`ImageMergeTileList`、`RH_DLSS5Enhance`、`LayerUtility: HLFrequencyDetailRestore`、`ImageBlend`、`SaveImage`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`LoadImage`、`LayerUtility: ImageReelComposit`、`VAEDecode`、`LayerUtility: ImageReel`、`ResolutionSelector`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

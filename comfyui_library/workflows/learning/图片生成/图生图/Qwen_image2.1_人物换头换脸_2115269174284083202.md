---
key: 图片生成/图生图/Qwen_image2.1_人物换头换脸_2115269174284083202.json
name: Qwen_image2.1_人物换头换脸_2115269174284083202
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_image2.1_人物换头换脸_2115269174284083202.json
hash: 50d6a45c2e7789a8
coverage: 0.795455
learned_at: 2026-10-30 17:51:13
nodes: [LoraLoaderModelOnly, CLIPLoader, VAELoader, Anything Everywhere3, UNETLoader, SeedVR2Preprocess, VAEEncodeTiled, SeedVR2Conditioning, GetImageSize, SplitImageToTileList, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ResizeImageMaskNode, KSampler, SeedVR2PostProcessing, VAEDecodeTiled, ImageMergeTileList, Image Comparer (rgthree), RH_DLSS5Enhance, LayerUtility: HLFrequencyDetailRestore, ImageBlend, SaveImage, SaveImage, UNETLoader, Image Comparer (rgthree), TextEncodeQwenImage21, EmptyLatentImage, LoraLoaderModelOnly, LoadImage, LoadImage, VAELoader, PrimitiveInt, PrimitiveInt, PrimitiveFloat, SaveImage, LayerUtility: ImageReelComposit, KSampler, VAEDecode, ComfySwitchNode, MarkdownNote, LayerUtility: ImageReel, ResolutionSelector, 孤海注释]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 42, "steps": 10, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen_image2.1_人物换头换脸_2115269174284083202.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_image2.1_人物换头换脸_2115269174284083202.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
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
- `MarkdownNote`
- `LayerUtility: ImageReel`
- `ResolutionSelector`
- `孤海注释`

## 关键参数

- `seed` = `42`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **80%**（35/44）

**有卡**：`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`SeedVR2Preprocess`、`VAEEncodeTiled`、`SeedVR2Conditioning`、`GetImageSize`、`SplitImageToTileList`、`ComfyMathExpression`、`ResizeImageMaskNode`、`KSampler`、`SeedVR2PostProcessing`、`VAEDecodeTiled`、`ImageMergeTileList`、`RH_DLSS5Enhance`、`LayerUtility: HLFrequencyDetailRestore`、`ImageBlend`、`SaveImage`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`LoadImage`、`LayerUtility: ImageReelComposit`、`VAEDecode`、`LayerUtility: ImageReel`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

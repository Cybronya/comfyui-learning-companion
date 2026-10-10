---
key: HerRAW-v0.1 配套工作流_2105122285165301761.json
name: HerRAW-v0.1 配套工作流_2105122285165301761
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/HerRAW-v0.1 配套工作流_2105122285165301761.json
hash: 59bacec04f6d6ffc
coverage: 0.764706
learned_at: 2026-10-10 20:58:39
nodes: [EmptyLatentImage, CLIPTextEncode, ConditioningZeroOut, SaveImage, ImageMergeTileList, SeedVR2PostProcessing, SeedVR2Conditioning, VAEEncodeTiled, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, SeedVR2Preprocess, KSampler, GetImageSize, VAEDecodeTiled, SplitImageToTileList, PrimitiveInt, PrimitiveInt, ResizeImageMaskNode, PrimitiveFloat, VAEDecode, Seed (rgthree), ResolutionSelector, Fast Groups Bypasser (rgthree), KSamplerAdvanced, MarkdownNote, VAELoader, CLIPLoader, LoraLoaderModelOnly, UNETLoader, VAELoader, PreviewImage, UNETLoader, PrimitiveStringMultiline]
patterns: [text_to_image]
missing: [Seed (rgthree)]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 8, "denoise": "beta", "height": 512, "sampler_name": 1, "scheduler": "ddim", "seed": "enable", "steps": "randomize", "width": 512}
discoveries: [次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# HerRAW-v0.1 配套工作流_2105122285165301761.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/HerRAW-v0.1 配套工作流_2105122285165301761.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `SaveImage`
- `ImageMergeTileList`
- `SeedVR2PostProcessing`
- `SeedVR2Conditioning`
- `VAEEncodeTiled` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `SeedVR2Preprocess`
- `KSampler` ★核心
- `GetImageSize`
- `VAEDecodeTiled` ★核心
- `SplitImageToTileList`
- `PrimitiveInt`
- `PrimitiveInt`
- `ResizeImageMaskNode`
- `PrimitiveFloat`
- `VAEDecode` ★核心
- `Seed (rgthree)`
- `ResolutionSelector`
- `Fast Groups Bypasser (rgthree)`
- `KSamplerAdvanced` ★核心
- `MarkdownNote`
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `PreviewImage`
- `UNETLoader` ★核心
- `PrimitiveStringMultiline`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `ddim`
- `denoise` = `beta`

## 知识

覆盖率 **76%**（26/34）

**有卡**：`EmptyLatentImage`、`CLIPTextEncode`、`ConditioningZeroOut`、`SaveImage`、`ImageMergeTileList`、`SeedVR2PostProcessing`、`SeedVR2Conditioning`、`VAEEncodeTiled`、`ComfyMathExpression`、`SeedVR2Preprocess`、`KSampler`、`GetImageSize`、`VAEDecodeTiled`、`SplitImageToTileList`、`ResizeImageMaskNode`、`VAEDecode`、`ResolutionSelector`、`KSamplerAdvanced`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`UNETLoader`

**缺卡**（1）：`Seed (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

---
key: Qwen_Image_2.1+SeedVR2+DLSS5_Upscale_2103710176829329409.json
name: Qwen_Image_2.1+SeedVR2+DLSS5_Upscale_2103710176829329409
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen_Image_2.1+SeedVR2+DLSS5_Upscale_2103710176829329409.json
hash: fe312eb509db9d83
coverage: 0.857143
learned_at: 2026-10-10 20:59:08
nodes: [PrimitiveInt, ComfyMathExpression, SeedVR2Preprocess, VAEEncodeTiled, PrimitiveInt, SeedVR2Conditioning, ComfyMathExpression, ImageMergeTileList, VAEDecodeTiled, ComfyMathExpression, GetImageSize, PrimitiveFloat, KSampler, SeedVR2PostProcessing, SplitImageToTileList, SamplerCustomAdvanced, SamplerCustomAdvanced, CLIPLoader, ResolutionSelector, BasicScheduler, CFGGuider, CFGGuider, KSamplerSelect, EmptyLatentImage, SplitSigmas, RandomNoise, VAEDecode, KSamplerSelect, ImageScale, SaveImageAdvanced, UNETLoader, VAELoader, UNETLoader, VAELoader, Seed (rgthree), ResizeImageMaskNode, LayerUtility: HLFrequencyDetailRestore, TextEncodeQwenImage21, ImageBlend, Image Comparer (rgthree), RH_DLSS5Enhance, SaveImage]
patterns: []
missing: [LayerUtility: HLFrequencyDetailRestore, Seed (rgthree)]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 959948902156062, "steps": 1, "width": 1024}
discoveries: [次要节点 `LayerUtility: HLFrequencyDetailRestore` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# Qwen_Image_2.1+SeedVR2+DLSS5_Upscale_2103710176829329409.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen_Image_2.1+SeedVR2+DLSS5_Upscale_2103710176829329409.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `PrimitiveInt`
- `ComfyMathExpression`
- `SeedVR2Preprocess`
- `VAEEncodeTiled` ★核心
- `PrimitiveInt`
- `SeedVR2Conditioning`
- `ComfyMathExpression`
- `ImageMergeTileList`
- `VAEDecodeTiled` ★核心
- `ComfyMathExpression`
- `GetImageSize`
- `PrimitiveFloat`
- `KSampler` ★核心
- `SeedVR2PostProcessing`
- `SplitImageToTileList`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `CLIPLoader`
- `ResolutionSelector`
- `BasicScheduler`
- `CFGGuider`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `EmptyLatentImage` ★核心
- `SplitSigmas`
- `RandomNoise`
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `ImageScale`
- `SaveImageAdvanced`
- `UNETLoader` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `VAELoader`
- `Seed (rgthree)`
- `ResizeImageMaskNode`
- `LayerUtility: HLFrequencyDetailRestore`
- `TextEncodeQwenImage21`
- `ImageBlend`
- `Image Comparer (rgthree)`
- `RH_DLSS5Enhance`
- `SaveImage`

## 关键参数

- `seed` = `959948902156062`
- `steps` = `1`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **86%**（36/42）

**有卡**：`ComfyMathExpression`、`SeedVR2Preprocess`、`VAEEncodeTiled`、`SeedVR2Conditioning`、`ImageMergeTileList`、`VAEDecodeTiled`、`GetImageSize`、`KSampler`、`SeedVR2PostProcessing`、`SplitImageToTileList`、`SamplerCustomAdvanced`、`CLIPLoader`、`ResolutionSelector`、`BasicScheduler`、`CFGGuider`、`KSamplerSelect`、`EmptyLatentImage`、`SplitSigmas`、`RandomNoise`、`VAEDecode`、`ImageScale`、`SaveImageAdvanced`、`UNETLoader`、`VAELoader`、`ResizeImageMaskNode`、`TextEncodeQwenImage21`、`ImageBlend`、`RH_DLSS5Enhance`、`SaveImage`

**缺卡**（2）：`LayerUtility: HLFrequencyDetailRestore`、`Seed (rgthree)`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: HLFrequencyDetailRestore` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

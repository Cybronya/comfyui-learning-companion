---
key: 图片生成/图生图/Qwen Image2.1动漫转真人_2111507074009092098.json
name: Qwen Image2.1动漫转真人_2111507074009092098
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image2.1动漫转真人_2111507074009092098.json
hash: 4d811490ee14ba17
coverage: 0.810526
learned_at: 2026-10-23 11:13:30
nodes: [PrimitiveInt, ManualSigmas, KSamplerSelect, CFGGuider, TextEncodeQwenImage21, UNETLoader, CLIPLoader, VAELoader, QwenImage21Cache, Seed (rgthree), ImageResizeKJv2, RandomNoise, SamplerCustomAdvanced, SamplerCustomAdvanced, RandomNoise, CFGGuider, KSamplerSelect, BasicScheduler, EmptyFlux2LatentImage, VAEEncode, ReferenceLatent, ConditioningZeroOut, GetImageSize, CLIPTextEncode, UNETLoader, CLIPLoader, VAELoader, UNETLoader, VAELoader, PrimitiveFloat, ResizeImageMaskNode, SeedVR2Preprocess, VAEEncodeTiled, SeedVR2Conditioning, SeedVR2PostProcessing, ImageMergeTileList, RH_DLSS5Enhance, VAEDecodeTiled, KSampler, LayerUtility: HLFrequencyDetailRestore, LoraLoaderModelOnly, PrimitiveInt, GetImageSize, ComfyMathExpression, ComfyMathExpression, VAEDecode, SplitImageToTileList, PreviewImage, ComfyMathExpression, ImageBlend, SaveImage, Image Comparer (rgthree), RegexReplace, CLIPLoader, ImageScaleToTotalPixels, StringConcatenate, StringTrim, TextGenerate, StringConcatenate, VOSR2Upscale, RH_DLSS5Enhance, VOSR2ModelLoader, SaveImage, Image Comparer (rgthree), SplitImageWithAlpha, VAEDecode, PreviewImage, Image Comparer (rgthree), LoraLoaderModelOnly, CLIPLoader, VAELoader, Anything Everywhere3, KSampler, ResolutionSelector, VOSR2Upscale, VOSR2ModelLoader, LoadImage, RH_DLSS5Enhance, VAEDecode, UNETLoader, LoadImage, PrimitiveStringMultiline, PrimitiveStringMultiline, Fast Groups Bypasser (rgthree), 孤海注释, MarkdownNote, LoraLoaderModelOnly, MarkdownNote, ComfySwitchNode, EmptyLatentImage, TextEncodeQwenImage21, SaveImage, Image Comparer (rgthree), SaveImage, Image Comparer (rgthree)]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 42, "steps": 10, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image2.1动漫转真人_2111507074009092098.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image2.1动漫转真人_2111507074009092098.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（95 个）：
- `PrimitiveInt`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `Seed (rgthree)`
- `ImageResizeKJv2`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `EmptyFlux2LatentImage`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ConditioningZeroOut`
- `GetImageSize`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `VAELoader`
- `PrimitiveFloat`
- `ResizeImageMaskNode`
- `SeedVR2Preprocess`
- `VAEEncodeTiled` ★核心
- `SeedVR2Conditioning`
- `SeedVR2PostProcessing`
- `ImageMergeTileList`
- `RH_DLSS5Enhance`
- `VAEDecodeTiled` ★核心
- `KSampler` ★核心
- `LayerUtility: HLFrequencyDetailRestore`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveInt`
- `GetImageSize`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `VAEDecode` ★核心
- `SplitImageToTileList`
- `PreviewImage`
- `ComfyMathExpression`
- `ImageBlend`
- `SaveImage`
- `Image Comparer (rgthree)`
- `RegexReplace`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `StringConcatenate`
- `StringTrim`
- `TextGenerate`
- `StringConcatenate`
- `VOSR2Upscale`
- `RH_DLSS5Enhance`
- `VOSR2ModelLoader`
- `SaveImage`
- `Image Comparer (rgthree)`
- `SplitImageWithAlpha`
- `VAEDecode` ★核心
- `PreviewImage`
- `Image Comparer (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `Anything Everywhere3`
- `KSampler` ★核心
- `ResolutionSelector`
- `VOSR2Upscale`
- `VOSR2ModelLoader`
- `LoadImage`
- `RH_DLSS5Enhance`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `Fast Groups Bypasser (rgthree)`
- `孤海注释`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `SaveImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `Image Comparer (rgthree)`

**识别到的模式**：text_to_image、image_to_image

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

覆盖率 **81%**（77/95）

**有卡**：`ManualSigmas`、`KSamplerSelect`、`CFGGuider`、`TextEncodeQwenImage21`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`Seed (rgthree)`、`ImageResizeKJv2`、`RandomNoise`、`SamplerCustomAdvanced`、`BasicScheduler`、`EmptyFlux2LatentImage`、`VAEEncode`、`ReferenceLatent`、`ConditioningZeroOut`、`GetImageSize`、`CLIPTextEncode`、`ResizeImageMaskNode`、`SeedVR2Preprocess`、`VAEEncodeTiled`、`SeedVR2Conditioning`、`SeedVR2PostProcessing`、`ImageMergeTileList`、`RH_DLSS5Enhance`、`VAEDecodeTiled`、`KSampler`、`LayerUtility: HLFrequencyDetailRestore`、`LoraLoaderModelOnly`、`ComfyMathExpression`、`VAEDecode`、`SplitImageToTileList`、`ImageBlend`、`SaveImage`、`RegexReplace`、`ImageScaleToTotalPixels`、`StringConcatenate`、`StringTrim`、`TextGenerate`、`VOSR2Upscale`、`VOSR2ModelLoader`、`SplitImageWithAlpha`、`ResolutionSelector`、`LoadImage`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

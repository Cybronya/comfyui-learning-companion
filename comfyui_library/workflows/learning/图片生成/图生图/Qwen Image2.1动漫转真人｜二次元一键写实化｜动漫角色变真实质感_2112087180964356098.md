---
key: 图片生成/图生图/Qwen Image2.1动漫转真人｜二次元一键写实化｜动漫角色变真实质感_2112087180964356098.json
name: Qwen Image2.1动漫转真人｜二次元一键写实化｜动漫角色变真实质感_2112087180964356098
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image2.1动漫转真人｜二次元一键写实化｜动漫角色变真实质感_2112087180964356098.json
hash: b86ea713c2d48b55
coverage: 0.859259
learned_at: 2026-10-23 11:13:31
nodes: [PrimitiveInt, ManualSigmas, KSamplerSelect, CFGGuider, TextEncodeQwenImage21, UNETLoader, CLIPLoader, VAELoader, QwenImage21Cache, Seed (rgthree), ImageResizeKJv2, RandomNoise, SamplerCustomAdvanced, SamplerCustomAdvanced, RandomNoise, CFGGuider, KSamplerSelect, BasicScheduler, EmptyFlux2LatentImage, VAEEncode, ReferenceLatent, ConditioningZeroOut, GetImageSize, CLIPTextEncode, UNETLoader, CLIPLoader, VAELoader, UNETLoader, VAELoader, PrimitiveFloat, ResizeImageMaskNode, SeedVR2Preprocess, VAEEncodeTiled, SeedVR2Conditioning, SeedVR2PostProcessing, ImageMergeTileList, RH_DLSS5Enhance, VAEDecodeTiled, KSampler, LayerUtility: HLFrequencyDetailRestore, LoraLoaderModelOnly, PrimitiveInt, GetImageSize, ComfyMathExpression, ComfyMathExpression, VAEDecode, SplitImageToTileList, PreviewImage, ComfyMathExpression, ImageBlend, SaveImage, Image Comparer (rgthree), RegexReplace, CLIPLoader, ImageScaleToTotalPixels, StringConcatenate, StringTrim, TextGenerate, StringConcatenate, VOSR2Upscale, RH_DLSS5Enhance, VOSR2ModelLoader, SaveImage, Image Comparer (rgthree), SplitImageWithAlpha, VAEDecode, PreviewImage, Image Comparer (rgthree), LoraLoaderModelOnly, CLIPLoader, VAELoader, Anything Everywhere3, KSampler, ResolutionSelector, VOSR2Upscale, VOSR2ModelLoader, LoadImage, RH_DLSS5Enhance, VAEDecode, UNETLoader, LoadImage, PrimitiveStringMultiline, PrimitiveStringMultiline, Fast Groups Bypasser (rgthree), LoraLoaderModelOnly, ComfySwitchNode, EmptyLatentImage, TextEncodeQwenImage21, SaveImage, Image Comparer (rgthree), SaveImage, Image Comparer (rgthree), 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image2.1动漫转真人｜二次元一键写实化｜动漫角色变真实质感_2112087180964356098.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image2.1动漫转真人｜二次元一键写实化｜动漫角色变真实质感_2112087180964356098.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（135 个）：
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
- `LoraLoaderModelOnly` ★核心
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `SaveImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `Image Comparer (rgthree)`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `CLIPTextEncode` ★核心
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

覆盖率 **86%**（116/135）

**有卡**：`ManualSigmas`、`KSamplerSelect`、`CFGGuider`、`TextEncodeQwenImage21`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`Seed (rgthree)`、`ImageResizeKJv2`、`RandomNoise`、`SamplerCustomAdvanced`、`BasicScheduler`、`EmptyFlux2LatentImage`、`VAEEncode`、`ReferenceLatent`、`ConditioningZeroOut`、`GetImageSize`、`CLIPTextEncode`、`ResizeImageMaskNode`、`SeedVR2Preprocess`、`VAEEncodeTiled`、`SeedVR2Conditioning`、`SeedVR2PostProcessing`、`ImageMergeTileList`、`RH_DLSS5Enhance`、`VAEDecodeTiled`、`KSampler`、`LayerUtility: HLFrequencyDetailRestore`、`LoraLoaderModelOnly`、`ComfyMathExpression`、`VAEDecode`、`SplitImageToTileList`、`ImageBlend`、`SaveImage`、`RegexReplace`、`ImageScaleToTotalPixels`、`StringConcatenate`、`StringTrim`、`TextGenerate`、`VOSR2Upscale`、`VOSR2ModelLoader`、`SplitImageWithAlpha`、`ResolutionSelector`、`LoadImage`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

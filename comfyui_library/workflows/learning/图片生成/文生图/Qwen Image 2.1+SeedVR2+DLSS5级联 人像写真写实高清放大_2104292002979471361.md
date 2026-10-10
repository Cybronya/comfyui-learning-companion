---
key: Qwen Image 2.1+SeedVR2+DLSS5级联 人像写真写实高清放大_2104292002979471361.json
name: Qwen Image 2.1+SeedVR2+DLSS5级联 人像写真写实高清放大_2104292002979471361
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1+SeedVR2+DLSS5级联 人像写真写实高清放大_2104292002979471361.json
hash: 0d0e9740a19d580f
coverage: 0.859155
learned_at: 2026-10-10 20:58:51
nodes: [PrimitiveInt, ComfyMathExpression, SeedVR2Preprocess, VAEEncodeTiled, PrimitiveInt, SeedVR2Conditioning, ComfyMathExpression, ImageMergeTileList, VAEDecodeTiled, ComfyMathExpression, GetImageSize, PrimitiveFloat, KSampler, SeedVR2PostProcessing, SplitImageToTileList, SamplerCustomAdvanced, SamplerCustomAdvanced, CLIPLoader, ResolutionSelector, BasicScheduler, CFGGuider, CFGGuider, KSamplerSelect, EmptyLatentImage, SplitSigmas, RandomNoise, VAEDecode, KSamplerSelect, ImageScale, SaveImageAdvanced, UNETLoader, VAELoader, UNETLoader, VAELoader, Seed (rgthree), ResizeImageMaskNode, LayerUtility: HLFrequencyDetailRestore, TextEncodeQwenImage21, ImageBlend, Image Comparer (rgthree), RH_DLSS5Enhance, SaveImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [LayerUtility: HLFrequencyDetailRestore, Seed (rgthree)]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `LayerUtility: HLFrequencyDetailRestore` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# Qwen Image 2.1+SeedVR2+DLSS5级联 人像写真写实高清放大_2104292002979471361.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1+SeedVR2+DLSS5级联 人像写真写实高清放大_2104292002979471361.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（71 个）：
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
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
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

覆盖率 **86%**（61/71）

**有卡**：`ComfyMathExpression`、`SeedVR2Preprocess`、`VAEEncodeTiled`、`SeedVR2Conditioning`、`ImageMergeTileList`、`VAEDecodeTiled`、`GetImageSize`、`KSampler`、`SeedVR2PostProcessing`、`SplitImageToTileList`、`SamplerCustomAdvanced`、`CLIPLoader`、`ResolutionSelector`、`BasicScheduler`、`CFGGuider`、`KSamplerSelect`、`EmptyLatentImage`、`SplitSigmas`、`RandomNoise`、`VAEDecode`、`ImageScale`、`SaveImageAdvanced`、`UNETLoader`、`VAELoader`、`ResizeImageMaskNode`、`TextEncodeQwenImage21`、`ImageBlend`、`RH_DLSS5Enhance`、`SaveImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**缺卡**（2）：`LayerUtility: HLFrequencyDetailRestore`、`Seed (rgthree)`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: HLFrequencyDetailRestore` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

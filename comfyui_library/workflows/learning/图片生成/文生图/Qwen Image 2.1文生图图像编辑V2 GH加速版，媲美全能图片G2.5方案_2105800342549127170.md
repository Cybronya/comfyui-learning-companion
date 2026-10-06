---
key: 图片生成/文生图/Qwen Image 2.1文生图图像编辑V2 GH加速版，媲美全能图片G2.5方案_2105800342549127170.json
name: Qwen Image 2.1文生图图像编辑V2 GH加速版，媲美全能图片G2.5方案_2105800342549127170
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图图像编辑V2 GH加速版，媲美全能图片G2.5方案_2105800342549127170.json
hash: b9bf6f357eb53f8e
coverage: 0.603774
learned_at: 2026-10-07 02:20:31
nodes: [LoadImage, CLIPLoader, VAELoader, CLIPTextEncode, VAEDecode, CLIPTextEncode, LatentSwitch, VAEEncode, VAELoader, CLIPLoader, ReferenceLatent, ReferenceLatent, KSamplerAdvanced, UNETLoader, ImageScaleToTotalPixels, PDIMAGE_LongerSize, SetNode, JWFloat, LoadImage, LoadImage, SetNode, SetNode, LoadImage, SetNode, SetNode, LoadImage, SetNode, GetNode, SetNode, VAEDecode, KSampler, GetNode, GetNode, GetNode, GetNode, GetNode, UNETLoader, GetNode, SetNode, GetNode, QwenImage21BlockCacheT8, GetNode, QwenImage21SpectrumT8, GoohaiRouteBlocker, TextEncodeQwenImage21GH, SetNode, GetNode, SaveImage, RestoreQwenImage21GH, SetNode, GetNode, GoohaiRouteBlocker, Fast Groups Bypasser (rgthree), SaveImage, QwenImagePromptOptimizer, GetNode, SetNode, GetNode, QwenImage21SageAttentionT8, GetNode, LoadImage, SetNode, FastGroupsBypassSwitch, GetNode, SetNode, CS_Preview_Any, easy showAnything, SetNode, GetNode, ShowText|pysssss, DF_Text_Box, Image Comparer (rgthree), GetNode, GetNode, PreviewImage, PreviewImage, GoohaiRatioAndResolution, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1文生图图像编辑V2 GH加速版，媲美全能图片G2.5方案_2105800342549127170.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图图像编辑V2 GH加速版，媲美全能图片G2.5方案_2105800342549127170.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（106 个）：
- `LoadImage`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LatentSwitch`
- `VAEEncode` ★核心
- `VAELoader`
- `CLIPLoader`
- `ReferenceLatent`
- `ReferenceLatent`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `ImageScaleToTotalPixels`
- `PDIMAGE_LongerSize`
- `SetNode`
- `JWFloat`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `SetNode`
- `LoadImage`
- `SetNode`
- `SetNode`
- `LoadImage`
- `SetNode`
- `GetNode`
- `SetNode`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `UNETLoader` ★核心
- `GetNode`
- `SetNode`
- `GetNode`
- `QwenImage21BlockCacheT8`
- `GetNode`
- `QwenImage21SpectrumT8`
- `GoohaiRouteBlocker`
- `TextEncodeQwenImage21GH`
- `SetNode`
- `GetNode`
- `SaveImage`
- `RestoreQwenImage21GH`
- `SetNode`
- `GetNode`
- `GoohaiRouteBlocker`
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`
- `QwenImagePromptOptimizer`
- `GetNode`
- `SetNode`
- `GetNode`
- `QwenImage21SageAttentionT8`
- `GetNode`
- `LoadImage`
- `SetNode`
- `FastGroupsBypassSwitch`
- `GetNode`
- `SetNode`
- `CS_Preview_Any`
- `easy showAnything`
- `SetNode`
- `GetNode`
- `ShowText|pysssss`
- `DF_Text_Box`
- `Image Comparer (rgthree)`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `PreviewImage`
- `GoohaiRatioAndResolution`
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

覆盖率 **60%**（64/106）

**有卡**：`LoadImage`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`VAEDecode`、`LatentSwitch`、`VAEEncode`、`ReferenceLatent`、`KSamplerAdvanced`、`UNETLoader`、`ImageScaleToTotalPixels`、`PDIMAGE_LongerSize`、`JWFloat`、`KSampler`、`QwenImage21BlockCacheT8`、`QwenImage21SpectrumT8`、`GoohaiRouteBlocker`、`TextEncodeQwenImage21GH`、`SaveImage`、`RestoreQwenImage21GH`、`QwenImagePromptOptimizer`、`QwenImage21SageAttentionT8`、`FastGroupsBypassSwitch`、`CS_Preview_Any`、`DF_Text_Box`、`GoohaiRatioAndResolution`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

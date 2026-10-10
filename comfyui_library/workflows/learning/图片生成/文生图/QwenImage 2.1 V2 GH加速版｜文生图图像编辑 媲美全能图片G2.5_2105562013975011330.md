---
key: QwenImage 2.1 V2 GH加速版｜文生图图像编辑 媲美全能图片G2.5_2105562013975011330.json
name: QwenImage 2.1 V2 GH加速版｜文生图图像编辑 媲美全能图片G2.5_2105562013975011330
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/QwenImage 2.1 V2 GH加速版｜文生图图像编辑 媲美全能图片G2.5_2105562013975011330.json
hash: 05293e76bd6b05f0
coverage: 0.655462
learned_at: 2026-10-10 20:59:07
nodes: [LoadImage, CLIPLoader, VAELoader, CLIPTextEncode, VAEDecode, CLIPTextEncode, LatentSwitch, VAEEncode, VAELoader, CLIPLoader, ReferenceLatent, ReferenceLatent, KSamplerAdvanced, UNETLoader, ImageScaleToTotalPixels, PDIMAGE_LongerSize, SetNode, JWFloat, LoadImage, LoadImage, SetNode, SetNode, LoadImage, SetNode, SetNode, LoadImage, SetNode, GetNode, SetNode, VAEDecode, KSampler, GetNode, GetNode, GetNode, GetNode, GetNode, UNETLoader, GetNode, SetNode, GetNode, QwenImage21BlockCacheT8, GetNode, QwenImage21SpectrumT8, GoohaiRouteBlocker, TextEncodeQwenImage21GH, SetNode, GetNode, SaveImage, RestoreQwenImage21GH, SetNode, GetNode, GoohaiRouteBlocker, Fast Groups Bypasser (rgthree), SaveImage, QwenImagePromptOptimizer, GetNode, SetNode, QwenImage21SageAttentionT8, GetNode, LoadImage, SetNode, FastGroupsBypassSwitch, GetNode, SetNode, CS_Preview_Any, easy showAnything, SetNode, GetNode, ShowText|pysssss, DF_Text_Box, Image Comparer (rgthree), GetNode, GetNode, PreviewImage, PreviewImage, GoohaiRatioAndResolution, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# QwenImage 2.1 V2 GH加速版｜文生图图像编辑 媲美全能图片G2.5_2105562013975011330.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/QwenImage 2.1 V2 GH加速版｜文生图图像编辑 媲美全能图片G2.5_2105562013975011330.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（119 个）：
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

覆盖率 **66%**（78/119）

**有卡**：`LoadImage`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`VAEDecode`、`LatentSwitch`、`VAEEncode`、`ReferenceLatent`、`KSamplerAdvanced`、`UNETLoader`、`ImageScaleToTotalPixels`、`PDIMAGE_LongerSize`、`JWFloat`、`KSampler`、`QwenImage21BlockCacheT8`、`QwenImage21SpectrumT8`、`GoohaiRouteBlocker`、`TextEncodeQwenImage21GH`、`SaveImage`、`RestoreQwenImage21GH`、`QwenImagePromptOptimizer`、`QwenImage21SageAttentionT8`、`FastGroupsBypassSwitch`、`CS_Preview_Any`、`DF_Text_Box`、`GoohaiRatioAndResolution`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

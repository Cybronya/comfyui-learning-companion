---
key: 图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5图像反推｜反推提示词高清放大｜三模型强强联合_2112113920214388737.json
name: Qwen-image2.1+Vosr2+DLSS5图像反推｜反推提示词高清放大｜三模型强强联合_2112113920214388737
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5图像反推｜反推提示词高清放大｜三模型强强联合_2112113920214388737.json
hash: dd548540e2c4fc0c
coverage: 0.888889
learned_at: 2026-10-23 11:18:21
nodes: [CLIPLoader, QwenImage21SageAttentionT8, ManualSigmas, VAELoader, RH_Screenwriter, easy showAnything, SaveImage, VAEDecode, ClownsharKSampler_Beta, PrimitiveStringMultiline, UNETLoader, LoadImage, WujiUpscaler2, TextEncodeQwenImage21, Image Comparer (rgthree), WujiPromptEditor, WujiImagePrompt, easy imageSize, EmptyLatentImage, ImageScaleToTotalPixels, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5图像反推｜反推提示词高清放大｜三模型强强联合_2112113920214388737.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5图像反推｜反推提示词高清放大｜三模型强强联合_2112113920214388737.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（63 个）：
- `CLIPLoader`
- `QwenImage21SageAttentionT8`
- `ManualSigmas`
- `VAELoader`
- `RH_Screenwriter`
- `easy showAnything`
- `SaveImage`
- `VAEDecode` ★核心
- `ClownsharKSampler_Beta` ★核心
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `LoadImage`
- `WujiUpscaler2`
- `TextEncodeQwenImage21`
- `Image Comparer (rgthree)`
- `WujiPromptEditor`
- `WujiImagePrompt`
- `easy imageSize`
- `EmptyLatentImage` ★核心
- `ImageScaleToTotalPixels`
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

覆盖率 **89%**（56/63）

**有卡**：`CLIPLoader`、`QwenImage21SageAttentionT8`、`ManualSigmas`、`VAELoader`、`RH_Screenwriter`、`SaveImage`、`VAEDecode`、`ClownsharKSampler_Beta`、`UNETLoader`、`LoadImage`、`WujiUpscaler2`、`TextEncodeQwenImage21`、`WujiPromptEditor`、`WujiImagePrompt`、`easy imageSize`、`EmptyLatentImage`、`ImageScaleToTotalPixels`、`CLIPTextEncode`、`KSampler`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

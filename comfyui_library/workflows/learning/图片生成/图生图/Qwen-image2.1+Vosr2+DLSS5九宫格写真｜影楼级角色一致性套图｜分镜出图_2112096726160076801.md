---
key: 图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5九宫格写真｜影楼级角色一致性套图｜分镜出图_2112096726160076801.json
name: Qwen-image2.1+Vosr2+DLSS5九宫格写真｜影楼级角色一致性套图｜分镜出图_2112096726160076801
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5九宫格写真｜影楼级角色一致性套图｜分镜出图_2112096726160076801.json
hash: b51937bd385cf71d
coverage: 0.887097
learned_at: 2026-10-23 11:18:21
nodes: [ManualSigmas, RH_Screenwriter, easy showAnything, ClownsharKSampler_Beta, WujiUpscaler2, PrimitiveStringMultiline, LoadImage, UNETLoader, CLIPLoader, VAELoader, ImageScaleToTotalPixels, QwenImage21SageAttentionT8, TextEncodeQwenImage21, AutoCropFaces, WujiPromptEditor, SaveImage, VAEDecode, PreviewImage, WujiImagePrompt, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5九宫格写真｜影楼级角色一致性套图｜分镜出图_2112096726160076801.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5九宫格写真｜影楼级角色一致性套图｜分镜出图_2112096726160076801.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（62 个）：
- `ManualSigmas`
- `RH_Screenwriter`
- `easy showAnything`
- `ClownsharKSampler_Beta` ★核心
- `WujiUpscaler2`
- `PrimitiveStringMultiline`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ImageScaleToTotalPixels`
- `QwenImage21SageAttentionT8`
- `TextEncodeQwenImage21`
- `AutoCropFaces`
- `WujiPromptEditor`
- `SaveImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `WujiImagePrompt`
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

覆盖率 **89%**（55/62）

**有卡**：`ManualSigmas`、`RH_Screenwriter`、`ClownsharKSampler_Beta`、`WujiUpscaler2`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ImageScaleToTotalPixels`、`QwenImage21SageAttentionT8`、`TextEncodeQwenImage21`、`AutoCropFaces`、`WujiPromptEditor`、`SaveImage`、`VAEDecode`、`WujiImagePrompt`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

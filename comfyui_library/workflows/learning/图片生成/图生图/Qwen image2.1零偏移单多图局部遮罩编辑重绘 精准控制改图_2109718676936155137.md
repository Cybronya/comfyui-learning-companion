---
key: 图片生成/图生图/Qwen image2.1零偏移单多图局部遮罩编辑重绘 精准控制改图_2109718676936155137.json
name: Qwen image2.1零偏移单多图局部遮罩编辑重绘 精准控制改图_2109718676936155137
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image2.1零偏移单多图局部遮罩编辑重绘 精准控制改图_2109718676936155137.json
hash: c785f31b067ec9ec
coverage: 0.87234
learned_at: 2026-10-23 11:14:26
nodes: [VAELoader, Image Comparer (rgthree), SaveImage, VAEDecode, WujiCleaner, CLIPLoader, LoadImage, PrimitiveStringMultiline, UNETLoader, LoadImage, WujiUpscaler2, QwenImage21SageAttentionT8, QwenImage21EditTextEncode_EditUtils, ConditioningZeroOut, WujiImagePrompt, RH_Screenwriter, ManualSigmas, ClownsharKSampler_Beta, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen image2.1零偏移单多图局部遮罩编辑重绘 精准控制改图_2109718676936155137.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image2.1零偏移单多图局部遮罩编辑重绘 精准控制改图_2109718676936155137.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `VAELoader`
- `Image Comparer (rgthree)`
- `SaveImage`
- `VAEDecode` ★核心
- `WujiCleaner`
- `CLIPLoader`
- `LoadImage`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `LoadImage`
- `WujiUpscaler2`
- `QwenImage21SageAttentionT8`
- `QwenImage21EditTextEncode_EditUtils`
- `ConditioningZeroOut`
- `WujiImagePrompt`
- `RH_Screenwriter`
- `ManualSigmas`
- `ClownsharKSampler_Beta` ★核心
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
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
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

覆盖率 **87%**（41/47）

**有卡**：`VAELoader`、`SaveImage`、`VAEDecode`、`WujiCleaner`、`CLIPLoader`、`LoadImage`、`UNETLoader`、`WujiUpscaler2`、`QwenImage21SageAttentionT8`、`QwenImage21EditTextEncode_EditUtils`、`ConditioningZeroOut`、`WujiImagePrompt`、`RH_Screenwriter`、`ManualSigmas`、`ClownsharKSampler_Beta`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

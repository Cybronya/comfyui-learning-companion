---
key: 图片生成/图生图/Qwen Image 2.1图像编辑接超分放大工作流，图生图高清修复方案_2103976463702781954.json
name: Qwen Image 2.1图像编辑接超分放大工作流，图生图高清修复方案_2103976463702781954
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1图像编辑接超分放大工作流，图生图高清修复方案_2103976463702781954.json
hash: 6550d7bd5df0eebc
coverage: 0.86
learned_at: 2026-10-21 00:42:29
nodes: [ComfySwitchNode, CM_IntToFloat, ImageScaleToTotalPixels, CLIPLoader, VAELoader, VAEDecode, QwenImage21BlockCacheT8, QwenImage21SpectrumT8, UNETLoader, LoadImage, LoadImage, KSampler, ResolutionSelector, EmptyLatentImage, QwenImage21Cache, LoadImage, SaveImage, QwenImage21SageAttentionT8, TextEncodeQwenImage21, PrimitiveInt, PrimitiveInt, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1图像编辑接超分放大工作流，图生图高清修复方案_2103976463702781954.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1图像编辑接超分放大工作流，图生图高清修复方案_2103976463702781954.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `ComfySwitchNode`
- `CM_IntToFloat`
- `ImageScaleToTotalPixels`
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `QwenImage21BlockCacheT8`
- `QwenImage21SpectrumT8`
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `KSampler` ★核心
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `QwenImage21Cache`
- `LoadImage`
- `SaveImage`
- `QwenImage21SageAttentionT8`
- `TextEncodeQwenImage21`
- `PrimitiveInt`
- `PrimitiveInt`
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

覆盖率 **86%**（43/50）

**有卡**：`CM_IntToFloat`、`ImageScaleToTotalPixels`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`QwenImage21BlockCacheT8`、`QwenImage21SpectrumT8`、`UNETLoader`、`LoadImage`、`KSampler`、`ResolutionSelector`、`EmptyLatentImage`、`QwenImage21Cache`、`SaveImage`、`QwenImage21SageAttentionT8`、`TextEncodeQwenImage21`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

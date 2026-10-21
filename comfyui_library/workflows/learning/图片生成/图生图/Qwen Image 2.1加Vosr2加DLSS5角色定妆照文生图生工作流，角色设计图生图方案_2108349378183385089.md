---
key: 图片生成/图生图/Qwen Image 2.1加Vosr2加DLSS5角色定妆照文生图生工作流，角色设计图生图方案_2108349378183385089.json
name: Qwen Image 2.1加Vosr2加DLSS5角色定妆照文生图生工作流，角色设计图生图方案_2108349378183385089
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1加Vosr2加DLSS5角色定妆照文生图生工作流，角色设计图生图方案_2108349378183385089.json
hash: d016c5987af17068
coverage: 0.863636
learned_at: 2026-10-21 00:42:21
nodes: [CLIPLoader, VAELoader, PrimitiveStringMultiline, UNETLoader, EmptyLatentImage, ClownsharKSampler_Beta, SaveImage, ResolutionSelector, LoadImage, Fast Groups Bypasser (rgthree), RH_LLMAPI_NODE, TextEncodeQwenImage21, VAEDecode, WujiCleaner, WujiUpscaler2, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1加Vosr2加DLSS5角色定妆照文生图生工作流，角色设计图生图方案_2108349378183385089.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1加Vosr2加DLSS5角色定妆照文生图生工作流，角色设计图生图方案_2108349378183385089.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `CLIPLoader`
- `VAELoader`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `ClownsharKSampler_Beta` ★核心
- `SaveImage`
- `ResolutionSelector`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `RH_LLMAPI_NODE`
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `WujiCleaner`
- `WujiUpscaler2`
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

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **86%**（38/44）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`EmptyLatentImage`、`ClownsharKSampler_Beta`、`SaveImage`、`ResolutionSelector`、`LoadImage`、`RH_LLMAPI_NODE`、`TextEncodeQwenImage21`、`VAEDecode`、`WujiCleaner`、`WujiUpscaler2`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

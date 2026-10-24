---
key: 图片生成/图生图/Qwen-image2.1加Vosr2加DLSS5，角色定妆照文生图图生图_2111522943825174530.json
name: Qwen-image2.1加Vosr2加DLSS5，角色定妆照文生图图生图_2111522943825174530
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1加Vosr2加DLSS5，角色定妆照文生图图生图_2111522943825174530.json
hash: 7b539c424000133c
coverage: 0.866667
learned_at: 2026-10-23 11:18:30
nodes: [CLIPLoader, QwenImage21SageAttentionT8, ManualSigmas, LoadImage, TextEncodeQwenImage21, VAELoader, RH_Screenwriter, easy showAnything, SaveImage, VAEDecode, WujiImagePrompt, ClownsharKSampler_Beta, PrimitiveStringMultiline, WujiPromptEditor, UNETLoader, WujiUpscaler2, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-image2.1加Vosr2加DLSS5，角色定妆照文生图图生图_2111522943825174530.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1加Vosr2加DLSS5，角色定妆照文生图图生图_2111522943825174530.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `CLIPLoader`
- `QwenImage21SageAttentionT8`
- `ManualSigmas`
- `LoadImage`
- `TextEncodeQwenImage21`
- `VAELoader`
- `RH_Screenwriter`
- `easy showAnything`
- `SaveImage`
- `VAEDecode` ★核心
- `WujiImagePrompt`
- `ClownsharKSampler_Beta` ★核心
- `PrimitiveStringMultiline`
- `WujiPromptEditor`
- `UNETLoader` ★核心
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

覆盖率 **87%**（39/45）

**有卡**：`CLIPLoader`、`QwenImage21SageAttentionT8`、`ManualSigmas`、`LoadImage`、`TextEncodeQwenImage21`、`VAELoader`、`RH_Screenwriter`、`SaveImage`、`VAEDecode`、`WujiImagePrompt`、`ClownsharKSampler_Beta`、`WujiPromptEditor`、`UNETLoader`、`WujiUpscaler2`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

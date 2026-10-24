---
key: 图片生成/图生图/分镜专用空镜有人无人两版，Qwein-image2.1场景道具出图_2112343437294002177.json
name: 分镜专用空镜有人无人两版，Qwein-image2.1场景道具出图_2112343437294002177
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/分镜专用空镜有人无人两版，Qwein-image2.1场景道具出图_2112343437294002177.json
hash: f5c4257b97e2106d
coverage: 0.847826
learned_at: 2026-10-23 12:22:43
nodes: [ManualSigmas, RH_Screenwriter, easy showAnything, ClownsharKSampler_Beta, WujiUpscaler2, UNETLoader, CLIPLoader, VAELoader, QwenImage21SageAttentionT8, SaveImage, VAEDecode, PreviewImage, TextEncodeQwenImage21, LoadImage, WujiImagePrompt, WujiPromptEditor, PrimitiveStringMultiline, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/分镜专用空镜有人无人两版，Qwein-image2.1场景道具出图_2112343437294002177.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/分镜专用空镜有人无人两版，Qwein-image2.1场景道具出图_2112343437294002177.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `ManualSigmas`
- `RH_Screenwriter`
- `easy showAnything`
- `ClownsharKSampler_Beta` ★核心
- `WujiUpscaler2`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `QwenImage21SageAttentionT8`
- `SaveImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `TextEncodeQwenImage21`
- `LoadImage`
- `WujiImagePrompt`
- `WujiPromptEditor`
- `PrimitiveStringMultiline`
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

覆盖率 **85%**（39/46）

**有卡**：`ManualSigmas`、`RH_Screenwriter`、`ClownsharKSampler_Beta`、`WujiUpscaler2`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`QwenImage21SageAttentionT8`、`SaveImage`、`VAEDecode`、`TextEncodeQwenImage21`、`LoadImage`、`WujiImagePrompt`、`WujiPromptEditor`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

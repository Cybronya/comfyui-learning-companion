---
key: 图片生成/文生图/Z-image-turbo 2.5D奶油风格生图Lora_2055258113829294081.json
name: Z-image-turbo 2.5D奶油风格生图Lora_2055258113829294081
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image-turbo 2.5D奶油风格生图Lora_2055258113829294081.json
hash: f2b47d83c85b2fae
coverage: 1
learned_at: 2026-10-21 02:56:15
nodes: [CLIPLoader, KSampler, VAEDecode, SaveImage, UNETLoader, EmptyLatentImage, RTXVideoSuperResolution, VAELoader, ConditioningZeroOut, CLIPTextEncode, LoraLoaderModelOnly]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 750478499103380, "steps": 8, "width": 1080}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z-image-turbo 2.5D奶油风格生图Lora_2055258113829294081.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image-turbo 2.5D奶油风格生图Lora_2055258113829294081.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（11 个）：
- `CLIPLoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `RTXVideoSuperResolution`
- `VAELoader`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `750478499103380`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`CLIPLoader`、`KSampler`、`VAEDecode`、`SaveImage`、`UNETLoader`、`EmptyLatentImage`、`RTXVideoSuperResolution`、`VAELoader`、`ConditioningZeroOut`、`CLIPTextEncode`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

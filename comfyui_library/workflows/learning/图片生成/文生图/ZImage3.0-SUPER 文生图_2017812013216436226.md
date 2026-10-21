---
key: 图片生成/文生图/ZImage3.0-SUPER 文生图_2017812013216436226.json
name: ZImage3.0-SUPER 文生图_2017812013216436226
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/ZImage3.0-SUPER 文生图_2017812013216436226.json
hash: 859508a791469ee3
coverage: 0.846154
learned_at: 2026-10-19 22:15:36
nodes: [VAELoader, VAEDecode, PrimitiveInt, ConditioningZeroOut, EmptyLatentImage, CLIPLoader, KSampler, SaveImage, LoraLoader, PrimitiveInt, UNETLoader, LoraLoader, CLIPTextEncode]
patterns: [text_to_image, lora]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "lora_name": "redcraftRedzimageUpdatedDEC03_redzimage15AIO.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 1039719160517277, "steps": 30, "strength_clip": 1, "strength_model": 0.6000000000000001, "width": 1080}
---

# 图片生成/文生图/ZImage3.0-SUPER 文生图_2017812013216436226.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/ZImage3.0-SUPER 文生图_2017812013216436226.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
- `VAELoader`
- `VAEDecode` ★核心
- `PrimitiveInt`
- `ConditioningZeroOut`
- `EmptyLatentImage` ★核心
- `CLIPLoader`
- `KSampler` ★核心
- `SaveImage`
- `LoraLoader` ★核心
- `PrimitiveInt`
- `UNETLoader` ★核心
- `LoraLoader` ★核心
- `CLIPTextEncode` ★核心

**识别到的模式**：text_to_image、lora

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `1039719160517277`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `lora_name` = `redcraftRedzimageUpdatedDEC03_redzimage15AIO.safetensors`
- `strength_model` = `0.6000000000000001`
- `strength_clip` = `1`

## 知识

覆盖率 **85%**（11/13）

**有卡**：`VAELoader`、`VAEDecode`、`ConditioningZeroOut`、`EmptyLatentImage`、`CLIPLoader`、`KSampler`、`SaveImage`、`LoraLoader`、`UNETLoader`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、UNETLoader

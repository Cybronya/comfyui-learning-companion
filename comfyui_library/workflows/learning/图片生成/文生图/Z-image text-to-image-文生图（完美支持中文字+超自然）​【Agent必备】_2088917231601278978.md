---
key: 图片生成/文生图/Z-image text-to-image-文生图（完美支持中文字+超自然）​【Agent必备】_2088917231601278978.json
name: Z-image text-to-image-文生图（完美支持中文字+超自然）​【Agent必备】_2088917231601278978
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image text-to-image-文生图（完美支持中文字+超自然）​【Agent必备】_2088917231601278978.json
hash: 70e92901f9f55a82
coverage: 0.846154
learned_at: 2026-10-20 00:59:43
nodes: [VAELoader, ConditioningZeroOut, KSampler, CLIPLoader, UNETLoader, VAEDecode, SetNode, GetNode, CLIPTextEncode, easy promptLine, SaveImage, CR Prompt Text, EmptyLatentImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1080, "sampler_name": "euler", "scheduler": "simple", "seed": 1060454432766293, "steps": 10, "width": 1920}
---

# 图片生成/文生图/Z-image text-to-image-文生图（完美支持中文字+超自然）​【Agent必备】_2088917231601278978.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image text-to-image-文生图（完美支持中文字+超自然）​【Agent必备】_2088917231601278978.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
- `VAELoader`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `easy promptLine`
- `SaveImage`
- `CR Prompt Text`
- `EmptyLatentImage` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `1060454432766293`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（11/13）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`KSampler`、`CLIPLoader`、`UNETLoader`、`VAEDecode`、`CLIPTextEncode`、`easy promptLine`、`SaveImage`、`CR Prompt Text`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、UNETLoader

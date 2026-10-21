---
key: 图片生成/文生图/Boogu-Image Turbo 文生图 VS Zimage-turbo_2069035083775963138.json
name: Boogu-Image Turbo 文生图 VS Zimage-turbo_2069035083775963138
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Boogu-Image Turbo 文生图 VS Zimage-turbo_2069035083775963138.json
hash: 9a2233ee1d441bc1
coverage: 0.809524
learned_at: 2026-10-19 23:21:17
nodes: [KSampler, VAEDecode, VAELoader, CLIPLoader, VAELoader, CLIPTextEncode, EmptyLatentImage, PrimitiveStringMultiline, CLIPTextEncode, KSampler, VAEDecode, ConditioningZeroOut, SaveImage, UNETLoader, PrimitiveStringMultiline, PrimitiveStringMultiline, ConditioningZeroOut, UNETLoader, CLIPLoader, PrimitiveStringMultiline, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 8, "width": 1080}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Boogu-Image Turbo 文生图 VS Zimage-turbo_2069035083775963138.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Boogu-Image Turbo 文生图 VS Zimage-turbo_2069035083775963138.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（21 个）：
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `PrimitiveStringMultiline`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `SaveImage`
- `UNETLoader` ★核心
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `0`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（17/21）

**有卡**：`KSampler`、`VAEDecode`、`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`EmptyLatentImage`、`ConditioningZeroOut`、`SaveImage`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

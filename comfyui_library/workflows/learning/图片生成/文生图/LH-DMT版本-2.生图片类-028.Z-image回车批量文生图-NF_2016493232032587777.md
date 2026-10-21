---
key: 图片生成/文生图/LH-DMT版本-2.生图片类-028.Z-image回车批量文生图-NF_2016493232032587777.json
name: LH-DMT版本-2.生图片类-028.Z-image回车批量文生图-NF_2016493232032587777
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/LH-DMT版本-2.生图片类-028.Z-image回车批量文生图-NF_2016493232032587777.json
hash: d93d2be652941795
coverage: 1
learned_at: 2026-10-19 22:15:12
nodes: [SaveImage, SaveImage, SaveImage, SaveImage, SaveImage, CLIPTextEncode, ConditioningZeroOut, UNETLoader, CLIPLoader, VAELoader, SaveImage, VAEDecode, KSampler, EmptyLatentImage, easy promptLine]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 720, "sampler_name": "euler", "scheduler": "simple", "seed": 367992813548700, "steps": 9, "width": 1280}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/LH-DMT版本-2.生图片类-028.Z-image回车批量文生图-NF_2016493232032587777.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/LH-DMT版本-2.生图片类-028.Z-image回车批量文生图-NF_2016493232032587777.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `SaveImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `easy promptLine`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `367992813548700`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1280`
- `height` = `720`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`SaveImage`、`CLIPTextEncode`、`ConditioningZeroOut`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`KSampler`、`EmptyLatentImage`、`easy promptLine`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

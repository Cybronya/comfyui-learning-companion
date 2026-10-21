---
key: 图片生成/文生图/LH-DMT版本-2.生图片类-027.Z-Image五列表文生图-NF_2016493212516487169.json
name: LH-DMT版本-2.生图片类-027.Z-Image五列表文生图-NF_2016493212516487169
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/LH-DMT版本-2.生图片类-027.Z-Image五列表文生图-NF_2016493212516487169.json
hash: 5c697b3cbdae7e69
coverage: 1
learned_at: 2026-10-19 22:15:12
nodes: [SaveImage, SaveImage, SaveImage, SaveImage, SaveImage, EmptyLatentImage, CLIPTextEncode, ConditioningZeroOut, UNETLoader, CLIPLoader, SaveImage, KSampler, VAEDecode, VAELoader, easy promptList]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "simple", "seed": 583975368780636, "steps": 9, "width": 720}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/LH-DMT版本-2.生图片类-027.Z-Image五列表文生图-NF_2016493212516487169.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/LH-DMT版本-2.生图片类-027.Z-Image五列表文生图-NF_2016493212516487169.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `CLIPLoader`
- `SaveImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `easy promptList`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `720`
- `height` = `1280`
- `batch_size` = `1`
- `seed` = `583975368780636`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`SaveImage`、`EmptyLatentImage`、`CLIPTextEncode`、`ConditioningZeroOut`、`UNETLoader`、`CLIPLoader`、`KSampler`、`VAEDecode`、`VAELoader`、`easy promptList`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

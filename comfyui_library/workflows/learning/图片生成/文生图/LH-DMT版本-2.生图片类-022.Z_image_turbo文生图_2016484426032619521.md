---
key: 图片生成/文生图/LH-DMT版本-2.生图片类-022.Z_image_turbo文生图_2016484426032619521.json
name: LH-DMT版本-2.生图片类-022.Z_image_turbo文生图_2016484426032619521
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/LH-DMT版本-2.生图片类-022.Z_image_turbo文生图_2016484426032619521.json
hash: ea4866eef2cb4033
coverage: 1
learned_at: 2026-10-19 22:15:12
nodes: [UNETLoader, VAELoader, CLIPLoader, ModelSamplingAuraFlow, CLIPTextEncode, VAEDecode, SaveImage, CLIPTextEncode, KSampler, EmptySD3LatentImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 896894967658967, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/LH-DMT版本-2.生图片类-022.Z_image_turbo文生图_2016484426032619521.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/LH-DMT版本-2.生图片类-022.Z_image_turbo文生图_2016484426032619521.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（10 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `EmptySD3LatentImage`

## 关键参数

- `seed` = `896894967658967`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`UNETLoader`、`VAELoader`、`CLIPLoader`、`ModelSamplingAuraFlow`、`CLIPTextEncode`、`VAEDecode`、`SaveImage`、`KSampler`、`EmptySD3LatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、SaveImage、EmptySD3LatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

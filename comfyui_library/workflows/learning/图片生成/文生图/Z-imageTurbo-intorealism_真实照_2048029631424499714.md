---
key: 图片生成/文生图/Z-imageTurbo-intorealism_真实照_2048029631424499714.json
name: Z-imageTurbo-intorealism_真实照_2048029631424499714
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-imageTurbo-intorealism_真实照_2048029631424499714.json
hash: 8da02fc400ecd73f
coverage: 0.916667
learned_at: 2026-10-21 02:56:17
nodes: [CLIPTextEncode, EmptySD3LatentImage, ModelSamplingAuraFlow, VAEDecode, SaveImage, CLIPTextEncode, CLIPLoader, VAELoader, SDXLAspectRatio, UNETLoader, Note, KSampler]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 952626267570175, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z-imageTurbo-intorealism_真实照_2048029631424499714.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-imageTurbo-intorealism_真实照_2048029631424499714.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（12 个）：
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `SDXLAspectRatio`
- `UNETLoader` ★核心
- `Note`
- `KSampler` ★核心

## 关键参数

- `seed` = `952626267570175`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **92%**（11/12）

**有卡**：`CLIPTextEncode`、`EmptySD3LatentImage`、`ModelSamplingAuraFlow`、`VAEDecode`、`SaveImage`、`CLIPLoader`、`VAELoader`、`SDXLAspectRatio`、`UNETLoader`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、SDXLAspectRatio、SaveImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

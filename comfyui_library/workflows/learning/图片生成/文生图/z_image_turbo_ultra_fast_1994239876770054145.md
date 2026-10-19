---
key: 图片生成/文生图/z_image_turbo_ultra_fast_1994239876770054145.json
name: z_image_turbo_ultra_fast_1994239876770054145
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/z_image_turbo_ultra_fast_1994239876770054145.json
hash: 819e5ea6e668a4e8
coverage: 0.909091
learned_at: 2026-10-19 21:33:18
nodes: [VAEDecode, Note, CLIPTextEncode, ModelSamplingAuraFlow, SaveImage, UNETLoader, CLIPLoader, VAELoader, CLIPTextEncode, KSampler, EmptySD3LatentImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 194035357035711, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/z_image_turbo_ultra_fast_1994239876770054145.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/z_image_turbo_ultra_fast_1994239876770054145.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（11 个）：
- `VAEDecode` ★核心
- `Note`
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `EmptySD3LatentImage`

## 关键参数

- `seed` = `194035357035711`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`VAEDecode`、`CLIPTextEncode`、`ModelSamplingAuraFlow`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`EmptySD3LatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、SaveImage、EmptySD3LatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

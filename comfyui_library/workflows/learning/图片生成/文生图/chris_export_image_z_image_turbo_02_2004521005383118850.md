---
key: 图片生成/文生图/chris_export_image_z_image_turbo_02_2004521005383118850.json
name: chris_export_image_z_image_turbo_02_2004521005383118850
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/chris_export_image_z_image_turbo_02_2004521005383118850.json
hash: 7641b8465b49777d
coverage: 0.909091
learned_at: 2026-10-19 21:47:15
nodes: [CLIPLoader, VAELoader, ConditioningZeroOut, UNETLoader, SaveImage, KSampler, VAEDecode, ModelSamplingAuraFlow, MarkdownNote, EmptySD3LatentImage, CLIPTextEncode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 215365327313290, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/chris_export_image_z_image_turbo_02_2004521005383118850.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/chris_export_image_z_image_turbo_02_2004521005383118850.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（11 个）：
- `CLIPLoader`
- `VAELoader`
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `SaveImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ModelSamplingAuraFlow`
- `MarkdownNote`
- `EmptySD3LatentImage`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `215365327313290`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`CLIPLoader`、`VAELoader`、`ConditioningZeroOut`、`UNETLoader`、`SaveImage`、`KSampler`、`VAEDecode`、`ModelSamplingAuraFlow`、`EmptySD3LatentImage`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、UNETLoader、SaveImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

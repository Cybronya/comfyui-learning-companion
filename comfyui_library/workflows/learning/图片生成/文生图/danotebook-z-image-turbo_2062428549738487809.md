---
key: 图片生成/文生图/danotebook-z-image-turbo_2062428549738487809.json
name: danotebook-z-image-turbo_2062428549738487809
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/danotebook-z-image-turbo_2062428549738487809.json
hash: 8b3e9340c04c65e9
coverage: 1
learned_at: 2026-10-19 23:03:08
nodes: [CLIPLoader, VAELoader, ConditioningZeroOut, VAEDecode, UNETLoader, CLIPTextEncode, EmptySD3LatentImage, ModelSamplingAuraFlow, KSampler, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 182604670673750, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/danotebook-z-image-turbo_2062428549738487809.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/danotebook-z-image-turbo_2062428549738487809.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（10 个）：
- `CLIPLoader`
- `VAELoader`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `SaveImage`

## 关键参数

- `seed` = `182604670673750`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`CLIPLoader`、`VAELoader`、`ConditioningZeroOut`、`VAEDecode`、`UNETLoader`、`CLIPTextEncode`、`EmptySD3LatentImage`、`ModelSamplingAuraFlow`、`KSampler`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、UNETLoader、SaveImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

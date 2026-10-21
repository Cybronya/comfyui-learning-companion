---
key: 图片生成/文生图/Z-Image-Turbo with Low VRAM(4-6 GB)_2075074765303410689.json
name: Z-Image-Turbo with Low VRAM(4-6 GB)_2075074765303410689
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image-Turbo with Low VRAM(4-6 GB)_2075074765303410689.json
hash: 5eba0e343d7b407a
coverage: 0.875
learned_at: 2026-10-20 00:20:15
nodes: [ConditioningZeroOut, EmptySD3LatentImage, Note, Note, SaveImage, VAELoader, KSampler, VAEDecode, ModelSamplingAuraFlow, VAEDecodeTiled, UNETLoader, CLIPTextEncode, CLIPLoader, UnetLoaderGGUF, LoadImage, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 37641644419391, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z-Image-Turbo with Low VRAM(4-6 GB)_2075074765303410689.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image-Turbo with Low VRAM(4-6 GB)_2075074765303410689.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `Note`
- `Note`
- `SaveImage`
- `VAELoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ModelSamplingAuraFlow`
- `VAEDecodeTiled` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `UnetLoaderGGUF` ★核心
- `LoadImage`
- `SaveImage`

## 关键参数

- `seed` = `37641644419391`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（14/16）

**有卡**：`ConditioningZeroOut`、`EmptySD3LatentImage`、`SaveImage`、`VAELoader`、`KSampler`、`VAEDecode`、`ModelSamplingAuraFlow`、`VAEDecodeTiled`、`UNETLoader`、`CLIPTextEncode`、`CLIPLoader`、`UnetLoaderGGUF`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

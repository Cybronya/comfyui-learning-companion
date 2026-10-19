---
key: 图片生成/文生图/Y-Z-Image-turbo+lenovo lora-workflow_1995640202892861441.json
name: Y-Z-Image-turbo+lenovo lora-workflow_1995640202892861441
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Y-Z-Image-turbo+lenovo lora-workflow_1995640202892861441.json
hash: fe49eb123f141be2
coverage: 0.928571
learned_at: 2026-10-19 21:32:45
nodes: [ConditioningZeroOut, VAEDecode, SaveImage, CLIPLoader, EmptySD3LatentImage, UNETLoader, easy cleanGpuUsed, ModelSamplingAuraFlow, VAELoader, SDXLAspectRatio, LoraLoaderModelOnly, CLIPTextEncode, Note, KSampler]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 958888370722868, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Y-Z-Image-turbo+lenovo lora-workflow_1995640202892861441.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Y-Z-Image-turbo+lenovo lora-workflow_1995640202892861441.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPLoader`
- `EmptySD3LatentImage`
- `UNETLoader` ★核心
- `easy cleanGpuUsed`
- `ModelSamplingAuraFlow`
- `VAELoader`
- `SDXLAspectRatio`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `KSampler` ★核心

## 关键参数

- `seed` = `958888370722868`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`ConditioningZeroOut`、`VAEDecode`、`SaveImage`、`CLIPLoader`、`EmptySD3LatentImage`、`UNETLoader`、`easy cleanGpuUsed`、`ModelSamplingAuraFlow`、`VAELoader`、`SDXLAspectRatio`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

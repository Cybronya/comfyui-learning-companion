---
key: 图片生成/文生图/Z-image-超现实模型3.0_2021938613541412866.json
name: Z-image-超现实模型3.0_2021938613541412866
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image-超现实模型3.0_2021938613541412866.json
hash: dc7980e377342e9e
coverage: 1
learned_at: 2026-10-19 22:30:05
nodes: [CLIPLoader, VAELoader, ConditioningZeroOut, SaveImage, ModelSamplingAuraFlow, LoraLoaderModelOnly, CLIPTextEncode, VAEDecode, UNETLoader, KSampler, EmptySD3LatentImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 407794064076405, "steps": 15}
---

# 图片生成/文生图/Z-image-超现实模型3.0_2021938613541412866.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image-超现实模型3.0_2021938613541412866.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（11 个）：
- `CLIPLoader`
- `VAELoader`
- `ConditioningZeroOut`
- `SaveImage`
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `EmptySD3LatentImage`

## 关键参数

- `seed` = `407794064076405`
- `steps` = `15`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`CLIPLoader`、`VAELoader`、`ConditioningZeroOut`、`SaveImage`、`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`VAEDecode`、`UNETLoader`、`KSampler`、`EmptySD3LatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、UNETLoader

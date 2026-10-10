---
key: sd3.5_large Turbo版 官方文生图示例_1848727011702476802.json
name: sd3.5_large Turbo版 官方文生图示例_1848727011702476802
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/sd3.5_large Turbo版 官方文生图示例_1848727011702476802.json
hash: 5015163b3b840ac4
coverage: 0.928571
learned_at: 2026-10-10 20:59:26
nodes: [CheckpointLoaderSimple, TripleCLIPLoader, ConditioningCombine, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, Note, EmptySD3LatentImage, ConditioningZeroOut, ConditioningSetTimestepRange, ConditioningSetTimestepRange, KSampler, SaveImage, VAEDecode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "sd3.5_large_turbo.safetensors", "denoise": 1, "sampler_name": "dpmpp_2m", "scheduler": "sgm_uniform", "seed": 335355169217840, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# sd3.5_large Turbo版 官方文生图示例_1848727011702476802.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/sd3.5_large Turbo版 官方文生图示例_1848727011702476802.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `CheckpointLoaderSimple` ★核心
- `TripleCLIPLoader`
- `ConditioningCombine`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `EmptySD3LatentImage`
- `ConditioningZeroOut`
- `ConditioningSetTimestepRange`
- `ConditioningSetTimestepRange`
- `KSampler` ★核心
- `SaveImage`
- `VAEDecode` ★核心

## 关键参数

- `checkpoint` = `sd3.5_large_turbo.safetensors`
- `seed` = `335355169217840`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`CheckpointLoaderSimple`、`TripleCLIPLoader`、`ConditioningCombine`、`ModelSamplingSD3`、`CLIPTextEncode`、`EmptySD3LatentImage`、`ConditioningZeroOut`、`ConditioningSetTimestepRange`、`KSampler`、`SaveImage`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、ConditioningSetTimestepRange、ConditioningCombine、TripleCLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

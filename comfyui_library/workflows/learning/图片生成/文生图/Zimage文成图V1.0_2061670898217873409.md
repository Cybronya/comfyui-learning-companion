---
key: 图片生成/文生图/Zimage文成图V1.0_2061670898217873409.json
name: Zimage文成图V1.0_2061670898217873409
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Zimage文成图V1.0_2061670898217873409.json
hash: 6de5793cbf06137a
coverage: 0.928571
learned_at: 2026-10-19 23:03:05
nodes: [UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingAuraFlow, EmptySD3LatentImage, VAELoader, VAEDecode, SaveImage, PreviewImage, CLIPTextEncode, CLIPLoader, KSampler, CLIPTextEncode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 1029776391838568, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Zimage文成图V1.0_2061670898217873409.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Zimage文成图V1.0_2061670898217873409.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `EmptySD3LatentImage`
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `1029776391838568`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`EmptySD3LatentImage`、`VAELoader`、`VAEDecode`、`SaveImage`、`CLIPTextEncode`、`CLIPLoader`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、SaveImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

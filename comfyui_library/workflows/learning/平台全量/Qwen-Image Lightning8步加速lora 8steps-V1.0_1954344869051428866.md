---
key: 平台全量/Qwen-Image Lightning8步加速lora 8steps-V1.0_1954344869051428866.json
name: Qwen-Image Lightning8步加速lora 8steps-V1.0_1954344869051428866
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen-Image Lightning8步加速lora 8steps-V1.0_1954344869051428866.json
hash: b40ad8113ae91bb6
coverage: 1
learned_at: 2026-11-14 00:51:31
nodes: [VAELoader, CLIPTextEncode, VAEDecode, LoraLoaderModelOnly, CLIPLoader, SaveImage, UNETLoader, EmptySD3LatentImage, CLIPTextEncode, ModelSamplingAuraFlow, KSampler]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 2, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 325855072664205, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Qwen-Image Lightning8步加速lora 8steps-V1.0_1954344869051428866.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen-Image Lightning8步加速lora 8steps-V1.0_1954344869051428866.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（11 个）：
- `VAELoader`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `SaveImage`
- `UNETLoader` ★核心
- `EmptySD3LatentImage`
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `KSampler` ★核心

## 关键参数

- `seed` = `325855072664205`
- `steps` = `8`
- `cfg` = `2`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`VAELoader`、`CLIPTextEncode`、`VAEDecode`、`LoraLoaderModelOnly`、`CLIPLoader`、`SaveImage`、`UNETLoader`、`EmptySD3LatentImage`、`ModelSamplingAuraFlow`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、UNETLoader、SaveImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

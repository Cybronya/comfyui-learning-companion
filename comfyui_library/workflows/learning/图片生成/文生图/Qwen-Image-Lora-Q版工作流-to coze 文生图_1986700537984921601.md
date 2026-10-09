---
key: 图片生成/文生图/Qwen-Image-Lora-Q版工作流-to coze 文生图_1986700537984921601.json
name: Qwen-Image-Lora-Q版工作流-to coze 文生图_1986700537984921601.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image-Lora-Q版工作流-to coze 文生图_1986700537984921601.json
hash: 722b8a5e6c5c892e
coverage: 1
learned_at: 2026-10-09 20:13:12
nodes: [VAEDecode, SaveImage, VAELoader, EmptySD3LatentImage, ModelSamplingAuraFlow, ConditioningZeroOut, CLIPLoader, LoraLoaderModelOnly, KSampler, CLIPTextEncode, UNETLoader]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 852410770297979, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen-Image-Lora-Q版工作流-to coze 文生图_1986700537984921601.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1986700537984921601.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（11 个）：
- `VAEDecode` ★核心
- `SaveImage`
- `VAELoader`
- `EmptySD3LatentImage`
- `ModelSamplingAuraFlow`
- `ConditioningZeroOut`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心

## 关键参数

- `seed` = `852410770297979`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`VAEDecode`、`SaveImage`、`VAELoader`、`EmptySD3LatentImage`、`ModelSamplingAuraFlow`、`ConditioningZeroOut`、`CLIPLoader`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

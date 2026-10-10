---
key: 写实加强版Wan2.2文生图工作流_1956995525369323522.json
name: 写实加强版Wan2.2文生图工作流_1956995525369323522
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/写实加强版Wan2.2文生图工作流_1956995525369323522.json
hash: e80b41b69dbe73e3
coverage: 1
learned_at: 2026-10-10 20:59:36
nodes: [CLIPTextEncode, ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, VAELoader, EmptySD3LatentImage, CLIPLoader, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, KSampler, VAEDecode, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 3.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1002007106935307, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 写实加强版Wan2.2文生图工作流_1956995525369323522.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/写实加强版Wan2.2文生图工作流_1956995525369323522.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptySD3LatentImage`
- `CLIPLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `seed` = `1002007106935307`
- `steps` = `6`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`CLIPTextEncode`、`ModelSamplingSD3`、`VAELoader`、`EmptySD3LatentImage`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、SaveImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

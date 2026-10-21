---
key: 图片生成/文生图/Zimage图片加速生成（Zimage Quick Text-to-Image Generatio）_2029019962836258817.json
name: Zimage图片加速生成（Zimage Quick Text-to-Image Generatio）_2029019962836258817
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Zimage图片加速生成（Zimage Quick Text-to-Image Generatio）_2029019962836258817.json
hash: 1f8cefee276b3bdf
coverage: 0.933333
learned_at: 2026-10-20 23:21:55
nodes: [UNETLoader, ModelSamplingAuraFlow, LoraLoaderModelOnly, CLIPLoader, VAELoader, VAEDecode, PreviewImage, SaveImage, KSampler, ConditioningZeroOut, CLIPTextEncode, easy promptList, EmptyZImageLatentImage //ZImagePowerNodes, CR Prompt Text, EmptySD3LatentImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "simple", "seed": 294762591384859, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Zimage图片加速生成（Zimage Quick Text-to-Image Generatio）_2029019962836258817.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Zimage图片加速生成（Zimage Quick Text-to-Image Generatio）_2029019962836258817.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `PreviewImage`
- `SaveImage`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `easy promptList`
- `EmptyZImageLatentImage //ZImagePowerNodes`
- `CR Prompt Text`
- `EmptySD3LatentImage`

## 关键参数

- `seed` = `294762591384859`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（14/15）

**有卡**：`UNETLoader`、`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`SaveImage`、`KSampler`、`ConditioningZeroOut`、`CLIPTextEncode`、`easy promptList`、`EmptyZImageLatentImage //ZImagePowerNodes`、`CR Prompt Text`、`EmptySD3LatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

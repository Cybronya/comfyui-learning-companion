---
key: 图片生成/文生图/生图效果大比拼：LongCat vs Z‑image vs Klein_2028831826680221697.json
name: 生图效果大比拼：LongCat vs Z‑image vs Klein_2028831826680221697
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/生图效果大比拼：LongCat vs Z‑image vs Klein_2028831826680221697.json
hash: 054cc5d84b9160cf
coverage: 0.892857
learned_at: 2026-10-20 23:22:17
nodes: [ConditioningZeroOut, KSamplerSelect, CFGGuider, RandomNoise, CLIPTextEncode, VAELoader, EmptyFlux2LatentImage, ConditioningZeroOut, Flux2Scheduler, UNETLoader, SamplerCustomAdvanced, easy int, easy int, ConditioningZeroOut, VAELoader, EmptySD3LatentImage, CLIPLoader, AddLabel, CLIPTextEncode, AddLabel, VAEDecode, CLIPTextEncode, EmptySD3LatentImage, UNETLoader, KSampler, CLIPLoader, VAELoader, CLIPLoader, KSampler, EmptySD3LatentImage, VAELoader, AddLabel, UNETLoader, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, ApplySageAttention, CFGNorm, KSampler, LoraLoaderModelOnly, AddLabel, VAEDecode, PreviewImage, VAEDecode, VAEDecode, PreviewImage, ShowText|pysssss, JDCN_StringToList, PreviewImage, UNETLoader, QwenVisionNode, LoadImage, PreviewImage, ImageConcatMulti, SaveImage, PreviewImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 666, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/生图效果大比拼：LongCat vs Z‑image vs Klein_2028831826680221697.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/生图效果大比拼：LongCat vs Z‑image vs Klein_2028831826680221697.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `ConditioningZeroOut`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyFlux2LatentImage`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `UNETLoader` ★核心
- `SamplerCustomAdvanced` ★核心
- `easy int`
- `easy int`
- `ConditioningZeroOut`
- `VAELoader`
- `EmptySD3LatentImage`
- `CLIPLoader`
- `AddLabel`
- `CLIPTextEncode` ★核心
- `AddLabel`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPLoader`
- `KSampler` ★核心
- `EmptySD3LatentImage`
- `VAELoader`
- `AddLabel`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `ApplySageAttention`
- `CFGNorm`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `AddLabel`
- `VAEDecode` ★核心
- `PreviewImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `ShowText|pysssss`
- `JDCN_StringToList`
- `PreviewImage`
- `UNETLoader` ★核心
- `QwenVisionNode`
- `LoadImage`
- `PreviewImage`
- `ImageConcatMulti`
- `SaveImage`
- `PreviewImage`

## 关键参数

- `seed` = `666`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（50/56）

**有卡**：`ConditioningZeroOut`、`KSamplerSelect`、`CFGGuider`、`RandomNoise`、`CLIPTextEncode`、`VAELoader`、`EmptyFlux2LatentImage`、`Flux2Scheduler`、`UNETLoader`、`SamplerCustomAdvanced`、`easy int`、`EmptySD3LatentImage`、`CLIPLoader`、`AddLabel`、`VAEDecode`、`KSampler`、`ApplySageAttention`、`CFGNorm`、`LoraLoaderModelOnly`、`JDCN_StringToList`、`QwenVisionNode`、`LoadImage`、`ImageConcatMulti`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

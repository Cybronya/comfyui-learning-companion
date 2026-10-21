---
key: 图片生成/文生图/Z-image-base、klein与Turbo图像对比_2016490330656346114.json
name: Z-image-base、klein与Turbo图像对比_2016490330656346114
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image-base、klein与Turbo图像对比_2016490330656346114.json
hash: 5d04bc9711549a19
coverage: 0.976744
learned_at: 2026-10-19 22:15:32
nodes: [ConditioningZeroOut, CLIPTextEncode, KSamplerSelect, CFGGuider, RandomNoise, CLIPTextEncode, VAELoader, EmptyFlux2LatentImage, ConditioningZeroOut, Flux2Scheduler, UNETLoader, SamplerCustomAdvanced, AILab_QwenVL, JDCN_StringToList, CLIPLoader, KSampler, easy int, easy int, VAEDecode, ModelSamplingAuraFlow, ConditioningZeroOut, CLIPTextEncode, ModelSamplingAuraFlow, ShowText|pysssss, CLIPLoader, VAEDecode, UNETLoader, AddLabel, VAEDecode, SaveImage, AddLabel, UNETLoader, CLIPLoader, VAELoader, EmptySD3LatentImage, EmptySD3LatentImage, VAELoader, AddLabel, ImageConcatMulti, KSampler, SaveImage, SaveImage, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 666, "steps": 30}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z-image-base、klein与Turbo图像对比_2016490330656346114.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image-base、klein与Turbo图像对比_2016490330656346114.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
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
- `AILab_QwenVL`
- `JDCN_StringToList`
- `CLIPLoader`
- `KSampler` ★核心
- `easy int`
- `easy int`
- `VAEDecode` ★核心
- `ModelSamplingAuraFlow`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `ShowText|pysssss`
- `CLIPLoader`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `AddLabel`
- `VAEDecode` ★核心
- `SaveImage`
- `AddLabel`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptySD3LatentImage`
- `EmptySD3LatentImage`
- `VAELoader`
- `AddLabel`
- `ImageConcatMulti`
- `KSampler` ★核心
- `SaveImage`
- `SaveImage`
- `SaveImage`

## 关键参数

- `seed` = `666`
- `steps` = `30`
- `cfg` = `2.5`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **98%**（42/43）

**有卡**：`ConditioningZeroOut`、`CLIPTextEncode`、`KSamplerSelect`、`CFGGuider`、`RandomNoise`、`VAELoader`、`EmptyFlux2LatentImage`、`Flux2Scheduler`、`UNETLoader`、`SamplerCustomAdvanced`、`AILab_QwenVL`、`JDCN_StringToList`、`CLIPLoader`、`KSampler`、`easy int`、`VAEDecode`、`ModelSamplingAuraFlow`、`AddLabel`、`SaveImage`、`EmptySD3LatentImage`、`ImageConcatMulti`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、CFGGuider

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

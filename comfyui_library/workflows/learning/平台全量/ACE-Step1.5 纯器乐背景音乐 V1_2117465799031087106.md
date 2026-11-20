---
key: 平台全量/ACE-Step1.5 纯器乐背景音乐 V1_2117465799031087106.json
name: ACE-Step1.5 纯器乐背景音乐 V1_2117465799031087106
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/ACE-Step1.5 纯器乐背景音乐 V1_2117465799031087106.json
hash: 1a7b5ea40fb91c3d
coverage: 1
learned_at: 2026-11-14 00:14:47
nodes: [KSampler, SaveAudio, CR Prompt Text, CR Prompt Text, VAEDecodeAudio, ConditioningZeroOut, ModelSamplingAuraFlow, TextEncodeAceStepAudio1.5, EmptyAceStep1.5LatentAudio, UNETLoader, DualCLIPLoader, VAELoader, LoraLoaderModelOnly]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 326095422709659, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 平台全量/ACE-Step1.5 纯器乐背景音乐 V1_2117465799031087106.json

> 来源文件 `comfyui_library/workflows/平台全量/ACE-Step1.5 纯器乐背景音乐 V1_2117465799031087106.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（13 个）：
- `KSampler` ★核心
- `SaveAudio`
- `CR Prompt Text`
- `CR Prompt Text`
- `VAEDecodeAudio` ★核心
- `ConditioningZeroOut`
- `ModelSamplingAuraFlow`
- `TextEncodeAceStepAudio1.5`
- `EmptyAceStep1.5LatentAudio`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `326095422709659`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`KSampler`、`SaveAudio`、`CR Prompt Text`、`VAEDecodeAudio`、`ConditioningZeroOut`、`ModelSamplingAuraFlow`、`TextEncodeAceStepAudio1.5`、`EmptyAceStep1.5LatentAudio`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAELoader、LoraLoaderModelOnly、ConditioningZeroOut、UNETLoader、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、VAEDecodeAudio

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

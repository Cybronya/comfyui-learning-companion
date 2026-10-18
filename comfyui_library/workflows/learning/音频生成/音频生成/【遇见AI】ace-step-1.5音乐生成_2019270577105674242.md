---
key: 音频生成/音频生成/【遇见AI】ace-step-1.5音乐生成_2019270577105674242.json
name: 【遇见AI】ace-step-1.5音乐生成_2019270577105674242
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/【遇见AI】ace-step-1.5音乐生成_2019270577105674242.json
hash: 972ab1b8d1eae270
coverage: 0.833333
learned_at: 2026-10-18 02:07:09
nodes: [VAELoader, DualCLIPLoader, ModelSamplingAuraFlow, UNETLoader, ConditioningZeroOut, KSampler, PrimitiveNode, PrimitiveNode, EmptyAceStep1.5LatentAudio, SaveAudioMP3, TextEncodeAceStepAudio1.5, VAEDecodeAudio]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 31, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/【遇见AI】ace-step-1.5音乐生成_2019270577105674242.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/【遇见AI】ace-step-1.5音乐生成_2019270577105674242.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（12 个）：
- `VAELoader`
- `DualCLIPLoader`
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `PrimitiveNode`
- `PrimitiveNode`
- `EmptyAceStep1.5LatentAudio`
- `SaveAudioMP3`
- `TextEncodeAceStepAudio1.5`
- `VAEDecodeAudio` ★核心

## 关键参数

- `seed` = `31`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（10/12）

**有卡**：`VAELoader`、`DualCLIPLoader`、`ModelSamplingAuraFlow`、`UNETLoader`、`ConditioningZeroOut`、`KSampler`、`EmptyAceStep1.5LatentAudio`、`SaveAudioMP3`、`TextEncodeAceStepAudio1.5`、`VAEDecodeAudio`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、SaveAudioMP3

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

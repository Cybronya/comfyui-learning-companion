---
key: 音频生成/音频生成/无限画布ACE-Step 1.5 XL Turbo音乐生成工作流_2074758959570968577.json
name: 无限画布ACE-Step 1.5 XL Turbo音乐生成工作流_2074758959570968577
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/无限画布ACE-Step 1.5 XL Turbo音乐生成工作流_2074758959570968577.json
hash: dd1c0f956a2cf351
coverage: 0.785714
learned_at: 2026-10-18 03:05:04
nodes: [UNETLoader, VAELoader, EmptyAceStep1.5LatentAudio, ConditioningZeroOut, ModelSamplingAuraFlow, DualCLIPLoader, MarkdownNote, KSampler, VAEDecodeAudio, PrimitiveInt, TextEncodeAceStepAudio1.5, CR Text, PrimitiveNode, SaveAudioMP3]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/无限画布ACE-Step 1.5 XL Turbo音乐生成工作流_2074758959570968577.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/无限画布ACE-Step 1.5 XL Turbo音乐生成工作流_2074758959570968577.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（14 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `EmptyAceStep1.5LatentAudio`
- `ConditioningZeroOut`
- `ModelSamplingAuraFlow`
- `DualCLIPLoader`
- `MarkdownNote`
- `KSampler` ★核心
- `VAEDecodeAudio` ★核心
- `PrimitiveInt`
- `TextEncodeAceStepAudio1.5`
- `CR Text`
- `PrimitiveNode`
- `SaveAudioMP3`

## 关键参数

- `seed` = `0`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **79%**（11/14）

**有卡**：`UNETLoader`、`VAELoader`、`EmptyAceStep1.5LatentAudio`、`ConditioningZeroOut`、`ModelSamplingAuraFlow`、`DualCLIPLoader`、`KSampler`、`VAEDecodeAudio`、`TextEncodeAceStepAudio1.5`、`CR Text`、`SaveAudioMP3`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、SaveAudioMP3

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

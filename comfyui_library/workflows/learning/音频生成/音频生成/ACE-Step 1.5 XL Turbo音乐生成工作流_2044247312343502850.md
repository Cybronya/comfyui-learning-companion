---
key: 音频生成/音频生成/ACE-Step 1.5 XL Turbo音乐生成工作流_2044247312343502850.json
name: ACE-Step 1.5 XL Turbo音乐生成工作流_2044247312343502850
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/ACE-Step 1.5 XL Turbo音乐生成工作流_2044247312343502850.json
hash: 69fb1a5179f3a3e7
coverage: 0.8125
learned_at: 2026-10-18 03:04:46
nodes: [UNETLoader, VAELoader, EmptyAceStep1.5LatentAudio, ConditioningZeroOut, ModelSamplingAuraFlow, DualCLIPLoader, MarkdownNote, KSampler, VAEDecodeAudio, PrimitiveNode, PrimitiveInt, TextEncodeAceStepAudio1.5, CR Text, SaveAudioMP3, Label (rgthree), Label (rgthree)]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/ACE-Step 1.5 XL Turbo音乐生成工作流_2044247312343502850.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/ACE-Step 1.5 XL Turbo音乐生成工作流_2044247312343502850.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（16 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `EmptyAceStep1.5LatentAudio`
- `ConditioningZeroOut`
- `ModelSamplingAuraFlow`
- `DualCLIPLoader`
- `MarkdownNote`
- `KSampler` ★核心
- `VAEDecodeAudio` ★核心
- `PrimitiveNode`
- `PrimitiveInt`
- `TextEncodeAceStepAudio1.5`
- `CR Text`
- `SaveAudioMP3`
- `Label (rgthree)`
- `Label (rgthree)`

## 关键参数

- `seed` = `0`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`UNETLoader`、`VAELoader`、`EmptyAceStep1.5LatentAudio`、`ConditioningZeroOut`、`ModelSamplingAuraFlow`、`DualCLIPLoader`、`KSampler`、`VAEDecodeAudio`、`TextEncodeAceStepAudio1.5`、`CR Text`、`SaveAudioMP3`、`Label (rgthree)`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、SaveAudioMP3

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

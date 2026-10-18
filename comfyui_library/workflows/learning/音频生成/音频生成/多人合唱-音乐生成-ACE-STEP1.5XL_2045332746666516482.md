---
key: 音频生成/音频生成/多人合唱-音乐生成-ACE-STEP1.5XL_2045332746666516482.json
name: 多人合唱-音乐生成-ACE-STEP1.5XL_2045332746666516482
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/多人合唱-音乐生成-ACE-STEP1.5XL_2045332746666516482.json
hash: d9412d0251e4db87
coverage: 0.789474
learned_at: 2026-10-18 03:05:03
nodes: [DualCLIPLoader, CR Text, Float, ConditioningZeroOut, EmptyAceStep1.5LatentAudio, PrimitiveInt, ModelSamplingAuraFlow, UNETLoader, KSampler, VAEDecodeAudio, Int, VAELoader, MarkdownNote, TextEncodeAceStepAudio1.5, SaveAudioMP3, Note, CR Text, JjkText, CR Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/多人合唱-音乐生成-ACE-STEP1.5XL_2045332746666516482.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/多人合唱-音乐生成-ACE-STEP1.5XL_2045332746666516482.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（19 个）：
- `DualCLIPLoader`
- `CR Text`
- `Float`
- `ConditioningZeroOut`
- `EmptyAceStep1.5LatentAudio`
- `PrimitiveInt`
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `VAEDecodeAudio` ★核心
- `Int`
- `VAELoader`
- `MarkdownNote`
- `TextEncodeAceStepAudio1.5`
- `SaveAudioMP3`
- `Note`
- `CR Text`
- `JjkText`
- `CR Text`

## 关键参数

- `seed` = `0`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **79%**（15/19）

**有卡**：`DualCLIPLoader`、`CR Text`、`Float`、`ConditioningZeroOut`、`EmptyAceStep1.5LatentAudio`、`ModelSamplingAuraFlow`、`UNETLoader`、`KSampler`、`VAEDecodeAudio`、`Int`、`VAELoader`、`TextEncodeAceStepAudio1.5`、`SaveAudioMP3`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、SaveAudioMP3

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

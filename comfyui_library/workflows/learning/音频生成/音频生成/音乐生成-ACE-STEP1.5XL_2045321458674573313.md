---
key: 音频生成/音频生成/音乐生成-ACE-STEP1.5XL_2045321458674573313.json
name: 音乐生成-ACE-STEP1.5XL_2045321458674573313
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/音乐生成-ACE-STEP1.5XL_2045321458674573313.json
hash: ac574e2819edfd36
coverage: 0.833333
learned_at: 2026-10-18 03:05:06
nodes: [DualCLIPLoader, CR Text, Float, TextEncodeAceStepAudio1.5, ConditioningZeroOut, EmptyAceStep1.5LatentAudio, PrimitiveInt, ModelSamplingAuraFlow, UNETLoader, KSampler, VAEDecodeAudio, Int, VAELoader, SaveAudioMP3, CR Text, CR Text, MarkdownNote, JjkText]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/音乐生成-ACE-STEP1.5XL_2045321458674573313.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/音乐生成-ACE-STEP1.5XL_2045321458674573313.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（18 个）：
- `DualCLIPLoader`
- `CR Text`
- `Float`
- `TextEncodeAceStepAudio1.5`
- `ConditioningZeroOut`
- `EmptyAceStep1.5LatentAudio`
- `PrimitiveInt`
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `VAEDecodeAudio` ★核心
- `Int`
- `VAELoader`
- `SaveAudioMP3`
- `CR Text`
- `CR Text`
- `MarkdownNote`
- `JjkText`

## 关键参数

- `seed` = `0`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`DualCLIPLoader`、`CR Text`、`Float`、`TextEncodeAceStepAudio1.5`、`ConditioningZeroOut`、`EmptyAceStep1.5LatentAudio`、`ModelSamplingAuraFlow`、`UNETLoader`、`KSampler`、`VAEDecodeAudio`、`Int`、`VAELoader`、`SaveAudioMP3`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、SaveAudioMP3

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

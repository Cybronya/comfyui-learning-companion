---
key: 音频生成/音频生成/ACE-STEP1.5XL_2044231615613767681.json
name: ACE-STEP1.5XL_2044231615613767681
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/ACE-STEP1.5XL_2044231615613767681.json
hash: 8484056df97b89ed
coverage: 0.888889
learned_at: 2026-10-18 03:04:46
nodes: [VAELoader, ConditioningZeroOut, VAEDecodeAudio, DualCLIPLoader, SaveAudioMP3, UNETLoader, ModelSamplingAuraFlow, KSampler, CR Text, PrimitiveInt, LoadImage, MarkdownNote, CR Text, TextEncodeAceStepAudio1.5, CR Text, EmptyAceStep1.5LatentAudio, Float, Int]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/ACE-STEP1.5XL_2044231615613767681.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/ACE-STEP1.5XL_2044231615613767681.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（18 个）：
- `VAELoader`
- `ConditioningZeroOut`
- `VAEDecodeAudio` ★核心
- `DualCLIPLoader`
- `SaveAudioMP3`
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `CR Text`
- `PrimitiveInt`
- `LoadImage`
- `MarkdownNote`
- `CR Text`
- `TextEncodeAceStepAudio1.5`
- `CR Text`
- `EmptyAceStep1.5LatentAudio`
- `Float`
- `Int`

## 关键参数

- `seed` = `0`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（16/18）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`VAEDecodeAudio`、`DualCLIPLoader`、`SaveAudioMP3`、`UNETLoader`、`ModelSamplingAuraFlow`、`KSampler`、`CR Text`、`LoadImage`、`TextEncodeAceStepAudio1.5`、`EmptyAceStep1.5LatentAudio`、`Float`、`Int`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、LoadImage、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

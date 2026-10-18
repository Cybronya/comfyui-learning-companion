---
key: 音频生成/音频生成/超越Suno！ACE-Step 1.5 XL Turbo音乐生成工作流_2045344730900336641.json
name: 超越Suno！ACE-Step 1.5 XL Turbo音乐生成工作流_2045344730900336641
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/超越Suno！ACE-Step 1.5 XL Turbo音乐生成工作流_2045344730900336641.json
hash: 8375f49e9825e068
coverage: 0.833333
learned_at: 2026-10-18 03:05:06
nodes: [UNETLoader, VAELoader, EmptyAceStep1.5LatentAudio, ConditioningZeroOut, ModelSamplingAuraFlow, MarkdownNote, VAEDecodeAudio, PrimitiveInt, LoadImage, LoadImage, LoadImage, KSampler, SaveAudioMP3, TextEncodeAceStepAudio1.5, PrimitiveNode, DualCLIPLoader, CR Text, CR Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/超越Suno！ACE-Step 1.5 XL Turbo音乐生成工作流_2045344730900336641.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/超越Suno！ACE-Step 1.5 XL Turbo音乐生成工作流_2045344730900336641.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（18 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `EmptyAceStep1.5LatentAudio`
- `ConditioningZeroOut`
- `ModelSamplingAuraFlow`
- `MarkdownNote`
- `VAEDecodeAudio` ★核心
- `PrimitiveInt`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `KSampler` ★核心
- `SaveAudioMP3`
- `TextEncodeAceStepAudio1.5`
- `PrimitiveNode`
- `DualCLIPLoader`
- `CR Text`
- `CR Text`

## 关键参数

- `seed` = `0`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`UNETLoader`、`VAELoader`、`EmptyAceStep1.5LatentAudio`、`ConditioningZeroOut`、`ModelSamplingAuraFlow`、`VAEDecodeAudio`、`LoadImage`、`KSampler`、`SaveAudioMP3`、`TextEncodeAceStepAudio1.5`、`DualCLIPLoader`、`CR Text`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、LoadImage、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

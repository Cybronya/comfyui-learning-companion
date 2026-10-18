---
key: 音频生成/音频生成/ACE-Step1.5 文生音乐双Clip_2018882325588742146.json
name: ACE-Step1.5 文生音乐双Clip_2018882325588742146
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/ACE-Step1.5 文生音乐双Clip_2018882325588742146.json
hash: 9296c8248a7cd8fc
coverage: 0.666667
learned_at: 2026-10-18 02:06:53
nodes: [ModelSamplingAuraFlow, VAEDecodeAudio, KSampler, ConditioningZeroOut, TextEncodeAceStepAudio1.5, SaveAudioMP3, PrimitiveNode, MarkdownNote, DualCLIPLoader, UNETLoader, PrimitiveNode, EmptyAceStep1.5LatentAudio, AV_VAELoader, PrimitiveStringMultiline, PrimitiveStringMultiline]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 31, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/ACE-Step1.5 文生音乐双Clip_2018882325588742146.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/ACE-Step1.5 文生音乐双Clip_2018882325588742146.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（15 个）：
- `ModelSamplingAuraFlow`
- `VAEDecodeAudio` ★核心
- `KSampler` ★核心
- `ConditioningZeroOut`
- `TextEncodeAceStepAudio1.5`
- `SaveAudioMP3`
- `PrimitiveNode`
- `MarkdownNote`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `PrimitiveNode`
- `EmptyAceStep1.5LatentAudio`
- `AV_VAELoader`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `31`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **67%**（10/15）

**有卡**：`ModelSamplingAuraFlow`、`VAEDecodeAudio`、`KSampler`、`ConditioningZeroOut`、`TextEncodeAceStepAudio1.5`、`SaveAudioMP3`、`DualCLIPLoader`、`UNETLoader`、`EmptyAceStep1.5LatentAudio`、`AV_VAELoader`

**用到的条目**：KSampler、ConditioningZeroOut、UNETLoader、VAEDecodeAudio、AV_VAELoader、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、SaveAudioMP3

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

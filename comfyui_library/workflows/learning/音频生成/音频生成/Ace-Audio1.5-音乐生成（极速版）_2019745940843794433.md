---
key: 音频生成/音频生成/Ace-Audio1.5-音乐生成（极速版）_2019745940843794433.json
name: Ace-Audio1.5-音乐生成（极速版）_2019745940843794433
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/Ace-Audio1.5-音乐生成（极速版）_2019745940843794433.json
hash: 3788c66262fdc0c7
coverage: 1
learned_at: 2026-10-18 02:06:54
nodes: [UNETLoader, DualCLIPLoader, KSampler, VAELoader, ModelSamplingAuraFlow, VAEDecodeAudio, ConditioningZeroOut, EmptyAceStep1.5LatentAudio, SaveAudioMP3, CR Text, TextEncodeAceStepAudio1.5, CR Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 24629638044655, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/Ace-Audio1.5-音乐生成（极速版）_2019745940843794433.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/Ace-Audio1.5-音乐生成（极速版）_2019745940843794433.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（12 个）：
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `KSampler` ★核心
- `VAELoader`
- `ModelSamplingAuraFlow`
- `VAEDecodeAudio` ★核心
- `ConditioningZeroOut`
- `EmptyAceStep1.5LatentAudio`
- `SaveAudioMP3`
- `CR Text`
- `TextEncodeAceStepAudio1.5`
- `CR Text`

## 关键参数

- `seed` = `24629638044655`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`UNETLoader`、`DualCLIPLoader`、`KSampler`、`VAELoader`、`ModelSamplingAuraFlow`、`VAEDecodeAudio`、`ConditioningZeroOut`、`EmptyAceStep1.5LatentAudio`、`SaveAudioMP3`、`CR Text`、`TextEncodeAceStepAudio1.5`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、SaveAudioMP3

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

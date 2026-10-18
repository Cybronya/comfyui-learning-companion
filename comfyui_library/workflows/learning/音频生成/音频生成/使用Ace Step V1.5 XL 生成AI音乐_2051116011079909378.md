---
key: 音频生成/音频生成/使用Ace Step V1.5 XL 生成AI音乐_2051116011079909378.json
name: 使用Ace Step V1.5 XL 生成AI音乐_2051116011079909378
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/使用Ace Step V1.5 XL 生成AI音乐_2051116011079909378.json
hash: 298f18b800b5eb25
coverage: 0.833333
learned_at: 2026-10-18 03:05:01
nodes: [UNETLoader, DualCLIPLoader, VAELoader, PrimitiveNode, TextEncodeAceStepAudio1.5, ConditioningZeroOut, KSampler, PrimitiveNode, EmptyAceStep1.5LatentAudio, VAEDecodeAudio, SaveAudioMP3, ModelSamplingAuraFlow]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1059745509800667, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/使用Ace Step V1.5 XL 生成AI音乐_2051116011079909378.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/使用Ace Step V1.5 XL 生成AI音乐_2051116011079909378.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（12 个）：
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `PrimitiveNode`
- `TextEncodeAceStepAudio1.5`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `PrimitiveNode`
- `EmptyAceStep1.5LatentAudio`
- `VAEDecodeAudio` ★核心
- `SaveAudioMP3`
- `ModelSamplingAuraFlow`

## 关键参数

- `seed` = `1059745509800667`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（10/12）

**有卡**：`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`TextEncodeAceStepAudio1.5`、`ConditioningZeroOut`、`KSampler`、`EmptyAceStep1.5LatentAudio`、`VAEDecodeAudio`、`SaveAudioMP3`、`ModelSamplingAuraFlow`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、SaveAudioMP3

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

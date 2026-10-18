---
key: 音频生成/音频生成/ACE STEP1.5 音乐生成_2019436598701596673.json
name: ACE STEP1.5 音乐生成_2019436598701596673
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/ACE STEP1.5 音乐生成_2019436598701596673.json
hash: 81bb43af1a2d4bf8
coverage: 0.833333
learned_at: 2026-10-18 02:06:52
nodes: [VAEDecodeAudio, ModelSamplingAuraFlow, ConditioningZeroOut, KSampler, EmptyAceStep1.5LatentAudio, PrimitiveNode, PrimitiveNode, VAELoader, DualCLIPLoader, UNETLoader, SaveAudioMP3, TextEncodeAceStepAudio1.5]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 31, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/ACE STEP1.5 音乐生成_2019436598701596673.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/ACE STEP1.5 音乐生成_2019436598701596673.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（12 个）：
- `VAEDecodeAudio` ★核心
- `ModelSamplingAuraFlow`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `EmptyAceStep1.5LatentAudio`
- `PrimitiveNode`
- `PrimitiveNode`
- `VAELoader`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `SaveAudioMP3`
- `TextEncodeAceStepAudio1.5`

## 关键参数

- `seed` = `31`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（10/12）

**有卡**：`VAEDecodeAudio`、`ModelSamplingAuraFlow`、`ConditioningZeroOut`、`KSampler`、`EmptyAceStep1.5LatentAudio`、`VAELoader`、`DualCLIPLoader`、`UNETLoader`、`SaveAudioMP3`、`TextEncodeAceStepAudio1.5`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、SaveAudioMP3

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

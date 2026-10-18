---
key: 音频生成/音频生成/方格智联-ACE-1.5音乐_2086670840938192898.json
name: 方格智联-ACE-1.5音乐_2086670840938192898
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/方格智联-ACE-1.5音乐_2086670840938192898.json
hash: 74e29d0c40ad6fa6
coverage: 0.933333
learned_at: 2026-10-18 03:05:04
nodes: [KSampler, VAEDecodeAudio, ConditioningZeroOut, ModelSamplingAuraFlow, TextEncodeAceStepAudio1.5, EmptyAceStep1.5LatentAudio, DualCLIPLoader, VAELoader, SaveAudioMP3, PrimitiveInt, UNETLoader, CR Text, Int, CR Text, Float]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 800741635720047, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/方格智联-ACE-1.5音乐_2086670840938192898.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/方格智联-ACE-1.5音乐_2086670840938192898.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（15 个）：
- `KSampler` ★核心
- `VAEDecodeAudio` ★核心
- `ConditioningZeroOut`
- `ModelSamplingAuraFlow`
- `TextEncodeAceStepAudio1.5`
- `EmptyAceStep1.5LatentAudio`
- `DualCLIPLoader`
- `VAELoader`
- `SaveAudioMP3`
- `PrimitiveInt`
- `UNETLoader` ★核心
- `CR Text`
- `Int`
- `CR Text`
- `Float`

## 关键参数

- `seed` = `800741635720047`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（14/15）

**有卡**：`KSampler`、`VAEDecodeAudio`、`ConditioningZeroOut`、`ModelSamplingAuraFlow`、`TextEncodeAceStepAudio1.5`、`EmptyAceStep1.5LatentAudio`、`DualCLIPLoader`、`VAELoader`、`SaveAudioMP3`、`UNETLoader`、`CR Text`、`Int`、`Float`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、SaveAudioMP3

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

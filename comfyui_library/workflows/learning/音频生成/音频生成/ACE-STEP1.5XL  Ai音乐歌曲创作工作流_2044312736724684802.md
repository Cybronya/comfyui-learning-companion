---
key: 音频生成/音频生成/ACE-STEP1.5XL  Ai音乐歌曲创作工作流_2044312736724684802.json
name: ACE-STEP1.5XL  Ai音乐歌曲创作工作流_2044312736724684802
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/ACE-STEP1.5XL  Ai音乐歌曲创作工作流_2044312736724684802.json
hash: b079735cf5af55cd
coverage: 0.833333
learned_at: 2026-10-18 03:04:46
nodes: [VAELoader, ConditioningZeroOut, DualCLIPLoader, UNETLoader, ModelSamplingAuraFlow, PrimitiveInt, TextEncodeAceStepAudio1.5, CR Text, Note, Float, Int, CR Text, CR Text, KSampler, EmptyAceStep1.5LatentAudio, Note, SaveAudioMP3, VAEDecodeAudio]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/ACE-STEP1.5XL  Ai音乐歌曲创作工作流_2044312736724684802.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/ACE-STEP1.5XL  Ai音乐歌曲创作工作流_2044312736724684802.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（18 个）：
- `VAELoader`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `PrimitiveInt`
- `TextEncodeAceStepAudio1.5`
- `CR Text`
- `Note`
- `Float`
- `Int`
- `CR Text`
- `CR Text`
- `KSampler` ★核心
- `EmptyAceStep1.5LatentAudio`
- `Note`
- `SaveAudioMP3`
- `VAEDecodeAudio` ★核心

## 关键参数

- `seed` = `0`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`DualCLIPLoader`、`UNETLoader`、`ModelSamplingAuraFlow`、`TextEncodeAceStepAudio1.5`、`CR Text`、`Float`、`Int`、`KSampler`、`EmptyAceStep1.5LatentAudio`、`SaveAudioMP3`、`VAEDecodeAudio`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、SaveAudioMP3

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

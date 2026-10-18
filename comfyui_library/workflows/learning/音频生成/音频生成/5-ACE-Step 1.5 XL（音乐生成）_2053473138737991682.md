---
key: 音频生成/音频生成/5-ACE-Step 1.5 XL（音乐生成）_2053473138737991682.json
name: 5-ACE-Step 1.5 XL（音乐生成）_2053473138737991682
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/5-ACE-Step 1.5 XL（音乐生成）_2053473138737991682.json
hash: ae002e725a45e445
coverage: 0.769231
learned_at: 2026-10-18 03:04:45
nodes: [PrimitiveNode, EmptyAceStep1.5LatentAudio, ConditioningZeroOut, KSampler, VAEDecodeAudio, PrimitiveInt, SaveAudioMP3, TextEncodeAceStepAudio1.5, ModelSamplingAuraFlow, UNETLoader, DualCLIPLoader, Note, VAELoader]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 50}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/5-ACE-Step 1.5 XL（音乐生成）_2053473138737991682.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/5-ACE-Step 1.5 XL（音乐生成）_2053473138737991682.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（13 个）：
- `PrimitiveNode`
- `EmptyAceStep1.5LatentAudio`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAEDecodeAudio` ★核心
- `PrimitiveInt`
- `SaveAudioMP3`
- `TextEncodeAceStepAudio1.5`
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `Note`
- `VAELoader`

## 关键参数

- `seed` = `0`
- `steps` = `50`
- `cfg` = `6`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **77%**（10/13）

**有卡**：`EmptyAceStep1.5LatentAudio`、`ConditioningZeroOut`、`KSampler`、`VAEDecodeAudio`、`SaveAudioMP3`、`TextEncodeAceStepAudio1.5`、`ModelSamplingAuraFlow`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、SaveAudioMP3

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

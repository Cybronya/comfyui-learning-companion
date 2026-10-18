---
key: 音频生成/音频生成/ACE-Step 1.5大模型：4G显存就能生成AI音乐！_2019019272000905218.json
name: ACE-Step 1.5大模型：4G显存就能生成AI音乐！_2019019272000905218
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/ACE-Step 1.5大模型：4G显存就能生成AI音乐！_2019019272000905218.json
hash: cad03422957c0ba4
coverage: 0.785714
learned_at: 2026-10-18 02:06:53
nodes: [ModelSamplingAuraFlow, VAEDecodeAudio, ConditioningZeroOut, MarkdownNote, CheckpointLoaderSimple, SaveAudioMP3, KSampler, Label (rgthree), Label (rgthree), TextEncodeAceStepAudio1.5, PrimitiveNode, EmptyAceStep1.5LatentAudio, CR Text, PrimitiveNode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ace_step_1.5_turbo_aio.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 88, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/ACE-Step 1.5大模型：4G显存就能生成AI音乐！_2019019272000905218.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/ACE-Step 1.5大模型：4G显存就能生成AI音乐！_2019019272000905218.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（14 个）：
- `ModelSamplingAuraFlow`
- `VAEDecodeAudio` ★核心
- `ConditioningZeroOut`
- `MarkdownNote`
- `CheckpointLoaderSimple` ★核心
- `SaveAudioMP3`
- `KSampler` ★核心
- `Label (rgthree)`
- `Label (rgthree)`
- `TextEncodeAceStepAudio1.5`
- `PrimitiveNode`
- `EmptyAceStep1.5LatentAudio`
- `CR Text`
- `PrimitiveNode`

## 关键参数

- `checkpoint` = `ace_step_1.5_turbo_aio.safetensors`
- `seed` = `88`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **79%**（11/14）

**有卡**：`ModelSamplingAuraFlow`、`VAEDecodeAudio`、`ConditioningZeroOut`、`CheckpointLoaderSimple`、`SaveAudioMP3`、`KSampler`、`Label (rgthree)`、`TextEncodeAceStepAudio1.5`、`EmptyAceStep1.5LatentAudio`、`CR Text`

**用到的条目**：KSampler、CheckpointLoaderSimple、ConditioningZeroOut、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、SaveAudioMP3、ModelSamplingAuraFlow

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

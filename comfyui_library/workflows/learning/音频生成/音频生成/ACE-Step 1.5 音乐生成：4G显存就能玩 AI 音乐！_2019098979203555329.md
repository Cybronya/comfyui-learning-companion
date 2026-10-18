---
key: 音频生成/音频生成/ACE-Step 1.5 音乐生成：4G显存就能玩 AI 音乐！_2019098979203555329.json
name: ACE-Step 1.5 音乐生成：4G显存就能玩 AI 音乐！_2019098979203555329
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/ACE-Step 1.5 音乐生成：4G显存就能玩 AI 音乐！_2019098979203555329.json
hash: e197e2a1bfacd37c
coverage: 0.928571
learned_at: 2026-10-18 02:06:53
nodes: [PrimitiveNode, VAEDecodeAudio, KSampler, ConditioningZeroOut, CheckpointLoaderSimple, ModelSamplingAuraFlow, Primitive integer [Crystools], TextEncodeAceStepAudio1.5, EmptyAceStep1.5LatentAudio, LoadImage, CR Prompt Text, CR Text, Float, SaveAudioMP3]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ace_step_1.5_turbo_aio.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 485881101253283, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/ACE-Step 1.5 音乐生成：4G显存就能玩 AI 音乐！_2019098979203555329.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/ACE-Step 1.5 音乐生成：4G显存就能玩 AI 音乐！_2019098979203555329.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（14 个）：
- `PrimitiveNode`
- `VAEDecodeAudio` ★核心
- `KSampler` ★核心
- `ConditioningZeroOut`
- `CheckpointLoaderSimple` ★核心
- `ModelSamplingAuraFlow`
- `Primitive integer [Crystools]`
- `TextEncodeAceStepAudio1.5`
- `EmptyAceStep1.5LatentAudio`
- `LoadImage`
- `CR Prompt Text`
- `CR Text`
- `Float`
- `SaveAudioMP3`

## 关键参数

- `seed` = `485881101253283`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `ace_step_1.5_turbo_aio.safetensors`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`VAEDecodeAudio`、`KSampler`、`ConditioningZeroOut`、`CheckpointLoaderSimple`、`ModelSamplingAuraFlow`、`Primitive integer [Crystools]`、`TextEncodeAceStepAudio1.5`、`EmptyAceStep1.5LatentAudio`、`LoadImage`、`CR Prompt Text`、`CR Text`、`Float`、`SaveAudioMP3`

**用到的条目**：KSampler、CheckpointLoaderSimple、ConditioningZeroOut、LoadImage、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、CR Prompt Text

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

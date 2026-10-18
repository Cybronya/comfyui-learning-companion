---
key: 音频生成/音频生成/ACE-STEP 1.5 音乐创作_2019331075352305666.json
name: ACE-STEP 1.5 音乐创作_2019331075352305666
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/ACE-STEP 1.5 音乐创作_2019331075352305666.json
hash: 3c5e90dfecb0ee56
coverage: 0.615385
learned_at: 2026-10-18 02:06:53
nodes: [CheckpointLoaderSimple, VAEDecodeAudio, ModelSamplingAuraFlow, EmptyAceStep1.5LatentAudio, ConditioningZeroOut, KSampler, PrimitiveNode, Note, PrimitiveNode, Note, Note, TextEncodeAceStepAudio1.5, SaveAudioMP3]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ace_step_1.5_turbo_aio.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 28, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/ACE-STEP 1.5 音乐创作_2019331075352305666.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/ACE-STEP 1.5 音乐创作_2019331075352305666.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（13 个）：
- `CheckpointLoaderSimple` ★核心
- `VAEDecodeAudio` ★核心
- `ModelSamplingAuraFlow`
- `EmptyAceStep1.5LatentAudio`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `PrimitiveNode`
- `Note`
- `PrimitiveNode`
- `Note`
- `Note`
- `TextEncodeAceStepAudio1.5`
- `SaveAudioMP3`

## 关键参数

- `checkpoint` = `ace_step_1.5_turbo_aio.safetensors`
- `seed` = `28`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **62%**（8/13）

**有卡**：`CheckpointLoaderSimple`、`VAEDecodeAudio`、`ModelSamplingAuraFlow`、`EmptyAceStep1.5LatentAudio`、`ConditioningZeroOut`、`KSampler`、`TextEncodeAceStepAudio1.5`、`SaveAudioMP3`

**用到的条目**：KSampler、CheckpointLoaderSimple、ConditioningZeroOut、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、SaveAudioMP3、ModelSamplingAuraFlow

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

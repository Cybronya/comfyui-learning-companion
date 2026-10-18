---
key: 音频生成/音频生成/ACE-Step1.5 文生音乐_2018856388780367874.json
name: ACE-Step1.5 文生音乐_2018856388780367874
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/ACE-Step1.5 文生音乐_2018856388780367874.json
hash: 5e90b0a279bcc314
coverage: 0.615385
learned_at: 2026-10-18 02:06:53
nodes: [ModelSamplingAuraFlow, VAEDecodeAudio, EmptyAceStep1.5LatentAudio, KSampler, PrimitiveNode, ConditioningZeroOut, PrimitiveNode, MarkdownNote, CheckpointLoaderSimple, SaveAudioMP3, PrimitiveStringMultiline, TextEncodeAceStepAudio1.5, PrimitiveStringMultiline]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ace_step_1.5_turbo_aio.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 31, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/ACE-Step1.5 文生音乐_2018856388780367874.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/ACE-Step1.5 文生音乐_2018856388780367874.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（13 个）：
- `ModelSamplingAuraFlow`
- `VAEDecodeAudio` ★核心
- `EmptyAceStep1.5LatentAudio`
- `KSampler` ★核心
- `PrimitiveNode`
- `ConditioningZeroOut`
- `PrimitiveNode`
- `MarkdownNote`
- `CheckpointLoaderSimple` ★核心
- `SaveAudioMP3`
- `PrimitiveStringMultiline`
- `TextEncodeAceStepAudio1.5`
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `31`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `ace_step_1.5_turbo_aio.safetensors`

## 知识

覆盖率 **62%**（8/13）

**有卡**：`ModelSamplingAuraFlow`、`VAEDecodeAudio`、`EmptyAceStep1.5LatentAudio`、`KSampler`、`ConditioningZeroOut`、`CheckpointLoaderSimple`、`SaveAudioMP3`、`TextEncodeAceStepAudio1.5`

**用到的条目**：KSampler、CheckpointLoaderSimple、ConditioningZeroOut、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、SaveAudioMP3、ModelSamplingAuraFlow

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

---
key: comfyui-workflow-templates-json/audio_ace_step_1_5_checkpoint.json
name: audio_ace_step_1_5_checkpoint
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/audio_ace_step_1_5_checkpoint.json
hash: aed2778141720491
official: true
coverage: 0.727273
learned_at: 2026-10-15 22:24:52
nodes: [CheckpointLoaderSimple, TextEncodeAceStepAudio1.5, ModelSamplingAuraFlow, VAEDecodeAudio, EmptyAceStep1.5LatentAudio, KSampler, PrimitiveNode, ConditioningZeroOut, PrimitiveNode, MarkdownNote, SaveAudioAdvanced]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ace_step_1.5_turbo_aio.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 31, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# comfyui-workflow-templates-json/audio_ace_step_1_5_checkpoint.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/audio_ace_step_1_5_checkpoint.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（11 个）：
- `CheckpointLoaderSimple` ★核心
- `TextEncodeAceStepAudio1.5`
- `ModelSamplingAuraFlow`
- `VAEDecodeAudio` ★核心
- `EmptyAceStep1.5LatentAudio`
- `KSampler` ★核心
- `PrimitiveNode`
- `ConditioningZeroOut`
- `PrimitiveNode`
- `MarkdownNote`
- `SaveAudioAdvanced`

## 关键参数

- `checkpoint` = `ace_step_1.5_turbo_aio.safetensors`
- `seed` = `31`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **73%**（8/11）

**有卡**：`CheckpointLoaderSimple`、`TextEncodeAceStepAudio1.5`、`ModelSamplingAuraFlow`、`VAEDecodeAudio`、`EmptyAceStep1.5LatentAudio`、`KSampler`、`ConditioningZeroOut`、`SaveAudioAdvanced`

**用到的条目**：KSampler、CheckpointLoaderSimple、ConditioningZeroOut、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、SaveAudioAdvanced、ModelSamplingAuraFlow

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

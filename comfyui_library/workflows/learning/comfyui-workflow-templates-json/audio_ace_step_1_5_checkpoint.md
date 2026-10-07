---
key: comfyui-workflow-templates-json/audio_ace_step_1_5_checkpoint.json
name: audio_ace_step_1_5_checkpoint
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/audio_ace_step_1_5_checkpoint.json
hash: aed2778141720491
official: true
coverage: 0.545455
learned_at: 2026-10-07 21:35:15
nodes: [CheckpointLoaderSimple, TextEncodeAceStepAudio1.5, ModelSamplingAuraFlow, VAEDecodeAudio, EmptyAceStep1.5LatentAudio, KSampler, PrimitiveNode, ConditioningZeroOut, PrimitiveNode, MarkdownNote, SaveAudioAdvanced]
patterns: []
missing: [EmptyAceStep1.5LatentAudio, TextEncodeAceStepAudio1.5]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ace_step_1.5_turbo_aio.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 31, "steps": 8}
discoveries: [次要节点 `EmptyAceStep1.5LatentAudio` 仅有 VAE 的通用知识，没有该节点自己的说明, 次要节点 `TextEncodeAceStepAudio1.5` 仅有 VAE 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
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

覆盖率 **55%**（6/11）

**有卡**：`CheckpointLoaderSimple`、`ModelSamplingAuraFlow`、`VAEDecodeAudio`、`KSampler`、`ConditioningZeroOut`、`SaveAudioAdvanced`

**缺卡**（2）：`EmptyAceStep1.5LatentAudio`、`TextEncodeAceStepAudio1.5`

**用到的条目**：KSampler、CheckpointLoaderSimple、ConditioningZeroOut、VAEDecodeAudio、SaveAudioAdvanced、ModelSamplingAuraFlow、sd15-t2i-basic、sd15-t2i-lora

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- 次要节点 `EmptyAceStep1.5LatentAudio` 仅有 VAE 的通用知识，没有该节点自己的说明
- 次要节点 `TextEncodeAceStepAudio1.5` 仅有 VAE 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

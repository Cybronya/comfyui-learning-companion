---
key: comfyui-workflow-templates-json/audio_ace_step_1_t2a_instrumentals.json
name: audio_ace_step_1_t2a_instrumentals
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/audio_ace_step_1_t2a_instrumentals.json
hash: ef0d26e72ea75882
official: true
coverage: 0.833333
learned_at: 2026-10-10 22:46:58
nodes: [KSampler, VAEDecodeAudio, ConditioningZeroOut, TextEncodeAceStepAudio, LatentOperationTonemapReinhard, SaveAudioMP3, MarkdownNote, Note, CheckpointLoaderSimple, EmptyAceStepLatentAudio, LatentApplyOperationCFG, ModelSamplingSD3]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 5, "checkpoint": "ace_step_v1_3.5b.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 257025689259434, "steps": 50}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# comfyui-workflow-templates-json/audio_ace_step_1_t2a_instrumentals.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/audio_ace_step_1_t2a_instrumentals.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（12 个）：
- `KSampler` ★核心
- `VAEDecodeAudio` ★核心
- `ConditioningZeroOut`
- `TextEncodeAceStepAudio`
- `LatentOperationTonemapReinhard`
- `SaveAudioMP3`
- `MarkdownNote`
- `Note`
- `CheckpointLoaderSimple` ★核心
- `EmptyAceStepLatentAudio`
- `LatentApplyOperationCFG`
- `ModelSamplingSD3`

## 关键参数

- `seed` = `257025689259434`
- `steps` = `50`
- `cfg` = `5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `ace_step_v1_3.5b.safetensors`

## 知识

覆盖率 **83%**（10/12）

**有卡**：`KSampler`、`VAEDecodeAudio`、`ConditioningZeroOut`、`TextEncodeAceStepAudio`、`LatentOperationTonemapReinhard`、`SaveAudioMP3`、`CheckpointLoaderSimple`、`EmptyAceStepLatentAudio`、`LatentApplyOperationCFG`、`ModelSamplingSD3`

**用到的条目**：KSampler、CheckpointLoaderSimple、ConditioningZeroOut、LatentApplyOperationCFG、VAEDecodeAudio、EmptyAceStepLatentAudio、LatentOperationTonemapReinhard、TextEncodeAceStepAudio

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

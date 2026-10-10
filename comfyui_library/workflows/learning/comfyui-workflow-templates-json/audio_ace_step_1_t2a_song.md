---
key: comfyui-workflow-templates-json/audio_ace_step_1_t2a_song.json
name: audio_ace_step_1_t2a_song
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/audio_ace_step_1_t2a_song.json
hash: a34afdb8af60fd38
official: true
coverage: 0.909091
learned_at: 2026-10-10 22:46:58
nodes: [CheckpointLoaderSimple, VAEDecodeAudio, ConditioningZeroOut, LatentOperationTonemapReinhard, EmptyAceStepLatentAudio, MarkdownNote, LatentApplyOperationCFG, KSampler, ModelSamplingSD3, TextEncodeAceStepAudio, SaveAudioAdvanced]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 5, "checkpoint": "ace_step_v1_3.5b.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 468254064217846, "steps": 50}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# comfyui-workflow-templates-json/audio_ace_step_1_t2a_song.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/audio_ace_step_1_t2a_song.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（11 个）：
- `CheckpointLoaderSimple` ★核心
- `VAEDecodeAudio` ★核心
- `ConditioningZeroOut`
- `LatentOperationTonemapReinhard`
- `EmptyAceStepLatentAudio`
- `MarkdownNote`
- `LatentApplyOperationCFG`
- `KSampler` ★核心
- `ModelSamplingSD3`
- `TextEncodeAceStepAudio`
- `SaveAudioAdvanced`

## 关键参数

- `checkpoint` = `ace_step_v1_3.5b.safetensors`
- `seed` = `468254064217846`
- `steps` = `50`
- `cfg` = `5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`CheckpointLoaderSimple`、`VAEDecodeAudio`、`ConditioningZeroOut`、`LatentOperationTonemapReinhard`、`EmptyAceStepLatentAudio`、`LatentApplyOperationCFG`、`KSampler`、`ModelSamplingSD3`、`TextEncodeAceStepAudio`、`SaveAudioAdvanced`

**用到的条目**：KSampler、CheckpointLoaderSimple、ConditioningZeroOut、LatentApplyOperationCFG、VAEDecodeAudio、EmptyAceStepLatentAudio、LatentOperationTonemapReinhard、TextEncodeAceStepAudio

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

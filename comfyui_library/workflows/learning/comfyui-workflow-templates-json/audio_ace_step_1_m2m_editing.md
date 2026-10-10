---
key: comfyui-workflow-templates-json/audio_ace_step_1_m2m_editing.json
name: audio_ace_step_1_m2m_editing
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/audio_ace_step_1_m2m_editing.json
hash: 0559213d99dc6208
official: true
coverage: 0.916667
learned_at: 2026-10-10 22:46:57
nodes: [LatentApplyOperationCFG, VAEDecodeAudio, ConditioningZeroOut, ModelSamplingSD3, LatentOperationTonemapReinhard, KSampler, VAEEncodeAudio, CheckpointLoaderSimple, MarkdownNote, TextEncodeAceStepAudio, LoadAudio, SaveAudioAdvanced]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 5, "checkpoint": "ace_step_v1_3.5b.safetensors", "denoise": 0.30000000000000004, "sampler_name": "euler", "scheduler": "simple", "seed": 378808614834773, "steps": 50}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# comfyui-workflow-templates-json/audio_ace_step_1_m2m_editing.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/audio_ace_step_1_m2m_editing.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（12 个）：
- `LatentApplyOperationCFG`
- `VAEDecodeAudio` ★核心
- `ConditioningZeroOut`
- `ModelSamplingSD3`
- `LatentOperationTonemapReinhard`
- `KSampler` ★核心
- `VAEEncodeAudio` ★核心
- `CheckpointLoaderSimple` ★核心
- `MarkdownNote`
- `TextEncodeAceStepAudio`
- `LoadAudio`
- `SaveAudioAdvanced`

## 关键参数

- `seed` = `378808614834773`
- `steps` = `50`
- `cfg` = `5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.30000000000000004`
- `checkpoint` = `ace_step_v1_3.5b.safetensors`

## 知识

覆盖率 **92%**（11/12）

**有卡**：`LatentApplyOperationCFG`、`VAEDecodeAudio`、`ConditioningZeroOut`、`ModelSamplingSD3`、`LatentOperationTonemapReinhard`、`KSampler`、`VAEEncodeAudio`、`CheckpointLoaderSimple`、`TextEncodeAceStepAudio`、`LoadAudio`、`SaveAudioAdvanced`

**用到的条目**：KSampler、CheckpointLoaderSimple、ConditioningZeroOut、LatentApplyOperationCFG、VAEDecodeAudio、VAEEncodeAudio、LatentOperationTonemapReinhard、TextEncodeAceStepAudio

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

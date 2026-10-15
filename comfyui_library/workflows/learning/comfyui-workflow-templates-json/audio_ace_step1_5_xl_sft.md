---
key: comfyui-workflow-templates-json/audio_ace_step1_5_xl_sft.json
name: audio_ace_step1_5_xl_sft
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/audio_ace_step1_5_xl_sft.json
hash: 3d23db9592dc6131
official: true
coverage: 0.833333
learned_at: 2026-10-15 22:24:52
nodes: [UNETLoader, VAELoader, PrimitiveNode, EmptyAceStep1.5LatentAudio, ConditioningZeroOut, DualCLIPLoader, PrimitiveInt, TextEncodeAceStepAudio1.5, KSampler, VAEDecodeAudio, ModelSamplingAuraFlow, SaveAudioAdvanced]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 7, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 50}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# comfyui-workflow-templates-json/audio_ace_step1_5_xl_sft.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/audio_ace_step1_5_xl_sft.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（12 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `PrimitiveNode`
- `EmptyAceStep1.5LatentAudio`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `PrimitiveInt`
- `TextEncodeAceStepAudio1.5`
- `KSampler` ★核心
- `VAEDecodeAudio` ★核心
- `ModelSamplingAuraFlow`
- `SaveAudioAdvanced`

## 关键参数

- `seed` = `0`
- `steps` = `50`
- `cfg` = `7`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（10/12）

**有卡**：`UNETLoader`、`VAELoader`、`EmptyAceStep1.5LatentAudio`、`ConditioningZeroOut`、`DualCLIPLoader`、`TextEncodeAceStepAudio1.5`、`KSampler`、`VAEDecodeAudio`、`ModelSamplingAuraFlow`、`SaveAudioAdvanced`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、SaveAudioAdvanced

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

---
key: 音频生成/音频生成/Ace Step 1.5 AIO_2019698387427266561.json
name: Ace Step 1.5 AIO_2019698387427266561
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/Ace Step 1.5 AIO_2019698387427266561.json
hash: b87bb3c8e1ce5dc4
coverage: 0.75
learned_at: 2026-10-18 02:06:54
nodes: [KSampler, VAEDecodeAudio, ConditioningZeroOut, ModelSamplingAuraFlow, TextEncodeAceStepAudio1.5, EmptyAceStep1.5LatentAudio, PrimitiveNode, MarkdownNote, CheckpointLoaderSimple, PrimitiveNode, PreviewAudio, SaveAudioMP3]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ace_step_1.5_turbo_aio.safetensors", "denoise": 1, "sampler_name": "res_2s", "scheduler": "beta57", "seed": 49, "steps": 12}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/Ace Step 1.5 AIO_2019698387427266561.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/Ace Step 1.5 AIO_2019698387427266561.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（12 个）：
- `KSampler` ★核心
- `VAEDecodeAudio` ★核心
- `ConditioningZeroOut`
- `ModelSamplingAuraFlow`
- `TextEncodeAceStepAudio1.5`
- `EmptyAceStep1.5LatentAudio`
- `PrimitiveNode`
- `MarkdownNote`
- `CheckpointLoaderSimple` ★核心
- `PrimitiveNode`
- `PreviewAudio`
- `SaveAudioMP3`

## 关键参数

- `seed` = `49`
- `steps` = `12`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `beta57`
- `denoise` = `1`
- `checkpoint` = `ace_step_1.5_turbo_aio.safetensors`

## 知识

覆盖率 **75%**（9/12）

**有卡**：`KSampler`、`VAEDecodeAudio`、`ConditioningZeroOut`、`ModelSamplingAuraFlow`、`TextEncodeAceStepAudio1.5`、`EmptyAceStep1.5LatentAudio`、`CheckpointLoaderSimple`、`PreviewAudio`、`SaveAudioMP3`

**用到的条目**：KSampler、CheckpointLoaderSimple、ConditioningZeroOut、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、PreviewAudio、SaveAudioMP3

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

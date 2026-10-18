---
key: 音频生成/音频生成/免费音乐创作（堪比suno）AceStep1.5_2020044996040200193.json
name: 免费音乐创作（堪比suno）AceStep1.5_2020044996040200193
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/免费音乐创作（堪比suno）AceStep1.5_2020044996040200193.json
hash: 206fd8eef8579b3d
coverage: 0.928571
learned_at: 2026-10-18 02:07:09
nodes: [KSampler, ConditioningZeroOut, ModelSamplingAuraFlow, CheckpointLoaderSimple, PrimitiveNode, EmptyAceStep1.5LatentAudio, SaveAudioMP3, VAEDecodeAudio, PreviewAudio, CR Text, CR Text, TextEncodeAceStepAudio1.5, JWInteger, DF_Int_to_Float]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ace_step_1.5_turbo_aio.safetensors", "denoise": 1, "sampler_name": "res_2s", "scheduler": "beta57", "seed": 49, "steps": 12}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/免费音乐创作（堪比suno）AceStep1.5_2020044996040200193.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/免费音乐创作（堪比suno）AceStep1.5_2020044996040200193.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（14 个）：
- `KSampler` ★核心
- `ConditioningZeroOut`
- `ModelSamplingAuraFlow`
- `CheckpointLoaderSimple` ★核心
- `PrimitiveNode`
- `EmptyAceStep1.5LatentAudio`
- `SaveAudioMP3`
- `VAEDecodeAudio` ★核心
- `PreviewAudio`
- `CR Text`
- `CR Text`
- `TextEncodeAceStepAudio1.5`
- `JWInteger`
- `DF_Int_to_Float`

## 关键参数

- `seed` = `49`
- `steps` = `12`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `beta57`
- `denoise` = `1`
- `checkpoint` = `ace_step_1.5_turbo_aio.safetensors`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`KSampler`、`ConditioningZeroOut`、`ModelSamplingAuraFlow`、`CheckpointLoaderSimple`、`EmptyAceStep1.5LatentAudio`、`SaveAudioMP3`、`VAEDecodeAudio`、`PreviewAudio`、`CR Text`、`TextEncodeAceStepAudio1.5`、`JWInteger`、`DF_Int_to_Float`

**用到的条目**：KSampler、CheckpointLoaderSimple、ConditioningZeroOut、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、PreviewAudio、SaveAudioMP3

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

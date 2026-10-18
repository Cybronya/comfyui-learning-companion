---
key: 音频生成/音频生成/45号特工：AceStepAudio1.5歌曲制作_2096144845957062657.json
name: 45号特工：AceStepAudio1.5歌曲制作_2096144845957062657
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/45号特工：AceStepAudio1.5歌曲制作_2096144845957062657.json
hash: ce72a8839aa708c3
coverage: 0.842105
learned_at: 2026-10-18 17:45:25
nodes: [ModelSamplingAuraFlow, ConditioningZeroOut, EmptyAceStep1.5LatentAudio, KSampler, SaveAudioNode, VAEDecodeAudio, SaveAudioAdvanced, SaveAudioAdvanced, CheckpointLoaderSimple, TextEncodeAceStepAudio1.5, Note, PrimitiveFloat, SeedNode, PreviewAudio, CR Text, CR Text, Note, LoadImage, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ace_step_1.5_turbo_aio.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 450773418190827, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/45号特工：AceStepAudio1.5歌曲制作_2096144845957062657.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/45号特工：AceStepAudio1.5歌曲制作_2096144845957062657.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（19 个）：
- `ModelSamplingAuraFlow`
- `ConditioningZeroOut`
- `EmptyAceStep1.5LatentAudio`
- `KSampler` ★核心
- `SaveAudioNode`
- `VAEDecodeAudio` ★核心
- `SaveAudioAdvanced`
- `SaveAudioAdvanced`
- `CheckpointLoaderSimple` ★核心
- `TextEncodeAceStepAudio1.5`
- `Note`
- `PrimitiveFloat`
- `SeedNode`
- `PreviewAudio`
- `CR Text`
- `CR Text`
- `Note`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `450773418190827`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `ace_step_1.5_turbo_aio.safetensors`

## 知识

覆盖率 **84%**（16/19）

**有卡**：`ModelSamplingAuraFlow`、`ConditioningZeroOut`、`EmptyAceStep1.5LatentAudio`、`KSampler`、`SaveAudioNode`、`VAEDecodeAudio`、`SaveAudioAdvanced`、`CheckpointLoaderSimple`、`TextEncodeAceStepAudio1.5`、`SeedNode`、`PreviewAudio`、`CR Text`、`LoadImage`

**用到的条目**：KSampler、CheckpointLoaderSimple、ConditioningZeroOut、LoadImage、SeedNode、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

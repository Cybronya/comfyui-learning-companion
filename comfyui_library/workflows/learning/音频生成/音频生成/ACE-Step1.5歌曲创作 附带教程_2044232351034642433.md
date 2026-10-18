---
key: 音频生成/音频生成/ACE-Step1.5歌曲创作 附带教程_2044232351034642433.json
name: ACE-Step1.5歌曲创作 附带教程_2044232351034642433
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/ACE-Step1.5歌曲创作 附带教程_2044232351034642433.json
hash: b21b86515dc4f411
coverage: 0.625
learned_at: 2026-10-18 03:04:46
nodes: [EmptyAceStep1.5LatentAudio, PreviewAudio, CheckpointLoaderSimple, Note, MarkdownNote, SaveAudioMP3, Float, TextEncodeAceStepAudio1.5, ConditioningZeroOut, PrimitiveNode, ModelSamplingAuraFlow, KSampler, VAEDecodeAudio, Note, PrimitiveStringMultiline, PrimitiveStringMultiline]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ace_step_1.5_turbo_aio.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 148372765236345, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/ACE-Step1.5歌曲创作 附带教程_2044232351034642433.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/ACE-Step1.5歌曲创作 附带教程_2044232351034642433.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（16 个）：
- `EmptyAceStep1.5LatentAudio`
- `PreviewAudio`
- `CheckpointLoaderSimple` ★核心
- `Note`
- `MarkdownNote`
- `SaveAudioMP3`
- `Float`
- `TextEncodeAceStepAudio1.5`
- `ConditioningZeroOut`
- `PrimitiveNode`
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `VAEDecodeAudio` ★核心
- `Note`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`

## 关键参数

- `checkpoint` = `ace_step_1.5_turbo_aio.safetensors`
- `seed` = `148372765236345`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **62%**（10/16）

**有卡**：`EmptyAceStep1.5LatentAudio`、`PreviewAudio`、`CheckpointLoaderSimple`、`SaveAudioMP3`、`Float`、`TextEncodeAceStepAudio1.5`、`ConditioningZeroOut`、`ModelSamplingAuraFlow`、`KSampler`、`VAEDecodeAudio`

**用到的条目**：KSampler、CheckpointLoaderSimple、ConditioningZeroOut、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、PreviewAudio、SaveAudioMP3

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

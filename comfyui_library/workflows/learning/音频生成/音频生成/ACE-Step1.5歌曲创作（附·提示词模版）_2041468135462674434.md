---
key: 音频生成/音频生成/ACE-Step1.5歌曲创作（附·提示词模版）_2041468135462674434.json
name: ACE-Step1.5歌曲创作（附·提示词模版）_2041468135462674434
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/ACE-Step1.5歌曲创作（附·提示词模版）_2041468135462674434.json
hash: 956b7ea875ef0eff
coverage: 0.642857
learned_at: 2026-10-18 02:28:38
nodes: [PrimitiveNode, EmptyAceStep1.5LatentAudio, CheckpointLoaderSimple, ModelSamplingAuraFlow, KSampler, ConditioningZeroOut, PrimitiveNode, TextEncodeAceStepAudio1.5, VAEDecodeAudio, PreviewAudio, SaveAudioMP3, Note, PrimitiveStringMultiline, PrimitiveStringMultiline]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ace_step_1.5_turbo_aio.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 94968821985748, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/ACE-Step1.5歌曲创作（附·提示词模版）_2041468135462674434.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/ACE-Step1.5歌曲创作（附·提示词模版）_2041468135462674434.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（14 个）：
- `PrimitiveNode`
- `EmptyAceStep1.5LatentAudio`
- `CheckpointLoaderSimple` ★核心
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `PrimitiveNode`
- `TextEncodeAceStepAudio1.5`
- `VAEDecodeAudio` ★核心
- `PreviewAudio`
- `SaveAudioMP3`
- `Note`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`

## 关键参数

- `checkpoint` = `ace_step_1.5_turbo_aio.safetensors`
- `seed` = `94968821985748`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **64%**（9/14）

**有卡**：`EmptyAceStep1.5LatentAudio`、`CheckpointLoaderSimple`、`ModelSamplingAuraFlow`、`KSampler`、`ConditioningZeroOut`、`TextEncodeAceStepAudio1.5`、`VAEDecodeAudio`、`PreviewAudio`、`SaveAudioMP3`

**用到的条目**：KSampler、CheckpointLoaderSimple、ConditioningZeroOut、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、PreviewAudio、SaveAudioMP3

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

---
key: 音频生成/音频生成/ACE_Step_1.5_音乐歌曲生成+音质提升_2020109101342138370.json
name: ACE_Step_1.5_音乐歌曲生成+音质提升_2020109101342138370
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/ACE_Step_1.5_音乐歌曲生成+音质提升_2020109101342138370.json
hash: 6474b65752a0a5b3
coverage: 0.866667
learned_at: 2026-10-18 02:06:53
nodes: [TextEncodeAceStepAudio1.5, ConditioningZeroOut, KSampler, VAEDecodeAudio, SaveAudio, CheckpointLoaderSimple, AudioQualityEffects, AudioQualityEnhancer, PreviewAudio, TextInput_, TextInput_, EmptyAceStep1.5LatentAudio, PrimitiveNode, PrimitiveNode, ModelSamplingAuraFlow]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ace_step_1.5_turbo_aio.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 31, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/ACE_Step_1.5_音乐歌曲生成+音质提升_2020109101342138370.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/ACE_Step_1.5_音乐歌曲生成+音质提升_2020109101342138370.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（15 个）：
- `TextEncodeAceStepAudio1.5`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAEDecodeAudio` ★核心
- `SaveAudio`
- `CheckpointLoaderSimple` ★核心
- `AudioQualityEffects`
- `AudioQualityEnhancer`
- `PreviewAudio`
- `TextInput_`
- `TextInput_`
- `EmptyAceStep1.5LatentAudio`
- `PrimitiveNode`
- `PrimitiveNode`
- `ModelSamplingAuraFlow`

## 关键参数

- `seed` = `31`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `ace_step_1.5_turbo_aio.safetensors`

## 知识

覆盖率 **87%**（13/15）

**有卡**：`TextEncodeAceStepAudio1.5`、`ConditioningZeroOut`、`KSampler`、`VAEDecodeAudio`、`SaveAudio`、`CheckpointLoaderSimple`、`AudioQualityEffects`、`AudioQualityEnhancer`、`PreviewAudio`、`TextInput_`、`EmptyAceStep1.5LatentAudio`、`ModelSamplingAuraFlow`

**用到的条目**：KSampler、CheckpointLoaderSimple、ConditioningZeroOut、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、SaveAudio、PreviewAudio

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

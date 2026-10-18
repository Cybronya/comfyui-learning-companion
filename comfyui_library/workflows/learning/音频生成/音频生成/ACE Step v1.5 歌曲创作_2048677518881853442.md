---
key: 音频生成/音频生成/ACE Step v1.5 歌曲创作_2048677518881853442.json
name: ACE Step v1.5 歌曲创作_2048677518881853442
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/ACE Step v1.5 歌曲创作_2048677518881853442.json
hash: ee07d43dae9b7e36
coverage: 0.916667
learned_at: 2026-10-18 03:04:46
nodes: [ConditioningZeroOut, VAEDecodeAudio, ModelSamplingAuraFlow, PrimitiveFloat, easy seed, EmptyAceStep1.5LatentAudio, KSampler, TextEncodeAceStepAudio1.5, UNETLoader, DualCLIPLoader, VAELoader, SaveAudioMP3]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1105896572181409, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/ACE Step v1.5 歌曲创作_2048677518881853442.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/ACE Step v1.5 歌曲创作_2048677518881853442.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（12 个）：
- `ConditioningZeroOut`
- `VAEDecodeAudio` ★核心
- `ModelSamplingAuraFlow`
- `PrimitiveFloat`
- `easy seed`
- `EmptyAceStep1.5LatentAudio`
- `KSampler` ★核心
- `TextEncodeAceStepAudio1.5`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `SaveAudioMP3`

## 关键参数

- `seed` = `1105896572181409`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（11/12）

**有卡**：`ConditioningZeroOut`、`VAEDecodeAudio`、`ModelSamplingAuraFlow`、`easy seed`、`EmptyAceStep1.5LatentAudio`、`KSampler`、`TextEncodeAceStepAudio1.5`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`SaveAudioMP3`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、UNETLoader、easy seed、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

---
key: 音频生成/音频生成/ACE-Step 1.5音乐生成 文本转音乐 长歌曲生成 翻唱 Demo快速生成_2019647657949532162.json
name: ACE-Step 1.5音乐生成 文本转音乐 长歌曲生成 翻唱 Demo快速生成_2019647657949532162
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/ACE-Step 1.5音乐生成 文本转音乐 长歌曲生成 翻唱 Demo快速生成_2019647657949532162.json
hash: ab993c8b1b30ffc7
coverage: 0.75
learned_at: 2026-10-18 02:06:53
nodes: [ModelSamplingAuraFlow, VAEDecodeAudio, ConditioningZeroOut, CheckpointLoaderSimple, SaveAudioMP3, KSampler, PrimitiveNode, CR Text, EmptyAceStep1.5LatentAudio, PrimitiveNode, TextEncodeAceStepAudio1.5, Note]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ace_step_1.5_turbo_aio.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 295537686155086, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/ACE-Step 1.5音乐生成 文本转音乐 长歌曲生成 翻唱 Demo快速生成_2019647657949532162.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/ACE-Step 1.5音乐生成 文本转音乐 长歌曲生成 翻唱 Demo快速生成_2019647657949532162.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（12 个）：
- `ModelSamplingAuraFlow`
- `VAEDecodeAudio` ★核心
- `ConditioningZeroOut`
- `CheckpointLoaderSimple` ★核心
- `SaveAudioMP3`
- `KSampler` ★核心
- `PrimitiveNode`
- `CR Text`
- `EmptyAceStep1.5LatentAudio`
- `PrimitiveNode`
- `TextEncodeAceStepAudio1.5`
- `Note`

## 关键参数

- `checkpoint` = `ace_step_1.5_turbo_aio.safetensors`
- `seed` = `295537686155086`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **75%**（9/12）

**有卡**：`ModelSamplingAuraFlow`、`VAEDecodeAudio`、`ConditioningZeroOut`、`CheckpointLoaderSimple`、`SaveAudioMP3`、`KSampler`、`CR Text`、`EmptyAceStep1.5LatentAudio`、`TextEncodeAceStepAudio1.5`

**用到的条目**：KSampler、CheckpointLoaderSimple、ConditioningZeroOut、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、SaveAudioMP3、ModelSamplingAuraFlow

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

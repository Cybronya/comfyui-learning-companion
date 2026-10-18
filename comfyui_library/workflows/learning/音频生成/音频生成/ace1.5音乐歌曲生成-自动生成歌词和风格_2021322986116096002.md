---
key: 音频生成/音频生成/ace1.5音乐歌曲生成-自动生成歌词和风格_2021322986116096002.json
name: ace1.5音乐歌曲生成-自动生成歌词和风格_2021322986116096002
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/ace1.5音乐歌曲生成-自动生成歌词和风格_2021322986116096002.json
hash: cb27313947fa593f
coverage: 0.764706
learned_at: 2026-10-18 02:07:08
nodes: [KSampler, PrimitiveNode, VAEDecodeAudio, ConditioningZeroOut, ModelSamplingAuraFlow, EmptyAceStep1.5LatentAudio, UNETLoader, VAELoader, PrimitiveNode, TextEncodeAceStepAudio1.5, Text Multiline, RH_LLMAPI_NODE, RH_LLMAPI_NODE, easy showAnything, DualCLIPLoader, SaveAudioMP3, easy showAnything]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 999, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/ace1.5音乐歌曲生成-自动生成歌词和风格_2021322986116096002.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/ace1.5音乐歌曲生成-自动生成歌词和风格_2021322986116096002.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（17 个）：
- `KSampler` ★核心
- `PrimitiveNode`
- `VAEDecodeAudio` ★核心
- `ConditioningZeroOut`
- `ModelSamplingAuraFlow`
- `EmptyAceStep1.5LatentAudio`
- `UNETLoader` ★核心
- `VAELoader`
- `PrimitiveNode`
- `TextEncodeAceStepAudio1.5`
- `Text Multiline`
- `RH_LLMAPI_NODE`
- `RH_LLMAPI_NODE`
- `easy showAnything`
- `DualCLIPLoader`
- `SaveAudioMP3`
- `easy showAnything`

## 关键参数

- `seed` = `999`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **76%**（13/17）

**有卡**：`KSampler`、`VAEDecodeAudio`、`ConditioningZeroOut`、`ModelSamplingAuraFlow`、`EmptyAceStep1.5LatentAudio`、`UNETLoader`、`VAELoader`、`TextEncodeAceStepAudio1.5`、`Text Multiline`、`RH_LLMAPI_NODE`、`DualCLIPLoader`、`SaveAudioMP3`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、SaveAudioMP3

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

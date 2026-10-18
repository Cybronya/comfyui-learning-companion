---
key: 音频生成/音频生成/ace1.5音乐生成_2018972681219088385.json
name: ace1.5音乐生成_2018972681219088385
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/ace1.5音乐生成_2018972681219088385.json
hash: 9f9282937f820b37
coverage: 0.8125
learned_at: 2026-10-18 02:07:08
nodes: [KSampler, PrimitiveNode, VAEDecodeAudio, ConditioningZeroOut, MarkdownNote, ModelSamplingAuraFlow, SaveAudioMP3, PrimitiveNode, EmptyAceStep1.5LatentAudio, TextEncodeAceStepAudio1.5, UNETLoader, DualCLIPLoader, VAELoader, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 999, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/ace1.5音乐生成_2018972681219088385.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/ace1.5音乐生成_2018972681219088385.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（16 个）：
- `KSampler` ★核心
- `PrimitiveNode`
- `VAEDecodeAudio` ★核心
- `ConditioningZeroOut`
- `MarkdownNote`
- `ModelSamplingAuraFlow`
- `SaveAudioMP3`
- `PrimitiveNode`
- `EmptyAceStep1.5LatentAudio`
- `TextEncodeAceStepAudio1.5`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `999`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`KSampler`、`VAEDecodeAudio`、`ConditioningZeroOut`、`ModelSamplingAuraFlow`、`SaveAudioMP3`、`EmptyAceStep1.5LatentAudio`、`TextEncodeAceStepAudio1.5`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`LoadImage`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、LoadImage、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

---
key: 音频生成/音频生成/ace1.5词生歌_2084554800502501377.json
name: ace1.5词生歌_2084554800502501377
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/ace1.5词生歌_2084554800502501377.json
hash: 15b181b57dcc737b
coverage: 0.666667
learned_at: 2026-10-18 03:04:58
nodes: [ConditioningZeroOut, KSampler, EmptyAceStep1.5LatentAudio, ModelSamplingAuraFlow, VAEDecodeAudio, PrimitiveNode, SaveAudioMP3, UNETLoader, DualCLIPLoader, VAELoader, PrimitiveNode, TextEncodeAceStepAudio1.5, MarkdownNote, MarkdownNote, MarkdownNote]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 302934198755327, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/ace1.5词生歌_2084554800502501377.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/ace1.5词生歌_2084554800502501377.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（15 个）：
- `ConditioningZeroOut`
- `KSampler` ★核心
- `EmptyAceStep1.5LatentAudio`
- `ModelSamplingAuraFlow`
- `VAEDecodeAudio` ★核心
- `PrimitiveNode`
- `SaveAudioMP3`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `PrimitiveNode`
- `TextEncodeAceStepAudio1.5`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`

## 关键参数

- `seed` = `302934198755327`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **67%**（10/15）

**有卡**：`ConditioningZeroOut`、`KSampler`、`EmptyAceStep1.5LatentAudio`、`ModelSamplingAuraFlow`、`VAEDecodeAudio`、`SaveAudioMP3`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`TextEncodeAceStepAudio1.5`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、SaveAudioMP3

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

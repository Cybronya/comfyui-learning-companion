---
key: 音频生成/音频生成/Acestep1.5音乐制作_2043518374143070209.json
name: Acestep1.5音乐制作_2043518374143070209
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/Acestep1.5音乐制作_2043518374143070209.json
hash: e69587418651e8a6
coverage: 0.666667
learned_at: 2026-10-18 02:28:38
nodes: [PrimitiveNode, VAEDecodeAudio, ConditioningZeroOut, MarkdownNote, DualCLIPLoader, VAELoader, ModelSamplingAuraFlow, EmptyAceStep1.5LatentAudio, TextEncodeAceStepAudio1.5, SaveAudioMP3, UNETLoader, KSampler, PrimitiveStringMultiline, PrimitiveFloat, PrimitiveStringMultiline]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 7, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 479676932623786, "steps": 50}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/Acestep1.5音乐制作_2043518374143070209.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/Acestep1.5音乐制作_2043518374143070209.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（15 个）：
- `PrimitiveNode`
- `VAEDecodeAudio` ★核心
- `ConditioningZeroOut`
- `MarkdownNote`
- `DualCLIPLoader`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `EmptyAceStep1.5LatentAudio`
- `TextEncodeAceStepAudio1.5`
- `SaveAudioMP3`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `PrimitiveStringMultiline`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `479676932623786`
- `steps` = `50`
- `cfg` = `7`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **67%**（10/15）

**有卡**：`VAEDecodeAudio`、`ConditioningZeroOut`、`DualCLIPLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`EmptyAceStep1.5LatentAudio`、`TextEncodeAceStepAudio1.5`、`SaveAudioMP3`、`UNETLoader`、`KSampler`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、SaveAudioMP3

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

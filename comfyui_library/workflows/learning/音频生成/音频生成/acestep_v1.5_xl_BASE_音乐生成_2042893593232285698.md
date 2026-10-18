---
key: 音频生成/音频生成/acestep_v1.5_xl_BASE_音乐生成_2042893593232285698.json
name: acestep_v1.5_xl_BASE_音乐生成_2042893593232285698
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/acestep_v1.5_xl_BASE_音乐生成_2042893593232285698.json
hash: e14bd4fb68a4f327
coverage: 0.705882
learned_at: 2026-10-18 02:28:45
nodes: [LoadImage, PrimitiveNode, VAEDecodeAudio, ConditioningZeroOut, MarkdownNote, PrimitiveStringMultiline, PrimitiveStringMultiline, DualCLIPLoader, VAELoader, ModelSamplingAuraFlow, EmptyAceStep1.5LatentAudio, LoadImage, TextEncodeAceStepAudio1.5, UNETLoader, KSampler, SaveAudioMP3, PrimitiveFloat]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 454214030870663, "steps": 50}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/acestep_v1.5_xl_BASE_音乐生成_2042893593232285698.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/acestep_v1.5_xl_BASE_音乐生成_2042893593232285698.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（17 个）：
- `LoadImage`
- `PrimitiveNode`
- `VAEDecodeAudio` ★核心
- `ConditioningZeroOut`
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `DualCLIPLoader`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `EmptyAceStep1.5LatentAudio`
- `LoadImage`
- `TextEncodeAceStepAudio1.5`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `SaveAudioMP3`
- `PrimitiveFloat`

## 关键参数

- `seed` = `454214030870663`
- `steps` = `50`
- `cfg` = `6`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **71%**（12/17）

**有卡**：`LoadImage`、`VAEDecodeAudio`、`ConditioningZeroOut`、`DualCLIPLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`EmptyAceStep1.5LatentAudio`、`TextEncodeAceStepAudio1.5`、`UNETLoader`、`KSampler`、`SaveAudioMP3`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、LoadImage、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

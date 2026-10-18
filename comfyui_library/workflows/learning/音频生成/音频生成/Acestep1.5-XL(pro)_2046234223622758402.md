---
key: 音频生成/音频生成/Acestep1.5-XL(pro)_2046234223622758402.json
name: Acestep1.5-XL(pro)_2046234223622758402
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/Acestep1.5-XL(pro)_2046234223622758402.json
hash: ddabfbbfbf8f0648
coverage: 0.923077
learned_at: 2026-10-18 03:04:47
nodes: [ModelSamplingAuraFlow, VAEDecodeAudio, ConditioningZeroOut, EmptyAceStep1.5LatentAudio, TextEncodeAceStepAudio1.5, UNETLoader, KSampler, CR Text, CR Text, VAELoader, MarkdownNote, SaveAudioMP3, DualCLIPLoader]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 893420317100010, "steps": 50}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/Acestep1.5-XL(pro)_2046234223622758402.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/Acestep1.5-XL(pro)_2046234223622758402.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（13 个）：
- `ModelSamplingAuraFlow`
- `VAEDecodeAudio` ★核心
- `ConditioningZeroOut`
- `EmptyAceStep1.5LatentAudio`
- `TextEncodeAceStepAudio1.5`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CR Text`
- `CR Text`
- `VAELoader`
- `MarkdownNote`
- `SaveAudioMP3`
- `DualCLIPLoader`

## 关键参数

- `seed` = `893420317100010`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`ModelSamplingAuraFlow`、`VAEDecodeAudio`、`ConditioningZeroOut`、`EmptyAceStep1.5LatentAudio`、`TextEncodeAceStepAudio1.5`、`UNETLoader`、`KSampler`、`CR Text`、`VAELoader`、`SaveAudioMP3`、`DualCLIPLoader`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、SaveAudioMP3

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

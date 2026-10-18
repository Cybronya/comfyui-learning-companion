---
key: 音频生成/音频生成/acestep_v1.5_xl_turbo 音乐生成_2016715807329361921.json
name: acestep_v1.5_xl_turbo 音乐生成_2016715807329361921
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/acestep_v1.5_xl_turbo 音乐生成_2016715807329361921.json
hash: f9a7cf902fa37595
coverage: 0.705882
learned_at: 2026-10-18 02:07:08
nodes: [LoadImage, PrimitiveNode, KSampler, VAEDecodeAudio, ConditioningZeroOut, MarkdownNote, PrimitiveStringMultiline, PrimitiveStringMultiline, DualCLIPLoader, VAELoader, PrimitiveFloat, SaveAudioMP3, ModelSamplingAuraFlow, EmptyAceStep1.5LatentAudio, UNETLoader, LoadImage, TextEncodeAceStepAudio1.5]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 233765767561453, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/acestep_v1.5_xl_turbo 音乐生成_2016715807329361921.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/acestep_v1.5_xl_turbo 音乐生成_2016715807329361921.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（17 个）：
- `LoadImage`
- `PrimitiveNode`
- `KSampler` ★核心
- `VAEDecodeAudio` ★核心
- `ConditioningZeroOut`
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `DualCLIPLoader`
- `VAELoader`
- `PrimitiveFloat`
- `SaveAudioMP3`
- `ModelSamplingAuraFlow`
- `EmptyAceStep1.5LatentAudio`
- `UNETLoader` ★核心
- `LoadImage`
- `TextEncodeAceStepAudio1.5`

## 关键参数

- `seed` = `233765767561453`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **71%**（12/17）

**有卡**：`LoadImage`、`KSampler`、`VAEDecodeAudio`、`ConditioningZeroOut`、`DualCLIPLoader`、`VAELoader`、`SaveAudioMP3`、`ModelSamplingAuraFlow`、`EmptyAceStep1.5LatentAudio`、`UNETLoader`、`TextEncodeAceStepAudio1.5`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、LoadImage、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

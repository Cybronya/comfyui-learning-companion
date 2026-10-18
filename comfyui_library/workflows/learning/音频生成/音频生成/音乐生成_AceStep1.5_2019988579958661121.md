---
key: 音频生成/音频生成/音乐生成_AceStep1.5_2019988579958661121.json
name: 音乐生成_AceStep1.5_2019988579958661121
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/音乐生成_AceStep1.5_2019988579958661121.json
hash: b20008d5671af8bb
coverage: 0.543478
learned_at: 2026-10-18 02:07:13
nodes: [KSampler, StringConcatenate, Reroute, Reroute, ModelSamplingAuraFlow, Reroute, easy showAnything, easy showAnything, MarkdownNote, Reroute, Reroute, Reroute, Reroute, StringConcatenate, StringTrim, StringConcatenate, SomethingToString, TextEncodeAceStepAudio1.5, VAEDecodeAudio, SaveStringKJ, Note, PreviewAny, PreviewAny, PrimitiveInt, SomethingToString, ConditioningZeroOut, StringConcatenate, Reroute, Note, Seed (rgthree), easy showAnything, easy showAnything, PrimitiveStringMultiline, EmptyAceStep1.5LatentAudio, easy float, PrimitiveStringMultiline, SaveAudio, easy showAnything, StringConcatenate, Qwen3_VQA, Seed (rgthree), JWStringSplit, JWStringSplit, UNETLoader, DualCLIPLoader, VAELoader]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 31, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/音乐生成_AceStep1.5_2019988579958661121.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/音乐生成_AceStep1.5_2019988579958661121.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（46 个）：
- `KSampler` ★核心
- `StringConcatenate`
- `Reroute`
- `Reroute`
- `ModelSamplingAuraFlow`
- `Reroute`
- `easy showAnything`
- `easy showAnything`
- `MarkdownNote`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `StringConcatenate`
- `StringTrim`
- `StringConcatenate`
- `SomethingToString`
- `TextEncodeAceStepAudio1.5`
- `VAEDecodeAudio` ★核心
- `SaveStringKJ`
- `Note`
- `PreviewAny`
- `PreviewAny`
- `PrimitiveInt`
- `SomethingToString`
- `ConditioningZeroOut`
- `StringConcatenate`
- `Reroute`
- `Note`
- `Seed (rgthree)`
- `easy showAnything`
- `easy showAnything`
- `PrimitiveStringMultiline`
- `EmptyAceStep1.5LatentAudio`
- `easy float`
- `PrimitiveStringMultiline`
- `SaveAudio`
- `easy showAnything`
- `StringConcatenate`
- `Qwen3_VQA`
- `Seed (rgthree)`
- `JWStringSplit`
- `JWStringSplit`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`

## 关键参数

- `seed` = `31`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **54%**（25/46）

**有卡**：`KSampler`、`StringConcatenate`、`ModelSamplingAuraFlow`、`StringTrim`、`SomethingToString`、`TextEncodeAceStepAudio1.5`、`VAEDecodeAudio`、`SaveStringKJ`、`ConditioningZeroOut`、`Seed (rgthree)`、`EmptyAceStep1.5LatentAudio`、`easy float`、`SaveAudio`、`Qwen3_VQA`、`JWStringSplit`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、UNETLoader、Seed (rgthree)、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

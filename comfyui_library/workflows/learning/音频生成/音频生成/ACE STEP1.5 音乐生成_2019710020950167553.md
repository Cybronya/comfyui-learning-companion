---
key: 音频生成/音频生成/ACE STEP1.5 音乐生成_2019710020950167553.json
name: ACE STEP1.5 音乐生成_2019710020950167553
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/ACE STEP1.5 音乐生成_2019710020950167553.json
hash: 5278c88d69c0ffbc
coverage: 0.764706
learned_at: 2026-10-18 02:06:52
nodes: [VAEDecodeAudio, ModelSamplingAuraFlow, ConditioningZeroOut, KSampler, VAELoader, DualCLIPLoader, UNETLoader, EmptyAceStep1.5LatentAudio, SaveAudioMP3, PrimitiveNode, TextEncodeAceStepAudio1.5, CR Prompt Text, CR Prompt Text, Float, Note, Note, Note]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 421313169480682, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/ACE STEP1.5 音乐生成_2019710020950167553.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/ACE STEP1.5 音乐生成_2019710020950167553.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（17 个）：
- `VAEDecodeAudio` ★核心
- `ModelSamplingAuraFlow`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `EmptyAceStep1.5LatentAudio`
- `SaveAudioMP3`
- `PrimitiveNode`
- `TextEncodeAceStepAudio1.5`
- `CR Prompt Text`
- `CR Prompt Text`
- `Float`
- `Note`
- `Note`
- `Note`

## 关键参数

- `seed` = `421313169480682`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **76%**（13/17）

**有卡**：`VAEDecodeAudio`、`ModelSamplingAuraFlow`、`ConditioningZeroOut`、`KSampler`、`VAELoader`、`DualCLIPLoader`、`UNETLoader`、`EmptyAceStep1.5LatentAudio`、`SaveAudioMP3`、`TextEncodeAceStepAudio1.5`、`CR Prompt Text`、`Float`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、CR Prompt Text

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

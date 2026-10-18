---
key: 音频生成/音频生成/ace1.5 多语言风格音乐生成_2019227846987751425.json
name: ace1.5 多语言风格音乐生成_2019227846987751425
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/ace1.5 多语言风格音乐生成_2019227846987751425.json
hash: bddde8fdc1399cba
coverage: 0.6875
learned_at: 2026-10-18 02:07:08
nodes: [KSampler, VAEDecodeAudio, ConditioningZeroOut, ModelSamplingAuraFlow, UNETLoader, DualCLIPLoader, Note, Note, Note, SaveAudioMP3, CR Prompt Text, EmptyAceStep1.5LatentAudio, TextEncodeAceStepAudio1.5, VAELoader, PrimitiveInt, PrimitiveNode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 999, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/ace1.5 多语言风格音乐生成_2019227846987751425.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/ace1.5 多语言风格音乐生成_2019227846987751425.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（16 个）：
- `KSampler` ★核心
- `VAEDecodeAudio` ★核心
- `ConditioningZeroOut`
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `Note`
- `Note`
- `Note`
- `SaveAudioMP3`
- `CR Prompt Text`
- `EmptyAceStep1.5LatentAudio`
- `TextEncodeAceStepAudio1.5`
- `VAELoader`
- `PrimitiveInt`
- `PrimitiveNode`

## 关键参数

- `seed` = `999`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **69%**（11/16）

**有卡**：`KSampler`、`VAEDecodeAudio`、`ConditioningZeroOut`、`ModelSamplingAuraFlow`、`UNETLoader`、`DualCLIPLoader`、`SaveAudioMP3`、`CR Prompt Text`、`EmptyAceStep1.5LatentAudio`、`TextEncodeAceStepAudio1.5`、`VAELoader`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、CR Prompt Text

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

---
key: 音频生成/音频生成/苏伦特ACE-step-1.5_2022764315853463554.json
name: 苏伦特ACE-step-1.5_2022764315853463554
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/苏伦特ACE-step-1.5_2022764315853463554.json
hash: 43b01fc7e4c87008
coverage: 0.764706
learned_at: 2026-10-18 02:07:12
nodes: [VAEDecodeAudio, ModelSamplingAuraFlow, ConditioningZeroOut, KSampler, VAELoader, DualCLIPLoader, UNETLoader, EmptyAceStep1.5LatentAudio, SaveAudioMP3, PrimitiveNode, TextEncodeAceStepAudio1.5, Note, Note, Note, Float, CR Prompt Text, CR Prompt Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 324864822668343, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/苏伦特ACE-step-1.5_2022764315853463554.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/苏伦特ACE-step-1.5_2022764315853463554.json`

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
- `Note`
- `Note`
- `Note`
- `Float`
- `CR Prompt Text`
- `CR Prompt Text`

## 关键参数

- `seed` = `324864822668343`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **76%**（13/17）

**有卡**：`VAEDecodeAudio`、`ModelSamplingAuraFlow`、`ConditioningZeroOut`、`KSampler`、`VAELoader`、`DualCLIPLoader`、`UNETLoader`、`EmptyAceStep1.5LatentAudio`、`SaveAudioMP3`、`TextEncodeAceStepAudio1.5`、`Float`、`CR Prompt Text`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、CR Prompt Text

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

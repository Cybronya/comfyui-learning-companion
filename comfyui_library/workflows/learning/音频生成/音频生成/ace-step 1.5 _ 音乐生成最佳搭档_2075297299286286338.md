---
key: 音频生成/音频生成/ace-step 1.5 _ 音乐生成最佳搭档_2075297299286286338.json
name: ace-step 1.5 _ 音乐生成最佳搭档_2075297299286286338
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/ace-step 1.5 _ 音乐生成最佳搭档_2075297299286286338.json
hash: 1ee75b79d86fd641
coverage: 0.933333
learned_at: 2026-10-18 03:04:58
nodes: [PrimitiveInt, EmptyAceStep1.5LatentAudio, ConditioningZeroOut, Float, Int, ModelSamplingAuraFlow, VAEDecodeAudio, KSampler, SaveAudioMP3, UNETLoader, CR Text, CR Text, TextEncodeAceStepAudio1.5, DualCLIPLoader, VAELoader]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/ace-step 1.5 _ 音乐生成最佳搭档_2075297299286286338.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/ace-step 1.5 _ 音乐生成最佳搭档_2075297299286286338.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（15 个）：
- `PrimitiveInt`
- `EmptyAceStep1.5LatentAudio`
- `ConditioningZeroOut`
- `Float`
- `Int`
- `ModelSamplingAuraFlow`
- `VAEDecodeAudio` ★核心
- `KSampler` ★核心
- `SaveAudioMP3`
- `UNETLoader` ★核心
- `CR Text`
- `CR Text`
- `TextEncodeAceStepAudio1.5`
- `DualCLIPLoader`
- `VAELoader`

## 关键参数

- `seed` = `0`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（14/15）

**有卡**：`EmptyAceStep1.5LatentAudio`、`ConditioningZeroOut`、`Float`、`Int`、`ModelSamplingAuraFlow`、`VAEDecodeAudio`、`KSampler`、`SaveAudioMP3`、`UNETLoader`、`CR Text`、`TextEncodeAceStepAudio1.5`、`DualCLIPLoader`、`VAELoader`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、SaveAudioMP3

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

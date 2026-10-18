---
key: 音频生成/音频生成/Ace-Step1.5X工作流(打造你的专属音乐)_2054411129350311938.json
name: Ace-Step1.5X工作流(打造你的专属音乐)_2054411129350311938
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/Ace-Step1.5X工作流(打造你的专属音乐)_2054411129350311938.json
hash: adde6c7836305a1c
coverage: 0.923077
learned_at: 2026-10-18 03:04:47
nodes: [VAELoader, VAEDecodeAudio, KSampler, ModelSamplingAuraFlow, EmptyAceStep1.5LatentAudio, ConditioningZeroOut, SaveAudioMP3, Float, PrimitiveInt, Int, TextEncodeAceStepAudio1.5, UNETLoader, DualCLIPLoader]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/Ace-Step1.5X工作流(打造你的专属音乐)_2054411129350311938.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/Ace-Step1.5X工作流(打造你的专属音乐)_2054411129350311938.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（13 个）：
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `KSampler` ★核心
- `ModelSamplingAuraFlow`
- `EmptyAceStep1.5LatentAudio`
- `ConditioningZeroOut`
- `SaveAudioMP3`
- `Float`
- `PrimitiveInt`
- `Int`
- `TextEncodeAceStepAudio1.5`
- `UNETLoader` ★核心
- `DualCLIPLoader`

## 关键参数

- `seed` = `0`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`VAELoader`、`VAEDecodeAudio`、`KSampler`、`ModelSamplingAuraFlow`、`EmptyAceStep1.5LatentAudio`、`ConditioningZeroOut`、`SaveAudioMP3`、`Float`、`Int`、`TextEncodeAceStepAudio1.5`、`UNETLoader`、`DualCLIPLoader`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、SaveAudioMP3

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

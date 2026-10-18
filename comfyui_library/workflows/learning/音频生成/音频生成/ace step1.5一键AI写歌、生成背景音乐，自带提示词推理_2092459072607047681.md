---
key: 音频生成/音频生成/ace step1.5一键AI写歌、生成背景音乐，自带提示词推理_2092459072607047681.json
name: ace step1.5一键AI写歌、生成背景音乐，自带提示词推理_2092459072607047681
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/ace step1.5一键AI写歌、生成背景音乐，自带提示词推理_2092459072607047681.json
hash: 32c06bf21fdd86d8
coverage: 0.846154
learned_at: 2026-10-18 17:45:47
nodes: [KSampler, ConditioningZeroOut, ModelSamplingAuraFlow, VAEDecodeAudio, PrimitiveInt, DualCLIPLoader, VAELoader, EmptyAceStep1.5LatentAudio, SaveAudioMP3, MarkdownNote, AceStepLLMSongPlanner, llama_cpp_model_loader, UNETLoader]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1012485216660077, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/ace step1.5一键AI写歌、生成背景音乐，自带提示词推理_2092459072607047681.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/ace step1.5一键AI写歌、生成背景音乐，自带提示词推理_2092459072607047681.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（13 个）：
- `KSampler` ★核心
- `ConditioningZeroOut`
- `ModelSamplingAuraFlow`
- `VAEDecodeAudio` ★核心
- `PrimitiveInt`
- `DualCLIPLoader`
- `VAELoader`
- `EmptyAceStep1.5LatentAudio`
- `SaveAudioMP3`
- `MarkdownNote`
- `AceStepLLMSongPlanner`
- `llama_cpp_model_loader`
- `UNETLoader` ★核心

## 关键参数

- `seed` = `1012485216660077`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（11/13）

**有卡**：`KSampler`、`ConditioningZeroOut`、`ModelSamplingAuraFlow`、`VAEDecodeAudio`、`DualCLIPLoader`、`VAELoader`、`EmptyAceStep1.5LatentAudio`、`SaveAudioMP3`、`AceStepLLMSongPlanner`、`llama_cpp_model_loader`、`UNETLoader`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、SaveAudioMP3、DualCLIPLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

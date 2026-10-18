---
key: 音频生成/音频生成/ACE-Step1.5 XL-自动生成歌词歌曲_2046006292061364225.json
name: ACE-Step1.5 XL-自动生成歌词歌曲_2046006292061364225
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/ACE-Step1.5 XL-自动生成歌词歌曲_2046006292061364225.json
hash: 147457799d8f3ee7
coverage: 0.7
learned_at: 2026-10-18 03:04:46
nodes: [ConditioningZeroOut, PrimitiveInt, easy cleanGpuUsed, llama_cpp_model_loader, llama_cpp_parameters, llama_cpp_parameters, llama_cpp_model_loader, Reroute, Reroute, llama_cpp_instruct_adv, AudioQualityEffects, AudioQualityEnhancer, SaveAudioMP3, easy cleanGpuUsed, SaveAudioMP3, easy cleanGpuUsed, ModelSamplingAuraFlow, KSampler, EmptyAceStep1.5LatentAudio, UNETLoader, DualCLIPLoader, VAELoader, VAEDecodeAudio, Reroute, easy cleanGpuUsed, Reroute, llama_cpp_instruct_adv, TextEncodeAceStepAudio1.5, TextInput_, TextInput_, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), PrimitiveNode, ShowText|pysssss, TextInput_, TextInput_, Note, ShowText|pysssss, TextInput_, Note]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/ACE-Step1.5 XL-自动生成歌词歌曲_2046006292061364225.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/ACE-Step1.5 XL-自动生成歌词歌曲_2046006292061364225.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（40 个）：
- `ConditioningZeroOut`
- `PrimitiveInt`
- `easy cleanGpuUsed`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `Reroute`
- `Reroute`
- `llama_cpp_instruct_adv`
- `AudioQualityEffects`
- `AudioQualityEnhancer`
- `SaveAudioMP3`
- `easy cleanGpuUsed`
- `SaveAudioMP3`
- `easy cleanGpuUsed`
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `EmptyAceStep1.5LatentAudio`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `Reroute`
- `easy cleanGpuUsed`
- `Reroute`
- `llama_cpp_instruct_adv`
- `TextEncodeAceStepAudio1.5`
- `TextInput_`
- `TextInput_`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveNode`
- `ShowText|pysssss`
- `TextInput_`
- `TextInput_`
- `Note`
- `ShowText|pysssss`
- `TextInput_`
- `Note`

## 关键参数

- `seed` = `0`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **70%**（28/40）

**有卡**：`ConditioningZeroOut`、`easy cleanGpuUsed`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`AudioQualityEffects`、`AudioQualityEnhancer`、`SaveAudioMP3`、`ModelSamplingAuraFlow`、`KSampler`、`EmptyAceStep1.5LatentAudio`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`VAEDecodeAudio`、`TextEncodeAceStepAudio1.5`、`TextInput_`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、UNETLoader、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、SaveAudioMP3

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

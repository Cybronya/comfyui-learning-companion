---
key: 音频生成/音频生成/ACE Step1.5+qwen3.5歌词歌曲创作_2046534389982564354.json
name: ACE Step1.5+qwen3.5歌词歌曲创作_2046534389982564354
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/ACE Step1.5+qwen3.5歌词歌曲创作_2046534389982564354.json
hash: 40d3cbeb8e90af73
coverage: 0.772727
learned_at: 2026-10-18 03:04:46
nodes: [VAEDecodeAudio, PrimitiveFloat, ModelSamplingAuraFlow, easy seed, EmptyAceStep1.5LatentAudio, llama_cpp_parameters, ShowText|pysssss, SaveAudioMP3, ConditioningZeroOut, RegexExtract, llama_cpp_model_loader, UNETLoader, DualCLIPLoader, VAELoader, TextEncodeAceStepAudio1.5, ShowText|pysssss, ShowText|pysssss, ShowText|pysssss, RegexExtract, llama_cpp_instruct_adv, Text, KSampler]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1105896572181409, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/ACE Step1.5+qwen3.5歌词歌曲创作_2046534389982564354.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/ACE Step1.5+qwen3.5歌词歌曲创作_2046534389982564354.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（22 个）：
- `VAEDecodeAudio` ★核心
- `PrimitiveFloat`
- `ModelSamplingAuraFlow`
- `easy seed`
- `EmptyAceStep1.5LatentAudio`
- `llama_cpp_parameters`
- `ShowText|pysssss`
- `SaveAudioMP3`
- `ConditioningZeroOut`
- `RegexExtract`
- `llama_cpp_model_loader`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `TextEncodeAceStepAudio1.5`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `RegexExtract`
- `llama_cpp_instruct_adv`
- `Text`
- `KSampler` ★核心

## 关键参数

- `seed` = `1105896572181409`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **77%**（17/22）

**有卡**：`VAEDecodeAudio`、`ModelSamplingAuraFlow`、`easy seed`、`EmptyAceStep1.5LatentAudio`、`llama_cpp_parameters`、`SaveAudioMP3`、`ConditioningZeroOut`、`RegexExtract`、`llama_cpp_model_loader`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`TextEncodeAceStepAudio1.5`、`llama_cpp_instruct_adv`、`Text`、`KSampler`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、UNETLoader、easy seed、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

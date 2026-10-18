---
key: 音频生成/音频生成/ACE Step 1.5 XL All-In-One 歌词注入版-MV-音乐生成（内部开发用）_2081784806165274625.json
name: ACE Step 1.5 XL All-In-One 歌词注入版-MV-音乐生成（内部开发用）_2081784806165274625
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/ACE Step 1.5 XL All-In-One 歌词注入版-MV-音乐生成（内部开发用）_2081784806165274625.json
hash: 56c489801fe1ea3a
coverage: 0.511111
learned_at: 2026-10-18 03:04:46
nodes: [easy showAnything, easy showAnything, JWStringToInteger, RegexExtract, easy showAnything, easy showAnything, easy showAnything, easy showAnything, ModelSamplingAuraFlow, SetNode, RegexExtract, GetNode, KSampler, SetNode, CR Seed, ShowText|pysssss, ShowText|pysssss, RegexExtract, SetNode, Text Concatenate, GetNode, ttN text, easy showAnything, easy showAnything, RegexExtract, DualCLIPLoader, DiffusionModelLoaderKJ, Note, ShowText|pysssss, ShowText|pysssss, ShowText|pysssss, SaveAudioMP3, GetNode, EmptyAceStep1.5LatentAudio, GetNode, ConditioningZeroOut, RegexExtract, RegexExtract, RegexExtract, easy cleanGpuUsed, VAEDecodeAudio, TextEncodeAceStepAudio1.5, VAELoader, PrimitiveNode, ttN text]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 133474517518198, "steps": 20}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/ACE Step 1.5 XL All-In-One 歌词注入版-MV-音乐生成（内部开发用）_2081784806165274625.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/ACE Step 1.5 XL All-In-One 歌词注入版-MV-音乐生成（内部开发用）_2081784806165274625.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（45 个）：
- `easy showAnything`
- `easy showAnything`
- `JWStringToInteger`
- `RegexExtract`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `ModelSamplingAuraFlow`
- `SetNode`
- `RegexExtract`
- `GetNode`
- `KSampler` ★核心
- `SetNode`
- `CR Seed`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `RegexExtract`
- `SetNode`
- `Text Concatenate`
- `GetNode`
- `ttN text`
- `easy showAnything`
- `easy showAnything`
- `RegexExtract`
- `DualCLIPLoader`
- `DiffusionModelLoaderKJ`
- `Note`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `SaveAudioMP3`
- `GetNode`
- `EmptyAceStep1.5LatentAudio`
- `GetNode`
- `ConditioningZeroOut`
- `RegexExtract`
- `RegexExtract`
- `RegexExtract`
- `easy cleanGpuUsed`
- `VAEDecodeAudio` ★核心
- `TextEncodeAceStepAudio1.5`
- `VAELoader`
- `PrimitiveNode`
- `ttN text`

## 关键参数

- `seed` = `133474517518198`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **51%**（23/45）

**有卡**：`JWStringToInteger`、`RegexExtract`、`ModelSamplingAuraFlow`、`KSampler`、`CR Seed`、`Text Concatenate`、`ttN text`、`DualCLIPLoader`、`DiffusionModelLoaderKJ`、`SaveAudioMP3`、`EmptyAceStep1.5LatentAudio`、`ConditioningZeroOut`、`easy cleanGpuUsed`、`VAEDecodeAudio`、`TextEncodeAceStepAudio1.5`、`VAELoader`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、CR Seed、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5、SaveAudioMP3

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

---
key: 音频生成/音频生成/ACE Step 1.5 XL All-In-One LLM自动提示词-MV-音乐生成_2081707754602975234.json
name: ACE Step 1.5 XL All-In-One LLM自动提示词-MV-音乐生成_2081707754602975234
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/ACE Step 1.5 XL All-In-One LLM自动提示词-MV-音乐生成_2081707754602975234.json
hash: 0914d137035b7c74
coverage: 0.64557
learned_at: 2026-10-18 03:04:45
nodes: [easy showAnything, easy showAnything, JWStringToInteger, RegexExtract, easy showAnything, easy showAnything, easy showAnything, easy showAnything, ModelSamplingAuraFlow, ttN text, EmptyImage, INTConstant, RegexExtract, KSampler, SetNode, CR Seed, ttN text, easy showAnything, Apply Whisper, ShowText|pysssss, ShowText|pysssss, ttN concat, ImageMaskSwitch, RegexExtract, SetNode, ShowText|pysssss, Text Concatenate, GetNode, ttN text, Text Concatenate, easy showAnything, easy showAnything, ttN concat, Text Concatenate, DualCLIPLoader, RegexExtract, DualCLIPLoader, DiffusionModelLoaderKJ, GetNode, ShowText|pysssss, Note, ShowText|pysssss, GetNode, ConditioningZeroOut, AudioInfo, RegexExtract, RegexExtract, RegexExtract, easy cleanGpuUsed, VAEDecodeAudio, VAELoader, LoadImage, Reroute, Any To Any, LoadAudioUI, Any To Any, Any To Any, easy float, GetNode, CR Integer To String, PreviewAny, CR Text Concatenate, ShowText|pysssss, ShowText|pysssss, Any Switch (rgthree), ttN text, ttN text, ShowText|pysssss, Any Switch (rgthree), ttN concat, ttN concat, easy float, TextGenerate, easy float, SaveAudioMP3, EmptyAceStep1.5LatentAudio, Any To Any, easy float, TextEncodeAceStepAudio1.5]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 502104302241813, "steps": 20}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/ACE Step 1.5 XL All-In-One LLM自动提示词-MV-音乐生成_2081707754602975234.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/ACE Step 1.5 XL All-In-One LLM自动提示词-MV-音乐生成_2081707754602975234.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（79 个）：
- `easy showAnything`
- `easy showAnything`
- `JWStringToInteger`
- `RegexExtract`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `ModelSamplingAuraFlow`
- `ttN text`
- `EmptyImage`
- `INTConstant`
- `RegexExtract`
- `KSampler` ★核心
- `SetNode`
- `CR Seed`
- `ttN text`
- `easy showAnything`
- `Apply Whisper`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `ttN concat`
- `ImageMaskSwitch`
- `RegexExtract`
- `SetNode`
- `ShowText|pysssss`
- `Text Concatenate`
- `GetNode`
- `ttN text`
- `Text Concatenate`
- `easy showAnything`
- `easy showAnything`
- `ttN concat`
- `Text Concatenate`
- `DualCLIPLoader`
- `RegexExtract`
- `DualCLIPLoader`
- `DiffusionModelLoaderKJ`
- `GetNode`
- `ShowText|pysssss`
- `Note`
- `ShowText|pysssss`
- `GetNode`
- `ConditioningZeroOut`
- `AudioInfo`
- `RegexExtract`
- `RegexExtract`
- `RegexExtract`
- `easy cleanGpuUsed`
- `VAEDecodeAudio` ★核心
- `VAELoader`
- `LoadImage`
- `Reroute`
- `Any To Any`
- `LoadAudioUI`
- `Any To Any`
- `Any To Any`
- `easy float`
- `GetNode`
- `CR Integer To String`
- `PreviewAny`
- `CR Text Concatenate`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `Any Switch (rgthree)`
- `ttN text`
- `ttN text`
- `ShowText|pysssss`
- `Any Switch (rgthree)`
- `ttN concat`
- `ttN concat`
- `easy float`
- `TextGenerate`
- `easy float`
- `SaveAudioMP3`
- `EmptyAceStep1.5LatentAudio`
- `Any To Any`
- `easy float`
- `TextEncodeAceStepAudio1.5`

## 关键参数

- `seed` = `502104302241813`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **65%**（51/79）

**有卡**：`JWStringToInteger`、`RegexExtract`、`ModelSamplingAuraFlow`、`ttN text`、`EmptyImage`、`INTConstant`、`KSampler`、`CR Seed`、`Apply Whisper`、`ttN concat`、`ImageMaskSwitch`、`Text Concatenate`、`DualCLIPLoader`、`DiffusionModelLoaderKJ`、`ConditioningZeroOut`、`AudioInfo`、`easy cleanGpuUsed`、`VAEDecodeAudio`、`VAELoader`、`LoadImage`、`Any To Any`、`LoadAudioUI`、`easy float`、`CR Integer To String`、`CR Text Concatenate`、`TextGenerate`、`SaveAudioMP3`、`EmptyAceStep1.5LatentAudio`、`TextEncodeAceStepAudio1.5`

**用到的条目**：KSampler、VAELoader、ConditioningZeroOut、LoadImage、CR Seed、VAEDecodeAudio、EmptyAceStep1.5LatentAudio、TextEncodeAceStepAudio1.5

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

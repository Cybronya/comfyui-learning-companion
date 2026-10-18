---
key: 音频生成/音频生成/Stable Audio 3音乐音效VFXOneShot生成_2059069757013450754.json
name: Stable Audio 3音乐音效VFXOneShot生成_2059069757013450754
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/Stable Audio 3音乐音效VFXOneShot生成_2059069757013450754.json
hash: 9718e8acb00340c5
coverage: 0.821429
learned_at: 2026-10-18 03:04:56
nodes: [CLIPTextEncode, CLIPTextEncode, PreviewAny, KSampler, VAEDecodeAudio, CLIPLoader, ComfySwitchNode, TextGenerate, CR Prompt Text, StringReplace, StringReplace, CR Prompt Text, CR Prompt Text, StringReplace, easy cleanGpuUsed, easy anythingIndexSwitch, JsonExtractString, EmptyLatentAudio, CLIPLoader, ComfyMathExpression, PreviewAny, CR Prompt Text, CheckpointLoaderSimple, PrimitiveBoolean, PrimitiveFloat, PrimitiveStringMultiline, SaveAudioMP3, SaveAudio]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "stable_audio_3_medium_20260526.safetensors", "denoise": 1, "height": 1, "sampler_name": "lcm", "scheduler": "simple", "seed": 55474776762621, "steps": 8, "width": 60}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/Stable Audio 3音乐音效VFXOneShot生成_2059069757013450754.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/Stable Audio 3音乐音效VFXOneShot生成_2059069757013450754.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（28 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PreviewAny`
- `KSampler` ★核心
- `VAEDecodeAudio` ★核心
- `CLIPLoader`
- `ComfySwitchNode`
- `TextGenerate`
- `CR Prompt Text`
- `StringReplace`
- `StringReplace`
- `CR Prompt Text`
- `CR Prompt Text`
- `StringReplace`
- `easy cleanGpuUsed`
- `easy anythingIndexSwitch`
- `JsonExtractString`
- `EmptyLatentAudio` ★核心
- `CLIPLoader`
- `ComfyMathExpression`
- `PreviewAny`
- `CR Prompt Text`
- `CheckpointLoaderSimple` ★核心
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `SaveAudioMP3`
- `SaveAudio`

## 关键参数

- `seed` = `55474776762621`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `lcm`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `60`
- `height` = `1`
- `checkpoint` = `stable_audio_3_medium_20260526.safetensors`

## 知识

覆盖率 **82%**（23/28）

**有卡**：`CLIPTextEncode`、`KSampler`、`VAEDecodeAudio`、`CLIPLoader`、`TextGenerate`、`CR Prompt Text`、`StringReplace`、`easy cleanGpuUsed`、`easy anythingIndexSwitch`、`JsonExtractString`、`EmptyLatentAudio`、`ComfyMathExpression`、`CheckpointLoaderSimple`、`PrimitiveBoolean`、`SaveAudioMP3`、`SaveAudio`

**用到的条目**：KSampler、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、VAEDecodeAudio、EmptyLatentAudio、CR Prompt Text、SaveAudio

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

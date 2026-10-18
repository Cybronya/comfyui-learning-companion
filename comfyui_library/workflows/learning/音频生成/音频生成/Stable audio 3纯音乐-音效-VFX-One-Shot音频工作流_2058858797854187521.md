---
key: 音频生成/音频生成/Stable audio 3纯音乐-音效-VFX-One-Shot音频工作流_2058858797854187521.json
name: Stable audio 3纯音乐-音效-VFX-One-Shot音频工作流_2058858797854187521
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/Stable audio 3纯音乐-音效-VFX-One-Shot音频工作流_2058858797854187521.json
hash: 79256459f3d85d63
coverage: 0.821429
learned_at: 2026-10-18 03:04:56
nodes: [CLIPTextEncode, EmptyLatentAudio, CLIPTextEncode, PreviewAny, KSampler, VAEDecodeAudio, CLIPLoader, easy cleanGpuUsed, CheckpointLoaderSimple, CLIPLoader, PrimitiveFloat, SaveAudioMP3, SaveAudio, PrimitiveBoolean, PrimitiveStringMultiline, ComfySwitchNode, TextGenerate, StringReplace, StringReplace, ComfyMathExpression, PreviewAny, StringReplace, JsonExtractString, easy anythingIndexSwitch, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "stable_audio_3_medium.safetensors", "denoise": 1, "height": 1, "sampler_name": "lcm", "scheduler": "simple", "seed": 134413461287220, "steps": 8, "width": 60}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/Stable audio 3纯音乐-音效-VFX-One-Shot音频工作流_2058858797854187521.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/Stable audio 3纯音乐-音效-VFX-One-Shot音频工作流_2058858797854187521.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（28 个）：
- `CLIPTextEncode` ★核心
- `EmptyLatentAudio` ★核心
- `CLIPTextEncode` ★核心
- `PreviewAny`
- `KSampler` ★核心
- `VAEDecodeAudio` ★核心
- `CLIPLoader`
- `easy cleanGpuUsed`
- `CheckpointLoaderSimple` ★核心
- `CLIPLoader`
- `PrimitiveFloat`
- `SaveAudioMP3`
- `SaveAudio`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `ComfySwitchNode`
- `TextGenerate`
- `StringReplace`
- `StringReplace`
- `ComfyMathExpression`
- `PreviewAny`
- `StringReplace`
- `JsonExtractString`
- `easy anythingIndexSwitch`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`

## 关键参数

- `width` = `60`
- `height` = `1`
- `seed` = `134413461287220`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `lcm`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `stable_audio_3_medium.safetensors`

## 知识

覆盖率 **82%**（23/28）

**有卡**：`CLIPTextEncode`、`EmptyLatentAudio`、`KSampler`、`VAEDecodeAudio`、`CLIPLoader`、`easy cleanGpuUsed`、`CheckpointLoaderSimple`、`SaveAudioMP3`、`SaveAudio`、`PrimitiveBoolean`、`TextGenerate`、`StringReplace`、`ComfyMathExpression`、`JsonExtractString`、`easy anythingIndexSwitch`、`CR Prompt Text`

**用到的条目**：KSampler、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、VAEDecodeAudio、EmptyLatentAudio、CR Prompt Text、SaveAudio

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

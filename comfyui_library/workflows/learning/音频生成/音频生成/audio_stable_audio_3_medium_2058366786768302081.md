---
key: 音频生成/音频生成/audio_stable_audio_3_medium_2058366786768302081.json
name: audio_stable_audio_3_medium_2058366786768302081
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/audio_stable_audio_3_medium_2058366786768302081.json
hash: d3220e0366ce4e0a
coverage: 0.71875
learned_at: 2026-10-18 03:04:58
nodes: [KSampler, ShowText|pysssss, easy anythingIndexSwitch, StringReplace, StringReplace, TextGenerate, CLIPLoader, ComfyMathExpression, PreviewAny, StringReplace, JsonExtractString, CLIPTextEncode, EmptyLatentAudio, CR Text, CR Text, CR Text, CR Text, CLIPTextEncode, MarkdownNote, MarkdownNote, VAEDecodeAudio, CheckpointLoaderSimple, CLIPLoader, ComfySwitchNode, CustomCombo, PrimitiveFloat, SaveAudioMP3, PreviewAny, PrimitiveStringMultiline, PrimitiveBoolean, Int, PrimitiveStringMultiline]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "stable_audio_3_medium.safetensors", "denoise": 1, "height": 1, "sampler_name": "lcm", "scheduler": "simple", "seed": 229048725537364, "steps": 8, "width": 60}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/audio_stable_audio_3_medium_2058366786768302081.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/audio_stable_audio_3_medium_2058366786768302081.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（32 个）：
- `KSampler` ★核心
- `ShowText|pysssss`
- `easy anythingIndexSwitch`
- `StringReplace`
- `StringReplace`
- `TextGenerate`
- `CLIPLoader`
- `ComfyMathExpression`
- `PreviewAny`
- `StringReplace`
- `JsonExtractString`
- `CLIPTextEncode` ★核心
- `EmptyLatentAudio` ★核心
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `VAEDecodeAudio` ★核心
- `CheckpointLoaderSimple` ★核心
- `CLIPLoader`
- `ComfySwitchNode`
- `CustomCombo`
- `PrimitiveFloat`
- `SaveAudioMP3`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `PrimitiveBoolean`
- `Int`
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `229048725537364`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `lcm`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `60`
- `height` = `1`
- `checkpoint` = `stable_audio_3_medium.safetensors`

## 知识

覆盖率 **72%**（23/32）

**有卡**：`KSampler`、`easy anythingIndexSwitch`、`StringReplace`、`TextGenerate`、`CLIPLoader`、`ComfyMathExpression`、`JsonExtractString`、`CLIPTextEncode`、`EmptyLatentAudio`、`CR Text`、`VAEDecodeAudio`、`CheckpointLoaderSimple`、`CustomCombo`、`SaveAudioMP3`、`PrimitiveBoolean`、`Int`

**用到的条目**：KSampler、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、VAEDecodeAudio、EmptyLatentAudio、SaveAudioMP3、ComfyMathExpression

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

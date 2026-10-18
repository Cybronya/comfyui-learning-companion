---
key: 音频生成/音频生成/【遇见AI】stable-audio-3 背景音模型small_music_2041013207766142977.json
name: 【遇见AI】stable-audio-3 背景音模型small_music_2041013207766142977
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/【遇见AI】stable-audio-3 背景音模型small_music_2041013207766142977.json
hash: 3fc3caeee4c0c5ca
coverage: 0.769231
learned_at: 2026-10-18 02:28:47
nodes: [CLIPTextEncode, VAEDecodeAudio, KSampler, CLIPTextEncode, LoadImage, MarkdownNote, LoadImage, MarkdownNote, EmptyLatentAudio, MarkdownNote, SaveAudioMP3, CLIPLoader, CheckpointLoaderSimple]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "stable_audio_3_small_music.safetensors", "denoise": 1, "height": 1, "sampler_name": "lcm", "scheduler": "simple", "seed": 388118301411304, "steps": 8, "width": 60}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/【遇见AI】stable-audio-3 背景音模型small_music_2041013207766142977.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/【遇见AI】stable-audio-3 背景音模型small_music_2041013207766142977.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
- `CLIPTextEncode` ★核心
- `VAEDecodeAudio` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `MarkdownNote`
- `LoadImage`
- `MarkdownNote`
- `EmptyLatentAudio` ★核心
- `MarkdownNote`
- `SaveAudioMP3`
- `CLIPLoader`
- `CheckpointLoaderSimple` ★核心

## 关键参数

- `seed` = `388118301411304`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `lcm`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `60`
- `height` = `1`
- `checkpoint` = `stable_audio_3_small_music.safetensors`

## 知识

覆盖率 **77%**（10/13）

**有卡**：`CLIPTextEncode`、`VAEDecodeAudio`、`KSampler`、`LoadImage`、`EmptyLatentAudio`、`SaveAudioMP3`、`CLIPLoader`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、VAEDecodeAudio、EmptyLatentAudio、SaveAudioMP3

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

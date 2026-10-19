---
key: 数字人/数字人/HeyGem+IndexTTS2.5数字人｜视频生视频快速语音迁移_2096324334888509441.json
name: HeyGem+IndexTTS2.5数字人｜视频生视频快速语音迁移_2096324334888509441
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/HeyGem+IndexTTS2.5数字人｜视频生视频快速语音迁移_2096324334888509441.json
hash: 7b58c30ad1992966
coverage: 0.909091
learned_at: 2026-10-19 00:19:09
nodes: [SoundFlow_TrimAudio, WujiCleaner, easy cleanGpuUsed, GetVideoComponents, AudioSeparation, LoadVideo, Qwen3ASRTranscribe, Qwen3ASRLoader, RunningHub_VoxCPM_LoadModel, RunningHub_VoxCPM_Generate, LoadAudio, CR Prompt Text, SaveAudioMP3, RH_HeyGemNode, SaveVideo, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, JjkText, EmptyLatentImage, solarL_SaveImagesToZip, VAEDecode, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/HeyGem+IndexTTS2.5数字人｜视频生视频快速语音迁移_2096324334888509441.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/HeyGem+IndexTTS2.5数字人｜视频生视频快速语音迁移_2096324334888509441.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（44 个）：
- `SoundFlow_TrimAudio`
- `WujiCleaner`
- `easy cleanGpuUsed`
- `GetVideoComponents`
- `AudioSeparation`
- `LoadVideo`
- `Qwen3ASRTranscribe`
- `Qwen3ASRLoader`
- `RunningHub_VoxCPM_LoadModel`
- `RunningHub_VoxCPM_Generate`
- `LoadAudio`
- `CR Prompt Text`
- `SaveAudioMP3`
- `RH_HeyGemNode`
- `SaveVideo`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `JjkText`
- `EmptyLatentImage` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **91%**（40/44）

**有卡**：`SoundFlow_TrimAudio`、`WujiCleaner`、`easy cleanGpuUsed`、`GetVideoComponents`、`AudioSeparation`、`LoadVideo`、`Qwen3ASRTranscribe`、`Qwen3ASRLoader`、`RunningHub_VoxCPM_LoadModel`、`RunningHub_VoxCPM_Generate`、`LoadAudio`、`CR Prompt Text`、`SaveAudioMP3`、`RH_HeyGemNode`、`SaveVideo`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`CLIPLoader`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`VAEDecode`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

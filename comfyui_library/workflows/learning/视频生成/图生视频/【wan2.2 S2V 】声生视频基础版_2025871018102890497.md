---
key: 视频生成/图生视频/【wan2.2 S2V 】声生视频基础版_2025871018102890497.json
name: 【wan2.2 S2V 】声生视频基础版_2025871018102890497.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2025871018102890497.json
hash: 93aad4f7d9348f4c
coverage: 1
learned_at: 2026-10-15 22:35:13
nodes: [LoadImage, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LoadAudio, UNETLoader, LoraLoaderModelOnly, SaveVideo, AudioEncoderEncode, CLIPLoader, VAELoader, ImageResizeKJv2, AudioEncoderLoader, CLIPTextEncode, CLIPTextEncode, WanSoundImageToVideo, LayerUtility: PurgeVRAM, VAEDecode, Int, CreateVideo, SimpleMath+, Float, KSampler]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 177185913373564, "steps": 5}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/【wan2.2 S2V 】声生视频基础版_2025871018102890497.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2025871018102890497.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `LoadImage`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `LoadAudio`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveVideo`
- `AudioEncoderEncode`
- `CLIPLoader`
- `VAELoader`
- `ImageResizeKJv2`
- `AudioEncoderLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `WanSoundImageToVideo`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `Int`
- `CreateVideo`
- `SimpleMath+`
- `Float`
- `KSampler` ★核心

## 关键参数

- `seed` = `177185913373564`
- `steps` = `5`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（22/22）

**有卡**：`LoadImage`、`LayerUtility: PurgeVRAM`、`LoadAudio`、`UNETLoader`、`LoraLoaderModelOnly`、`SaveVideo`、`AudioEncoderEncode`、`CLIPLoader`、`VAELoader`、`ImageResizeKJv2`、`AudioEncoderLoader`、`CLIPTextEncode`、`WanSoundImageToVideo`、`VAEDecode`、`Int`、`CreateVideo`、`SimpleMath+`、`Float`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

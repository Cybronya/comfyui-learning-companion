---
key: 平台全量/Wan2.2-S2V对口型-视频到视频动态参考_1961064943288303618.json
name: Wan2.2-S2V对口型-视频到视频动态参考_1961064943288303618
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2-S2V对口型-视频到视频动态参考_1961064943288303618.json
hash: 2ab895d8bacbbc21
coverage: 1
learned_at: 2026-11-14 01:06:01
nodes: [CLIPTextEncode, ModelSamplingSD3, AudioEncoderEncode, AudioSeparation, UNETLoader, LoraLoaderModelOnly, AudioEncoderLoader, CLIPLoader, VAEDecode, VHS_VideoCombine, AudioCrop, KSampler, VAELoader, INTConstant, ImageResizeKJv2, WanSoundImageToVideo, VHS_LoadVideo, LoadAudio, CLIPTextEncode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 403483089857448, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Wan2.2-S2V对口型-视频到视频动态参考_1961064943288303618.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2-S2V对口型-视频到视频动态参考_1961064943288303618.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（19 个）：
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `AudioEncoderEncode`
- `AudioSeparation`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `AudioEncoderLoader`
- `CLIPLoader`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `AudioCrop`
- `KSampler` ★核心
- `VAELoader`
- `INTConstant`
- `ImageResizeKJv2`
- `WanSoundImageToVideo`
- `VHS_LoadVideo`
- `LoadAudio`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `403483089857448`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（19/19）

**有卡**：`CLIPTextEncode`、`ModelSamplingSD3`、`AudioEncoderEncode`、`AudioSeparation`、`UNETLoader`、`LoraLoaderModelOnly`、`AudioEncoderLoader`、`CLIPLoader`、`VAEDecode`、`VHS_VideoCombine`、`AudioCrop`、`KSampler`、`VAELoader`、`INTConstant`、`ImageResizeKJv2`、`WanSoundImageToVideo`、`VHS_LoadVideo`、`LoadAudio`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、UNETLoader、AudioEncoderEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

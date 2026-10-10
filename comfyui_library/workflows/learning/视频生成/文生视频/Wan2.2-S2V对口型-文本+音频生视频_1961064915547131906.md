---
key: 视频生成/文生视频/Wan2.2-S2V对口型-文本+音频生视频_1961064915547131906.json
name: Wan2.2-S2V对口型-文本+音频生视频_1961064915547131906
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2-S2V对口型-文本+音频生视频_1961064915547131906.json
hash: ec5591bb13526422
coverage: 1
learned_at: 2026-10-10 23:07:14
nodes: [VAELoader, CLIPTextEncode, ModelSamplingSD3, AudioEncoderEncode, WanSoundImageToVideo, AudioSeparation, UNETLoader, LoraLoaderModelOnly, AudioEncoderLoader, CLIPLoader, KSampler, VAEDecode, VHS_VideoCombine, AudioCrop, LoadAudio, CLIPTextEncode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 888167936615732, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Wan2.2-S2V对口型-文本+音频生视频_1961064915547131906.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2-S2V对口型-文本+音频生视频_1961064915547131906.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（16 个）：
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `AudioEncoderEncode`
- `WanSoundImageToVideo`
- `AudioSeparation`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `AudioEncoderLoader`
- `CLIPLoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `AudioCrop`
- `LoadAudio`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `888167936615732`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`VAELoader`、`CLIPTextEncode`、`ModelSamplingSD3`、`AudioEncoderEncode`、`WanSoundImageToVideo`、`AudioSeparation`、`UNETLoader`、`LoraLoaderModelOnly`、`AudioEncoderLoader`、`CLIPLoader`、`KSampler`、`VAEDecode`、`VHS_VideoCombine`、`AudioCrop`、`LoadAudio`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、AudioEncoderLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

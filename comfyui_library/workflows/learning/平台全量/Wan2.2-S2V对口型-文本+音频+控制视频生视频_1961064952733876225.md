---
key: 平台全量/Wan2.2-S2V对口型-文本+音频+控制视频生视频_1961064952733876225.json
name: Wan2.2-S2V对口型-文本+音频+控制视频生视频_1961064952733876225
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2-S2V对口型-文本+音频+控制视频生视频_1961064952733876225.json
hash: 78537b31d43e9634
coverage: 1
learned_at: 2026-11-14 01:06:01
nodes: [CLIPTextEncode, ModelSamplingSD3, AudioEncoderEncode, AudioSeparation, UNETLoader, LoraLoaderModelOnly, AudioEncoderLoader, CLIPLoader, VAEDecode, VHS_VideoCombine, AudioCrop, KSampler, VAELoader, INTConstant, WanSoundImageToVideo, ImageResizeKJv2, VHS_LoadVideo, LoadAudio, DWPreprocessor, CLIPTextEncode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 456158050275266, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Wan2.2-S2V对口型-文本+音频+控制视频生视频_1961064952733876225.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2-S2V对口型-文本+音频+控制视频生视频_1961064952733876225.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（20 个）：
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
- `WanSoundImageToVideo`
- `ImageResizeKJv2`
- `VHS_LoadVideo`
- `LoadAudio`
- `DWPreprocessor`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `456158050275266`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（20/20）

**有卡**：`CLIPTextEncode`、`ModelSamplingSD3`、`AudioEncoderEncode`、`AudioSeparation`、`UNETLoader`、`LoraLoaderModelOnly`、`AudioEncoderLoader`、`CLIPLoader`、`VAEDecode`、`VHS_VideoCombine`、`AudioCrop`、`KSampler`、`VAELoader`、`INTConstant`、`WanSoundImageToVideo`、`ImageResizeKJv2`、`VHS_LoadVideo`、`LoadAudio`、`DWPreprocessor`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、UNETLoader、AudioEncoderEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

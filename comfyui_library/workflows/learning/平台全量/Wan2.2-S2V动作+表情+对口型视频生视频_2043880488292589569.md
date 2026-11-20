---
key: 平台全量/Wan2.2-S2V动作+表情+对口型视频生视频_2043880488292589569.json
name: Wan2.2-S2V动作+表情+对口型视频生视频_2043880488292589569
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2-S2V动作+表情+对口型视频生视频_2043880488292589569.json
hash: 6fe8ed4f39d9537c
coverage: 1
learned_at: 2026-11-14 01:06:00
nodes: [CLIPTextEncode, ModelSamplingSD3, AudioEncoderEncode, AudioSeparation, LoraLoaderModelOnly, AudioEncoderLoader, CLIPLoader, AudioCrop, KSampler, VAELoader, INTConstant, WanSoundImageToVideo, ImageResizeKJv2, VHS_LoadVideo, UNETLoader, LoadAudio, CLIPTextEncode, ImageResizeKJv2, DWPreprocessor, VHS_LoadVideo, VAEDecode, VHS_VideoCombine]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 1032059299341377, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Wan2.2-S2V动作+表情+对口型视频生视频_2043880488292589569.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2-S2V动作+表情+对口型视频生视频_2043880488292589569.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（22 个）：
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `AudioEncoderEncode`
- `AudioSeparation`
- `LoraLoaderModelOnly` ★核心
- `AudioEncoderLoader`
- `CLIPLoader`
- `AudioCrop`
- `KSampler` ★核心
- `VAELoader`
- `INTConstant`
- `WanSoundImageToVideo`
- `ImageResizeKJv2`
- `VHS_LoadVideo`
- `UNETLoader` ★核心
- `LoadAudio`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `DWPreprocessor`
- `VHS_LoadVideo`
- `VAEDecode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `1032059299341377`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（22/22）

**有卡**：`CLIPTextEncode`、`ModelSamplingSD3`、`AudioEncoderEncode`、`AudioSeparation`、`LoraLoaderModelOnly`、`AudioEncoderLoader`、`CLIPLoader`、`AudioCrop`、`KSampler`、`VAELoader`、`INTConstant`、`WanSoundImageToVideo`、`ImageResizeKJv2`、`VHS_LoadVideo`、`UNETLoader`、`LoadAudio`、`DWPreprocessor`、`VAEDecode`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、UNETLoader、AudioEncoderEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

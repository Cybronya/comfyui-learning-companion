---
key: 音频生成/音频生成/Wan2.2-S2V 音频到视频数字人对口型_1961331106094235649.json
name: Wan2.2-S2V 音频到视频数字人对口型_1961331106094235649
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/Wan2.2-S2V 音频到视频数字人对口型_1961331106094235649.json
hash: b868b7eb3531a7b9
coverage: 0.862069
learned_at: 2026-10-18 01:24:03
nodes: [ModelSamplingSD3, LoraLoaderModelOnly, AudioEncoderLoader, UNETLoader, CLIPLoader, CLIPTextEncode, AudioCombine, AudioCombine, RH_GetAudioDuration, AudioSeparation, AudioCombine, VAELoader, VAEDecode, VHS_VideoCombine, LoadImage, PrimitiveString, CR SDXL Aspect Ratio, KSampler, WanSoundImageToVideo, AudioEncoderEncode, SimpleMath+, ImageResizeKJv2, CLIPTextEncode, LoadAudio, TrimAudio, PrimitiveFloat, PrimitiveFloat, PrimitiveFloat, PreviewAudio]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 893274579547132, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 音频生成/音频生成/Wan2.2-S2V 音频到视频数字人对口型_1961331106094235649.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/Wan2.2-S2V 音频到视频数字人对口型_1961331106094235649.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（29 个）：
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `AudioEncoderLoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `AudioCombine`
- `AudioCombine`
- `RH_GetAudioDuration`
- `AudioSeparation`
- `AudioCombine`
- `VAELoader`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `PrimitiveString`
- `CR SDXL Aspect Ratio`
- `KSampler` ★核心
- `WanSoundImageToVideo`
- `AudioEncoderEncode`
- `SimpleMath+`
- `ImageResizeKJv2`
- `CLIPTextEncode` ★核心
- `LoadAudio`
- `TrimAudio`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `PreviewAudio`

## 关键参数

- `seed` = `893274579547132`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（25/29）

**有卡**：`ModelSamplingSD3`、`LoraLoaderModelOnly`、`AudioEncoderLoader`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`AudioCombine`、`RH_GetAudioDuration`、`AudioSeparation`、`VAELoader`、`VAEDecode`、`VHS_VideoCombine`、`LoadImage`、`CR SDXL Aspect Ratio`、`KSampler`、`WanSoundImageToVideo`、`AudioEncoderEncode`、`SimpleMath+`、`ImageResizeKJv2`、`LoadAudio`、`TrimAudio`、`PreviewAudio`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

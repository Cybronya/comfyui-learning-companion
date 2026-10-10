---
key: 视频生成/文生视频/Wan2.2-S2V对口型-文本+音频+图片+控制视频生视频_1961064966939983873.json
name: Wan2.2-S2V对口型-文本+音频+图片+控制视频生视频_1961064966939983873
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2-S2V对口型-文本+音频+图片+控制视频生视频_1961064966939983873.json
hash: 437758e8fa258819
coverage: 1
learned_at: 2026-10-10 23:07:13
nodes: [CLIPTextEncode, ModelSamplingSD3, AudioEncoderEncode, WanSoundImageToVideo, AudioSeparation, UNETLoader, LoraLoaderModelOnly, AudioEncoderLoader, CLIPLoader, VAEDecode, VHS_VideoCombine, AudioCrop, KSampler, VAELoader, ImageResizeKJv2, ImageResizeKJv2, INTConstant, VHS_LoadVideo, LoadImage, LoadAudio, CLIPTextEncode, DWPreprocessor]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 744834867715933, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Wan2.2-S2V对口型-文本+音频+图片+控制视频生视频_1961064966939983873.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2-S2V对口型-文本+音频+图片+控制视频生视频_1961064966939983873.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（22 个）：
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `AudioEncoderEncode`
- `WanSoundImageToVideo`
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
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `INTConstant`
- `VHS_LoadVideo`
- `LoadImage`
- `LoadAudio`
- `CLIPTextEncode` ★核心
- `DWPreprocessor`

## 关键参数

- `seed` = `744834867715933`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（22/22）

**有卡**：`CLIPTextEncode`、`ModelSamplingSD3`、`AudioEncoderEncode`、`WanSoundImageToVideo`、`AudioSeparation`、`UNETLoader`、`LoraLoaderModelOnly`、`AudioEncoderLoader`、`CLIPLoader`、`VAEDecode`、`VHS_VideoCombine`、`AudioCrop`、`KSampler`、`VAELoader`、`ImageResizeKJv2`、`INTConstant`、`VHS_LoadVideo`、`LoadImage`、`LoadAudio`、`DWPreprocessor`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

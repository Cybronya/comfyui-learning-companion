---
key: 视频生成/图生视频/S2V 声音生成视频 Wan2.2_1967070568195481602.json
name: S2V 声音生成视频 Wan2.2_1967070568195481602.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/S2V 声音生成视频 Wan2.2_1967070568195481602.json
hash: 0259bf46ea2f6243
coverage: 1
learned_at: 2026-10-15 22:31:40
nodes: [CLIPLoader, VAELoader, UNETLoader, LoraLoaderModelOnly, KSampler, LoadAudio, LoadImage, ImageResizeKJv2, SimpleMath+, easy int, ToInt, Display Int (rgthree), AudioCrop, SaveAudio, Display Int (rgthree), SoundFlow_GetLength, easy cleanGpuUsed, ModelSamplingSD3, WanSoundImageToVideo, AudioEncoderLoader, AudioEncoderEncode, CLIPTextEncode, CLIPTextEncode, easy cleanGpuUsed, VAEDecode, VHS_VideoCombine]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 788368928023972, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/S2V 声音生成视频 Wan2.2_1967070568195481602.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1967070568195481602.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `LoadAudio`
- `LoadImage`
- `ImageResizeKJv2`
- `SimpleMath+`
- `easy int`
- `ToInt`
- `Display Int (rgthree)`
- `AudioCrop`
- `SaveAudio`
- `Display Int (rgthree)`
- `SoundFlow_GetLength`
- `easy cleanGpuUsed`
- `ModelSamplingSD3`
- `WanSoundImageToVideo`
- `AudioEncoderLoader`
- `AudioEncoderEncode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `788368928023972`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（26/26）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`LoadAudio`、`LoadImage`、`ImageResizeKJv2`、`SimpleMath+`、`easy int`、`ToInt`、`Display Int (rgthree)`、`AudioCrop`、`SaveAudio`、`SoundFlow_GetLength`、`easy cleanGpuUsed`、`ModelSamplingSD3`、`WanSoundImageToVideo`、`AudioEncoderLoader`、`AudioEncoderEncode`、`CLIPTextEncode`、`VAEDecode`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

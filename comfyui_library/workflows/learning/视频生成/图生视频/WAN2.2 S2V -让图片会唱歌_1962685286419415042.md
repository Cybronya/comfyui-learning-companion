---
key: 视频生成/图生视频/WAN2.2 S2V -让图片会唱歌_1962685286419415042.json
name: WAN2.2 S2V -让图片会唱歌_1962685286419415042.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WAN2.2 S2V -让图片会唱歌_1962685286419415042.json
hash: 31253cec1676b389
coverage: 1
learned_at: 2026-10-15 22:31:31
nodes: [CLIPTextEncode, AudioEncoderEncode, AudioEncoderLoader, SimpleMath+, Display Any (rgthree), PreviewAudio, Display Any (rgthree), CR Float To Integer, WanSoundImageToVideo, ModelSamplingSD3, VAEDecode, PathchSageAttentionKJ, KSampler, wanBlockSwap, VHS_VideoCombine, UNETLoader, CLIPLoader, LoraLoaderModelOnly, VAELoader, AudioCropProcessUTK, LoadImage, CLIPTextEncode, ImageResizeKJv2, LoadAudio]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 1736, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/WAN2.2 S2V -让图片会唱歌_1962685286419415042.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1962685286419415042.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（24 个）：
- `CLIPTextEncode` ★核心
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `SimpleMath+`
- `Display Any (rgthree)`
- `PreviewAudio`
- `Display Any (rgthree)`
- `CR Float To Integer`
- `WanSoundImageToVideo`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `PathchSageAttentionKJ`
- `KSampler` ★核心
- `wanBlockSwap`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `AudioCropProcessUTK`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `LoadAudio`

## 关键参数

- `seed` = `1736`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（24/24）

**有卡**：`CLIPTextEncode`、`AudioEncoderEncode`、`AudioEncoderLoader`、`SimpleMath+`、`Display Any (rgthree)`、`PreviewAudio`、`CR Float To Integer`、`WanSoundImageToVideo`、`ModelSamplingSD3`、`VAEDecode`、`PathchSageAttentionKJ`、`KSampler`、`wanBlockSwap`、`VHS_VideoCombine`、`UNETLoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`VAELoader`、`AudioCropProcessUTK`、`LoadImage`、`ImageResizeKJv2`、`LoadAudio`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

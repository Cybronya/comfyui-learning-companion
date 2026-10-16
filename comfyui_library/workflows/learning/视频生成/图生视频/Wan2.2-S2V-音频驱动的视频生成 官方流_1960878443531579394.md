---
key: 视频生成/图生视频/Wan2.2-S2V-音频驱动的视频生成 官方流_1960878443531579394.json
name: Wan2.2-S2V-音频驱动的视频生成 官方流_1960878443531579394.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1960878443531579394.json
hash: 8da9c7b0b1cb78e2
coverage: 0.909091
learned_at: 2026-10-15 22:31:27
nodes: [ModelSamplingSD3, CLIPTextEncode, VAEDecode, VAELoader, CLIPLoader, Float, easy showAnything, UNETLoader, CLIPTextEncode, AudioEncoderEncode, SimpleMath+, VHS_VideoCombine, MarkdownNote, Note Plus (mtb), AudioEncoderLoader, AudioSeparation, Audio Duration (mtb), ImpactInt, ImpactInt, PathchSageAttentionKJ, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, ImageResizeKJv2, ImageConcanate, easy convertAnything, WanSoundImageToVideo, Reroute, LoadImage, CR Text, LoadAudio, TorchCompileModel, KSampler]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 666, "steps": 20}
---

# 视频生成/图生视频/Wan2.2-S2V-音频驱动的视频生成 官方流_1960878443531579394.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1960878443531579394.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（33 个）：
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `Float`
- `easy showAnything`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `AudioEncoderEncode`
- `SimpleMath+`
- `VHS_VideoCombine`
- `MarkdownNote`
- `Note Plus (mtb)`
- `AudioEncoderLoader`
- `AudioSeparation`
- `Audio Duration (mtb)`
- `ImpactInt`
- `ImpactInt`
- `PathchSageAttentionKJ`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `ImageConcanate`
- `easy convertAnything`
- `WanSoundImageToVideo`
- `Reroute`
- `LoadImage`
- `CR Text`
- `LoadAudio`
- `TorchCompileModel`
- `KSampler` ★核心

## 关键参数

- `seed` = `666`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（30/33）

**有卡**：`ModelSamplingSD3`、`CLIPTextEncode`、`VAEDecode`、`VAELoader`、`CLIPLoader`、`Float`、`UNETLoader`、`AudioEncoderEncode`、`SimpleMath+`、`VHS_VideoCombine`、`Note Plus (mtb)`、`AudioEncoderLoader`、`AudioSeparation`、`Audio Duration (mtb)`、`ImpactInt`、`PathchSageAttentionKJ`、`VHS_LoadVideo`、`ImageResizeKJv2`、`ImageConcanate`、`easy convertAnything`、`WanSoundImageToVideo`、`LoadImage`、`CR Text`、`LoadAudio`、`TorchCompileModel`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、AudioEncoderLoader

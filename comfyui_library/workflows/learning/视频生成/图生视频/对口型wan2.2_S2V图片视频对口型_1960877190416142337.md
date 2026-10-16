---
key: 视频生成/图生视频/对口型wan2.2_S2V图片视频对口型_1960877190416142337.json
name: 对口型wan2.2_S2V图片视频对口型_1960877190416142337.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1960877190416142337.json
hash: c851f06531635373
coverage: 0.96
learned_at: 2026-10-15 22:31:27
nodes: [ModelSamplingSD3, CLIPLoader, VAELoader, LoadImage, VHS_LoadVideo, ToInt, SimpleMath+, Int, PathchSageAttentionKJ, TorchCompileModel, CLIPTextEncode, WanSoundImageToVideo, CLIPTextEncode, VHS_VideoCombine, easy showAnything, KSampler, AudioEncoderLoader, AudioEncoderEncode, AudioSeparation, RH_GetAudioDuration, UNETLoader, LoadAudio, VAEDecode, ImageConcanate, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 728491967620486, "steps": 20}
---

# 视频生成/图生视频/对口型wan2.2_S2V图片视频对口型_1960877190416142337.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1960877190416142337.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（25 个）：
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `VHS_LoadVideo`
- `ToInt`
- `SimpleMath+`
- `Int`
- `PathchSageAttentionKJ`
- `TorchCompileModel`
- `CLIPTextEncode` ★核心
- `WanSoundImageToVideo`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `easy showAnything`
- `KSampler` ★核心
- `AudioEncoderLoader`
- `AudioEncoderEncode`
- `AudioSeparation`
- `RH_GetAudioDuration`
- `UNETLoader` ★核心
- `LoadAudio`
- `VAEDecode` ★核心
- `ImageConcanate`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `728491967620486`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **96%**（24/25）

**有卡**：`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`LoadImage`、`VHS_LoadVideo`、`ToInt`、`SimpleMath+`、`Int`、`PathchSageAttentionKJ`、`TorchCompileModel`、`CLIPTextEncode`、`WanSoundImageToVideo`、`VHS_VideoCombine`、`KSampler`、`AudioEncoderLoader`、`AudioEncoderEncode`、`AudioSeparation`、`RH_GetAudioDuration`、`UNETLoader`、`LoadAudio`、`VAEDecode`、`ImageConcanate`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、AudioEncoderLoader

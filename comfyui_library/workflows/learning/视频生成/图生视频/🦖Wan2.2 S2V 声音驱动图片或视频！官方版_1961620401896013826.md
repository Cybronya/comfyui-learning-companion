---
key: 视频生成/图生视频/🦖Wan2.2 S2V 声音驱动图片或视频！官方版_1961620401896013826.json
name: 🦖Wan2.2 S2V 声音驱动图片或视频！官方版_1961620401896013826.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/🦖Wan2.2 S2V 声音驱动图片或视频！官方版_1961620401896013826.json
hash: 2b4a6c388041550e
coverage: 0.689189
learned_at: 2026-10-15 22:31:28
nodes: [PathchSageAttentionKJ, DeepTranslatorTextNode, ModelSamplingSD3, VAEDecode, SetNode, AudioEncoderEncode, CLIPTextEncode, VAELoader, AudioEncoderLoader, CLIPLoader, GetNode, TorchCompileModel, Mute / Bypass Repeater (rgthree), Any Switch (rgthree), DepthAnythingV2Preprocessor, PathchSageAttentionKJ, WanSoundImageToVideo, ModelSamplingSD3, PreviewAny, CLIPTextEncode, DWPreprocessor, VAELoader, AudioEncoderLoader, CLIPLoader, TorchCompileModelWanVideoV2, ImageResizeKJ, TorchCompileModel, UNETLoader, GetNode, AudioEncoderEncode, GetNode, PreviewImage, FrameSelector, ResizeLongestToNode, GetNode, ImageResizeKJv2, AudioCrop, SetNode, LoadAudio, SetNode, VAEDecode, KSampler, KSampler, CLIPTextEncode, ResizeLongestToNode, ACE_ImageGetSize, VHS_VideoCombine, GetNode, CLIPTextEncode, TorchCompileModelWanVideoV2, PreviewAny, WanSoundImageToVideo, easy int, SetNode, VHS_VideoCombine, GetNode, GetNode, SetNode, AudioSeparation, GetNode, ImageResizeKJv2, AudioSeparation, GetNode, UNETLoader, Note, LoadImage, PrimitiveStringMultiline, VHS_LoadVideo, Note, Mute / Bypass Relay (rgthree), DeepTranslatorTextNode, GetNode, Fast Groups Muter (rgthree), ACE_ImageGetSize]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 666, "steps": 25}
---

# 视频生成/图生视频/🦖Wan2.2 S2V 声音驱动图片或视频！官方版_1961620401896013826.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1961620401896013826.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（74 个）：
- `PathchSageAttentionKJ`
- `DeepTranslatorTextNode`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `SetNode`
- `AudioEncoderEncode`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `AudioEncoderLoader`
- `CLIPLoader`
- `GetNode`
- `TorchCompileModel`
- `Mute / Bypass Repeater (rgthree)`
- `Any Switch (rgthree)`
- `DepthAnythingV2Preprocessor`
- `PathchSageAttentionKJ`
- `WanSoundImageToVideo`
- `ModelSamplingSD3`
- `PreviewAny`
- `CLIPTextEncode` ★核心
- `DWPreprocessor`
- `VAELoader`
- `AudioEncoderLoader`
- `CLIPLoader`
- `TorchCompileModelWanVideoV2`
- `ImageResizeKJ`
- `TorchCompileModel`
- `UNETLoader` ★核心
- `GetNode`
- `AudioEncoderEncode`
- `GetNode`
- `PreviewImage`
- `FrameSelector`
- `ResizeLongestToNode`
- `GetNode`
- `ImageResizeKJv2`
- `AudioCrop`
- `SetNode`
- `LoadAudio`
- `SetNode`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `ResizeLongestToNode`
- `ACE_ImageGetSize`
- `VHS_VideoCombine`
- `GetNode`
- `CLIPTextEncode` ★核心
- `TorchCompileModelWanVideoV2`
- `PreviewAny`
- `WanSoundImageToVideo`
- `easy int`
- `SetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `SetNode`
- `AudioSeparation`
- `GetNode`
- `ImageResizeKJv2`
- `AudioSeparation`
- `GetNode`
- `UNETLoader` ★核心
- `Note`
- `LoadImage`
- `PrimitiveStringMultiline`
- `VHS_LoadVideo`
- `Note`
- `Mute / Bypass Relay (rgthree)`
- `DeepTranslatorTextNode`
- `GetNode`
- `Fast Groups Muter (rgthree)`
- `ACE_ImageGetSize`

## 关键参数

- `seed` = `666`
- `steps` = `25`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **69%**（51/74）

**有卡**：`PathchSageAttentionKJ`、`DeepTranslatorTextNode`、`ModelSamplingSD3`、`VAEDecode`、`AudioEncoderEncode`、`CLIPTextEncode`、`VAELoader`、`AudioEncoderLoader`、`CLIPLoader`、`TorchCompileModel`、`Mute / Bypass Repeater (rgthree)`、`DepthAnythingV2Preprocessor`、`WanSoundImageToVideo`、`DWPreprocessor`、`TorchCompileModelWanVideoV2`、`ImageResizeKJ`、`UNETLoader`、`FrameSelector`、`ResizeLongestToNode`、`ImageResizeKJv2`、`AudioCrop`、`LoadAudio`、`KSampler`、`ACE_ImageGetSize`、`VHS_VideoCombine`、`easy int`、`AudioSeparation`、`LoadImage`、`VHS_LoadVideo`、`Mute / Bypass Relay (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、DepthAnythingV2Preprocessor

---
key: 视频生成/文生视频/LTX2.3板块：首尾帧工作流_2050777299921973250.json
name: LTX2.3板块：首尾帧工作流_2050777299921973250
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3板块：首尾帧工作流_2050777299921973250.json
hash: 730df3debd082fac
coverage: 0.593023
learned_at: 2026-10-15 22:45:14
nodes: [CLIPTextEncode, Note, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, LTXAVTextEncoderLoader, PathchSageAttentionKJ, ModelPatchTorchSettings, Reroute, Reroute, easy showAnything, Reroute, Reroute, Reroute, LTXVSeparateAVLatent, LTXVAudioVAEDecode, SamplerCustomAdvanced, RandomNoise, CFGGuider, Reroute, Reroute, ManualSigmas, LTXVConcatAVLatent, LTXVLatentUpsampler, Reroute, LTXVAudioVAELoader, LTXVAudioVAELoader, CFGGuider, Reroute, KSamplerSelect, KSamplerSelect, ManualSigmas, LTXVChunkFeedForward, VHS_VideoCombine, VAEDecodeTiled, LTXVImgToVideoInplace, LatentUpscaleModelLoader, RandomNoise, VAEDecodeTiled, VHS_VideoCombine, LTXVAudioVAEDecode, SamplerCustomAdvanced, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, LTXVSeparateAVLatent, LTXVCropGuides, Reroute, Reroute, ImageResize+, LoraLoaderModelOnly, LoraLoaderModelOnly, LTXVConditioning, EmptyLTXVLatentVideo, CheckpointLoaderSimple, LTXVPreprocess, LTXVConcatAVLatent, LTXVAddGuide, easy int, easy int, LTXVEmptyLatentAudio, SimpleMath+, LTXVCropGuides, LTXVAddGuide, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, GetNode, GetNode, easy showAnything, easy showAnything, SetNode, SetNode, SetNode, LTXVPreprocess, ManualSigmas, LoadImage, CLIPTextEncode, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.3板块：首尾帧工作流_2050777299921973250.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3板块：首尾帧工作流_2050777299921973250.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（86 个）：
- `CLIPTextEncode` ★核心
- `Note`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LTXAVTextEncoderLoader`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `Reroute`
- `Reroute`
- `easy showAnything`
- `Reroute`
- `Reroute`
- `Reroute`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `CFGGuider`
- `Reroute`
- `Reroute`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `Reroute`
- `LTXVAudioVAELoader`
- `LTXVAudioVAELoader`
- `CFGGuider`
- `Reroute`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVChunkFeedForward`
- `VHS_VideoCombine`
- `VAEDecodeTiled` ★核心
- `LTXVImgToVideoInplace`
- `LatentUpscaleModelLoader`
- `RandomNoise`
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `LTXVAudioVAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `Reroute`
- `Reroute`
- `ImageResize+`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `CheckpointLoaderSimple` ★核心
- `LTXVPreprocess`
- `LTXVConcatAVLatent`
- `LTXVAddGuide`
- `easy int`
- `easy int`
- `LTXVEmptyLatentAudio` ★核心
- `SimpleMath+`
- `LTXVCropGuides`
- `LTXVAddGuide`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `easy showAnything`
- `SetNode`
- `SetNode`
- `SetNode`
- `LTXVPreprocess`
- `ManualSigmas`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LoadImage`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **59%**（51/86）

**有卡**：`CLIPTextEncode`、`LTXAVTextEncoderLoader`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`SamplerCustomAdvanced`、`RandomNoise`、`CFGGuider`、`ManualSigmas`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`LTXVAudioVAELoader`、`KSamplerSelect`、`LTXVChunkFeedForward`、`VHS_VideoCombine`、`VAEDecodeTiled`、`LTXVImgToVideoInplace`、`LatentUpscaleModelLoader`、`LTXVCropGuides`、`ImageResize+`、`LoraLoaderModelOnly`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`CheckpointLoaderSimple`、`LTXVPreprocess`、`LTXVAddGuide`、`easy int`、`LTXVEmptyLatentAudio`、`SimpleMath+`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

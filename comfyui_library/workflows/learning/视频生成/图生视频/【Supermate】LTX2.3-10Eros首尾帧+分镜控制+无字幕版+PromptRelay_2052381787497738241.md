---
key: 视频生成/图生视频/【Supermate】LTX2.3-10Eros首尾帧+分镜控制+无字幕版+PromptRelay_2052381787497738241.json
name: 【Supermate】LTX2.3-10Eros首尾帧+分镜控制+无字幕版+PromptRelay_2052381787497738241.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2052381787497738241.json
hash: a194f97d48bfc33f
coverage: 0.546392
learned_at: 2026-10-15 22:37:29
nodes: [Reroute, CFGGuider, RandomNoise, LTXVSeparateAVLatent, Reroute, Reroute, Reroute, Reroute, LTXVCropGuides, Reroute, Reroute, LoraLoaderModelOnly, Reroute, ImpactFloat, LTXVCropGuides, LTXVAudioVAEDecode, LTXVSeparateAVLatent, SamplerCustomAdvanced, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, KSamplerSelect, ImageResizeKJ, LTXVConcatAVLatent, LTXVAddGuide, LTXVConditioning, GetNode, GetNode, GetNode, Reroute, LoraLoaderModelOnly, LTXVAudioVAEDecode, LTX2_NAG, GetNode, GetNode, CLIPTextEncode, EmptyLTXVLatentVideo, GetNode, SetNode, Reroute, SamplerCustomAdvanced, LTXVAddGuide, LoraLoaderModelOnly, LTXVPreprocess, easy showAnything, easy showAnything, PathchSageAttentionKJ, ModelPatchTorchSettings, LTXVChunkFeedForward, LTXVAudioVAELoader, LTXAVTextEncoderLoader, CFGGuider, KSamplerSelect, Reroute, GetNode, LatentUpscaleModelLoader, LoraLoaderModelOnly, CheckpointLoaderSimple, LayerUtility: ImageScaleByAspectRatio V2, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, LTXVConcatAVLatent, ManualSigmas, Reroute, Reroute, Reroute, ManualSigmas, SimpleMath+, easy int, SetNode, easy showAnything, LTXVEmptyLatentAudio, Reroute, LTXVImgToVideoInplace, LTXVLatentUpsampler, SetNode, SetNode, LTXVPreprocess, SetNode, SetNode, Reroute, ImpactInt, VAEDecodeTiled, VHS_VideoCombine, VAEDecode, VHS_VideoCombine, RandomNoise, LoadImage, LoadImage, PromptRelayEncodeTimeline]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "10Eros_v1-fp8mixed_learned.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/【Supermate】LTX2.3-10Eros首尾帧+分镜控制+无字幕版+PromptRelay_2052381787497738241.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2052381787497738241.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（97 个）：
- `Reroute`
- `CFGGuider`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LTXVCropGuides`
- `Reroute`
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `Reroute`
- `ImpactFloat`
- `LTXVCropGuides`
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `KSamplerSelect` ★核心
- `ImageResizeKJ`
- `LTXVConcatAVLatent`
- `LTXVAddGuide`
- `LTXVConditioning`
- `GetNode`
- `GetNode`
- `GetNode`
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTX2_NAG`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `EmptyLTXVLatentVideo`
- `GetNode`
- `SetNode`
- `Reroute`
- `SamplerCustomAdvanced` ★核心
- `LTXVAddGuide`
- `LoraLoaderModelOnly` ★核心
- `LTXVPreprocess`
- `easy showAnything`
- `easy showAnything`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `LTXVChunkFeedForward`
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `Reroute`
- `GetNode`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `Reroute`
- `Reroute`
- `Reroute`
- `ManualSigmas`
- `SimpleMath+`
- `easy int`
- `SetNode`
- `easy showAnything`
- `LTXVEmptyLatentAudio` ★核心
- `Reroute`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler` ★核心
- `SetNode`
- `SetNode`
- `LTXVPreprocess`
- `SetNode`
- `SetNode`
- `Reroute`
- `ImpactInt`
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `RandomNoise`
- `LoadImage`
- `LoadImage`
- `PromptRelayEncodeTimeline`

## 关键参数

- `checkpoint` = `10Eros_v1-fp8mixed_learned.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **55%**（53/97）

**有卡**：`CFGGuider`、`RandomNoise`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LoraLoaderModelOnly`、`ImpactFloat`、`LTXVAudioVAEDecode`、`SamplerCustomAdvanced`、`KSamplerSelect`、`ImageResizeKJ`、`LTXVConcatAVLatent`、`LTXVAddGuide`、`LTXVConditioning`、`LTX2_NAG`、`CLIPTextEncode`、`EmptyLTXVLatentVideo`、`LTXVPreprocess`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`CheckpointLoaderSimple`、`LayerUtility: ImageScaleByAspectRatio V2`、`ManualSigmas`、`SimpleMath+`、`easy int`、`LTXVEmptyLatentAudio`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`ImpactInt`、`VAEDecodeTiled`、`VHS_VideoCombine`、`VAEDecode`、`LoadImage`、`PromptRelayEncodeTimeline`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect

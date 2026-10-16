---
key: 视频生成/图生视频/【Supermate】LTX2.3-10Eros单图+分镜控制+无字幕版+PromptRelay_2052409270473371649.json
name: 【Supermate】LTX2.3-10Eros单图+分镜控制+无字幕版+PromptRelay_2052409270473371649.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2052409270473371649.json
hash: ba184aa4c10f1bb2
coverage: 0.55914
learned_at: 2026-10-15 22:37:29
nodes: [Reroute, CFGGuider, RandomNoise, LTXVSeparateAVLatent, Reroute, Reroute, Reroute, Reroute, LTXVCropGuides, Reroute, Reroute, Reroute, LTXVCropGuides, LTXVAudioVAEDecode, LTXVSeparateAVLatent, SamplerCustomAdvanced, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, KSamplerSelect, LTXVConcatAVLatent, LTXVConditioning, Reroute, LoraLoaderModelOnly, LTXVAudioVAEDecode, LTX2_NAG, GetNode, EmptyLTXVLatentVideo, Reroute, SamplerCustomAdvanced, PathchSageAttentionKJ, ModelPatchTorchSettings, LTXVChunkFeedForward, LTXAVTextEncoderLoader, CFGGuider, KSamplerSelect, Reroute, LatentUpscaleModelLoader, LoraLoaderModelOnly, CheckpointLoaderSimple, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, LTXVConcatAVLatent, ManualSigmas, Reroute, Reroute, Reroute, ManualSigmas, LTXVEmptyLatentAudio, Reroute, LTXVImgToVideoInplace, LTXVLatentUpsampler, Reroute, VAEDecodeTiled, VHS_VideoCombine, VAEDecode, VHS_VideoCombine, RandomNoise, ImpactFloat, SetNode, SetNode, GetNode, LTXVAddGuide, Int, Int, SetNode, ImageResizeKJv2, GetNode, GetNode, LoadImage, TTResolutionSelector, SetNode, SetNode, Reroute, Bool, LoraLoaderModelOnly, LoraLoaderModelOnly, easy int, SimpleMath+, easy showAnything, ImpactInt, LTXVAudioVAELoader, PromptRelayEncodeTimeline, GetNode, GetNode, CLIPTextEncode]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "10Eros_v1-fp8mixed_learned.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/【Supermate】LTX2.3-10Eros单图+分镜控制+无字幕版+PromptRelay_2052409270473371649.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2052409270473371649.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（93 个）：
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
- `Reroute`
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
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTX2_NAG`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `Reroute`
- `SamplerCustomAdvanced` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `LTXVChunkFeedForward`
- `LTXAVTextEncoderLoader`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `Reroute`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
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
- `LTXVEmptyLatentAudio` ★核心
- `Reroute`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler` ★核心
- `Reroute`
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `RandomNoise`
- `ImpactFloat`
- `SetNode`
- `SetNode`
- `GetNode`
- `LTXVAddGuide`
- `Int`
- `Int`
- `SetNode`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `LoadImage`
- `TTResolutionSelector`
- `SetNode`
- `SetNode`
- `Reroute`
- `Bool`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy int`
- `SimpleMath+`
- `easy showAnything`
- `ImpactInt`
- `LTXVAudioVAELoader`
- `PromptRelayEncodeTimeline`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心

## 关键参数

- `checkpoint` = `10Eros_v1-fp8mixed_learned.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **56%**（52/93）

**有卡**：`CFGGuider`、`RandomNoise`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LTXVAudioVAEDecode`、`SamplerCustomAdvanced`、`KSamplerSelect`、`LTXVConcatAVLatent`、`LTXVConditioning`、`LoraLoaderModelOnly`、`LTX2_NAG`、`EmptyLTXVLatentVideo`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`CheckpointLoaderSimple`、`ManualSigmas`、`LTXVEmptyLatentAudio`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`VHS_VideoCombine`、`VAEDecode`、`ImpactFloat`、`LTXVAddGuide`、`Int`、`ImageResizeKJv2`、`LoadImage`、`TTResolutionSelector`、`Bool`、`easy int`、`SimpleMath+`、`ImpactInt`、`LTXVAudioVAELoader`、`PromptRelayEncodeTimeline`、`CLIPTextEncode`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

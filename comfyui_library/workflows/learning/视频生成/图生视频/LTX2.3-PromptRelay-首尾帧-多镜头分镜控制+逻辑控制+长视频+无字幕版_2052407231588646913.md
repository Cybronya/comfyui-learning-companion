---
key: 视频生成/图生视频/LTX2.3-PromptRelay-首尾帧-多镜头分镜控制+逻辑控制+长视频+无字幕版_2052407231588646913.json
name: LTX2.3-PromptRelay-首尾帧-多镜头分镜控制+逻辑控制+长视频+无字幕版_2052407231588646913.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3-PromptRelay-首尾帧-多镜头分镜控制+逻辑控制+长视频+无字幕版_2052407231588646913.json
hash: 90150f958580602e
coverage: 0.541284
learned_at: 2026-10-15 22:37:29
nodes: [Reroute, CFGGuider, RandomNoise, Reroute, LTXVSeparateAVLatent, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, LTXVCropGuides, Reroute, Reroute, Reroute, Reroute, LTXVPreprocess, LoraLoaderModelOnly, Reroute, Reroute, Reroute, LTXVImgToVideoInplaceKJ, SetNode, SetNode, LTXVPreprocess, SetNode, easy showAnything, easy showAnything, LTXVChunkFeedForward, ModelPatchTorchSettings, LTXVAudioVAELoader, KSamplerSelect, ImageResizeKJ, LTXVConcatAVLatent, LTXVAddGuide, LTXVConditioning, GetNode, Reroute, LoraLoaderModelOnly, LoraLoaderModelOnly, CheckpointLoaderSimple, PathchSageAttentionKJ, SimpleMath+, ManualSigmas, LTXVScheduler, easy showAnything, LTX2_NAG, LTXAVTextEncoderLoader, GetNode, LTXVEmptyLatentAudio, GetNode, EmptyLTXVLatentVideo, GetNode, SetNode, Reroute, SamplerCustomAdvanced, LTXVAddGuide, SetNode, easy showAnything, Reroute, Reroute, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, LoadImage, CLIPTextEncode, ImpactFloat, ImpactInt, easy int, PromptRelayEncodeTimeline, LayerUtility: ImageScaleByAspectRatio V2, Int, GetNode, GetNode, SetNode, Reroute, Reroute, Reroute, LatentUpscaleModelLoader, LTXVLatentUpsampler, GetNode, LTXVImgToVideoInplace, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, RandomNoise, CFGGuider, Reroute, Reroute, LTXVAudioVAEDecode, Reroute, VHS_VideoCombine, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, VAEDecode, Fast Groups Bypasser (rgthree), VAEDecodeTiled, Reroute, Reroute, VHS_VideoCombine, VAEDecodeTiled, LTXVAudioVAEDecode, Reroute, VHS_VideoCombine, Reroute]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3-PromptRelay-首尾帧-多镜头分镜控制+逻辑控制+长视频+无字幕版_2052407231588646913.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2052407231588646913.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（109 个）：
- `Reroute`
- `CFGGuider`
- `RandomNoise`
- `Reroute`
- `LTXVSeparateAVLatent`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LTXVCropGuides`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LTXVPreprocess`
- `LoraLoaderModelOnly` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `LTXVImgToVideoInplaceKJ`
- `SetNode`
- `SetNode`
- `LTXVPreprocess`
- `SetNode`
- `easy showAnything`
- `easy showAnything`
- `LTXVChunkFeedForward`
- `ModelPatchTorchSettings`
- `LTXVAudioVAELoader`
- `KSamplerSelect` ★核心
- `ImageResizeKJ`
- `LTXVConcatAVLatent`
- `LTXVAddGuide`
- `LTXVConditioning`
- `GetNode`
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `PathchSageAttentionKJ`
- `SimpleMath+`
- `ManualSigmas`
- `LTXVScheduler`
- `easy showAnything`
- `LTX2_NAG`
- `LTXAVTextEncoderLoader`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `SetNode`
- `Reroute`
- `SamplerCustomAdvanced` ★核心
- `LTXVAddGuide`
- `SetNode`
- `easy showAnything`
- `Reroute`
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `ImpactFloat`
- `ImpactInt`
- `easy int`
- `PromptRelayEncodeTimeline`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `GetNode`
- `GetNode`
- `SetNode`
- `Reroute`
- `Reroute`
- `Reroute`
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `CFGGuider`
- `Reroute`
- `Reroute`
- `LTXVAudioVAEDecode` ★核心
- `Reroute`
- `VHS_VideoCombine`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `VAEDecode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `VAEDecodeTiled` ★核心
- `Reroute`
- `Reroute`
- `VHS_VideoCombine`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `Reroute`
- `VHS_VideoCombine`
- `Reroute`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **54%**（59/109）

**有卡**：`CFGGuider`、`RandomNoise`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LTXVPreprocess`、`LoraLoaderModelOnly`、`LTXVImgToVideoInplaceKJ`、`LTXVChunkFeedForward`、`ModelPatchTorchSettings`、`LTXVAudioVAELoader`、`KSamplerSelect`、`ImageResizeKJ`、`LTXVConcatAVLatent`、`LTXVAddGuide`、`LTXVConditioning`、`CheckpointLoaderSimple`、`PathchSageAttentionKJ`、`SimpleMath+`、`ManualSigmas`、`LTXVScheduler`、`LTX2_NAG`、`LTXAVTextEncoderLoader`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`SamplerCustomAdvanced`、`LoadImage`、`CLIPTextEncode`、`ImpactFloat`、`ImpactInt`、`easy int`、`PromptRelayEncodeTimeline`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`、`VAEDecode`、`VAEDecodeTiled`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect

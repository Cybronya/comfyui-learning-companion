---
key: 视频生成/图生视频/LTX2.3-PromptRelay-V2-多镜头分镜控制+逻辑控制+长视频+无字幕版图生视频_2058206526581600258.json
name: LTX2.3-PromptRelay-V2-多镜头分镜控制+逻辑控制+长视频+无字幕版图生视频_2058206526581600258.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2058206526581600258.json
hash: f59070d093eaaa43
coverage: 0.655914
learned_at: 2026-10-15 22:38:19
nodes: [PathchSageAttentionKJ, ModelPatchTorchSettings, Reroute, Reroute, LTXVChunkFeedForward, Reroute, Reroute, Reroute, SamplerCustomAdvanced, RandomNoise, KSamplerSelect, LTXVImgToVideoInplace, Reroute, LTXVConcatAVLatent, Reroute, LTXVCropGuides, Reroute, LTXVCropGuides, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, LTXVLatentUpsampler, LatentUpscaleModelLoader, LTXVSeparateAVLatent, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, LTXVAudioVAELoader, LTXVImgToVideoInplace, LTXVConcatAVLatent, Reroute, Reroute, CLIPTextEncode, LTXVScheduler, ManualSigmas, LTXVEmptyLatentAudio, VAEDecodeTiled, LTXVAudioVAEDecode, easy showAnything, easy showAnything, easy showAnything, Reroute, VAEDecode, LTXVAudioVAEDecode, SimpleMath+, VHS_VideoCombine, ManualSigmas, LTXAVTextEncoderLoader, VAELoaderKJ, VHS_VideoCombine, LTXVCropGuides, CFGGuider, easy int, SimpleMath+, easy int, ManualSigmas, LTXVSeparateAVLatent, SamplerCustomAdvanced, KSamplerSelect, Reroute, easy int, CheckpointLoaderSimple, LTX2SamplingPreviewOverride, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LTX2_NAG, Reroute, CFGGuider, LTXVConditioning, RandomNoise, easy int, SimpleMath+, ImageResizeKJv2, LTXVPreprocess, ImageScaleBy, GetImageSize, EmptyLTXVLatentVideo, VHS_VideoCombine, PromptRelayEncodeTimeline, LoadImage, Fast Groups Bypasser (rgthree), easy showAnything, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 24, "width": 97}
---

# 视频生成/图生视频/LTX2.3-PromptRelay-V2-多镜头分镜控制+逻辑控制+长视频+无字幕版图生视频_2058206526581600258.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2058206526581600258.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（93 个）：
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `Reroute`
- `Reroute`
- `LTXVChunkFeedForward`
- `Reroute`
- `Reroute`
- `Reroute`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `LTXVImgToVideoInplace`
- `Reroute`
- `LTXVConcatAVLatent`
- `Reroute`
- `LTXVCropGuides`
- `Reroute`
- `LTXVCropGuides`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LTXVLatentUpsampler` ★核心
- `LatentUpscaleModelLoader`
- `LTXVSeparateAVLatent`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LTXVAudioVAELoader`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `Reroute`
- `Reroute`
- `CLIPTextEncode` ★核心
- `LTXVScheduler`
- `ManualSigmas`
- `LTXVEmptyLatentAudio` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `Reroute`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `SimpleMath+`
- `VHS_VideoCombine`
- `ManualSigmas`
- `LTXAVTextEncoderLoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `LTXVCropGuides`
- `CFGGuider`
- `easy int`
- `SimpleMath+`
- `easy int`
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `Reroute`
- `easy int`
- `CheckpointLoaderSimple` ★核心
- `LTX2SamplingPreviewOverride`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTX2_NAG`
- `Reroute`
- `CFGGuider`
- `LTXVConditioning`
- `RandomNoise`
- `easy int`
- `SimpleMath+`
- `ImageResizeKJv2`
- `LTXVPreprocess`
- `ImageScaleBy`
- `GetImageSize`
- `EmptyLTXVLatentVideo`
- `VHS_VideoCombine`
- `PromptRelayEncodeTimeline`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `easy showAnything`
- `MarkdownNote`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **66%**（61/93）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`SamplerCustomAdvanced`、`RandomNoise`、`KSamplerSelect`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`LTXVSeparateAVLatent`、`LTXVAudioVAELoader`、`CLIPTextEncode`、`LTXVScheduler`、`ManualSigmas`、`LTXVEmptyLatentAudio`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`VAEDecode`、`SimpleMath+`、`VHS_VideoCombine`、`LTXAVTextEncoderLoader`、`VAELoaderKJ`、`CFGGuider`、`easy int`、`CheckpointLoaderSimple`、`LTX2SamplingPreviewOverride`、`LoraLoaderModelOnly`、`LTX2_NAG`、`LTXVConditioning`、`ImageResizeKJv2`、`LTXVPreprocess`、`ImageScaleBy`、`GetImageSize`、`EmptyLTXVLatentVideo`、`PromptRelayEncodeTimeline`、`LoadImage`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

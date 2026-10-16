---
key: 视频生成/图生视频/【LTX2.3+PromptRelay-V2】-多镜头分镜控制+逻辑控制+长视频+无字幕版图生视频_2058353151778058241.json
name: 【LTX2.3+PromptRelay-V2】-多镜头分镜控制+逻辑控制+长视频+无字幕版图生视频_2058353151778058241.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2058353151778058241.json
hash: deef3dfd9ff18dc8
coverage: 0.897059
learned_at: 2026-10-15 22:38:20
nodes: [ModelPatchTorchSettings, SamplerCustomAdvanced, Reroute, LTXVImgToVideoInplace, LTXVScheduler, LTXVEmptyLatentAudio, easy showAnything, easy showAnything, SimpleMath+, ManualSigmas, VHS_VideoCombine, SimpleMath+, SimpleMath+, ImageResizeKJv2, LTXVPreprocess, ImageScaleBy, GetImageSize, EmptyLTXVLatentVideo, easy showAnything, LTXVConcatAVLatent, CFGGuider, LTXAVTextEncoderLoader, LTXVAudioVAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LTX2SamplingPreviewOverride, LoraLoaderModelOnly, easy int, easy int, easy int, easy int, LTXVChunkFeedForward, CheckpointLoaderSimple, PathchSageAttentionKJ, LoraLoaderModelOnly, VAELoaderKJ, CLIPTextEncode, LTX2_NAG, KSamplerSelect, LTXVConditioning, RandomNoise, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, LTXVAudioVAEDecode, easy showAnything, VAEDecodeTiled, VHS_VideoCombine, LTXVImgToVideoInplace, RandomNoise, CFGGuider, LTXVCropGuides, KSamplerSelect, ManualSigmas, LTXVLatentUpsampler, LatentUpscaleModelLoader, LTXVConcatAVLatent, LTXVSeparateAVLatent, VAEDecode, LTXVAudioVAEDecode, LTXVCropGuides, LoadImage, PromptRelayEncodeTimeline, MarkdownNote, VHS_VideoCombine, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 24, "width": 97}
---

# 视频生成/图生视频/【LTX2.3+PromptRelay-V2】-多镜头分镜控制+逻辑控制+长视频+无字幕版图生视频_2058353151778058241.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2058353151778058241.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（68 个）：
- `ModelPatchTorchSettings`
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `LTXVImgToVideoInplace`
- `LTXVScheduler`
- `LTXVEmptyLatentAudio` ★核心
- `easy showAnything`
- `easy showAnything`
- `SimpleMath+`
- `ManualSigmas`
- `VHS_VideoCombine`
- `SimpleMath+`
- `SimpleMath+`
- `ImageResizeKJv2`
- `LTXVPreprocess`
- `ImageScaleBy`
- `GetImageSize`
- `EmptyLTXVLatentVideo`
- `easy showAnything`
- `LTXVConcatAVLatent`
- `CFGGuider`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTX2SamplingPreviewOverride`
- `LoraLoaderModelOnly` ★核心
- `easy int`
- `easy int`
- `easy int`
- `easy int`
- `LTXVChunkFeedForward`
- `CheckpointLoaderSimple` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `VAELoaderKJ`
- `CLIPTextEncode` ★核心
- `LTX2_NAG`
- `KSamplerSelect` ★核心
- `LTXVConditioning`
- `RandomNoise`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVAudioVAEDecode` ★核心
- `easy showAnything`
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `LTXVImgToVideoInplace`
- `RandomNoise`
- `CFGGuider`
- `LTXVCropGuides`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVLatentUpsampler` ★核心
- `LatentUpscaleModelLoader`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVCropGuides`
- `LoadImage`
- `PromptRelayEncodeTimeline`
- `MarkdownNote`
- `VHS_VideoCombine`
- `MarkdownNote`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **90%**（61/68）

**有卡**：`ModelPatchTorchSettings`、`SamplerCustomAdvanced`、`LTXVImgToVideoInplace`、`LTXVScheduler`、`LTXVEmptyLatentAudio`、`SimpleMath+`、`ManualSigmas`、`VHS_VideoCombine`、`ImageResizeKJv2`、`LTXVPreprocess`、`ImageScaleBy`、`GetImageSize`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`CFGGuider`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`LoraLoaderModelOnly`、`LTX2SamplingPreviewOverride`、`easy int`、`LTXVChunkFeedForward`、`CheckpointLoaderSimple`、`PathchSageAttentionKJ`、`VAELoaderKJ`、`CLIPTextEncode`、`LTX2_NAG`、`KSamplerSelect`、`LTXVConditioning`、`RandomNoise`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`VAEDecode`、`LoadImage`、`PromptRelayEncodeTimeline`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

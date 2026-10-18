---
key: 视频生成/图生视频/LTX2.3-多镜头分镜控制+逻辑控制+长视频+无字幕版图生视频PromptRelay_2051939042543063041.json
name: LTX2.3-多镜头分镜控制+逻辑控制+长视频+无字幕版图生视频PromptRelay_2051939042543063041.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3-多镜头分镜控制+逻辑控制+长视频+无字幕版图生视频PromptRelay_2051939042543063041.json
hash: f216522abcf92feb
coverage: 0.609756
learned_at: 2026-10-15 22:37:25
nodes: [Note, Reroute, PathchSageAttentionKJ, ModelPatchTorchSettings, MarkdownNote, Reroute, easy showAnything, Reroute, LayerUtility: ImageScaleByAspectRatio V2, KSamplerSelect, ManualSigmas, RandomNoise, LTXVChunkFeedForward, VAEDecodeTiled, Reroute, LTXVSeparateAVLatent, SamplerCustomAdvanced, CFGGuider, ManualSigmas, Reroute, Reroute, VAEDecode, LTXVConditioning, VHS_VideoCombine, VHS_VideoCombine, SamplerCustomAdvanced, RandomNoise, KSamplerSelect, CFGGuider, LTXVImgToVideoInplace, ManualSigmas, Reroute, LTXVConcatAVLatent, Reroute, LTXVAudioVAEDecode, LTXVCropGuides, LTXVAudioVAEDecode, Reroute, LTXVCropGuides, VAEDecodeTiled, Reroute, LTXVCropGuides, Reroute, Reroute, Reroute, Reroute, Reroute, LTXVLatentUpsampler, LatentUpscaleModelLoader, LTXVSeparateAVLatent, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, CheckpointLoaderSimple, LoraLoaderModelOnly, Reroute, LoraLoaderModelOnly, LoraLoaderModelOnly, LTXAVTextEncoderLoader, LTXVAudioVAELoader, SimpleMath+, easy showAnything, easy showAnything, EmptyLTXVLatentVideo, LTXVPreprocess, LTXVImgToVideoInplace, LTXVEmptyLatentAudio, LTXVConcatAVLatent, LTXVScheduler, Reroute, Reroute, LTX2_NAG, easy int, easy showAnything, LoadImage, PromptRelayEncodeTimeline, CLIPTextEncode]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 30, "width": 97}
---

# 视频生成/图生视频/LTX2.3-多镜头分镜控制+逻辑控制+长视频+无字幕版图生视频PromptRelay_2051939042543063041.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2051939042543063041.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（82 个）：
- `Note`
- `Reroute`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `MarkdownNote`
- `Reroute`
- `easy showAnything`
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `LTXVChunkFeedForward`
- `VAEDecodeTiled` ★核心
- `Reroute`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `ManualSigmas`
- `Reroute`
- `Reroute`
- `VAEDecode` ★核心
- `LTXVConditioning`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `LTXVImgToVideoInplace`
- `ManualSigmas`
- `Reroute`
- `LTXVConcatAVLatent`
- `Reroute`
- `LTXVAudioVAEDecode` ★核心
- `LTXVCropGuides`
- `LTXVAudioVAEDecode` ★核心
- `Reroute`
- `LTXVCropGuides`
- `VAEDecodeTiled` ★核心
- `Reroute`
- `LTXVCropGuides`
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
- `Reroute`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `SimpleMath+`
- `easy showAnything`
- `easy showAnything`
- `EmptyLTXVLatentVideo`
- `LTXVPreprocess`
- `LTXVImgToVideoInplace`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `LTXVScheduler`
- `Reroute`
- `Reroute`
- `LTX2_NAG`
- `easy int`
- `easy showAnything`
- `LoadImage`
- `PromptRelayEncodeTimeline`
- `CLIPTextEncode` ★核心

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `30`
- `batch_size` = `1`

## 知识

覆盖率 **61%**（50/82）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSamplerSelect`、`ManualSigmas`、`RandomNoise`、`LTXVChunkFeedForward`、`VAEDecodeTiled`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`CFGGuider`、`VAEDecode`、`LTXVConditioning`、`VHS_VideoCombine`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`LTXVAudioVAEDecode`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`SimpleMath+`、`EmptyLTXVLatentVideo`、`LTXVPreprocess`、`LTXVEmptyLatentAudio`、`LTXVScheduler`、`LTX2_NAG`、`easy int`、`LoadImage`、`PromptRelayEncodeTimeline`、`CLIPTextEncode`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

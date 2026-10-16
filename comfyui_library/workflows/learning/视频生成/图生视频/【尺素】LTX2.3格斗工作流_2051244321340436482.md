---
key: 视频生成/图生视频/【尺素】LTX2.3格斗工作流_2051244321340436482.json
name: 【尺素】LTX2.3格斗工作流_2051244321340436482.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2051244321340436482.json
hash: b2a694018171350c
coverage: 0.645161
learned_at: 2026-10-15 22:37:21
nodes: [PreviewAny, Reroute, LTX2SamplingPreviewOverride, Reroute, Reroute, Reroute, ManualSigmas, Reroute, Reroute, Reroute, Reroute, Reroute, RandomNoise, MathExpression|pysssss, Reroute, SetLatentNoiseMask, KSamplerSelect, LTXVEmptyLatentAudio, Reroute, Reroute, Reroute, Reroute, Reroute, LTXVAudioVAEDecode, LTXVConditioning, CLIPTextEncode, CFGGuider, LTXVAudioVAEEncode, Reroute, Reroute, LTXVImgToVideoInplace, PrimitiveBoolean, Reroute, Reroute, LTXVConcatAVLatent, RandomNoise, SimpleMath+, SimpleMath+, Reroute, LTXVAudioVAELoader, LTXAVTextEncoderLoader, MelBandRoFormerModelLoader, LoraLoaderModelOnly, LatentUpscaleModelLoader, LTXVSeparateAVLatent, LTXVLatentUpsampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAEDecodeTiled, VHS_VideoCombine, TextGenerateLTX2Prompt, PreviewAny, Reroute, EmptyLTXVLatentVideo, VHS_VideoCombine, LTXVSeparateAVLatent, SamplerCustomAdvanced, SamplerCustomAdvanced, SolidMask, LTXVImgToVideoInplace, ManualSigmas, MelBandRoFormerSampler, VAELoader, CheckpointLoaderSimple, GetImageSize, ImageScaleBy, ResizeImagesByLongerEdge, LTXVPreprocess, LayerUtility: ImageScaleByAspectRatio V2, Reroute, LoraLoader, PreviewAudio, Audio Duration (mtb), CLIPTextEncode, LTX2_NAG, LoadAudio, CFGGuider, PrimitiveFloat, PrimitiveInt, easy seed, VAEDecodeTiled, Reroute, Reroute, MarkdownNote, LoraLoaderModelOnly, MarkdownNote, MarkdownNote, LoadImage, PrimitiveStringMultiline, ComfySwitchNode, AudioCrop]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors", "height": 25, "lora_name": "gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors", "strength_clip": 1, "strength_model": 1, "width": 121}
---

# 视频生成/图生视频/【尺素】LTX2.3格斗工作流_2051244321340436482.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2051244321340436482.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（93 个）：
- `PreviewAny`
- `Reroute`
- `LTX2SamplingPreviewOverride`
- `Reroute`
- `Reroute`
- `Reroute`
- `ManualSigmas`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `RandomNoise`
- `MathExpression|pysssss`
- `Reroute`
- `SetLatentNoiseMask`
- `KSamplerSelect` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LTXVAudioVAEDecode` ★核心
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `LTXVAudioVAEEncode` ★核心
- `Reroute`
- `Reroute`
- `LTXVImgToVideoInplace`
- `PrimitiveBoolean`
- `Reroute`
- `Reroute`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `SimpleMath+`
- `SimpleMath+`
- `Reroute`
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `MelBandRoFormerModelLoader`
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `TextGenerateLTX2Prompt`
- `PreviewAny`
- `Reroute`
- `EmptyLTXVLatentVideo`
- `VHS_VideoCombine`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `SolidMask`
- `LTXVImgToVideoInplace`
- `ManualSigmas`
- `MelBandRoFormerSampler` ★核心
- `VAELoader`
- `CheckpointLoaderSimple` ★核心
- `GetImageSize`
- `ImageScaleBy`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Reroute`
- `LoraLoader` ★核心
- `PreviewAudio`
- `Audio Duration (mtb)`
- `CLIPTextEncode` ★核心
- `LTX2_NAG`
- `LoadAudio`
- `CFGGuider`
- `PrimitiveFloat`
- `PrimitiveInt`
- `easy seed`
- `VAEDecodeTiled` ★核心
- `Reroute`
- `Reroute`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`
- `PrimitiveStringMultiline`
- `ComfySwitchNode`
- `AudioCrop`

**识别到的模式**：lora

## 关键参数

- `width` = `121`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`
- `lora_name` = `gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **65%**（60/93）

**有卡**：`LTX2SamplingPreviewOverride`、`ManualSigmas`、`RandomNoise`、`MathExpression|pysssss`、`SetLatentNoiseMask`、`KSamplerSelect`、`LTXVEmptyLatentAudio`、`LTXVAudioVAEDecode`、`LTXVConditioning`、`CLIPTextEncode`、`CFGGuider`、`LTXVAudioVAEEncode`、`LTXVImgToVideoInplace`、`PrimitiveBoolean`、`LTXVConcatAVLatent`、`SimpleMath+`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`MelBandRoFormerModelLoader`、`LoraLoaderModelOnly`、`LatentUpscaleModelLoader`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`VHS_VideoCombine`、`TextGenerateLTX2Prompt`、`EmptyLTXVLatentVideo`、`SamplerCustomAdvanced`、`SolidMask`、`MelBandRoFormerSampler`、`VAELoader`、`CheckpointLoaderSimple`、`GetImageSize`、`ImageScaleBy`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoraLoader`、`PreviewAudio`、`Audio Duration (mtb)`、`LTX2_NAG`、`LoadAudio`、`easy seed`、`LoadImage`、`AudioCrop`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect

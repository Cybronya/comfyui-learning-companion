---
key: 视频生成/图生视频/LTX 2.3  图片语音生成数字人工作流_2072578791876161538.json
name: LTX 2.3  图片语音生成数字人工作流_2072578791876161538.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2072578791876161538.json
hash: 4217196bfc89a4d4
coverage: 0.482456
learned_at: 2026-10-15 22:40:56
nodes: [GetNode, CLIPTextEncode, LTXVConditioning, SetNode, SetNode, SimpleMath+, GetNode, GetNode, GetNode, EmptyLTXVLatentVideo, GetNode, GetNode, GetNode, ManualSigmas, GetNode, GetNode, SamplerCustom, VAEDecodeTiled, GetNode, SimpleMath+, GetNode, GetNode, GetNode, SamplerCustom, GetNode, GetNode, ManualSigmas, LTXVConcatAVLatent, GetNode, LTXVLatentUpsampler, GetNode, LTXVSeparateAVLatent, GetNode, SetNode, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, VAEDecodeTiled, GetNode, VHS_VideoCombine, GetNode, SimpleMath+, GetNode, GetNode, LTXVAudioVAEEncode, SolidMask, GetNode, SetLatentNoiseMask, SetNode, GetNode, VHS_VideoCombine, PreviewImage, ResizeImageMaskNode, GetImageSize, SetNode, SetNode, SetNode, SimpleMath+, AudioInfo, SimpleMath+, Display Any (rgthree), SetNode, GetNode, SetNode, MelBandRoFormerSampler, GetNode, GetNode, LTXVConcatAVLatent, SetNode, SetNode, LTXVEmptyLatentAudio, GetNode, GetNode, LTXVSeparateAVLatent, SetNode, MarkdownNote, LoraLoaderModelOnly, DiffusionModelLoaderKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, SetNode, LatentUpscaleModelLoader, DualCLIPLoader, SetNode, SetNode, VAELoaderKJ, SetNode, VAELoaderKJ, SetNode, Seed (rgthree), SetNode, INTConstant, SetNode, KSamplerSelect, GetNode, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2SamplingPreviewOverride, AudioCrop, PreviewAudio, GetNode, ResizeImagesByLongerEdge, Note, CLIPTextEncode, LoadImage, LoadAudio, MelBandRoFormerModelLoader, GetNode, LTXVImgToVideoInplaceKJ, LTXVPreprocess, SetNode, LTXVImgToVideoInplaceKJ]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 121}
---

# 视频生成/图生视频/LTX 2.3  图片语音生成数字人工作流_2072578791876161538.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2072578791876161538.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（114 个）：
- `GetNode`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `SetNode`
- `SetNode`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `ManualSigmas`
- `GetNode`
- `GetNode`
- `SamplerCustom` ★核心
- `VAEDecodeTiled` ★核心
- `GetNode`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `GetNode`
- `SamplerCustom` ★核心
- `GetNode`
- `GetNode`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `GetNode`
- `SetLatentNoiseMask`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `PreviewImage`
- `ResizeImageMaskNode`
- `GetImageSize`
- `SetNode`
- `SetNode`
- `SetNode`
- `SimpleMath+`
- `AudioInfo`
- `SimpleMath+`
- `Display Any (rgthree)`
- `SetNode`
- `GetNode`
- `SetNode`
- `MelBandRoFormerSampler` ★核心
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `SetNode`
- `SetNode`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `SetNode`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `DiffusionModelLoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `LatentUpscaleModelLoader`
- `DualCLIPLoader`
- `SetNode`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `Seed (rgthree)`
- `SetNode`
- `INTConstant`
- `SetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `KSamplerSelect` ★核心
- `LTX2SamplingPreviewOverride`
- `LTX2SamplingPreviewOverride`
- `AudioCrop`
- `PreviewAudio`
- `GetNode`
- `ResizeImagesByLongerEdge`
- `Note`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadAudio`
- `MelBandRoFormerModelLoader`
- `GetNode`
- `LTXVImgToVideoInplaceKJ`
- `LTXVPreprocess`
- `SetNode`
- `LTXVImgToVideoInplaceKJ`

## 关键参数

- `width` = `121`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **48%**（55/114）

**有卡**：`CLIPTextEncode`、`LTXVConditioning`、`SimpleMath+`、`EmptyLTXVLatentVideo`、`ManualSigmas`、`SamplerCustom`、`VAEDecodeTiled`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`LTXVSeparateAVLatent`、`VHS_VideoCombine`、`LTXVAudioVAEEncode`、`SolidMask`、`SetLatentNoiseMask`、`ResizeImageMaskNode`、`GetImageSize`、`AudioInfo`、`Display Any (rgthree)`、`MelBandRoFormerSampler`、`LTXVEmptyLatentAudio`、`LoraLoaderModelOnly`、`DiffusionModelLoaderKJ`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`VAELoaderKJ`、`Seed (rgthree)`、`INTConstant`、`KSamplerSelect`、`LTX2SamplingPreviewOverride`、`AudioCrop`、`PreviewAudio`、`ResizeImagesByLongerEdge`、`LoadImage`、`LoadAudio`、`MelBandRoFormerModelLoader`、`LTXVImgToVideoInplaceKJ`、`LTXVPreprocess`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、KSamplerSelect、SamplerCustom、MelBandRoFormerSampler、LTXVLatentUpsampler、Seed (rgthree)

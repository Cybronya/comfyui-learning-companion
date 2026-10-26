---
key: 数字人/数字人/LTX 2.3  单图数字人高清工作流_2074911807369732098.json
name: LTX 2.3  单图数字人高清工作流_2074911807369732098
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX 2.3  单图数字人高清工作流_2074911807369732098.json
hash: ad9dc377db1d8fbd
coverage: 0.473282
learned_at: 2026-10-26 01:55:41
nodes: [GetNode, GetNode, GetNode, GetNode, SimpleMath+, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, EmptyLTXVLatentVideo, GetNode, VAEDecodeTiled, SetNode, LTXVConcatAVLatent, SetNode, LTXVEmptyLatentAudio, SetNode, GetNode, GetNode, LTXVSeparateAVLatent, KSamplerSelect, SamplerCustom, GetNode, GetNode, SetNode, VAEDecodeTiled, GetNode, SimpleMath+, GetNode, LTXVPreprocess, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, LTX2SamplingPreviewOverride, Display Any (rgthree), ShowText|pysssss, TextInput_, GetNode, RH_LLMAPI_Pro_Node, LTXVImgToVideoInplaceKJ, LoraLoaderModelOnly, SetNode, GetNode, GetNode, LTXVSeparateAVLatent, GetNode, GetNode, GetNode, ImageFlip, SetNode, ResizeImageMaskNode, GetImageSize, SetNode, SetNode, GetNode, GetNode, SimpleMath+, AudioInfo, GetNode, SimpleMath+, MelBandRoFormerSampler, MelBandRoFormerModelLoader, PreviewAudio, SetNode, GetNode, SetNode, LTXVAudioVAEEncode, SetLatentNoiseMask, SolidMask, GetNode, DiffusionModelLoaderKJ, DualCLIPLoader, VAELoaderKJ, VAELoaderKJ, ManualSigmas, SetNode, Seed (rgthree), SetNode, CLIPTextEncode, SimpleMath+, GetNode, GetNode, GetNode, LTXVConcatAVLatent, SamplerCustom, GetNode, KSamplerSelect, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVImgToVideoInplaceKJ, ManualSigmas, SetNode, LTX2SamplingPreviewOverride, Fast Groups Bypasser (rgthree), TextInput_, SetNode, LatentUpscaleModelLoader, SetNode, Note, SetNode, MarkdownNote, ImageResizeKJv2, INTConstant, VHS_VideoCombine, INTConstant, INTConstant, SetNode, SetNode, LoadImage, LTXVConditioning, PreviewAudio, SetNode, GetNode, VHS_VideoCombine, AudioCrop, SetNode, CLIPTextEncode, LoadAudio]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 121}
---

# 数字人/数字人/LTX 2.3  单图数字人高清工作流_2074911807369732098.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX 2.3  单图数字人高清工作流_2074911807369732098.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（131 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `SetNode`
- `LTXVConcatAVLatent`
- `SetNode`
- `LTXVEmptyLatentAudio` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `KSamplerSelect` ★核心
- `SamplerCustom` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `SimpleMath+`
- `GetNode`
- `LTXVPreprocess`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTX2SamplingPreviewOverride`
- `Display Any (rgthree)`
- `ShowText|pysssss`
- `TextInput_`
- `GetNode`
- `RH_LLMAPI_Pro_Node`
- `LTXVImgToVideoInplaceKJ`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageFlip`
- `SetNode`
- `ResizeImageMaskNode`
- `GetImageSize`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SimpleMath+`
- `AudioInfo`
- `GetNode`
- `SimpleMath+`
- `MelBandRoFormerSampler` ★核心
- `MelBandRoFormerModelLoader`
- `PreviewAudio`
- `SetNode`
- `GetNode`
- `SetNode`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `SolidMask`
- `GetNode`
- `DiffusionModelLoaderKJ`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `ManualSigmas`
- `SetNode`
- `Seed (rgthree)`
- `SetNode`
- `CLIPTextEncode` ★核心
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `SamplerCustom` ★核心
- `GetNode`
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplaceKJ`
- `ManualSigmas`
- `SetNode`
- `LTX2SamplingPreviewOverride`
- `Fast Groups Bypasser (rgthree)`
- `TextInput_`
- `SetNode`
- `LatentUpscaleModelLoader`
- `SetNode`
- `Note`
- `SetNode`
- `MarkdownNote`
- `ImageResizeKJv2`
- `INTConstant`
- `VHS_VideoCombine`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LTXVConditioning`
- `PreviewAudio`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `AudioCrop`
- `SetNode`
- `CLIPTextEncode` ★核心
- `LoadAudio`

## 关键参数

- `width` = `121`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **47%**（62/131）

**有卡**：`SimpleMath+`、`EmptyLTXVLatentVideo`、`VAEDecodeTiled`、`LTXVConcatAVLatent`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`KSamplerSelect`、`SamplerCustom`、`LTXVPreprocess`、`LoraLoaderModelOnly`、`LTX2SamplingPreviewOverride`、`Display Any (rgthree)`、`TextInput_`、`RH_LLMAPI_Pro_Node`、`LTXVImgToVideoInplaceKJ`、`ImageFlip`、`ResizeImageMaskNode`、`GetImageSize`、`AudioInfo`、`MelBandRoFormerSampler`、`MelBandRoFormerModelLoader`、`PreviewAudio`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`SolidMask`、`DiffusionModelLoaderKJ`、`DualCLIPLoader`、`VAELoaderKJ`、`ManualSigmas`、`Seed (rgthree)`、`CLIPTextEncode`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`ImageResizeKJv2`、`INTConstant`、`VHS_VideoCombine`、`LoadImage`、`LTXVConditioning`、`AudioCrop`、`LoadAudio`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、KSamplerSelect、SamplerCustom、MelBandRoFormerSampler、LTXVLatentUpsampler、Seed (rgthree)

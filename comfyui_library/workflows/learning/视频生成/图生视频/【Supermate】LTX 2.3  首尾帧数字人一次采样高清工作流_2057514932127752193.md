---
key: 视频生成/图生视频/【Supermate】LTX 2.3  首尾帧数字人一次采样高清工作流_2057514932127752193.json
name: 【Supermate】LTX 2.3  首尾帧数字人一次采样高清工作流_2057514932127752193.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【Supermate】LTX 2.3  首尾帧数字人一次采样高清工作流_2057514932127752193.json
hash: bf5a7406f54614ff
coverage: 0.479452
learned_at: 2026-10-15 22:38:13
nodes: [SetNode, LTXVSeparateAVLatent, LTXVAudioVAEEncode, SolidMask, SetNode, SetNode, SetNode, MelBandRoFormerSampler, SetNode, PreviewAudio, GetNode, GetNode, GetNode, GetNode, GetNode, SimpleMath+, GetNode, GetNode, INTConstant, GetNode, GetNode, GetNode, GetNode, KSamplerSelect, GetNode, GetNode, GetNode, SetNode, SetNode, LTXVLatentUpsampler, GetNode, GetNode, SimpleMath+, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, EmptyLTXVLatentVideo, LTXVConditioning, SetNode, ImageResizeKJv2, GetImageSize, SetNode, GetNode, ImageFlip, VAEDecodeTiled, LTXVConcatAVLatent, SetNode, LTXVEmptyLatentAudio, GetNode, CLIPTextEncode, Seed (rgthree), SetNode, GetNode, GetNode, GetNode, KSamplerSelect, GetNode, LTXVSeparateAVLatent, GetNode, GetNode, ImageResizeKJv2, ResizeImageMaskNode, GetNode, PreviewAudio, ImageFlip, GetNode, LTXVPreprocess, GetNode, SimpleMath+, AudioInfo, SimpleMath+, GetNode, Display Any (rgthree), VAELoaderKJ, VAELoaderKJ, LTXVImgToVideoInplaceKJ, ManualSigmas, LTXVConcatAVLatent, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, LatentUpscaleModelLoader, SetNode, MelBandRoFormerModelLoader, DualCLIPLoader, ManualSigmas, SetNode, SetNode, SetNode, ShowText|pysssss, SetNode, GetNode, PreviewImage, ImageConcanate, GetNode, RH_LLMAPI_Pro_Node, Note, TextInput_, GetNode, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), SetNode, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, GetNode, GetNode, GetNode, GetNode, INTConstant, INTConstant, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), CLIPTextEncode, SamplerCustom, VAEDecodeTiled, SetNode, LTXVImgToVideoInplaceKJ, MemoryCleaner, SamplerCustom, MemoryCleaner, SetNode, SetLatentNoiseMask, SetNode, LoraLoaderModelOnly, DiffusionModelLoaderKJ, SimpleMath+, VHS_VideoCombine, VHS_VideoCombine, TextInput_, LoadAudio, AudioCrop, GetNode, LTXVSeparateAVLatent, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 121}
---

# 视频生成/图生视频/【Supermate】LTX 2.3  首尾帧数字人一次采样高清工作流_2057514932127752193.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2057514932127752193.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（146 个）：
- `SetNode`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `SetNode`
- `SetNode`
- `SetNode`
- `MelBandRoFormerSampler` ★核心
- `SetNode`
- `PreviewAudio`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `INTConstant`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `GetNode`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `LTXVConditioning`
- `SetNode`
- `ImageResizeKJv2`
- `GetImageSize`
- `SetNode`
- `GetNode`
- `ImageFlip`
- `VAEDecodeTiled` ★核心
- `LTXVConcatAVLatent`
- `SetNode`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `Seed (rgthree)`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `ResizeImageMaskNode`
- `GetNode`
- `PreviewAudio`
- `ImageFlip`
- `GetNode`
- `LTXVPreprocess`
- `GetNode`
- `SimpleMath+`
- `AudioInfo`
- `SimpleMath+`
- `GetNode`
- `Display Any (rgthree)`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LTXVImgToVideoInplaceKJ`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LatentUpscaleModelLoader`
- `SetNode`
- `MelBandRoFormerModelLoader`
- `DualCLIPLoader`
- `ManualSigmas`
- `SetNode`
- `SetNode`
- `SetNode`
- `ShowText|pysssss`
- `SetNode`
- `GetNode`
- `PreviewImage`
- `ImageConcanate`
- `GetNode`
- `RH_LLMAPI_Pro_Node`
- `Note`
- `TextInput_`
- `GetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `SamplerCustom` ★核心
- `VAEDecodeTiled` ★核心
- `SetNode`
- `LTXVImgToVideoInplaceKJ`
- `MemoryCleaner`
- `SamplerCustom` ★核心
- `MemoryCleaner`
- `SetNode`
- `SetLatentNoiseMask`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `DiffusionModelLoaderKJ`
- `SimpleMath+`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `TextInput_`
- `LoadAudio`
- `AudioCrop`
- `GetNode`
- `LTXVSeparateAVLatent`
- `MarkdownNote`

## 关键参数

- `width` = `121`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **48%**（70/146）

**有卡**：`LTXVSeparateAVLatent`、`LTXVAudioVAEEncode`、`SolidMask`、`MelBandRoFormerSampler`、`PreviewAudio`、`SimpleMath+`、`INTConstant`、`KSamplerSelect`、`LTXVLatentUpsampler`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`ImageResizeKJv2`、`GetImageSize`、`ImageFlip`、`VAEDecodeTiled`、`LTXVConcatAVLatent`、`LTXVEmptyLatentAudio`、`CLIPTextEncode`、`Seed (rgthree)`、`ResizeImageMaskNode`、`LTXVPreprocess`、`AudioInfo`、`Display Any (rgthree)`、`VAELoaderKJ`、`LTXVImgToVideoInplaceKJ`、`ManualSigmas`、`LatentUpscaleModelLoader`、`MelBandRoFormerModelLoader`、`DualCLIPLoader`、`ImageConcanate`、`RH_LLMAPI_Pro_Node`、`TextInput_`、`Label (rgthree)`、`LoraLoaderModelOnly`、`LoadImage`、`SamplerCustom`、`MemoryCleaner`、`SetLatentNoiseMask`、`DiffusionModelLoaderKJ`、`VHS_VideoCombine`、`LoadAudio`、`AudioCrop`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、KSamplerSelect、SamplerCustom、MelBandRoFormerSampler、LTXVLatentUpsampler、Seed (rgthree)

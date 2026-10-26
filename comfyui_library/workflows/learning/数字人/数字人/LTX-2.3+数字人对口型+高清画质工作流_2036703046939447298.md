---
key: 数字人/数字人/LTX-2.3+数字人对口型+高清画质工作流_2036703046939447298.json
name: LTX-2.3+数字人对口型+高清画质工作流_2036703046939447298
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX-2.3+数字人对口型+高清画质工作流_2036703046939447298.json
hash: dae2f2602f8ca2e0
coverage: 0.487805
learned_at: 2026-10-26 01:55:43
nodes: [LTXVImgToVideoInplace, LTXVSeparateAVLatent, LTXVConcatAVLatent, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, LTXVLatentUpsampler, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VAEDecodeTiled, GetNode, GetNode, GetNode, SetNode, LTXVPreprocess, GetNode, SetNode, SamplerCustom, SamplerCustom, SetNode, Seed (rgthree), LatentUpscaleModelLoader, DualCLIPLoader, VAELoader, VAELoaderKJ, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, LTXVChunkFeedForward, PathchSageAttentionKJ, SetNode, SetNode, GetNode, LTXVConditioning, LTXVScheduler, CLIPTextEncode, JoinStrings, TextInput_, TextInput_, SetNode, RH_LLMAPI_NODE, GetNode, SetLatentNoiseMask, GetNode, LTXVAudioVAEEncode, GetNode, GetNode, MelBandRoFormerSampler, SetNode, PreviewAudio, PreviewAudio, SetNode, SimpleMath+, SetNode, MelBandRoFormerModelLoader, Display Any (rgthree), SimpleMath+, AudioInfo, GetNode, SolidMask, SetNode, SetNode, SetNode, SetNode, PrimitiveBoolean, INTConstant, INTConstant, INTConstant, ResizeImagesByLongerEdge, GetNode, GetNode, SetNode, ImageResizeKJv2, SetNode, SetNode, SetNode, JDC_ResizeFactor, GetNode, GetNode, VHS_VideoCombine, SimpleMath+, GetImageSize, ManualSigmas, ManualSigmas, ShowText|pysssss, LTXVScheduler, UNETLoader, LoraLoaderModelOnly, LTX2_NAG, GetNode, GetNode, GetNode, KSamplerSelect, KSamplerSelect, Fast Groups Bypasser (rgthree), CLIPTextEncode, GetNode, LoadImage, LTXVConcatAVLatent, SetNode, GetNode, TextInput_, LoadAudio, AudioCrop, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
---

# 数字人/数字人/LTX-2.3+数字人对口型+高清画质工作流_2036703046939447298.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX-2.3+数字人对口型+高清画质工作流_2036703046939447298.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（123 个）：
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `LTXVPreprocess`
- `GetNode`
- `SetNode`
- `SamplerCustom` ★核心
- `SamplerCustom` ★核心
- `SetNode`
- `Seed (rgthree)`
- `LatentUpscaleModelLoader`
- `DualCLIPLoader`
- `VAELoader`
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LTXVChunkFeedForward`
- `PathchSageAttentionKJ`
- `SetNode`
- `SetNode`
- `GetNode`
- `LTXVConditioning`
- `LTXVScheduler`
- `CLIPTextEncode` ★核心
- `JoinStrings`
- `TextInput_`
- `TextInput_`
- `SetNode`
- `RH_LLMAPI_NODE`
- `GetNode`
- `SetLatentNoiseMask`
- `GetNode`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `GetNode`
- `MelBandRoFormerSampler` ★核心
- `SetNode`
- `PreviewAudio`
- `PreviewAudio`
- `SetNode`
- `SimpleMath+`
- `SetNode`
- `MelBandRoFormerModelLoader`
- `Display Any (rgthree)`
- `SimpleMath+`
- `AudioInfo`
- `GetNode`
- `SolidMask`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PrimitiveBoolean`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `ResizeImagesByLongerEdge`
- `GetNode`
- `GetNode`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `SetNode`
- `JDC_ResizeFactor`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `SimpleMath+`
- `GetImageSize`
- `ManualSigmas`
- `ManualSigmas`
- `ShowText|pysssss`
- `LTXVScheduler`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTX2_NAG`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `Fast Groups Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `GetNode`
- `LoadImage`
- `LTXVConcatAVLatent`
- `SetNode`
- `GetNode`
- `TextInput_`
- `LoadAudio`
- `AudioCrop`
- `Fast Groups Bypasser (rgthree)`

## 知识

覆盖率 **49%**（60/123）

**有卡**：`LTXVImgToVideoInplace`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`LTXVPreprocess`、`SamplerCustom`、`Seed (rgthree)`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`VAELoader`、`VAELoaderKJ`、`LTXVChunkFeedForward`、`PathchSageAttentionKJ`、`LTXVConditioning`、`LTXVScheduler`、`CLIPTextEncode`、`JoinStrings`、`TextInput_`、`RH_LLMAPI_NODE`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`MelBandRoFormerSampler`、`PreviewAudio`、`SimpleMath+`、`MelBandRoFormerModelLoader`、`Display Any (rgthree)`、`AudioInfo`、`SolidMask`、`PrimitiveBoolean`、`INTConstant`、`ResizeImagesByLongerEdge`、`ImageResizeKJv2`、`JDC_ResizeFactor`、`VHS_VideoCombine`、`GetImageSize`、`ManualSigmas`、`UNETLoader`、`LoraLoaderModelOnly`、`LTX2_NAG`、`KSamplerSelect`、`LoadImage`、`LoadAudio`、`AudioCrop`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、MelBandRoFormerSampler

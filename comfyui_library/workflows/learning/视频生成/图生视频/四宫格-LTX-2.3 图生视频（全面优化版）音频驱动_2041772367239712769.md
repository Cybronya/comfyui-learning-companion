---
key: 视频生成/图生视频/四宫格-LTX-2.3 图生视频（全面优化版）音频驱动_2041772367239712769.json
name: 四宫格-LTX-2.3 图生视频（全面优化版）音频驱动_2041772367239712769.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2041772367239712769.json
hash: 7df44ea935a41f08
coverage: 0.641304
learned_at: 2026-10-15 22:36:22
nodes: [SetNode, SetNode, SimpleMath+, SetNode, PrimitiveFloat, LTXVAudioVAEDecode, GetNode, ImageResizeKJv2, ImageResizeKJv2, SetNode, GuHaiAutoImageSplit, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, SetNode, SetNode, ImageResizeKJv2, SetNode, GetNode, GetNode, GetNode, VAELoaderKJ, DualCLIPLoader, SetNode, CFGGuider, RandomNoise, KSamplerSelect, ManualSigmas, GetNode, GetNode, CLIPTextEncode, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVConditioning, GetNode, easy cleanGpuUsed, VAEDecodeTiled, ImageFromBatch+, VHS_VideoCombine, SetNode, PreviewImage, RH_LLMAPI_Pro_Node, easy showAnything, Fast Groups Bypasser (rgthree), VAELoader, PrimitiveNode, LoadImage, LoadImage, LoadImage, LoadImage, RH_Nano_Banana2_Gemini31Flash, SaveImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), CR Text, RH_LLMAPI_Pro_Node, easy cleanGpuUsed, easy showAnything, Text, UNETLoader, UNETLoader, LatentUpscaleModelLoader, SetNode, GetNode, SetNode, SetNode, LTXVConcatAVLatent, ImageResizeKJv2, LTXVCropGuides, TTResolutionSelector, LTXVAudioVAEEncode, Display Any (rgthree), PreviewAudio, SetLatentNoiseMask, SolidMask, GetNode, SimpleMath+, EmptyLTXVLatentVideo, GetNode, GetNode, INTConstant, LoadImage, GetNode, PreviewAudio, MelBandRoFormerModelLoader, MelBandRoFormerSampler, AudioInfo, GetNode, LoadAudio, AudioCrop, LTXVAddGuideMulti, CLIPTextEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/四宫格-LTX-2.3 图生视频（全面优化版）音频驱动_2041772367239712769.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2041772367239712769.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（92 个）：
- `SetNode`
- `SetNode`
- `SimpleMath+`
- `SetNode`
- `PrimitiveFloat`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `SetNode`
- `GuHaiAutoImageSplit`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `SetNode`
- `CFGGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVConditioning`
- `GetNode`
- `easy cleanGpuUsed`
- `VAEDecodeTiled` ★核心
- `ImageFromBatch+`
- `VHS_VideoCombine`
- `SetNode`
- `PreviewImage`
- `RH_LLMAPI_Pro_Node`
- `easy showAnything`
- `Fast Groups Bypasser (rgthree)`
- `VAELoader`
- `PrimitiveNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `RH_Nano_Banana2_Gemini31Flash`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `CR Text`
- `RH_LLMAPI_Pro_Node`
- `easy cleanGpuUsed`
- `easy showAnything`
- `Text`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LatentUpscaleModelLoader`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `LTXVConcatAVLatent`
- `ImageResizeKJv2`
- `LTXVCropGuides`
- `TTResolutionSelector`
- `LTXVAudioVAEEncode` ★核心
- `Display Any (rgthree)`
- `PreviewAudio`
- `SetLatentNoiseMask`
- `SolidMask`
- `GetNode`
- `SimpleMath+`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetNode`
- `INTConstant`
- `LoadImage`
- `GetNode`
- `PreviewAudio`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler` ★核心
- `AudioInfo`
- `GetNode`
- `LoadAudio`
- `AudioCrop`
- `LTXVAddGuideMulti`
- `CLIPTextEncode` ★核心

## 知识

覆盖率 **64%**（59/92）

**有卡**：`SimpleMath+`、`LTXVAudioVAEDecode`、`ImageResizeKJv2`、`GuHaiAutoImageSplit`、`ImageFromBatch+`、`VAELoaderKJ`、`DualCLIPLoader`、`CFGGuider`、`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVConditioning`、`easy cleanGpuUsed`、`VAEDecodeTiled`、`VHS_VideoCombine`、`RH_LLMAPI_Pro_Node`、`VAELoader`、`LoadImage`、`RH_Nano_Banana2_Gemini31Flash`、`SaveImage`、`CR Text`、`Text`、`UNETLoader`、`LatentUpscaleModelLoader`、`LTXVConcatAVLatent`、`LTXVCropGuides`、`TTResolutionSelector`、`LTXVAudioVAEEncode`、`Display Any (rgthree)`、`PreviewAudio`、`SetLatentNoiseMask`、`SolidMask`、`EmptyLTXVLatentVideo`、`INTConstant`、`MelBandRoFormerModelLoader`、`MelBandRoFormerSampler`、`AudioInfo`、`LoadAudio`、`AudioCrop`、`LTXVAddGuideMulti`

**用到的条目**：VAELoader、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler

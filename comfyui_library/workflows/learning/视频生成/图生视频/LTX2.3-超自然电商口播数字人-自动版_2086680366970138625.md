---
key: 视频生成/图生视频/LTX2.3-超自然电商口播数字人-自动版_2086680366970138625.json
name: LTX2.3-超自然电商口播数字人-自动版_2086680366970138625
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3-超自然电商口播数字人-自动版_2086680366970138625.json
hash: 13f60c42783d7c90
coverage: 0.443396
learned_at: 2026-10-16 21:07:14
nodes: [GetNode, PreviewAny, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, easy cleanGpuUsed, GetNode, GetNode, JSON取值节点, SetNode, SetNode, PreviewAny, PreviewAny, SetNode, PromptRelayEncode, DualCLIPLoader, VAELoaderKJ, VAELoaderKJ, LoraLoaderModelOnly, SetNode, SetNode, SetNode, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVConditioning, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, EmptyLTXVLatentVideo, SetNode, LTXVConcatAVLatent, KSamplerSelect, SetNode, IntToString, JoinStrings, JSON取值节点, JSON取值节点, Float, SetNode, GetNode, GetNode, GetNode, LTXVImgToVideoInplaceKJ, SetLatentNoiseMask, LTXVAudioVAEEncode, SolidMask, LoadImage, ImageResizeKJv2, DiffusionModelLoaderKJ, SetNode, SetNode, MelBandRoFormerModelLoader, SetNode, SetNode, SetNode, SetNode, Audio Duration (mtb), MathExpression|pysssss, easy showAnything, MathExpression|pysssss, MelBandRoFormerSampler, SetNode, PreviewImage, Int, Int, JoinStrings, PrimitiveString, Float, PrimitiveString, PreviewAny, Text, 1hew_StringJoinMulti, CLIPTextEncode, PreviewAny, VHS_VideoCombine, SamplerCustom, GetNode, GetNode, GetNode, ManualSigmas, GetNode, GetNode, LTXVSeparateAVLatent, VAEDecodeTiled, GetNode, GetNode, TTResolutionSelector, Note, Text, LoadAudio, AudioCrop, RH_LLMAPI_Pro_Node]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX2.3-超自然电商口播数字人-自动版_2086680366970138625.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.3-超自然电商口播数字人-自动版_2086680366970138625.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（106 个）：
- `GetNode`
- `PreviewAny`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `JSON取值节点`
- `SetNode`
- `SetNode`
- `PreviewAny`
- `PreviewAny`
- `SetNode`
- `PromptRelayEncode`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConditioning`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `SetNode`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `SetNode`
- `IntToString`
- `JoinStrings`
- `JSON取值节点`
- `JSON取值节点`
- `Float`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoInplaceKJ`
- `SetLatentNoiseMask`
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `LoadImage`
- `ImageResizeKJv2`
- `DiffusionModelLoaderKJ`
- `SetNode`
- `SetNode`
- `MelBandRoFormerModelLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Audio Duration (mtb)`
- `MathExpression|pysssss`
- `easy showAnything`
- `MathExpression|pysssss`
- `MelBandRoFormerSampler` ★核心
- `SetNode`
- `PreviewImage`
- `Int`
- `Int`
- `JoinStrings`
- `PrimitiveString`
- `Float`
- `PrimitiveString`
- `PreviewAny`
- `Text`
- `1hew_StringJoinMulti`
- `CLIPTextEncode` ★核心
- `PreviewAny`
- `VHS_VideoCombine`
- `SamplerCustom` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `ManualSigmas`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `GetNode`
- `TTResolutionSelector`
- `Note`
- `Text`
- `LoadAudio`
- `AudioCrop`
- `RH_LLMAPI_Pro_Node`

## 知识

覆盖率 **44%**（47/106）

**有卡**：`easy cleanGpuUsed`、`JSON取值节点`、`PromptRelayEncode`、`DualCLIPLoader`、`VAELoaderKJ`、`LoraLoaderModelOnly`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`KSamplerSelect`、`IntToString`、`JoinStrings`、`Float`、`LTXVImgToVideoInplaceKJ`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`SolidMask`、`LoadImage`、`ImageResizeKJv2`、`DiffusionModelLoaderKJ`、`MelBandRoFormerModelLoader`、`Audio Duration (mtb)`、`MathExpression|pysssss`、`MelBandRoFormerSampler`、`Int`、`Text`、`1hew_StringJoinMulti`、`CLIPTextEncode`、`VHS_VideoCombine`、`SamplerCustom`、`ManualSigmas`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`TTResolutionSelector`、`LoadAudio`、`AudioCrop`、`RH_LLMAPI_Pro_Node`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、KSamplerSelect、SamplerCustom、MelBandRoFormerSampler、LTXVConcatAVLatent、LTXVSeparateAVLatent

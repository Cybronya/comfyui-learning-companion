---
key: 数字人/数字人/LTX2.3-超自然口播数字人_2092655473743982594.json
name: LTX2.3-超自然口播数字人_2092655473743982594
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.3-超自然口播数字人_2092655473743982594.json
hash: e24a35ddb75966bc
coverage: 0.443396
learned_at: 2026-10-18 22:17:10
nodes: [GetNode, PreviewAny, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, easy cleanGpuUsed, GetNode, GetNode, JSON取值节点, SetNode, SetNode, PreviewAny, PreviewAny, SetNode, PromptRelayEncode, DualCLIPLoader, VAELoaderKJ, VAELoaderKJ, LoraLoaderModelOnly, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVConditioning, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, EmptyLTXVLatentVideo, SetNode, LTXVConcatAVLatent, KSamplerSelect, SetNode, IntToString, JoinStrings, JSON取值节点, JSON取值节点, GetNode, GetNode, GetNode, LTXVImgToVideoInplaceKJ, SetLatentNoiseMask, LTXVAudioVAEEncode, SolidMask, ImageResizeKJv2, DiffusionModelLoaderKJ, MelBandRoFormerModelLoader, SetNode, Audio Duration (mtb), MathExpression|pysssss, easy showAnything, MelBandRoFormerSampler, SetNode, JoinStrings, PrimitiveString, PrimitiveString, PreviewAny, 1hew_StringJoinMulti, CLIPTextEncode, PreviewAny, VHS_VideoCombine, SamplerCustom, GetNode, GetNode, GetNode, ManualSigmas, GetNode, GetNode, LTXVSeparateAVLatent, VAEDecodeTiled, GetNode, GetNode, AudioCrop, RH_LLMAPI_Pro_Node, LoraLoaderModelOnly, LoraLoaderModelOnly, PreviewImage, LoadImage, LoadAudio, Float, SetNode, Int, Int, TTResolutionSelector, SetNode, SetNode, MathExpression|pysssss, SetNode, SetNode, SetNode, Float, Note, Text, Text]
patterns: []
missing: []
---

# 数字人/数字人/LTX2.3-超自然口播数字人_2092655473743982594.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.3-超自然口播数字人_2092655473743982594.json`

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
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoInplaceKJ`
- `SetLatentNoiseMask`
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `ImageResizeKJv2`
- `DiffusionModelLoaderKJ`
- `MelBandRoFormerModelLoader`
- `SetNode`
- `Audio Duration (mtb)`
- `MathExpression|pysssss`
- `easy showAnything`
- `MelBandRoFormerSampler` ★核心
- `SetNode`
- `JoinStrings`
- `PrimitiveString`
- `PrimitiveString`
- `PreviewAny`
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
- `AudioCrop`
- `RH_LLMAPI_Pro_Node`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `LoadImage`
- `LoadAudio`
- `Float`
- `SetNode`
- `Int`
- `Int`
- `TTResolutionSelector`
- `SetNode`
- `SetNode`
- `MathExpression|pysssss`
- `SetNode`
- `SetNode`
- `SetNode`
- `Float`
- `Note`
- `Text`
- `Text`

## 知识

覆盖率 **44%**（47/106）

**有卡**：`easy cleanGpuUsed`、`JSON取值节点`、`PromptRelayEncode`、`DualCLIPLoader`、`VAELoaderKJ`、`LoraLoaderModelOnly`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`KSamplerSelect`、`IntToString`、`JoinStrings`、`LTXVImgToVideoInplaceKJ`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`SolidMask`、`ImageResizeKJv2`、`DiffusionModelLoaderKJ`、`MelBandRoFormerModelLoader`、`Audio Duration (mtb)`、`MathExpression|pysssss`、`MelBandRoFormerSampler`、`1hew_StringJoinMulti`、`CLIPTextEncode`、`VHS_VideoCombine`、`SamplerCustom`、`ManualSigmas`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`AudioCrop`、`RH_LLMAPI_Pro_Node`、`LoadImage`、`LoadAudio`、`Float`、`Int`、`TTResolutionSelector`、`Text`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、KSamplerSelect、SamplerCustom、MelBandRoFormerSampler、LTXVConcatAVLatent、LTXVSeparateAVLatent

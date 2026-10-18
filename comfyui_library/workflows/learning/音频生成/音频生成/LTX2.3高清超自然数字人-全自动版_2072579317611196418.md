---
key: 音频生成/音频生成/LTX2.3高清超自然数字人-全自动版_2072579317611196418.json
name: LTX2.3高清超自然数字人-全自动版_2072579317611196418
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/LTX2.3高清超自然数字人-全自动版_2072579317611196418.json
hash: 2bbe2cb24a196c49
coverage: 0.447619
learned_at: 2026-10-18 03:04:51
nodes: [SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, GetNode, LTXVConcatAVLatent, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, EmptyLTXVLatentVideo, VAELoaderKJ, VAELoaderKJ, GetNode, SetNode, GetNode, LTXVImgToVideoInplaceKJ, GetNode, KSamplerSelect, LTXVSeparateAVLatent, ManualSigmas, GetNode, SolidMask, VAEDecodeTiled, SetNode, ImageResizeKJv2, LTXVAudioVAEEncode, SetLatentNoiseMask, SamplerCustom, GetNode, GetNode, LTXVConditioning, SetNode, GetNode, GetNode, LoraLoaderModelOnly, DualCLIPLoader, easy cleanGpuUsed, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, SetNode, SetNode, PreviewImage, LoraLoaderModelOnly, SetNode, Float, SetNode, GetNode, RH_LLMAPI_Pro_Node, JSON取值节点, JSON取值节点, JSON取值节点, Float, SetNode, SetNode, PreviewAny, PreviewAny, PreviewAny, SetNode, PrimitiveString, JoinStrings, PrimitiveString, JoinStrings, GetNode, IntToString, Int, Int, PromptRelayEncode, VHS_VideoCombine, LoraLoaderModelOnly, DiffusionModelLoaderKJ, Text, PreviewAny, LoadImage, LoadAudio, TTResolutionSelector, Text, 1hew_StringJoinMulti, PreviewAny, MelBandRoFormerSampler, MelBandRoFormerModelLoader, AudioCrop, SetNode, Audio Duration (mtb), SetNode, MathExpression|pysssss, SetNode, MathExpression|pysssss, easy showAnything, SetNode, GetNode]
patterns: []
missing: []
---

# 音频生成/音频生成/LTX2.3高清超自然数字人-全自动版_2072579317611196418.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/LTX2.3高清超自然数字人-全自动版_2072579317611196418.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（105 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `GetNode`
- `SetNode`
- `GetNode`
- `LTXVImgToVideoInplaceKJ`
- `GetNode`
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `GetNode`
- `SolidMask`
- `VAEDecodeTiled` ★核心
- `SetNode`
- `ImageResizeKJv2`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `SamplerCustom` ★核心
- `GetNode`
- `GetNode`
- `LTXVConditioning`
- `SetNode`
- `GetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `Float`
- `SetNode`
- `GetNode`
- `RH_LLMAPI_Pro_Node`
- `JSON取值节点`
- `JSON取值节点`
- `JSON取值节点`
- `Float`
- `SetNode`
- `SetNode`
- `PreviewAny`
- `PreviewAny`
- `PreviewAny`
- `SetNode`
- `PrimitiveString`
- `JoinStrings`
- `PrimitiveString`
- `JoinStrings`
- `GetNode`
- `IntToString`
- `Int`
- `Int`
- `PromptRelayEncode`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `DiffusionModelLoaderKJ`
- `Text`
- `PreviewAny`
- `LoadImage`
- `LoadAudio`
- `TTResolutionSelector`
- `Text`
- `1hew_StringJoinMulti`
- `PreviewAny`
- `MelBandRoFormerSampler` ★核心
- `MelBandRoFormerModelLoader`
- `AudioCrop`
- `SetNode`
- `Audio Duration (mtb)`
- `SetNode`
- `MathExpression|pysssss`
- `SetNode`
- `MathExpression|pysssss`
- `easy showAnything`
- `SetNode`
- `GetNode`

## 知识

覆盖率 **45%**（47/105）

**有卡**：`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`VAELoaderKJ`、`LTXVImgToVideoInplaceKJ`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`ManualSigmas`、`SolidMask`、`VAEDecodeTiled`、`ImageResizeKJv2`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`SamplerCustom`、`LTXVConditioning`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`easy cleanGpuUsed`、`CLIPTextEncode`、`Float`、`RH_LLMAPI_Pro_Node`、`JSON取值节点`、`JoinStrings`、`IntToString`、`Int`、`PromptRelayEncode`、`VHS_VideoCombine`、`DiffusionModelLoaderKJ`、`Text`、`LoadImage`、`LoadAudio`、`TTResolutionSelector`、`1hew_StringJoinMulti`、`MelBandRoFormerSampler`、`MelBandRoFormerModelLoader`、`AudioCrop`、`Audio Duration (mtb)`、`MathExpression|pysssss`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、KSamplerSelect、SamplerCustom、MelBandRoFormerSampler、LTXVConcatAVLatent、LTXVSeparateAVLatent

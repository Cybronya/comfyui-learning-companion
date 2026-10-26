---
key: 数字人/数字人/绝对真实超自然 带货数字人【LTX2.3 高清全自动 奇变版】_2057303275329904641.json
name: 绝对真实超自然 带货数字人【LTX2.3 高清全自动 奇变版】_2057303275329904641
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/绝对真实超自然 带货数字人【LTX2.3 高清全自动 奇变版】_2057303275329904641.json
hash: b206fc067ac03263
coverage: 0.5125
learned_at: 2026-10-26 02:04:19
nodes: [GetNode, GetNode, GetNode, SolidMask, LTXVAudioVAEEncode, SetLatentNoiseMask, LTXVConditioning, SetNode, LTXVSeparateAVLatent, SamplerCustom, EmptyLTXVLatentVideo, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVImgToVideoInplaceKJ, LTXVConcatAVLatent, DualCLIPLoader, SetNode, VAELoaderKJ, SetNode, VAELoaderKJ, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, RHHiddenNodes, SetNode, SetNode, GetNode, PromptRelayEncode, RHHiddenNodes, ManualSigmas, GetNode, GetNode, GetNode, MathExpression|pysssss, MathExpression|pysssss, SetNode, SetNode, SetNode, Audio Duration (mtb), SetNode, MelBandRoFormerModelLoader, SetNode, AudioCrop, SetNode, SetNode, PrimitiveString, IntToString, GetNode, PrimitiveString, RHHiddenNodes, VAEDecodeTiled, LayerUtility: ImageScaleByAspectRatio V2, SetNode, MelBandRoFormerSampler, 1hew_StringJoinMulti, JoinStrings, JoinStrings, LoadImage, LoadImage, LoadAudio, Text, Float, VHS_VideoCombine, SetNode, JSON取值节点, JSON取值节点, SetNode, JSON取值节点, SetNode, Float, SetNode, RH_LLMAPI_Pro_Node]
patterns: []
missing: []
---

# 数字人/数字人/绝对真实超自然 带货数字人【LTX2.3 高清全自动 奇变版】_2057303275329904641.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/绝对真实超自然 带货数字人【LTX2.3 高清全自动 奇变版】_2057303275329904641.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（80 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `SolidMask`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `LTXVConditioning`
- `SetNode`
- `LTXVSeparateAVLatent`
- `SamplerCustom` ★核心
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoInplaceKJ`
- `LTXVConcatAVLatent`
- `DualCLIPLoader`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `RHHiddenNodes`
- `SetNode`
- `SetNode`
- `GetNode`
- `PromptRelayEncode`
- `RHHiddenNodes`
- `ManualSigmas`
- `GetNode`
- `GetNode`
- `GetNode`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `SetNode`
- `SetNode`
- `SetNode`
- `Audio Duration (mtb)`
- `SetNode`
- `MelBandRoFormerModelLoader`
- `SetNode`
- `AudioCrop`
- `SetNode`
- `SetNode`
- `PrimitiveString`
- `IntToString`
- `GetNode`
- `PrimitiveString`
- `RHHiddenNodes`
- `VAEDecodeTiled` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `MelBandRoFormerSampler` ★核心
- `1hew_StringJoinMulti`
- `JoinStrings`
- `JoinStrings`
- `LoadImage`
- `LoadImage`
- `LoadAudio`
- `Text`
- `Float`
- `VHS_VideoCombine`
- `SetNode`
- `JSON取值节点`
- `JSON取值节点`
- `SetNode`
- `JSON取值节点`
- `SetNode`
- `Float`
- `SetNode`
- `RH_LLMAPI_Pro_Node`

## 知识

覆盖率 **51%**（41/80）

**有卡**：`SolidMask`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`SamplerCustom`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplaceKJ`、`LTXVConcatAVLatent`、`DualCLIPLoader`、`VAELoaderKJ`、`CLIPTextEncode`、`RHHiddenNodes`、`PromptRelayEncode`、`ManualSigmas`、`MathExpression|pysssss`、`Audio Duration (mtb)`、`MelBandRoFormerModelLoader`、`AudioCrop`、`IntToString`、`VAEDecodeTiled`、`LayerUtility: ImageScaleByAspectRatio V2`、`MelBandRoFormerSampler`、`1hew_StringJoinMulti`、`JoinStrings`、`LoadImage`、`LoadAudio`、`Text`、`Float`、`VHS_VideoCombine`、`JSON取值节点`、`RH_LLMAPI_Pro_Node`

**用到的条目**：CLIPTextEncode、LoadImage、SamplerCustom、MelBandRoFormerSampler、LTXVConcatAVLatent、LTXVSeparateAVLatent、SetLatentNoiseMask、VAEDecodeTiled

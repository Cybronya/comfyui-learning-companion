---
key: 数字人/数字人/LTX2.3多场景数字人_2080282380560060417.json
name: LTX2.3多场景数字人_2080282380560060417
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.3多场景数字人_2080282380560060417.json
hash: 26c34af4f0b87ad8
coverage: 0.567568
learned_at: 2026-10-18 19:07:41
nodes: [VAELoaderKJ, SetNode, VAELoaderKJ, SetNode, SetNode, EmptyLTXVLatentVideo, SetNode, SetNode, ImageResizeKJv2, SetNode, GetNode, GetNode, RandomNoise, KSamplerSelect, LTXVImgToVideoInplace, SetNode, GetNode, GetNode, LTXVConcatAVLatent, SamplerCustomAdvanced, GetNode, LTXVSeparateAVLatent, GetNode, LTXVSpatioTemporalTiledVAEDecode, GetNode, MelBandRoFormerModelLoader, GetNode, MelBandRoFormerSampler, SetNode, LTXVAudioVAEEncode, SetLatentNoiseMask, SolidMask, LTXVAudioVAEDecode, Float, MathExpression|pysssss, SetNode, SetNode, GetNode, GetNode, LTXVConditioning, GetNode, Note, Int, Bool, Int, Reroute, GetNode, GetNode, DualCLIPLoader, LTX2_NAG, SetNode, DiffusionModelLoaderKJ, CLIPTextEncode, GetNode, TTResolutionSelector, MathExpression|pysssss, Audio Duration (mtb), SetNode, SetNode, RHHiddenNodes, Text, CFGGuider, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, ManualSigmas, RHHiddenNodes, LoraLoaderModelOnly, GetNode, GetNode, GetNode, LoadImage, LoadAudio, AudioCrop]
patterns: []
missing: []
---

# 数字人/数字人/LTX2.3多场景数字人_2080282380560060417.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.3多场景数字人_2080282380560060417.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（74 个）：
- `VAELoaderKJ`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `EmptyLTXVLatentVideo`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `LTXVImgToVideoInplace`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `LTXVSpatioTemporalTiledVAEDecode` ★核心
- `GetNode`
- `MelBandRoFormerModelLoader`
- `GetNode`
- `MelBandRoFormerSampler` ★核心
- `SetNode`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `SolidMask`
- `LTXVAudioVAEDecode` ★核心
- `Float`
- `MathExpression|pysssss`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVConditioning`
- `GetNode`
- `Note`
- `Int`
- `Bool`
- `Int`
- `Reroute`
- `GetNode`
- `GetNode`
- `DualCLIPLoader`
- `LTX2_NAG`
- `SetNode`
- `DiffusionModelLoaderKJ`
- `CLIPTextEncode` ★核心
- `GetNode`
- `TTResolutionSelector`
- `MathExpression|pysssss`
- `Audio Duration (mtb)`
- `SetNode`
- `SetNode`
- `RHHiddenNodes`
- `Text`
- `CFGGuider`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ManualSigmas`
- `RHHiddenNodes`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `LoadAudio`
- `AudioCrop`

## 知识

覆盖率 **57%**（42/74）

**有卡**：`VAELoaderKJ`、`EmptyLTXVLatentVideo`、`ImageResizeKJv2`、`RandomNoise`、`KSamplerSelect`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVSpatioTemporalTiledVAEDecode`、`MelBandRoFormerModelLoader`、`MelBandRoFormerSampler`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`SolidMask`、`LTXVAudioVAEDecode`、`Float`、`MathExpression|pysssss`、`LTXVConditioning`、`Int`、`Bool`、`DualCLIPLoader`、`LTX2_NAG`、`DiffusionModelLoaderKJ`、`CLIPTextEncode`、`TTResolutionSelector`、`Audio Duration (mtb)`、`RHHiddenNodes`、`Text`、`CFGGuider`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`ManualSigmas`、`LoadImage`、`LoadAudio`、`AudioCrop`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler、LTXVConcatAVLatent

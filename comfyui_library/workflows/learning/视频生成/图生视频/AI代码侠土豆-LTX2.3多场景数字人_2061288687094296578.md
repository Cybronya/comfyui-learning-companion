---
key: 视频生成/图生视频/AI代码侠土豆-LTX2.3多场景数字人_2061288687094296578.json
name: AI代码侠土豆-LTX2.3多场景数字人_2061288687094296578.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2061288687094296578.json
hash: 5843426f4aeb540c
coverage: 0.567568
learned_at: 2026-10-15 22:38:52
nodes: [VAELoaderKJ, SetNode, VAELoaderKJ, SetNode, SetNode, EmptyLTXVLatentVideo, SetNode, SetNode, ImageResizeKJv2, SetNode, GetNode, GetNode, RandomNoise, KSamplerSelect, LTXVImgToVideoInplace, SetNode, GetNode, GetNode, LTXVConcatAVLatent, SamplerCustomAdvanced, GetNode, LTXVSeparateAVLatent, GetNode, LTXVSpatioTemporalTiledVAEDecode, GetNode, MelBandRoFormerModelLoader, GetNode, MelBandRoFormerSampler, SetNode, LTXVAudioVAEEncode, SetLatentNoiseMask, SolidMask, LTXVAudioVAEDecode, Float, MathExpression|pysssss, SetNode, SetNode, GetNode, GetNode, LTXVConditioning, GetNode, Note, Int, Bool, Int, Reroute, GetNode, GetNode, DualCLIPLoader, LTX2_NAG, SetNode, DiffusionModelLoaderKJ, CLIPTextEncode, GetNode, TTResolutionSelector, MathExpression|pysssss, Audio Duration (mtb), SetNode, LoadImage, LoadAudio, SetNode, AudioCrop, RHHiddenNodes, Text, CFGGuider, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, ManualSigmas, RHHiddenNodes, LoraLoaderModelOnly, GetNode, GetNode, GetNode]
patterns: []
missing: []
---

# 视频生成/图生视频/AI代码侠土豆-LTX2.3多场景数字人_2061288687094296578.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2061288687094296578.json`

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
- `LoadImage`
- `LoadAudio`
- `SetNode`
- `AudioCrop`
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

## 知识

覆盖率 **57%**（42/74）

**有卡**：`VAELoaderKJ`、`EmptyLTXVLatentVideo`、`ImageResizeKJv2`、`RandomNoise`、`KSamplerSelect`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVSpatioTemporalTiledVAEDecode`、`MelBandRoFormerModelLoader`、`MelBandRoFormerSampler`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`SolidMask`、`LTXVAudioVAEDecode`、`Float`、`MathExpression|pysssss`、`LTXVConditioning`、`Int`、`Bool`、`DualCLIPLoader`、`LTX2_NAG`、`DiffusionModelLoaderKJ`、`CLIPTextEncode`、`TTResolutionSelector`、`Audio Duration (mtb)`、`LoadImage`、`LoadAudio`、`AudioCrop`、`RHHiddenNodes`、`Text`、`CFGGuider`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`ManualSigmas`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler、LTXVConcatAVLatent

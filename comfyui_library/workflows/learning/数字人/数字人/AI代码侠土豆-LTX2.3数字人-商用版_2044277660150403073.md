---
key: 数字人/数字人/AI代码侠土豆-LTX2.3数字人-商用版_2044277660150403073.json
name: AI代码侠土豆-LTX2.3数字人-商用版_2044277660150403073
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/AI代码侠土豆-LTX2.3数字人-商用版_2044277660150403073.json
hash: fd796af416bfca13
coverage: 0.56338
learned_at: 2026-10-26 01:53:38
nodes: [VAELoaderKJ, SetNode, VAELoaderKJ, SetNode, SetNode, EmptyLTXVLatentVideo, GetNode, SetNode, SetNode, ImageResizeKJv2, SetNode, GetNode, GetNode, RandomNoise, CFGGuider, KSamplerSelect, ManualSigmas, LTXVImgToVideoInplace, SetNode, GetNode, GetNode, LTXVConcatAVLatent, SamplerCustomAdvanced, GetNode, LTXVSeparateAVLatent, GetNode, CLIPTextEncode, LTXVSpatioTemporalTiledVAEDecode, GetNode, MelBandRoFormerModelLoader, GetNode, MelBandRoFormerSampler, GetNode, GetNode, SetNode, LTXVAudioVAEEncode, SetLatentNoiseMask, SolidMask, LTXVAudioVAEDecode, MathExpression|pysssss, Float, MathExpression|pysssss, SetNode, SetNode, GetNode, GetNode, GetNode, LTXVConditioning, GetNode, Note, VHS_VideoCombine, Int, Bool, Int, Audio Duration (mtb), Reroute, LoadAudio, SetNode, GetNode, GetNode, LoadImage, TTResolutionSelector, CLIPTextEncode, DualCLIPLoader, DiffusionModelLoaderKJ, LoraLoaderModelOnly, LTX2_NAG, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, AudioCrop]
patterns: []
missing: []
---

# 数字人/数字人/AI代码侠土豆-LTX2.3数字人-商用版_2044277660150403073.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/AI代码侠土豆-LTX2.3数字人-商用版_2044277660150403073.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（71 个）：
- `VAELoaderKJ`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVImgToVideoInplace`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `CLIPTextEncode` ★核心
- `LTXVSpatioTemporalTiledVAEDecode` ★核心
- `GetNode`
- `MelBandRoFormerModelLoader`
- `GetNode`
- `MelBandRoFormerSampler` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `SolidMask`
- `LTXVAudioVAEDecode` ★核心
- `MathExpression|pysssss`
- `Float`
- `MathExpression|pysssss`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConditioning`
- `GetNode`
- `Note`
- `VHS_VideoCombine`
- `Int`
- `Bool`
- `Int`
- `Audio Duration (mtb)`
- `Reroute`
- `LoadAudio`
- `SetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `TTResolutionSelector`
- `CLIPTextEncode` ★核心
- `DualCLIPLoader`
- `DiffusionModelLoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `LTX2_NAG`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `AudioCrop`

## 知识

覆盖率 **56%**（40/71）

**有卡**：`VAELoaderKJ`、`EmptyLTXVLatentVideo`、`ImageResizeKJv2`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`CLIPTextEncode`、`LTXVSpatioTemporalTiledVAEDecode`、`MelBandRoFormerModelLoader`、`MelBandRoFormerSampler`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`SolidMask`、`LTXVAudioVAEDecode`、`MathExpression|pysssss`、`Float`、`LTXVConditioning`、`VHS_VideoCombine`、`Int`、`Bool`、`Audio Duration (mtb)`、`LoadAudio`、`LoadImage`、`TTResolutionSelector`、`DualCLIPLoader`、`DiffusionModelLoaderKJ`、`LoraLoaderModelOnly`、`LTX2_NAG`、`AudioCrop`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler、LTXVConcatAVLatent

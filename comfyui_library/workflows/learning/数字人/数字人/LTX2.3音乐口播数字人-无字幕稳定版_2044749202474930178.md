---
key: 数字人/数字人/LTX2.3音乐口播数字人-无字幕稳定版_2044749202474930178.json
name: LTX2.3音乐口播数字人-无字幕稳定版_2044749202474930178
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.3音乐口播数字人-无字幕稳定版_2044749202474930178.json
hash: 627ed52a66f10609
coverage: 0.617284
learned_at: 2026-10-26 01:56:13
nodes: [SetNode, VAELoaderKJ, SetNode, VAELoaderKJ, SetNode, EmptyLTXVLatentVideo, GetNode, SetNode, SetNode, ImageResizeKJv2, SetNode, GetNode, SetNode, GetNode, GetNode, LTXVConcatAVLatent, GetNode, GetNode, LTXVSpatioTemporalTiledVAEDecode, GetNode, GetNode, MelBandRoFormerSampler, GetNode, GetNode, SetNode, LTXVAudioVAEEncode, SetLatentNoiseMask, SolidMask, LTXVAudioVAEDecode, RandomNoise, GetNode, CFGGuider, KSamplerSelect, ManualSigmas, LTXVSeparateAVLatent, GetNode, GetNode, SamplerCustomAdvanced, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVConcatAVLatent, LatentUpscaleModelLoader, LatentUpscaleModelLoader, Audio Duration (mtb), MathExpression|pysssss, MathExpression|pysssss, SetNode, SetNode, Float, Bool, GetNode, GetNode, MelBandRoFormerModelLoader, SetNode, GetNode, DiffusionModelLoaderKJ, DualCLIPLoader, GetNode, SetNode, GetNode, LTXVSeparateAVLatent, SamplerCustomAdvanced, CFGGuider, LoadImage, LoadAudio, AudioCrop, LTXVConditioning, Int, Int, GetNode, VHS_VideoCombine, LTX2_NAG, TTResolutionSelector, KSamplerSelect, ManualSigmas, RandomNoise, LTXVImgToVideoInplace, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly]
patterns: []
missing: []
---

# 数字人/数字人/LTX2.3音乐口播数字人-无字幕稳定版_2044749202474930178.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.3音乐口播数字人-无字幕稳定版_2044749202474930178.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（81 个）：
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `LTXVSpatioTemporalTiledVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `MelBandRoFormerSampler` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `SolidMask`
- `LTXVAudioVAEDecode` ★核心
- `RandomNoise`
- `GetNode`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `LatentUpscaleModelLoader`
- `LatentUpscaleModelLoader`
- `Audio Duration (mtb)`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `SetNode`
- `SetNode`
- `Float`
- `Bool`
- `GetNode`
- `GetNode`
- `MelBandRoFormerModelLoader`
- `SetNode`
- `GetNode`
- `DiffusionModelLoaderKJ`
- `DualCLIPLoader`
- `GetNode`
- `SetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `LoadImage`
- `LoadAudio`
- `AudioCrop`
- `LTXVConditioning`
- `Int`
- `Int`
- `GetNode`
- `VHS_VideoCombine`
- `LTX2_NAG`
- `TTResolutionSelector`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `LTXVImgToVideoInplace`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心

## 知识

覆盖率 **62%**（50/81）

**有卡**：`VAELoaderKJ`、`EmptyLTXVLatentVideo`、`ImageResizeKJv2`、`LTXVConcatAVLatent`、`LTXVSpatioTemporalTiledVAEDecode`、`MelBandRoFormerSampler`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`SolidMask`、`LTXVAudioVAEDecode`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`Audio Duration (mtb)`、`MathExpression|pysssss`、`Float`、`Bool`、`MelBandRoFormerModelLoader`、`DiffusionModelLoaderKJ`、`DualCLIPLoader`、`LoadImage`、`LoadAudio`、`AudioCrop`、`LTXVConditioning`、`Int`、`VHS_VideoCombine`、`LTX2_NAG`、`TTResolutionSelector`、`LoraLoaderModelOnly`、`CLIPTextEncode`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler、LTXVLatentUpsampler

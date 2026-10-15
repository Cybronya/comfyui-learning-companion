---
key: 视频生成/文生视频/AA--LTX-2.0文生视频MV(歌曲MP3对口型)_2015272887397130242.json
name: AA--LTX-2.0文生视频MV(歌曲MP3对口型)_2015272887397130242
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/AA--LTX-2.0文生视频MV(歌曲MP3对口型)_2015272887397130242.json
hash: 7d2eb13891538f9c
coverage: 0.712329
learned_at: 2026-10-15 22:43:58
nodes: [RandomNoise, VAEDecodeTiled, MelBandRoFormerModelLoader, SolidMask, LTXVAudioVAEEncode, SetLatentNoiseMask, MelBandRoFormerSampler, LatentUpscaleModelLoader, SetNode, SetNode, SetNode, TrimAudioDuration, VAELoaderKJ, LTXVSeparateAVLatent, ManualSigmas, KSamplerSelect, EmptyImage, ImageScaleBy, GetImageSize, EmptyLTXVLatentVideo, GetNode, GetNode, GetNode, LTXVConditioning, SetNode, CLIPTextEncode, CFGGuider, GetNode, PrimitiveFloat, CM_FloatBinaryOperation, easy showAnything, CM_FloatToInt, CM_FloatBinaryOperation, CM_FloatBinaryOperation, PathchSageAttentionKJ, DualCLIPLoaderGGUF, VAELoader, SetNode, SetNode, GetNode, VHS_VideoCombine, UnetLoaderGGUF, UNETLoader, LoraLoaderModelOnly, GetNode, LoraLoaderModelOnly, SetNode, LoadAudio, LTXVChunkFeedForward, Note, RandomNoise, CFGGuider, KSamplerSelect, SamplerCustomAdvanced, LTXVConcatAVLatent, LTXVLatentUpsampler, LTXVScheduler, LoraLoaderModelOnly, LTXVConcatAVLatent, GetNode, GetNode, GetNode, SamplerCustomAdvanced, LTXVSeparateAVLatent, GetNode, LTXVAudioVAEDecode, CLIPTextEncode, Note, easy float, easy float, INTConstant, INTConstant, INTConstant]
patterns: []
missing: []
---

# 视频生成/文生视频/AA--LTX-2.0文生视频MV(歌曲MP3对口型)_2015272887397130242.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/AA--LTX-2.0文生视频MV(歌曲MP3对口型)_2015272887397130242.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（73 个）：
- `RandomNoise`
- `VAEDecodeTiled` ★核心
- `MelBandRoFormerModelLoader`
- `SolidMask`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `MelBandRoFormerSampler` ★核心
- `LatentUpscaleModelLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `TrimAudioDuration`
- `VAELoaderKJ`
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `EmptyImage`
- `ImageScaleBy`
- `GetImageSize`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConditioning`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `GetNode`
- `PrimitiveFloat`
- `CM_FloatBinaryOperation`
- `easy showAnything`
- `CM_FloatToInt`
- `CM_FloatBinaryOperation`
- `CM_FloatBinaryOperation`
- `PathchSageAttentionKJ`
- `DualCLIPLoaderGGUF`
- `VAELoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `UnetLoaderGGUF` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `LoadAudio`
- `LTXVChunkFeedForward`
- `Note`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVScheduler`
- `LoraLoaderModelOnly` ★核心
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `easy float`
- `easy float`
- `INTConstant`
- `INTConstant`
- `INTConstant`

## 知识

覆盖率 **71%**（52/73）

**有卡**：`RandomNoise`、`VAEDecodeTiled`、`MelBandRoFormerModelLoader`、`SolidMask`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`MelBandRoFormerSampler`、`LatentUpscaleModelLoader`、`TrimAudioDuration`、`VAELoaderKJ`、`LTXVSeparateAVLatent`、`ManualSigmas`、`KSamplerSelect`、`EmptyImage`、`ImageScaleBy`、`GetImageSize`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`CLIPTextEncode`、`CFGGuider`、`CM_FloatBinaryOperation`、`CM_FloatToInt`、`PathchSageAttentionKJ`、`DualCLIPLoaderGGUF`、`VAELoader`、`VHS_VideoCombine`、`UnetLoaderGGUF`、`UNETLoader`、`LoraLoaderModelOnly`、`LoadAudio`、`LTXVChunkFeedForward`、`SamplerCustomAdvanced`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`LTXVScheduler`、`LTXVAudioVAEDecode`、`easy float`、`INTConstant`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler

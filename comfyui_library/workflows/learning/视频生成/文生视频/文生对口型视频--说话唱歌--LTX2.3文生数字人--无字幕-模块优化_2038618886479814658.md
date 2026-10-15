---
key: 视频生成/文生视频/文生对口型视频--说话唱歌--LTX2.3文生数字人--无字幕-模块优化_2038618886479814658.json
name: 文生对口型视频--说话唱歌--LTX2.3文生数字人--无字幕-模块优化_2038618886479814658
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/文生对口型视频--说话唱歌--LTX2.3文生数字人--无字幕-模块优化_2038618886479814658.json
hash: 6652ad06bc5197af
coverage: 0.963636
learned_at: 2026-10-15 22:48:41
nodes: [KSamplerSelect, BasicScheduler, LTXVAudioVAELoader, SamplerCustomAdvanced, MelBandRoFormerSampler, INTConstant, SimpleMath+, SolidMask, INTConstant, SimpleMath+, LTXAVTextEncoderLoader, RandomNoise, LTXVConditioning, LTXVAudioVAEEncode, EmptyLTXVLatentVideo, SetLatentNoiseMask, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, LTXVLatentUpsampler, LTXVConcatAVLatent, SamplerCustomAdvanced, Int, RandomNoise, LTXVSeparateAVLatent, LTXVCropGuides, LTXVSeparateAVLatent, VAEDecodeTiled, INTConstant, SoundFlow_GetLength, CM_FloatToInt, MelBandRoFormerModelLoader, easy showAnything, CheckpointLoaderSimple, CFGGuider, CFGGuider, LoraLoaderModelOnly, RH_LLMAPI_Pro_Node, ShowAnything|Mie, VHS_VideoCombine, PreviewAudio, LoraLoaderModelOnly, CR Prompt Text, CLIPTextEncode, CLIPTextEncode, AudioCrop, LoadAudio, LoraLoaderModelOnly, CR Text, LatentUpscaleModelLoader, Int, Int, SimpleMath+, CM_IntToFloat, Note]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev.safetensors"}
---

# 视频生成/文生视频/文生对口型视频--说话唱歌--LTX2.3文生数字人--无字幕-模块优化_2038618886479814658.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/文生对口型视频--说话唱歌--LTX2.3文生数字人--无字幕-模块优化_2038618886479814658.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Other

**节点**（55 个）：
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `LTXVAudioVAELoader`
- `SamplerCustomAdvanced` ★核心
- `MelBandRoFormerSampler` ★核心
- `INTConstant`
- `SimpleMath+`
- `SolidMask`
- `INTConstant`
- `SimpleMath+`
- `LTXAVTextEncoderLoader`
- `RandomNoise`
- `LTXVConditioning`
- `LTXVAudioVAEEncode` ★核心
- `EmptyLTXVLatentVideo`
- `SetLatentNoiseMask`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `Int`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `INTConstant`
- `SoundFlow_GetLength`
- `CM_FloatToInt`
- `MelBandRoFormerModelLoader`
- `easy showAnything`
- `CheckpointLoaderSimple` ★核心
- `CFGGuider`
- `CFGGuider`
- `LoraLoaderModelOnly` ★核心
- `RH_LLMAPI_Pro_Node`
- `ShowAnything|Mie`
- `VHS_VideoCombine`
- `PreviewAudio`
- `LoraLoaderModelOnly` ★核心
- `CR Prompt Text`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `AudioCrop`
- `LoadAudio`
- `LoraLoaderModelOnly` ★核心
- `CR Text`
- `LatentUpscaleModelLoader`
- `Int`
- `Int`
- `SimpleMath+`
- `CM_IntToFloat`
- `Note`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **96%**（53/55）

**有卡**：`KSamplerSelect`、`BasicScheduler`、`LTXVAudioVAELoader`、`SamplerCustomAdvanced`、`MelBandRoFormerSampler`、`INTConstant`、`SimpleMath+`、`SolidMask`、`LTXAVTextEncoderLoader`、`RandomNoise`、`LTXVConditioning`、`LTXVAudioVAEEncode`、`EmptyLTXVLatentVideo`、`SetLatentNoiseMask`、`LTXVConcatAVLatent`、`ManualSigmas`、`LTXVLatentUpsampler`、`Int`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`VAEDecodeTiled`、`SoundFlow_GetLength`、`CM_FloatToInt`、`MelBandRoFormerModelLoader`、`CheckpointLoaderSimple`、`CFGGuider`、`LoraLoaderModelOnly`、`RH_LLMAPI_Pro_Node`、`ShowAnything|Mie`、`VHS_VideoCombine`、`PreviewAudio`、`CR Prompt Text`、`CLIPTextEncode`、`AudioCrop`、`LoadAudio`、`CR Text`、`LatentUpscaleModelLoader`、`CM_IntToFloat`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler、LTXVLatentUpsampler

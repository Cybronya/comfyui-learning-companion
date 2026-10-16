---
key: 视频生成/图生视频/图+音频生视频：音乐MV-对口型-图生视频 ltx2.3双采+VBVR+Qwen3.5_2054885295354589185.json
name: 图+音频生视频：音乐MV-对口型-图生视频 ltx2.3双采+VBVR+Qwen3.5_2054885295354589185.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2054885295354589185.json
hash: f0a41702390fc276
coverage: 0.520661
learned_at: 2026-10-15 22:37:53
nodes: [SetNode, SetNode, SolidMask, LTXVAudioVAEEncode, MelBandRoFormerSampler, EmptyLTXVLatentVideo, SetLatentNoiseMask, LTXVConcatAVLatent, SetNode, easy cleanGpuUsed, GetNode, ManualSigmas, KSamplerSelect, SetNode, SetNode, GetNode, GetNode, LTXVSeparateAVLatent, SamplerCustomAdvanced, GetNode, CFGGuider, GetNode, SetNode, LTXVConcatAVLatent, LTXVImgToVideoInplace, SamplerCustomAdvanced, LTXVLatentUpsampler, LTXVSeparateAVLatent, ImageScaleBy, CFGGuider, SetNode, LTXVSpatioTemporalTiledVAEDecode, easy cleanGpuUsed, KSamplerSelect, ManualSigmas, SetNode, GetNode, SetNode, SetNode, SetNode, GetNode, SetNode, SetNode, LTXVConditioning, LatentUpscaleModelLoader, SetNode, LTXVPreprocess, GetNode, LTXVImgToVideoInplace, GetNode, SimpleMath+, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, Seed (rgthree), GetNode, RandomNoise, GetNode, GetNode, RandomNoise, GetNode, GetNode, llama_cpp_parameters, GetNode, AudioInfo, PrimitiveInt, easy showAnything, SetNode, SimpleMath+, GetNode, GetNode, Int to String, GetNode, CheckpointLoaderSimple, SetNode, PathchSageAttentionKJ, LTXVAudioVAELoader, LTXAVTextEncoderLoader, llama_cpp_instruct_adv, CM_FloatToInt, SetNode, SetNode, StringFunction|pysssss, GetNode, easy cleanGpuUsed, MelBandRoFormerModelLoader, Note, GetNode, Note, Note, CLIPTextEncode, LTX2_NAG, StringFunction|pysssss, InversionDemoLazySwitch, Float, Int, easy showAnything, easy showAnything, Text, AudioCrop, Text, SetNode, Text, Text, Note, Note, CLIPTextEncode, Note, Note, Text, llama_cpp_model_loader, LoraLoaderModelOnly, GetNode, LoadAudio, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, LoadImage]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors"}
---

# 视频生成/图生视频/图+音频生视频：音乐MV-对口型-图生视频 ltx2.3双采+VBVR+Qwen3.5_2054885295354589185.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2054885295354589185.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（121 个）：
- `SetNode`
- `SetNode`
- `SolidMask`
- `LTXVAudioVAEEncode` ★核心
- `MelBandRoFormerSampler` ★核心
- `EmptyLTXVLatentVideo`
- `SetLatentNoiseMask`
- `LTXVConcatAVLatent`
- `SetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `CFGGuider`
- `GetNode`
- `SetNode`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVSeparateAVLatent`
- `ImageScaleBy`
- `CFGGuider`
- `SetNode`
- `LTXVSpatioTemporalTiledVAEDecode` ★核心
- `easy cleanGpuUsed`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `LTXVConditioning`
- `LatentUpscaleModelLoader`
- `SetNode`
- `LTXVPreprocess`
- `GetNode`
- `LTXVImgToVideoInplace`
- `GetNode`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `Seed (rgthree)`
- `GetNode`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `llama_cpp_parameters`
- `GetNode`
- `AudioInfo`
- `PrimitiveInt`
- `easy showAnything`
- `SetNode`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `Int to String`
- `GetNode`
- `CheckpointLoaderSimple` ★核心
- `SetNode`
- `PathchSageAttentionKJ`
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `llama_cpp_instruct_adv`
- `CM_FloatToInt`
- `SetNode`
- `SetNode`
- `StringFunction|pysssss`
- `GetNode`
- `easy cleanGpuUsed`
- `MelBandRoFormerModelLoader`
- `Note`
- `GetNode`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `LTX2_NAG`
- `StringFunction|pysssss`
- `InversionDemoLazySwitch`
- `Float`
- `Int`
- `easy showAnything`
- `easy showAnything`
- `Text`
- `AudioCrop`
- `Text`
- `SetNode`
- `Text`
- `Text`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `Note`
- `Note`
- `Text`
- `llama_cpp_model_loader`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `LoadAudio`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`

## 知识

覆盖率 **52%**（63/121）

**有卡**：`SolidMask`、`LTXVAudioVAEEncode`、`MelBandRoFormerSampler`、`EmptyLTXVLatentVideo`、`SetLatentNoiseMask`、`LTXVConcatAVLatent`、`easy cleanGpuUsed`、`ManualSigmas`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`CFGGuider`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`ImageScaleBy`、`LTXVSpatioTemporalTiledVAEDecode`、`LTXVConditioning`、`LatentUpscaleModelLoader`、`LTXVPreprocess`、`SimpleMath+`、`Seed (rgthree)`、`RandomNoise`、`llama_cpp_parameters`、`AudioInfo`、`Int to String`、`CheckpointLoaderSimple`、`PathchSageAttentionKJ`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`llama_cpp_instruct_adv`、`CM_FloatToInt`、`StringFunction|pysssss`、`MelBandRoFormerModelLoader`、`CLIPTextEncode`、`LTX2_NAG`、`InversionDemoLazySwitch`、`Float`、`Int`、`Text`、`AudioCrop`、`llama_cpp_model_loader`、`LoraLoaderModelOnly`、`LoadAudio`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler

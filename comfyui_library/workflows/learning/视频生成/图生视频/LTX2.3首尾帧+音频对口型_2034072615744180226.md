---
key: 视频生成/图生视频/LTX2.3首尾帧+音频对口型_2034072615744180226.json
name: LTX2.3首尾帧+音频对口型_2034072615744180226.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3首尾帧+音频对口型_2034072615744180226.json
hash: 5b2c832b8a42fd01
coverage: 0.581633
learned_at: 2026-10-15 22:35:42
nodes: [MelBandRoFormerModelLoader, LatentUpscaleModelLoader, SetNode, CR Text, GetNode, GetNode, GetNode, GetNode, GetNode, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, LTXVConditioning, CLIPTextEncode, SetNode, SetNode, GetNode, GetNode, RandomNoise, GetNode, GetNode, CFGGuider, easy cleanGpuUsed, SamplerCustomAdvanced, KSamplerSelect, SetNode, SetNode, LTXVSeparateAVLatent, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, VAEDecodeTiled, GetNode, GetNode, GetNode, GetNode, Int, GetNode, CR Text, CR String To Combo, GetNode, GetNode, GetNode, SolidMask, Int, Display Any (rgthree), InversionDemoLazySwitch, Int, LTXVAudioVAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVConcatAVLatent, LTXVCropGuides, easy cleanGpuUsed, SamplerCustomAdvanced, easy cleanGpuUsed, GetNode, LTXVPreprocess, GetNode, SetNode, GetNode, LTXVLatentUpsampler, SetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, GetNode, SetNode, LTXVPreprocess, SetNode, SetNode, ResizeImagesByLongerEdge, GetNode, GetNode, GetNode, GetNode, CFGGuider, LayerUtility: ImageScaleByAspectRatio V2, SetNode, ImageResizeKJv2, ResizeImagesByLongerEdge, SetNode, SetNode, SetNode, SetNode, CR Text, Display Any (rgthree), GetNode, EmptyLTXVLatentVideo, GetNode, GetNode, GetNode, GetImageSize, ImageScaleBy, SetNode, SetNode, SetNode, GetNode, ImageResizeKJv2, easy imageConcat, Fast Groups Muter (rgthree), WhisperSTT, GetNode, SetNode, ASRMW, MelBandRoFormerSampler, LTXVAudioVAEEncode, SetLatentNoiseMask, CR Text Concatenate, GetNode, GetNode, GetNode, AudioSeparation, GetNode, GetNode, PreviewAudio, LTXVConcatAVLatent, RandomNoise, VHS_VideoCombine, LTXVAudioVAEDecode, easy compare, EmptyImage, Display Any (rgthree), JWInteger, JWInteger, AudioToFPS, VAEDecodeTiled, VHS_VideoCombine, GetNode, SomethingToString, easy cleanGpuUsed, ProcessString, ShowText|pysssss, Any To String (mtb), SetNode, ImpactSwitch, LoadImage, LoadImage, DualCLIPLoader, SetNode, SetNode, SetNode, SetNode, LoadImage, LoadImage, GetNode, Any To String (mtb), SetNode, VRAMReserver, LoraLoaderModelOnly, Switch any [Crystools], LoraLoaderModelOnly, SetNode, easy boolean, ttN concat, LTXVScheduler, KSamplerSelect, GetNode, LTXVFirstLastFrameControl_TTP, ManualSigmas, LTXVSeparateAVLatent, CR Text, SetNode, LoadAudio, AudioCrop, SetNode, UnetLoaderGGUF, CR Text, LoadAudio, CR Text, ShowText|pysssss, ManualSigmas, VAELoaderKJ, VAELoaderKJ, GetNode, ShowText|pysssss, CR Text Concatenate, CR Text, Qwen3_VQA, CR Text, LTX2_NAG, CLIPTextEncode, LoraLoaderModelOnly, SetNode, CR Text, ImpactSwitch, LoraLoaderModelOnly, LTXVFirstLastFrameControl_TTP, CheckpointLoaderSimple, UNETLoader]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-distilled-fp8.safetensors"}
---

# 视频生成/图生视频/LTX2.3首尾帧+音频对口型_2034072615744180226.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2034072615744180226.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（196 个）：
- `MelBandRoFormerModelLoader`
- `LatentUpscaleModelLoader`
- `SetNode`
- `CR Text`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `easy cleanGpuUsed`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `SetNode`
- `SetNode`
- `LTXVSeparateAVLatent`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Int`
- `GetNode`
- `CR Text`
- `CR String To Combo`
- `GetNode`
- `GetNode`
- `GetNode`
- `SolidMask`
- `Int`
- `Display Any (rgthree)`
- `InversionDemoLazySwitch`
- `Int`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `LTXVCropGuides`
- `easy cleanGpuUsed`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `GetNode`
- `LTXVPreprocess`
- `GetNode`
- `SetNode`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `SetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `GetNode`
- `SetNode`
- `LTXVPreprocess`
- `SetNode`
- `SetNode`
- `ResizeImagesByLongerEdge`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `ImageResizeKJv2`
- `ResizeImagesByLongerEdge`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `CR Text`
- `Display Any (rgthree)`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageSize`
- `ImageScaleBy`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `ImageResizeKJv2`
- `easy imageConcat`
- `Fast Groups Muter (rgthree)`
- `WhisperSTT`
- `GetNode`
- `SetNode`
- `ASRMW`
- `MelBandRoFormerSampler` ★核心
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `CR Text Concatenate`
- `GetNode`
- `GetNode`
- `GetNode`
- `AudioSeparation`
- `GetNode`
- `GetNode`
- `PreviewAudio`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `VHS_VideoCombine`
- `LTXVAudioVAEDecode` ★核心
- `easy compare`
- `EmptyImage`
- `Display Any (rgthree)`
- `JWInteger`
- `JWInteger`
- `AudioToFPS`
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `GetNode`
- `SomethingToString`
- `easy cleanGpuUsed`
- `ProcessString`
- `ShowText|pysssss`
- `Any To String (mtb)`
- `SetNode`
- `ImpactSwitch`
- `LoadImage`
- `LoadImage`
- `DualCLIPLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `GetNode`
- `Any To String (mtb)`
- `SetNode`
- `VRAMReserver`
- `LoraLoaderModelOnly` ★核心
- `Switch any [Crystools]`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `easy boolean`
- `ttN concat`
- `LTXVScheduler`
- `KSamplerSelect` ★核心
- `GetNode`
- `LTXVFirstLastFrameControl_TTP`
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `CR Text`
- `SetNode`
- `LoadAudio`
- `AudioCrop`
- `SetNode`
- `UnetLoaderGGUF` ★核心
- `CR Text`
- `LoadAudio`
- `CR Text`
- `ShowText|pysssss`
- `ManualSigmas`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `GetNode`
- `ShowText|pysssss`
- `CR Text Concatenate`
- `CR Text`
- `Qwen3_VQA`
- `CR Text`
- `LTX2_NAG`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `CR Text`
- `ImpactSwitch`
- `LoraLoaderModelOnly` ★核心
- `LTXVFirstLastFrameControl_TTP`
- `CheckpointLoaderSimple` ★核心
- `UNETLoader` ★核心

## 关键参数

- `checkpoint` = `ltx-2.3-22b-distilled-fp8.safetensors`

## 知识

覆盖率 **58%**（114/196）

**有卡**：`MelBandRoFormerModelLoader`、`LatentUpscaleModelLoader`、`CR Text`、`easy cleanGpuUsed`、`LTXVConditioning`、`CLIPTextEncode`、`RandomNoise`、`CFGGuider`、`SamplerCustomAdvanced`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`Int`、`CR String To Combo`、`SolidMask`、`Display Any (rgthree)`、`InversionDemoLazySwitch`、`LTXVAudioVAEDecode`、`LTXVConcatAVLatent`、`LTXVCropGuides`、`LTXVPreprocess`、`LTXVLatentUpsampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`ResizeImagesByLongerEdge`、`ImageResizeKJv2`、`EmptyLTXVLatentVideo`、`GetImageSize`、`ImageScaleBy`、`easy imageConcat`、`WhisperSTT`、`ASRMW`、`MelBandRoFormerSampler`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`CR Text Concatenate`、`AudioSeparation`、`PreviewAudio`、`VHS_VideoCombine`、`easy compare`、`EmptyImage`、`JWInteger`、`AudioToFPS`、`SomethingToString`、`ProcessString`、`Any To String (mtb)`、`LoadImage`、`DualCLIPLoader`、`VRAMReserver`、`LoraLoaderModelOnly`、`Switch any [Crystools]`、`easy boolean`、`ttN concat`、`LTXVScheduler`、`LTXVFirstLastFrameControl_TTP`、`ManualSigmas`、`LoadAudio`、`AudioCrop`、`UnetLoaderGGUF`、`VAELoaderKJ`、`Qwen3_VQA`、`LTX2_NAG`、`CheckpointLoaderSimple`、`UNETLoader`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect

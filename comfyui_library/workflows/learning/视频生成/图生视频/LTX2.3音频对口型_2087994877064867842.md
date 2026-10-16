---
key: 视频生成/图生视频/LTX2.3音频对口型_2087994877064867842.json
name: LTX2.3音频对口型_2087994877064867842
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3音频对口型_2087994877064867842.json
hash: 0c5a867cbd5d10b3
coverage: 0.58125
learned_at: 2026-10-16 21:27:35
nodes: [MelBandRoFormerModelLoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ASRMW, LayerUtility: ImageScaleByAspectRatio V2, GetNode, TextInput_, GetNode, LayerUtility: ImageScaleByAspectRatio V2, Display Any (rgthree), CR Text, TextInput_, CR Text, SetNode, PrimitiveBoolean, JWInteger, SetNode, SetNode, SetNode, DualCLIPLoader, VAELoaderKJ, VAELoaderKJ, LatentUpscaleModelLoader, UNETLoader, LoraLoaderModelOnly, VRAMReserver, GetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Switch any [Crystools], SetNode, SetNode, MelBandRoFormerSampler, LTXVAudioVAEEncode, GetNode, GetNode, SetNode, SetLatentNoiseMask, SolidMask, GetNode, GetNode, easy compare, InversionDemoLazySwitch, EmptyImage, GetImageSize, ImageScaleBy, EmptyLTXVLatentVideo, GetNode, GetNode, LTXVImgToVideoInplace, GetNode, LTXVConcatAVLatent, SetNode, GetNode, easy cleanGpuUsed, easy cleanGpuUsed, LTXVConditioning, SetNode, SetNode, GetNode, easy cleanGpuUsed, CLIPTextEncode, CLIPTextEncode, ProcessString, SomethingToString, SetNode, CR Text Concatenate, Display Any (rgthree), CR Text, Qwen3_VQA, GetNode, JjkText, ImpactSwitch, CR Text, CR Text, ImpactSwitch, JoinStrings, ShowText|pysssss, easy cleanGpuUsed, Any To String (mtb), GetNode, CR Text, LTX2_NAG, KSamplerSelect, CFGGuider, LTXVSeparateAVLatent, SetNode, SetNode, SamplerCustomAdvanced, SetNode, SetNode, GetNode, GetNode, LTXVLatentUpsampler, GetNode, LTXVCropGuides, GetNode, LTXVImgToVideoInplace, GetNode, easy cleanGpuUsed, LTXVConcatAVLatent, GetNode, RandomNoise, CFGGuider, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, easy cleanGpuUsed, LTXVSeparateAVLatent, GetNode, GetNode, GetNode, VAEDecodeTiled, VHS_VideoCombine, SetNode, SetNode, GetNode, SetNode, SetNode, ResizeImagesByLongerEdge, SetNode, SetNode, SetNode, SetNode, SetNode, Int, DF_Get_image_size, LTXVPreprocess, CR Text, CR Text, CR Text Concatenate, SetNode, GetNode, RH_LLMAPI_NODE, easy cleanGpuUsed, Display Any (rgthree), Display Any (rgthree), LTXVScheduler, GetNode, GetNode, GetNode, GetNode, RandomNoise, CR Text, LoadAudio, LoadImage, AudioCrop, GetNode, GetNode, SetNode, Display Any (rgthree), Display Any (rgthree), AudioToFPS, JWInteger, Display Any (rgthree)]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX2.3音频对口型_2087994877064867842.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.3音频对口型_2087994877064867842.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（160 个）：
- `MelBandRoFormerModelLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ASRMW`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `TextInput_`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Display Any (rgthree)`
- `CR Text`
- `TextInput_`
- `CR Text`
- `SetNode`
- `PrimitiveBoolean`
- `JWInteger`
- `SetNode`
- `SetNode`
- `SetNode`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LatentUpscaleModelLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VRAMReserver`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Switch any [Crystools]`
- `SetNode`
- `SetNode`
- `MelBandRoFormerSampler` ★核心
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `SetLatentNoiseMask`
- `SolidMask`
- `GetNode`
- `GetNode`
- `easy compare`
- `InversionDemoLazySwitch`
- `EmptyImage`
- `GetImageSize`
- `ImageScaleBy`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoInplace`
- `GetNode`
- `LTXVConcatAVLatent`
- `SetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LTXVConditioning`
- `SetNode`
- `SetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ProcessString`
- `SomethingToString`
- `SetNode`
- `CR Text Concatenate`
- `Display Any (rgthree)`
- `CR Text`
- `Qwen3_VQA`
- `GetNode`
- `JjkText`
- `ImpactSwitch`
- `CR Text`
- `CR Text`
- `ImpactSwitch`
- `JoinStrings`
- `ShowText|pysssss`
- `easy cleanGpuUsed`
- `Any To String (mtb)`
- `GetNode`
- `CR Text`
- `LTX2_NAG`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `LTXVSeparateAVLatent`
- `SetNode`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `LTXVCropGuides`
- `GetNode`
- `LTXVImgToVideoInplace`
- `GetNode`
- `easy cleanGpuUsed`
- `LTXVConcatAVLatent`
- `GetNode`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `ResizeImagesByLongerEdge`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Int`
- `DF_Get_image_size`
- `LTXVPreprocess`
- `CR Text`
- `CR Text`
- `CR Text Concatenate`
- `SetNode`
- `GetNode`
- `RH_LLMAPI_NODE`
- `easy cleanGpuUsed`
- `Display Any (rgthree)`
- `Display Any (rgthree)`
- `LTXVScheduler`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `CR Text`
- `LoadAudio`
- `LoadImage`
- `AudioCrop`
- `GetNode`
- `GetNode`
- `SetNode`
- `Display Any (rgthree)`
- `Display Any (rgthree)`
- `AudioToFPS`
- `JWInteger`
- `Display Any (rgthree)`

## 知识

覆盖率 **58%**（93/160）

**有卡**：`MelBandRoFormerModelLoader`、`ASRMW`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextInput_`、`Display Any (rgthree)`、`CR Text`、`PrimitiveBoolean`、`JWInteger`、`DualCLIPLoader`、`VAELoaderKJ`、`LatentUpscaleModelLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`VRAMReserver`、`Switch any [Crystools]`、`MelBandRoFormerSampler`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`SolidMask`、`easy compare`、`InversionDemoLazySwitch`、`EmptyImage`、`GetImageSize`、`ImageScaleBy`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`easy cleanGpuUsed`、`LTXVConditioning`、`CLIPTextEncode`、`ProcessString`、`SomethingToString`、`CR Text Concatenate`、`Qwen3_VQA`、`JoinStrings`、`Any To String (mtb)`、`LTX2_NAG`、`KSamplerSelect`、`CFGGuider`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`RandomNoise`、`ManualSigmas`、`VAEDecodeTiled`、`VHS_VideoCombine`、`ResizeImagesByLongerEdge`、`Int`、`DF_Get_image_size`、`LTXVPreprocess`、`RH_LLMAPI_NODE`、`LTXVScheduler`、`LoadAudio`、`LoadImage`、`AudioCrop`、`AudioToFPS`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

---
key: 视频生成/图生视频/LTX2.3音频对口型【优化版】_2034928738709807106.json
name: LTX2.3音频对口型【优化版】_2034928738709807106.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2034928738709807106.json
hash: 20fb46a81906f3ca
coverage: 0.604167
learned_at: 2026-10-15 22:35:46
nodes: [MelBandRoFormerModelLoader, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, SetNode, SetNode, GetNode, CFGGuider, easy cleanGpuUsed, SetNode, SetNode, LTXVSeparateAVLatent, GetNode, GetNode, easy cleanGpuUsed, LTXVSeparateAVLatent, SetNode, SetNode, GetNode, SetNode, LTXVPreprocess, GetNode, SetNode, VAEDecodeTiled, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, MelBandRoFormerSampler, easy compare, Display Any (rgthree), Display Any (rgthree), JWInteger, EmptyImage, ImageScaleBy, GetNode, GetNode, GetNode, GetNode, ASRMW, RH_LLMAPI_NODE, CR Text Concatenate, LayerUtility: ImageScaleByAspectRatio V2, Any To String (mtb), SetNode, LTXVAudioVAEDecode, GetNode, GetNode, LTXVConcatAVLatent, LTXVAudioVAEDecode, ttN concat, easy cleanGpuUsed, SetNode, CLIPTextEncode, SetNode, SetNode, SetNode, SetNode, GetNode, LTXVAudioVAEEncode, SolidMask, SetLatentNoiseMask, SetNode, ProcessString, CR Text Concatenate, GetNode, Display Any (rgthree), easy convertAnything, CR Value, TextInput_, CR Text, easy cleanGpuUsed, CreateVideo, GetNode, GetNode, GetNode, LatentUpscaleModelLoader, GetNode, PreviewAudio, LTXVAudioVideoMask, GetImageSize, SetNode, LTXVAudioVAELoader, LTXAVTextEncoderLoader, EmptyLTXVLatentVideo, CR Text, LoraLoaderModelOnly, SetNode, SetNode, GetNode, LoadAudio, Display Any (rgthree), GetNode, SetNode, SetNode, CR Text, RandomNoise, UnetLoaderGGUF, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, AudioToFPS, LTXVConditioning, Int, GetNode, LTXVImgToVideoInplace, CFGGuider, RandomNoise, GetNode, LTXVCropGuides, GetNode, AudioCrop, CLIPTextEncode, LTX2_NAG, VHS_VideoCombine, InversionDemoLazySwitch, GetNode, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, CheckpointLoaderSimple, VAELoaderKJ, VAELoaderKJ, UNETLoader, DualCLIPLoader, SamplerCustomAdvanced, GetNode, LTXVImgToVideoInplace, SaveVideo, LoadImage, LTXVConcatAVLatent, ManualSigmas, KSamplerSelect, LTXVLatentUpsampler, SamplerCustomAdvanced, Display Any (rgthree), Display Any (rgthree), SetNode, CR Text, TextInput_, GetNode, LTXVScheduler, JWInteger, SomethingToString, Qwen3_VQA, GetNode, JoinStrings, JjkText, CR Text, CR Text, CR Text, VHS_VideoCombine, Any To String (mtb), GetNode, ImpactSwitch, CR Text, SetNode, CR Text Concatenate, CR Text, ImpactSwitch, VRAMReserver, easy boolean, CR Text, LoraLoaderModelOnly, CR Text, CR Text, LoraLoaderModelOnly, CR Text, PrimitiveBoolean, ShowText|pysssss, Switch any [Crystools], ResizeImagesByLongerEdge, ManualSigmas, LoraLoaderModelOnly, LoraLoaderModelOnly, VAEDecodeTiled, RTXVideoSuperResolution]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-distilled-fp8.safetensors"}
---

# 视频生成/图生视频/LTX2.3音频对口型【优化版】_2034928738709807106.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2034928738709807106.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（192 个）：
- `MelBandRoFormerModelLoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `SetNode`
- `SetNode`
- `GetNode`
- `CFGGuider`
- `easy cleanGpuUsed`
- `SetNode`
- `SetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `LTXVSeparateAVLatent`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `LTXVPreprocess`
- `GetNode`
- `SetNode`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `MelBandRoFormerSampler` ★核心
- `easy compare`
- `Display Any (rgthree)`
- `Display Any (rgthree)`
- `JWInteger`
- `EmptyImage`
- `ImageScaleBy`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ASRMW`
- `RH_LLMAPI_NODE`
- `CR Text Concatenate`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Any To String (mtb)`
- `SetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `ttN concat`
- `easy cleanGpuUsed`
- `SetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `SetLatentNoiseMask`
- `SetNode`
- `ProcessString`
- `CR Text Concatenate`
- `GetNode`
- `Display Any (rgthree)`
- `easy convertAnything`
- `CR Value`
- `TextInput_`
- `CR Text`
- `easy cleanGpuUsed`
- `CreateVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `LatentUpscaleModelLoader`
- `GetNode`
- `PreviewAudio`
- `LTXVAudioVideoMask`
- `GetImageSize`
- `SetNode`
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `EmptyLTXVLatentVideo`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `LoadAudio`
- `Display Any (rgthree)`
- `GetNode`
- `SetNode`
- `SetNode`
- `CR Text`
- `RandomNoise`
- `UnetLoaderGGUF` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `AudioToFPS`
- `LTXVConditioning`
- `Int`
- `GetNode`
- `LTXVImgToVideoInplace`
- `CFGGuider`
- `RandomNoise`
- `GetNode`
- `LTXVCropGuides`
- `GetNode`
- `AudioCrop`
- `CLIPTextEncode` ★核心
- `LTX2_NAG`
- `VHS_VideoCombine`
- `InversionDemoLazySwitch`
- `GetNode`
- `KSamplerSelect` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CheckpointLoaderSimple` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `LTXVImgToVideoInplace`
- `SaveVideo`
- `LoadImage`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `LTXVLatentUpsampler` ★核心
- `SamplerCustomAdvanced` ★核心
- `Display Any (rgthree)`
- `Display Any (rgthree)`
- `SetNode`
- `CR Text`
- `TextInput_`
- `GetNode`
- `LTXVScheduler`
- `JWInteger`
- `SomethingToString`
- `Qwen3_VQA`
- `GetNode`
- `JoinStrings`
- `JjkText`
- `CR Text`
- `CR Text`
- `CR Text`
- `VHS_VideoCombine`
- `Any To String (mtb)`
- `GetNode`
- `ImpactSwitch`
- `CR Text`
- `SetNode`
- `CR Text Concatenate`
- `CR Text`
- `ImpactSwitch`
- `VRAMReserver`
- `easy boolean`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `CR Text`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `CR Text`
- `PrimitiveBoolean`
- `ShowText|pysssss`
- `Switch any [Crystools]`
- `ResizeImagesByLongerEdge`
- `ManualSigmas`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecodeTiled` ★核心
- `RTXVideoSuperResolution`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-distilled-fp8.safetensors`

## 知识

覆盖率 **60%**（116/192）

**有卡**：`MelBandRoFormerModelLoader`、`easy cleanGpuUsed`、`CFGGuider`、`LTXVSeparateAVLatent`、`LTXVPreprocess`、`VAEDecodeTiled`、`MelBandRoFormerSampler`、`easy compare`、`Display Any (rgthree)`、`JWInteger`、`EmptyImage`、`ImageScaleBy`、`ASRMW`、`RH_LLMAPI_NODE`、`CR Text Concatenate`、`LayerUtility: ImageScaleByAspectRatio V2`、`Any To String (mtb)`、`LTXVAudioVAEDecode`、`LTXVConcatAVLatent`、`ttN concat`、`CLIPTextEncode`、`LTXVAudioVAEEncode`、`SolidMask`、`SetLatentNoiseMask`、`ProcessString`、`easy convertAnything`、`CR Value`、`TextInput_`、`CR Text`、`CreateVideo`、`LatentUpscaleModelLoader`、`PreviewAudio`、`LTXVAudioVideoMask`、`GetImageSize`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`EmptyLTXVLatentVideo`、`LoraLoaderModelOnly`、`LoadAudio`、`RandomNoise`、`UnetLoaderGGUF`、`AudioToFPS`、`LTXVConditioning`、`Int`、`LTXVImgToVideoInplace`、`LTXVCropGuides`、`AudioCrop`、`LTX2_NAG`、`VHS_VideoCombine`、`InversionDemoLazySwitch`、`KSamplerSelect`、`CheckpointLoaderSimple`、`VAELoaderKJ`、`UNETLoader`、`DualCLIPLoader`、`SamplerCustomAdvanced`、`SaveVideo`、`LoadImage`、`ManualSigmas`、`LTXVLatentUpsampler`、`LTXVScheduler`、`SomethingToString`、`Qwen3_VQA`、`JoinStrings`、`VRAMReserver`、`easy boolean`、`PrimitiveBoolean`、`Switch any [Crystools]`、`ResizeImagesByLongerEdge`、`RTXVideoSuperResolution`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect

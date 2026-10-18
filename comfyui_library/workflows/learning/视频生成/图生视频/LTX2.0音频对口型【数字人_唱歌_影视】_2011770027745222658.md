---
key: 视频生成/图生视频/LTX2.0音频对口型【数字人_唱歌_影视】_2011770027745222658.json
name: LTX2.0音频对口型【数字人_唱歌_影视】_2011770027745222658.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.0音频对口型【数字人_唱歌_影视】_2011770027745222658.json
hash: 3310513824f4c7c3
coverage: 0.614583
learned_at: 2026-10-15 22:34:24
nodes: [MelBandRoFormerModelLoader, SetNode, CR Text, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, LTXVConditioning, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, CFGGuider, easy cleanGpuUsed, SetNode, SetNode, LTXVSeparateAVLatent, GetNode, LTXVLatentUpsampler, LTXVCropGuides, GetNode, GetNode, SamplerCustomAdvanced, easy cleanGpuUsed, LTXVSeparateAVLatent, SetNode, SetNode, GetNode, SetNode, LTXVPreprocess, ResizeImagesByLongerEdge, LayerUtility: ImageScaleByAspectRatio V2, GetNode, SetNode, CR Text, CR Text, CR Text, CR Text, CR Text, VAEDecodeTiled, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, Int, SetNode, GetNode, SetNode, SetNode, CR Text, GetNode, CR String To Combo, LoraLoaderModelOnly, easy boolean, GetNode, GetNode, GetNode, MelBandRoFormerSampler, GetNode, GetNode, GetNode, GetImageSize, easy compare, Int, Display Any (rgthree), Display Any (rgthree), InversionDemoLazySwitch, JWInteger, EmptyImage, ImageScaleBy, EmptyLTXVLatentVideo, GetNode, GetNode, GetNode, Int, SetNode, SetNode, SetNode, CR Text, GetNode, GetNode, ASRMW, Display Any (rgthree), SetNode, CR Text, RH_LLMAPI_NODE, Display Any (rgthree), GetNode, CR Text Concatenate, LayerUtility: ImageScaleByAspectRatio V2, Any To String (mtb), Display Any (rgthree), SetNode, LTXVAudioVAEDecode, GetNode, GetNode, LTXVConcatAVLatent, GetNode, LTXVAudioVAEDecode, ttN concat, SomethingToString, easy cleanGpuUsed, Any To String (mtb), SetNode, CFGGuider, SamplerCustomAdvanced, CLIPTextEncode, SetNode, SetNode, SetNode, LatentUpscaleModelLoader, CLIPTextEncode, SetNode, GetNode, RandomNoise, CR Text, AudioToFPS, PreviewAudio, LTXVAudioVAEEncode, SolidMask, SetLatentNoiseMask, LTXVAudioVideoMask, CR Text, VHS_VideoCombine, LoraLoaderModelOnly, Switch any [Crystools], VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, SetNode, LTXVImgToVideoInplace, GetNode, Qwen3_VQA, ProcessString, CR Text Concatenate, CR Text Concatenate, GetNode, Display Any (rgthree), easy convertAnything, CR Value, LTXVAudioVAELoader, LTXAVTextEncoderLoader, CheckpointLoaderSimple, UnetLoaderGGUF, TextInput_, TextInput_, CR Text, RandomNoise, CR Text, LoraLoaderModelOnly, JWInteger, VRAMReserver, SetNode, SetNode, LTXVConcatAVLatent, KSamplerSelect, GetNode, VAEDecodeTiled, ImpactSwitch, CR Text, VHS_VideoCombine, KSamplerSelect, easy cleanGpuUsed, CreateVideo, SaveVideo, AudioCrop, LoadAudio, GetNode, CheckpointLoaderSimple, LTXVScheduler, LTXVImgToVideoInplace, ManualSigmas, CR Text, ShowText|pysssss, CR Text, JoinStrings, ImpactSwitch, SetNode, LoadImage, ManualSigmas, UNETLoader]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2-19b-distilled-fp8.safetensors"}
---

# 视频生成/图生视频/LTX2.0音频对口型【数字人_唱歌_影视】_2011770027745222658.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2011770027745222658.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（192 个）：
- `MelBandRoFormerModelLoader`
- `SetNode`
- `CR Text`
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
- `LTXVConditioning`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `easy cleanGpuUsed`
- `SetNode`
- `SetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `LTXVCropGuides`
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `LTXVSeparateAVLatent`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `LTXVPreprocess`
- `ResizeImagesByLongerEdge`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `SetNode`
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
- `SetNode`
- `GetNode`
- `Int`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `CR Text`
- `GetNode`
- `CR String To Combo`
- `LoraLoaderModelOnly` ★核心
- `easy boolean`
- `GetNode`
- `GetNode`
- `GetNode`
- `MelBandRoFormerSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageSize`
- `easy compare`
- `Int`
- `Display Any (rgthree)`
- `Display Any (rgthree)`
- `InversionDemoLazySwitch`
- `JWInteger`
- `EmptyImage`
- `ImageScaleBy`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `Int`
- `SetNode`
- `SetNode`
- `SetNode`
- `CR Text`
- `GetNode`
- `GetNode`
- `ASRMW`
- `Display Any (rgthree)`
- `SetNode`
- `CR Text`
- `RH_LLMAPI_NODE`
- `Display Any (rgthree)`
- `GetNode`
- `CR Text Concatenate`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Any To String (mtb)`
- `Display Any (rgthree)`
- `SetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `ttN concat`
- `SomethingToString`
- `easy cleanGpuUsed`
- `Any To String (mtb)`
- `SetNode`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `LatentUpscaleModelLoader`
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `RandomNoise`
- `CR Text`
- `AudioToFPS`
- `PreviewAudio`
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `SetLatentNoiseMask`
- `LTXVAudioVideoMask`
- `CR Text`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `Switch any [Crystools]`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `SetNode`
- `LTXVImgToVideoInplace`
- `GetNode`
- `Qwen3_VQA`
- `ProcessString`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `GetNode`
- `Display Any (rgthree)`
- `easy convertAnything`
- `CR Value`
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `CheckpointLoaderSimple` ★核心
- `UnetLoaderGGUF` ★核心
- `TextInput_`
- `TextInput_`
- `CR Text`
- `RandomNoise`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `JWInteger`
- `VRAMReserver`
- `SetNode`
- `SetNode`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `GetNode`
- `VAEDecodeTiled` ★核心
- `ImpactSwitch`
- `CR Text`
- `VHS_VideoCombine`
- `KSamplerSelect` ★核心
- `easy cleanGpuUsed`
- `CreateVideo`
- `SaveVideo`
- `AudioCrop`
- `LoadAudio`
- `GetNode`
- `CheckpointLoaderSimple` ★核心
- `LTXVScheduler`
- `LTXVImgToVideoInplace`
- `ManualSigmas`
- `CR Text`
- `ShowText|pysssss`
- `CR Text`
- `JoinStrings`
- `ImpactSwitch`
- `SetNode`
- `LoadImage`
- `ManualSigmas`
- `UNETLoader` ★核心

## 关键参数

- `checkpoint` = `ltx-2-19b-distilled-fp8.safetensors`

## 知识

覆盖率 **61%**（118/192）

**有卡**：`MelBandRoFormerModelLoader`、`CR Text`、`easy cleanGpuUsed`、`LTXVConditioning`、`CFGGuider`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`SamplerCustomAdvanced`、`LTXVPreprocess`、`ResizeImagesByLongerEdge`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecodeTiled`、`Int`、`CR String To Combo`、`LoraLoaderModelOnly`、`easy boolean`、`MelBandRoFormerSampler`、`GetImageSize`、`easy compare`、`Display Any (rgthree)`、`InversionDemoLazySwitch`、`JWInteger`、`EmptyImage`、`ImageScaleBy`、`EmptyLTXVLatentVideo`、`ASRMW`、`RH_LLMAPI_NODE`、`CR Text Concatenate`、`Any To String (mtb)`、`LTXVAudioVAEDecode`、`LTXVConcatAVLatent`、`ttN concat`、`SomethingToString`、`CLIPTextEncode`、`LatentUpscaleModelLoader`、`RandomNoise`、`AudioToFPS`、`PreviewAudio`、`LTXVAudioVAEEncode`、`SolidMask`、`SetLatentNoiseMask`、`LTXVAudioVideoMask`、`VHS_VideoCombine`、`Switch any [Crystools]`、`VAELoaderKJ`、`DualCLIPLoader`、`LTXVImgToVideoInplace`、`Qwen3_VQA`、`ProcessString`、`easy convertAnything`、`CR Value`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`CheckpointLoaderSimple`、`UnetLoaderGGUF`、`TextInput_`、`VRAMReserver`、`KSamplerSelect`、`CreateVideo`、`SaveVideo`、`AudioCrop`、`LoadAudio`、`LTXVScheduler`、`ManualSigmas`、`JoinStrings`、`LoadImage`、`UNETLoader`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect

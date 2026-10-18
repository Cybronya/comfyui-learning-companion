---
key: 视频生成/图生视频/LTX2.3+QwenTTS音色克隆对口型【角色说话】_2033108960152133633.json
name: LTX2.3+QwenTTS音色克隆对口型【角色说话】_2033108960152133633.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3+QwenTTS音色克隆对口型【角色说话】_2033108960152133633.json
hash: c0eb529ea2c7e88e
coverage: 0.593909
learned_at: 2026-10-15 22:35:38
nodes: [MelBandRoFormerModelLoader, CR Text, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, CLIPTextEncode, SetNode, GetNode, RandomNoise, easy cleanGpuUsed, KSamplerSelect, SetNode, SetNode, LTXVSeparateAVLatent, GetNode, LTXVLatentUpsampler, LTXVCropGuides, GetNode, GetNode, easy cleanGpuUsed, CFGGuider, SetNode, SetNode, GetNode, SetNode, LTXVPreprocess, ResizeImagesByLongerEdge, LayerUtility: ImageScaleByAspectRatio V2, SetNode, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, VAEDecodeTiled, GetNode, SetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, GetNode, Int, GetNode, SaveVideo, CreateVideo, SetNode, SetNode, CR Text, CR String To Combo, GetNode, GetNode, GetNode, GetImageSize, easy compare, Int, Display Any (rgthree), InversionDemoLazySwitch, EmptyImage, ImageScaleBy, EmptyLTXVLatentVideo, GetNode, GetNode, Int, SetNode, SetNode, GetNode, GetNode, ASRMW, Display Any (rgthree), SetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, GetNode, GetNode, GetNode, CR Prompt Text, SetNode, LoadAudio, SetNode, CR Text, SetNode, GetNode, GetNode, WhisperSTT, LoadImage, RandomNoise, SetNode, SetNode, SetNode, SetNode, LatentUpscaleModelLoader, SetNode, KSamplerSelect, VAEDecodeTiled, CR Text Concatenate, CR Text Concatenate, Display Any (rgthree), SetNode, CR Text, GetNode, SamplerCustomAdvanced, SamplerCustomAdvanced, SetNode, GetNode, easy cleanGpuUsed, LTXVSeparateAVLatent, SetNode, LTXVAudioVAEDecode, VHS_VideoCombine, GetNode, SetNode, AudioToFPS, GetNode, SaveAudioMP3, FB_Qwen3TTSVoiceClone, GetNode, MelBandRoFormerSampler, GetNode, LTXVAudioVAEEncode, GetNode, SolidMask, SetLatentNoiseMask, SetNode, GetNode, VRAMReserver, LoraLoaderModelOnly, Switch any [Crystools], LoraLoaderModelOnly, LTXVConditioning, SetNode, JWInteger, ttN concat, GetNode, JWInteger, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVConcatAVLatent, SetNode, easy boolean, Any To String (mtb), LoraLoaderModelOnly, GetNode, LTXVAudioVAEDecode, ImpactSwitch, ProcessString, easy cleanGpuUsed, Any To String (mtb), CR Text, CR Text, SomethingToString, ShowText|pysssss, Qwen3_VQA, JoinStrings, CR Text, GetNode, TextInput_, CR Text, AudioToFPS, LayerUtility: PurgeVRAM, AudioResample, AudioDither, AudioPad, GetNode, SetNode, Display Any (rgthree), Display Any (rgthree), DualCLIPLoader, ImpactSwitch, PreviewAudio, easy cleanGpuUsed, VAELoaderKJ, LTXVImgToVideoInplace, CFGGuider, SaveAudio, GetNode, ManualSigmas, GetNode, GetNode, GetNode, LTX2SamplingPreviewOverride, LTX2_NAG, CheckpointLoaderSimple, ManualSigmas, VAELoaderKJ, UNETLoader, LTXVScheduler, CLIPTextEncode]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-distilled.safetensors"}
---

# 视频生成/图生视频/LTX2.3+QwenTTS音色克隆对口型【角色说话】_2033108960152133633.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2033108960152133633.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（197 个）：
- `MelBandRoFormerModelLoader`
- `CR Text`
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
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `RandomNoise`
- `easy cleanGpuUsed`
- `KSamplerSelect` ★核心
- `SetNode`
- `SetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `LTXVCropGuides`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `CFGGuider`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `LTXVPreprocess`
- `ResizeImagesByLongerEdge`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `Int`
- `GetNode`
- `SaveVideo`
- `CreateVideo`
- `SetNode`
- `SetNode`
- `CR Text`
- `CR String To Combo`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageSize`
- `easy compare`
- `Int`
- `Display Any (rgthree)`
- `InversionDemoLazySwitch`
- `EmptyImage`
- `ImageScaleBy`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetNode`
- `Int`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ASRMW`
- `Display Any (rgthree)`
- `SetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CR Prompt Text`
- `SetNode`
- `LoadAudio`
- `SetNode`
- `CR Text`
- `SetNode`
- `GetNode`
- `GetNode`
- `WhisperSTT`
- `LoadImage`
- `RandomNoise`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LatentUpscaleModelLoader`
- `SetNode`
- `KSamplerSelect` ★核心
- `VAEDecodeTiled` ★核心
- `CR Text Concatenate`
- `CR Text Concatenate`
- `Display Any (rgthree)`
- `SetNode`
- `CR Text`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `LTXVSeparateAVLatent`
- `SetNode`
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`
- `GetNode`
- `SetNode`
- `AudioToFPS`
- `GetNode`
- `SaveAudioMP3`
- `FB_Qwen3TTSVoiceClone`
- `GetNode`
- `MelBandRoFormerSampler` ★核心
- `GetNode`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `SolidMask`
- `SetLatentNoiseMask`
- `SetNode`
- `GetNode`
- `VRAMReserver`
- `LoraLoaderModelOnly` ★核心
- `Switch any [Crystools]`
- `LoraLoaderModelOnly` ★核心
- `LTXVConditioning`
- `SetNode`
- `JWInteger`
- `ttN concat`
- `GetNode`
- `JWInteger`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LTXVConcatAVLatent`
- `SetNode`
- `easy boolean`
- `Any To String (mtb)`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `ImpactSwitch`
- `ProcessString`
- `easy cleanGpuUsed`
- `Any To String (mtb)`
- `CR Text`
- `CR Text`
- `SomethingToString`
- `ShowText|pysssss`
- `Qwen3_VQA`
- `JoinStrings`
- `CR Text`
- `GetNode`
- `TextInput_`
- `CR Text`
- `AudioToFPS`
- `LayerUtility: PurgeVRAM`
- `AudioResample`
- `AudioDither`
- `AudioPad`
- `GetNode`
- `SetNode`
- `Display Any (rgthree)`
- `Display Any (rgthree)`
- `DualCLIPLoader`
- `ImpactSwitch`
- `PreviewAudio`
- `easy cleanGpuUsed`
- `VAELoaderKJ`
- `LTXVImgToVideoInplace`
- `CFGGuider`
- `SaveAudio`
- `GetNode`
- `ManualSigmas`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `CheckpointLoaderSimple` ★核心
- `ManualSigmas`
- `VAELoaderKJ`
- `UNETLoader` ★核心
- `LTXVScheduler`
- `CLIPTextEncode` ★核心

## 关键参数

- `checkpoint` = `ltx-2.3-22b-distilled.safetensors`

## 知识

覆盖率 **59%**（117/197）

**有卡**：`MelBandRoFormerModelLoader`、`CR Text`、`easy cleanGpuUsed`、`CLIPTextEncode`、`RandomNoise`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`CFGGuider`、`LTXVPreprocess`、`ResizeImagesByLongerEdge`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecodeTiled`、`VHS_VideoCombine`、`Int`、`SaveVideo`、`CreateVideo`、`CR String To Combo`、`GetImageSize`、`easy compare`、`Display Any (rgthree)`、`InversionDemoLazySwitch`、`EmptyImage`、`ImageScaleBy`、`EmptyLTXVLatentVideo`、`ASRMW`、`CR Prompt Text`、`LoadAudio`、`WhisperSTT`、`LoadImage`、`LatentUpscaleModelLoader`、`CR Text Concatenate`、`SamplerCustomAdvanced`、`LTXVAudioVAEDecode`、`AudioToFPS`、`SaveAudioMP3`、`FB_Qwen3TTSVoiceClone`、`MelBandRoFormerSampler`、`LTXVAudioVAEEncode`、`SolidMask`、`SetLatentNoiseMask`、`VRAMReserver`、`LoraLoaderModelOnly`、`Switch any [Crystools]`、`LTXVConditioning`、`JWInteger`、`ttN concat`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`easy boolean`、`Any To String (mtb)`、`ProcessString`、`SomethingToString`、`Qwen3_VQA`、`JoinStrings`、`TextInput_`、`LayerUtility: PurgeVRAM`、`AudioResample`、`AudioDither`、`AudioPad`、`DualCLIPLoader`、`PreviewAudio`、`VAELoaderKJ`、`SaveAudio`、`ManualSigmas`、`LTX2SamplingPreviewOverride`、`LTX2_NAG`、`CheckpointLoaderSimple`、`UNETLoader`、`LTXVScheduler`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect

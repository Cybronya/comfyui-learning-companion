---
key: 视频生成/图生视频/QwenTTS+LTX2.0角色说话_2017601157362884610.json
name: QwenTTS+LTX2.0角色说话_2017601157362884610.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/QwenTTS+LTX2.0角色说话_2017601157362884610.json
hash: 839fa9b22f161120
coverage: 0.592784
learned_at: 2026-10-15 22:34:50
nodes: [MelBandRoFormerModelLoader, CR Text, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, CLIPTextEncode, CLIPTextEncode, SetNode, GetNode, GetNode, RandomNoise, GetNode, GetNode, CFGGuider, easy cleanGpuUsed, KSamplerSelect, SetNode, SetNode, LTXVSeparateAVLatent, GetNode, LTXVLatentUpsampler, LTXVCropGuides, GetNode, GetNode, easy cleanGpuUsed, CFGGuider, SetNode, SetNode, GetNode, SetNode, LTXVPreprocess, ResizeImagesByLongerEdge, LayerUtility: ImageScaleByAspectRatio V2, SetNode, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, VAEDecodeTiled, GetNode, SetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, GetNode, Int, GetNode, SaveVideo, CreateVideo, SetNode, SetNode, CR Text, CR String To Combo, GetNode, GetNode, GetNode, GetImageSize, easy compare, Int, Display Any (rgthree), InversionDemoLazySwitch, EmptyImage, ImageScaleBy, EmptyLTXVLatentVideo, GetNode, GetNode, Int, SetNode, SetNode, GetNode, GetNode, ASRMW, Display Any (rgthree), SetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, GetNode, GetNode, GetNode, CR Prompt Text, SetNode, LoadAudio, SetNode, CR Text, SetNode, GetNode, GetNode, WhisperSTT, LoadImage, RandomNoise, SetNode, SetNode, VAELoaderKJ, VAELoaderKJ, SetNode, SetNode, LatentUpscaleModelLoader, SetNode, KSamplerSelect, VAEDecodeTiled, CR Text Concatenate, CR Text Concatenate, Display Any (rgthree), SetNode, CR Text, GetNode, SamplerCustomAdvanced, SamplerCustomAdvanced, SetNode, GetNode, easy cleanGpuUsed, LTXVSeparateAVLatent, SetNode, LTXVAudioVAEDecode, VHS_VideoCombine, GetNode, SetNode, AudioToFPS, GetNode, SaveAudioMP3, FB_Qwen3TTSVoiceClone, GetNode, MelBandRoFormerSampler, GetNode, LTXVAudioVAEEncode, GetNode, SolidMask, SetLatentNoiseMask, SetNode, GetNode, VRAMReserver, LoraLoaderModelOnly, Switch any [Crystools], LoraLoaderModelOnly, LTXVConditioning, SetNode, JWInteger, ttN concat, GetNode, JWInteger, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVConcatAVLatent, SetNode, easy boolean, Any To String (mtb), LoraLoaderModelOnly, GetNode, LTXVAudioVAEDecode, ImpactSwitch, ProcessString, easy cleanGpuUsed, Any To String (mtb), CR Text, CR Text, SomethingToString, ShowText|pysssss, Qwen3_VQA, JoinStrings, CR Text, GetNode, TextInput_, CR Text, AudioToFPS, LayerUtility: PurgeVRAM, AudioResample, AudioDither, AudioPad, GetNode, SetNode, Display Any (rgthree), Display Any (rgthree), ManualSigmas, ManualSigmas, LTXVImgToVideoInplace, DualCLIPLoader, LTXVScheduler, ImpactSwitch, SaveAudio, PreviewAudio, easy cleanGpuUsed, UNETLoader, CheckpointLoaderSimple]
patterns: []
missing: []
parameters: {"checkpoint": "ltx2-phr00tmerge-sfw-v5.safetensors"}
---

# 视频生成/图生视频/QwenTTS+LTX2.0角色说话_2017601157362884610.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2017601157362884610.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（194 个）：
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
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `CFGGuider`
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
- `VAELoaderKJ`
- `VAELoaderKJ`
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
- `ManualSigmas`
- `ManualSigmas`
- `LTXVImgToVideoInplace`
- `DualCLIPLoader`
- `LTXVScheduler`
- `ImpactSwitch`
- `SaveAudio`
- `PreviewAudio`
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `CheckpointLoaderSimple` ★核心

## 关键参数

- `checkpoint` = `ltx2-phr00tmerge-sfw-v5.safetensors`

## 知识

覆盖率 **59%**（115/194）

**有卡**：`MelBandRoFormerModelLoader`、`CR Text`、`easy cleanGpuUsed`、`CLIPTextEncode`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`LTXVPreprocess`、`ResizeImagesByLongerEdge`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecodeTiled`、`VHS_VideoCombine`、`Int`、`SaveVideo`、`CreateVideo`、`CR String To Combo`、`GetImageSize`、`easy compare`、`Display Any (rgthree)`、`InversionDemoLazySwitch`、`EmptyImage`、`ImageScaleBy`、`EmptyLTXVLatentVideo`、`ASRMW`、`CR Prompt Text`、`LoadAudio`、`WhisperSTT`、`LoadImage`、`VAELoaderKJ`、`LatentUpscaleModelLoader`、`CR Text Concatenate`、`SamplerCustomAdvanced`、`LTXVAudioVAEDecode`、`AudioToFPS`、`SaveAudioMP3`、`FB_Qwen3TTSVoiceClone`、`MelBandRoFormerSampler`、`LTXVAudioVAEEncode`、`SolidMask`、`SetLatentNoiseMask`、`VRAMReserver`、`LoraLoaderModelOnly`、`Switch any [Crystools]`、`LTXVConditioning`、`JWInteger`、`ttN concat`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`easy boolean`、`Any To String (mtb)`、`ProcessString`、`SomethingToString`、`Qwen3_VQA`、`JoinStrings`、`TextInput_`、`LayerUtility: PurgeVRAM`、`AudioResample`、`AudioDither`、`AudioPad`、`ManualSigmas`、`DualCLIPLoader`、`LTXVScheduler`、`SaveAudio`、`PreviewAudio`、`UNETLoader`、`CheckpointLoaderSimple`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect

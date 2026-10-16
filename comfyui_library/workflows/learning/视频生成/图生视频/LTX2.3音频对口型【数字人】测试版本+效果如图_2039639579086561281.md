---
key: 视频生成/图生视频/LTX2.3音频对口型【数字人】测试版本+效果如图_2039639579086561281.json
name: LTX2.3音频对口型【数字人】测试版本+效果如图_2039639579086561281.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2039639579086561281.json
hash: 839bad46f0ec8895
coverage: 0.95122
learned_at: 2026-10-15 22:36:10
nodes: [MelBandRoFormerModelLoader, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, CFGGuider, easy cleanGpuUsed, LTXVSeparateAVLatent, easy cleanGpuUsed, LTXVSeparateAVLatent, LTXVPreprocess, MelBandRoFormerSampler, easy compare, EmptyImage, ImageScaleBy, ASRMW, LayerUtility: ImageScaleByAspectRatio V2, LTXVConcatAVLatent, easy cleanGpuUsed, CLIPTextEncode, LTXVAudioVAEEncode, SolidMask, SetLatentNoiseMask, ProcessString, CR Text Concatenate, easy cleanGpuUsed, LatentUpscaleModelLoader, GetImageSize, EmptyLTXVLatentVideo, RandomNoise, AudioToFPS, LTXVConditioning, LTXVImgToVideoInplace, CFGGuider, RandomNoise, LTXVCropGuides, CLIPTextEncode, LTX2_NAG, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, VAELoaderKJ, VAELoaderKJ, UNETLoader, DualCLIPLoader, SamplerCustomAdvanced, LTXVImgToVideoInplace, LTXVConcatAVLatent, ManualSigmas, KSamplerSelect, LTXVLatentUpsampler, SamplerCustomAdvanced, LTXVScheduler, JWInteger, SomethingToString, Qwen3_VQA, JoinStrings, JjkText, CR Text, VHS_VideoCombine, ImpactSwitch, CR Text, CR Text Concatenate, ImpactSwitch, VRAMReserver, easy boolean, LoraLoaderModelOnly, LoraLoaderModelOnly, CR Text, PrimitiveBoolean, ShowText|pysssss, Switch any [Crystools], ResizeImagesByLongerEdge, LoraLoaderModelOnly, LoraLoaderModelOnly, VAEDecodeTiled, Int, InversionDemoLazySwitch, JWInteger, LoadImage, LoadAudio, AudioCrop, CR Text, Any To String (mtb)]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX2.3音频对口型【数字人】测试版本+效果如图_2039639579086561281.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2039639579086561281.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（82 个）：
- `MelBandRoFormerModelLoader`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `CFGGuider`
- `easy cleanGpuUsed`
- `LTXVSeparateAVLatent`
- `easy cleanGpuUsed`
- `LTXVSeparateAVLatent`
- `LTXVPreprocess`
- `MelBandRoFormerSampler` ★核心
- `easy compare`
- `EmptyImage`
- `ImageScaleBy`
- `ASRMW`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LTXVConcatAVLatent`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `SetLatentNoiseMask`
- `ProcessString`
- `CR Text Concatenate`
- `easy cleanGpuUsed`
- `LatentUpscaleModelLoader`
- `GetImageSize`
- `EmptyLTXVLatentVideo`
- `RandomNoise`
- `AudioToFPS`
- `LTXVConditioning`
- `LTXVImgToVideoInplace`
- `CFGGuider`
- `RandomNoise`
- `LTXVCropGuides`
- `CLIPTextEncode` ★核心
- `LTX2_NAG`
- `KSamplerSelect` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `SamplerCustomAdvanced` ★核心
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `LTXVLatentUpsampler` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVScheduler`
- `JWInteger`
- `SomethingToString`
- `Qwen3_VQA`
- `JoinStrings`
- `JjkText`
- `CR Text`
- `VHS_VideoCombine`
- `ImpactSwitch`
- `CR Text`
- `CR Text Concatenate`
- `ImpactSwitch`
- `VRAMReserver`
- `easy boolean`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Text`
- `PrimitiveBoolean`
- `ShowText|pysssss`
- `Switch any [Crystools]`
- `ResizeImagesByLongerEdge`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecodeTiled` ★核心
- `Int`
- `InversionDemoLazySwitch`
- `JWInteger`
- `LoadImage`
- `LoadAudio`
- `AudioCrop`
- `CR Text`
- `Any To String (mtb)`

## 知识

覆盖率 **95%**（78/82）

**有卡**：`MelBandRoFormerModelLoader`、`easy cleanGpuUsed`、`CFGGuider`、`LTXVSeparateAVLatent`、`LTXVPreprocess`、`MelBandRoFormerSampler`、`easy compare`、`EmptyImage`、`ImageScaleBy`、`ASRMW`、`LayerUtility: ImageScaleByAspectRatio V2`、`LTXVConcatAVLatent`、`CLIPTextEncode`、`LTXVAudioVAEEncode`、`SolidMask`、`SetLatentNoiseMask`、`ProcessString`、`CR Text Concatenate`、`LatentUpscaleModelLoader`、`GetImageSize`、`EmptyLTXVLatentVideo`、`RandomNoise`、`AudioToFPS`、`LTXVConditioning`、`LTXVImgToVideoInplace`、`LTXVCropGuides`、`LTX2_NAG`、`KSamplerSelect`、`VAELoaderKJ`、`UNETLoader`、`DualCLIPLoader`、`SamplerCustomAdvanced`、`ManualSigmas`、`LTXVLatentUpsampler`、`LTXVScheduler`、`JWInteger`、`SomethingToString`、`Qwen3_VQA`、`JoinStrings`、`CR Text`、`VHS_VideoCombine`、`VRAMReserver`、`easy boolean`、`LoraLoaderModelOnly`、`PrimitiveBoolean`、`Switch any [Crystools]`、`ResizeImagesByLongerEdge`、`VAEDecodeTiled`、`Int`、`InversionDemoLazySwitch`、`LoadImage`、`LoadAudio`、`AudioCrop`、`Any To String (mtb)`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

---
key: 视频生成/图生视频/LTX 2.3  首尾帧数字人高清+30秒视频41分钟pius模式_2046223171501694978.json
name: LTX 2.3  首尾帧数字人高清+30秒视频41分钟pius模式_2046223171501694978.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX 2.3  首尾帧数字人高清+30秒视频41分钟pius模式_2046223171501694978.json
hash: 3a3f0c0554f1506b
coverage: 0.496599
learned_at: 2026-10-15 22:36:56
nodes: [SetNode, LTXVSeparateAVLatent, SetLatentNoiseMask, LTXVAudioVAEEncode, SolidMask, SetNode, MelBandRoFormerSampler, SetNode, PreviewAudio, GetNode, GetNode, GetNode, GetNode, GetNode, SimpleMath+, SetNode, GetNode, GetNode, INTConstant, GetNode, GetNode, GetNode, GetNode, KSamplerSelect, GetNode, GetNode, GetNode, SetNode, SetNode, LTXVLatentUpsampler, GetNode, GetNode, SimpleMath+, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, EmptyLTXVLatentVideo, LTXVConditioning, SetNode, ImageResizeKJv2, GetImageSize, SetNode, GetNode, ImageFlip, VAEDecodeTiled, LTXVConcatAVLatent, SetNode, LTXVEmptyLatentAudio, GetNode, CLIPTextEncode, Seed (rgthree), SetNode, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, KSamplerSelect, GetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, GetNode, GetNode, LTXVSeparateAVLatent, GetNode, SetNode, VAEDecodeTiled, GetNode, ResizeImageMaskNode, GetNode, PreviewAudio, ImageFlip, GetNode, LTXVPreprocess, GetNode, AudioInfo, SimpleMath+, GetNode, Display Any (rgthree), VAELoaderKJ, VAELoaderKJ, LTXVImgToVideoInplaceKJ, ManualSigmas, LTXVConcatAVLatent, LTXVImgToVideoInplaceKJ, GetNode, GetNode, GetNode, GetNode, GetNode, SimpleMath+, SetNode, SetNode, SetNode, SetNode, LatentUpscaleModelLoader, SetNode, MelBandRoFormerModelLoader, DualCLIPLoader, DiffusionModelLoaderKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, PainterVRAM, LoraLoaderModelOnly, SamplerCustom, ManualSigmas, SetNode, SetNode, SetNode, CLIPTextEncode, SetNode, GetNode, PreviewImage, ImageConcanate, GetNode, RH_LLMAPI_Pro_Node, GetNode, GetNode, ImageResizeKJv2, LoadImage, LoadImage, AudioCrop, ShowText|pysssss, SetNode, WujiCleaner, WujiCleaner, WujiCleaner, WujiCleaner, WujiCleaner, WujiCleaner, WujiCleaner, SamplerCustom, WujiCleaner, TextInput_, INTConstant, INTConstant, SetNode, LoadAudio, SetNode, Note, Fast Groups Bypasser (rgthree), TextInput_, SetNode, SimpleMath+]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 121}
---

# 视频生成/图生视频/LTX 2.3  首尾帧数字人高清+30秒视频41分钟pius模式_2046223171501694978.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2046223171501694978.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（147 个）：
- `SetNode`
- `LTXVSeparateAVLatent`
- `SetLatentNoiseMask`
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `SetNode`
- `MelBandRoFormerSampler` ★核心
- `SetNode`
- `PreviewAudio`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SimpleMath+`
- `SetNode`
- `GetNode`
- `GetNode`
- `INTConstant`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `GetNode`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `LTXVConditioning`
- `SetNode`
- `ImageResizeKJv2`
- `GetImageSize`
- `SetNode`
- `GetNode`
- `ImageFlip`
- `VAEDecodeTiled` ★核心
- `LTXVConcatAVLatent`
- `SetNode`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `Seed (rgthree)`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `KSamplerSelect` ★核心
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `SetNode`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `ResizeImageMaskNode`
- `GetNode`
- `PreviewAudio`
- `ImageFlip`
- `GetNode`
- `LTXVPreprocess`
- `GetNode`
- `AudioInfo`
- `SimpleMath+`
- `GetNode`
- `Display Any (rgthree)`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LTXVImgToVideoInplaceKJ`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplaceKJ`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SimpleMath+`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LatentUpscaleModelLoader`
- `SetNode`
- `MelBandRoFormerModelLoader`
- `DualCLIPLoader`
- `DiffusionModelLoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PainterVRAM`
- `LoraLoaderModelOnly` ★核心
- `SamplerCustom` ★核心
- `ManualSigmas`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `PreviewImage`
- `ImageConcanate`
- `GetNode`
- `RH_LLMAPI_Pro_Node`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadImage`
- `AudioCrop`
- `ShowText|pysssss`
- `SetNode`
- `WujiCleaner`
- `WujiCleaner`
- `WujiCleaner`
- `WujiCleaner`
- `WujiCleaner`
- `WujiCleaner`
- `WujiCleaner`
- `SamplerCustom` ★核心
- `WujiCleaner`
- `TextInput_`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `LoadAudio`
- `SetNode`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `TextInput_`
- `SetNode`
- `SimpleMath+`

## 关键参数

- `width` = `121`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **50%**（73/147）

**有卡**：`LTXVSeparateAVLatent`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`SolidMask`、`MelBandRoFormerSampler`、`PreviewAudio`、`SimpleMath+`、`INTConstant`、`KSamplerSelect`、`LTXVLatentUpsampler`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`ImageResizeKJv2`、`GetImageSize`、`ImageFlip`、`VAEDecodeTiled`、`LTXVConcatAVLatent`、`LTXVEmptyLatentAudio`、`CLIPTextEncode`、`Seed (rgthree)`、`VHS_VideoCombine`、`ResizeImageMaskNode`、`LTXVPreprocess`、`AudioInfo`、`Display Any (rgthree)`、`VAELoaderKJ`、`LTXVImgToVideoInplaceKJ`、`ManualSigmas`、`LatentUpscaleModelLoader`、`MelBandRoFormerModelLoader`、`DualCLIPLoader`、`DiffusionModelLoaderKJ`、`LoraLoaderModelOnly`、`PainterVRAM`、`SamplerCustom`、`ImageConcanate`、`RH_LLMAPI_Pro_Node`、`LoadImage`、`AudioCrop`、`WujiCleaner`、`TextInput_`、`LoadAudio`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、KSamplerSelect、SamplerCustom、MelBandRoFormerSampler、LTXVLatentUpsampler、Seed (rgthree)

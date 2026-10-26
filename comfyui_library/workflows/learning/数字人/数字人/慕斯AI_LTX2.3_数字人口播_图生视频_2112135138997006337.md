---
key: 数字人/数字人/慕斯AI_LTX2.3_数字人口播_图生视频_2112135138997006337.json
name: 慕斯AI_LTX2.3_数字人口播_图生视频_2112135138997006337
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/慕斯AI_LTX2.3_数字人口播_图生视频_2112135138997006337.json
hash: e7c3fe9383b55720
coverage: 0.53125
learned_at: 2026-10-26 02:02:11
nodes: [SetNode, SetNode, SetNode, GetNode, GetNode, SolidMask, GetNode, GetNode, GetNode, SetNode, SetNode, LTXVConcatAVLatent, SetNode, SetNode, SetNode, GetNode, SetNode, GetNode, LTXVAudioVAEEncode, VAELoader, INTConstant, INTConstant, ImageResizeKJv2, SetNode, SetNode, DualCLIPLoader, VAELoader, GetNode, JoinStrings, SetNode, LTXVConditioning, GetNode, GetNode, VAEDecode, LayerUtility: PurgeVRAM, LTXVSeparateAVLatent, Note, PrimitiveFloat, VHS_VideoCombine, LTXVCropGuides, INTConstant, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, VAELoaderKJ, SetLatentNoiseMask, SimpleCalculatorKJ, SetNode, LTXVPreprocess, MelBandRoFormerModelLoader, RandomNoise, GetNode, SetNode, GetImageSize, ResizeImageMaskNode, SetNode, SetNode, SetNode, SetNode, CLIPTextEncode, CFGGuider, ModelSamplingSD3, SetNode, BasicScheduler, SetNode, ImageResizeKJv2, GetNode, SetNode, MelBandRoFormerSampler, TrimAudioDuration, LTXVImgToVideoInplaceKJ, LTX2_NAG, GetNode, CLIPTextEncode, LTX2SamplingPreviewOverride, TrimAudioDuration, LatentUpscaleModelLoader, LayerUtility: PurgeVRAM, EmptyLTXVLatentVideo, SimpleMath+, SimpleMath+, KSamplerSelect, SetNode, SamplerCustomAdvanced, VHS_LoadAudioUpload, GetNode, GetNode, SetNode, GetNode, ComfySwitchNode, SetNode, SimpleMath+, SetNode, SetNode, easy showAnything, PreviewAudio, PrimitiveFloat, PrimitiveFloat, UNETLoader, PrimitiveStringMultiline, PathchSageAttentionKJ, LTX2AttentionTunerPatch, GetNode, GetNode, InversionDemoLazySwitch, Compare, Int, INTConstant, INTConstant, PrimitiveStringMultiline, LoadImage, PrimitiveStringMultiline, JoinStrings, SimpleMath+, ResizeImageMaskNode, GetImageSize, LTXVLatentUpsampler, LTXVImgToVideoInplaceKJ, LTXVConcatAVLatent, CFGGuider, ManualSigmas, KSamplerSelect, SamplerCustomAdvanced, LTXVSeparateAVLatent]
patterns: []
missing: []
---

# 数字人/数字人/慕斯AI_LTX2.3_数字人口播_图生视频_2112135138997006337.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/慕斯AI_LTX2.3_数字人口播_图生视频_2112135138997006337.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（128 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SolidMask`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `LTXVConcatAVLatent`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `LTXVAudioVAEEncode` ★核心
- `VAELoader`
- `INTConstant`
- `INTConstant`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `DualCLIPLoader`
- `VAELoader`
- `GetNode`
- `JoinStrings`
- `SetNode`
- `LTXVConditioning`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `LTXVSeparateAVLatent`
- `Note`
- `PrimitiveFloat`
- `VHS_VideoCombine`
- `LTXVCropGuides`
- `INTConstant`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `VAELoaderKJ`
- `SetLatentNoiseMask`
- `SimpleCalculatorKJ`
- `SetNode`
- `LTXVPreprocess`
- `MelBandRoFormerModelLoader`
- `RandomNoise`
- `GetNode`
- `SetNode`
- `GetImageSize`
- `ResizeImageMaskNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `ModelSamplingSD3`
- `SetNode`
- `BasicScheduler`
- `SetNode`
- `ImageResizeKJv2`
- `GetNode`
- `SetNode`
- `MelBandRoFormerSampler` ★核心
- `TrimAudioDuration`
- `LTXVImgToVideoInplaceKJ`
- `LTX2_NAG`
- `GetNode`
- `CLIPTextEncode` ★核心
- `LTX2SamplingPreviewOverride`
- `TrimAudioDuration`
- `LatentUpscaleModelLoader`
- `LayerUtility: PurgeVRAM`
- `EmptyLTXVLatentVideo`
- `SimpleMath+`
- `SimpleMath+`
- `KSamplerSelect` ★核心
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `VHS_LoadAudioUpload`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `ComfySwitchNode`
- `SetNode`
- `SimpleMath+`
- `SetNode`
- `SetNode`
- `easy showAnything`
- `PreviewAudio`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `UNETLoader` ★核心
- `PrimitiveStringMultiline`
- `PathchSageAttentionKJ`
- `LTX2AttentionTunerPatch`
- `GetNode`
- `GetNode`
- `InversionDemoLazySwitch`
- `Compare`
- `Int`
- `INTConstant`
- `INTConstant`
- `PrimitiveStringMultiline`
- `LoadImage`
- `PrimitiveStringMultiline`
- `JoinStrings`
- `SimpleMath+`
- `ResizeImageMaskNode`
- `GetImageSize`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplaceKJ`
- `LTXVConcatAVLatent`
- `CFGGuider`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`

## 知识

覆盖率 **53%**（68/128）

**有卡**：`SolidMask`、`LTXVConcatAVLatent`、`LTXVAudioVAEEncode`、`VAELoader`、`INTConstant`、`ImageResizeKJv2`、`DualCLIPLoader`、`JoinStrings`、`LTXVConditioning`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`LTXVSeparateAVLatent`、`VHS_VideoCombine`、`LTXVCropGuides`、`VAELoaderKJ`、`SetLatentNoiseMask`、`SimpleCalculatorKJ`、`LTXVPreprocess`、`MelBandRoFormerModelLoader`、`RandomNoise`、`GetImageSize`、`ResizeImageMaskNode`、`CLIPTextEncode`、`CFGGuider`、`ModelSamplingSD3`、`BasicScheduler`、`MelBandRoFormerSampler`、`TrimAudioDuration`、`LTXVImgToVideoInplaceKJ`、`LTX2_NAG`、`LTX2SamplingPreviewOverride`、`LatentUpscaleModelLoader`、`EmptyLTXVLatentVideo`、`SimpleMath+`、`KSamplerSelect`、`SamplerCustomAdvanced`、`VHS_LoadAudioUpload`、`PreviewAudio`、`UNETLoader`、`PathchSageAttentionKJ`、`LTX2AttentionTunerPatch`、`InversionDemoLazySwitch`、`Compare`、`Int`、`LoadImage`、`LTXVLatentUpsampler`、`ManualSigmas`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

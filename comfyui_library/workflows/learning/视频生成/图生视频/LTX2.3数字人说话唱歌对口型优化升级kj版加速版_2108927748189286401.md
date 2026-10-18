---
key: 视频生成/图生视频/LTX2.3数字人说话唱歌对口型优化升级kj版加速版_2108927748189286401.json
name: LTX2.3数字人说话唱歌对口型优化升级kj版加速版_2108927748189286401
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3数字人说话唱歌对口型优化升级kj版加速版_2108927748189286401.json
hash: a2a72c24776640c8
coverage: 0.482759
learned_at: 2026-10-17 22:49:42
nodes: [SetNode, SetNode, SetNode, GetNode, GetNode, SolidMask, GetNode, GetNode, GetNode, SetNode, SetNode, LTXVConcatAVLatent, SetNode, SetNode, SetNode, GetNode, SetNode, GetNode, LTXVAudioVAEEncode, VAELoader, INTConstant, INTConstant, ImageResizeKJv2, SetNode, SetNode, DualCLIPLoader, VAELoader, GetNode, JoinStrings, SetNode, LTXVConditioning, GetNode, GetNode, VAEDecode, LayerUtility: PurgeVRAM, LTXVSeparateAVLatent, PrimitiveFloat, LTXVCropGuides, INTConstant, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, VAELoaderKJ, SetLatentNoiseMask, SimpleCalculatorKJ, SetNode, LTXVPreprocess, MelBandRoFormerModelLoader, RandomNoise, GetNode, SetNode, GetImageSize, ResizeImageMaskNode, SetNode, SetNode, SetNode, SetNode, CLIPTextEncode, CFGGuider, ModelSamplingSD3, SetNode, BasicScheduler, SetNode, ImageResizeKJv2, GetNode, SetNode, MelBandRoFormerSampler, TrimAudioDuration, LTXVImgToVideoInplaceKJ, LTX2_NAG, GetNode, CLIPTextEncode, LTX2SamplingPreviewOverride, TrimAudioDuration, LatentUpscaleModelLoader, LayerUtility: PurgeVRAM, EmptyLTXVLatentVideo, SimpleMath+, SimpleMath+, KSamplerSelect, SetNode, SamplerCustomAdvanced, VHS_LoadAudioUpload, GetNode, GetNode, SetNode, GetNode, ComfySwitchNode, SetNode, SimpleMath+, SetNode, SetNode, easy showAnything, INTConstant, PreviewAudio, PrimitiveFloat, PrimitiveFloat, UNETLoader, PrimitiveStringMultiline, PrimitiveStringMultiline, PathchSageAttentionKJ, LTX2AttentionTunerPatch, GetNode, GetNode, InversionDemoLazySwitch, Compare, Int, INTConstant, LoadImage, VHS_VideoCombine, 孤海注释, 孤海注释]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX2.3数字人说话唱歌对口型优化升级kj版加速版_2108927748189286401.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.3数字人说话唱歌对口型优化升级kj版加速版_2108927748189286401.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（116 个）：
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
- `PrimitiveFloat`
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
- `INTConstant`
- `PreviewAudio`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `UNETLoader` ★核心
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PathchSageAttentionKJ`
- `LTX2AttentionTunerPatch`
- `GetNode`
- `GetNode`
- `InversionDemoLazySwitch`
- `Compare`
- `Int`
- `INTConstant`
- `LoadImage`
- `VHS_VideoCombine`
- `孤海注释`
- `孤海注释`

## 知识

覆盖率 **48%**（56/116）

**有卡**：`SolidMask`、`LTXVConcatAVLatent`、`LTXVAudioVAEEncode`、`VAELoader`、`INTConstant`、`ImageResizeKJv2`、`DualCLIPLoader`、`JoinStrings`、`LTXVConditioning`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`VAELoaderKJ`、`SetLatentNoiseMask`、`SimpleCalculatorKJ`、`LTXVPreprocess`、`MelBandRoFormerModelLoader`、`RandomNoise`、`GetImageSize`、`ResizeImageMaskNode`、`CLIPTextEncode`、`CFGGuider`、`ModelSamplingSD3`、`BasicScheduler`、`MelBandRoFormerSampler`、`TrimAudioDuration`、`LTXVImgToVideoInplaceKJ`、`LTX2_NAG`、`LTX2SamplingPreviewOverride`、`LatentUpscaleModelLoader`、`EmptyLTXVLatentVideo`、`SimpleMath+`、`KSamplerSelect`、`SamplerCustomAdvanced`、`VHS_LoadAudioUpload`、`PreviewAudio`、`UNETLoader`、`PathchSageAttentionKJ`、`LTX2AttentionTunerPatch`、`InversionDemoLazySwitch`、`Compare`、`Int`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

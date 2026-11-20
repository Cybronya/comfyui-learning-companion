---
key: 平台全量/LTX2.3数字人说话唱歌对口型！长视频版本2_2121162298231447553.json
name: LTX2.3数字人说话唱歌对口型！长视频版本2_2121162298231447553
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX2.3数字人说话唱歌对口型！长视频版本2_2121162298231447553.json
hash: 00b70335e0dfe03b
coverage: 0.533835
learned_at: 2026-11-14 00:38:42
nodes: [SetNode, SetNode, SetNode, GetNode, GetNode, SolidMask, GetNode, GetNode, GetNode, SetNode, SetNode, LTXVConcatAVLatent, SetNode, SetNode, SetNode, GetNode, SetNode, GetNode, LTXVAudioVAEEncode, VAELoader, INTConstant, INTConstant, ImageResizeKJv2, SetNode, SetNode, DualCLIPLoader, VAELoader, GetNode, JoinStrings, SetNode, LTXVConditioning, GetNode, GetNode, VAEDecode, LayerUtility: PurgeVRAM, LTXVSeparateAVLatent, Note, PrimitiveFloat, LoadImage, VHS_VideoCombine, LTXVCropGuides, INTConstant, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, VAELoaderKJ, SetLatentNoiseMask, SimpleCalculatorKJ, SetNode, LTXVPreprocess, MelBandRoFormerModelLoader, RandomNoise, GetNode, SetNode, GetImageSize, ResizeImageMaskNode, SetNode, SetNode, SetNode, SetNode, CLIPTextEncode, CFGGuider, ModelSamplingSD3, SetNode, BasicScheduler, SetNode, ImageResizeKJv2, GetNode, SetNode, MelBandRoFormerSampler, TrimAudioDuration, LTXVImgToVideoInplaceKJ, LTX2_NAG, GetNode, CLIPTextEncode, LTX2SamplingPreviewOverride, TrimAudioDuration, LatentUpscaleModelLoader, LayerUtility: PurgeVRAM, EmptyLTXVLatentVideo, SimpleMath+, SimpleMath+, KSamplerSelect, SetNode, SamplerCustomAdvanced, VHS_LoadAudioUpload, GetNode, GetNode, SetNode, GetNode, ComfySwitchNode, SetNode, SimpleMath+, SetNode, SetNode, easy showAnything, INTConstant, PreviewAudio, PrimitiveFloat, PrimitiveFloat, UNETLoader, PrimitiveStringMultiline, PrimitiveStringMultiline, PathchSageAttentionKJ, LTX2AttentionTunerPatch, GetNode, GetNode, InversionDemoLazySwitch, Compare, Int, INTConstant, GetNode, INTConstant, INTConstant, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, easy showAnything, SetNode, SimpleMath+, SimpleMath+, LTXVLatentUpsampler, LTXVImgToVideoInplaceKJ, LTXVConcatAVLatent, ManualSigmas, RandomNoise, SamplerCustomAdvanced, LTXVSeparateAVLatent]
patterns: []
missing: []
---

# 平台全量/LTX2.3数字人说话唱歌对口型！长视频版本2_2121162298231447553.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX2.3数字人说话唱歌对口型！长视频版本2_2121162298231447553.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（133 个）：
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
- `LoadImage`
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
- `GetNode`
- `INTConstant`
- `INTConstant`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `easy showAnything`
- `SetNode`
- `SimpleMath+`
- `SimpleMath+`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplaceKJ`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`

## 知识

覆盖率 **53%**（71/133）

**有卡**：`SolidMask`、`LTXVConcatAVLatent`、`LTXVAudioVAEEncode`、`VAELoader`、`INTConstant`、`ImageResizeKJv2`、`DualCLIPLoader`、`JoinStrings`、`LTXVConditioning`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`LTXVSeparateAVLatent`、`LoadImage`、`VHS_VideoCombine`、`LTXVCropGuides`、`VAELoaderKJ`、`SetLatentNoiseMask`、`SimpleCalculatorKJ`、`LTXVPreprocess`、`MelBandRoFormerModelLoader`、`RandomNoise`、`GetImageSize`、`ResizeImageMaskNode`、`CLIPTextEncode`、`CFGGuider`、`ModelSamplingSD3`、`BasicScheduler`、`MelBandRoFormerSampler`、`TrimAudioDuration`、`LTXVImgToVideoInplaceKJ`、`LTX2_NAG`、`LTX2SamplingPreviewOverride`、`LatentUpscaleModelLoader`、`EmptyLTXVLatentVideo`、`SimpleMath+`、`KSamplerSelect`、`SamplerCustomAdvanced`、`VHS_LoadAudioUpload`、`PreviewAudio`、`UNETLoader`、`PathchSageAttentionKJ`、`LTX2AttentionTunerPatch`、`InversionDemoLazySwitch`、`Compare`、`Int`、`LTXVLatentUpsampler`、`ManualSigmas`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、LTXVLatentUpsampler

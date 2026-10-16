---
key: 视频生成/图生视频/数字人带货视频LTX2.3_2083076708705587201.json
name: 数字人带货视频LTX2.3_2083076708705587201
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/数字人带货视频LTX2.3_2083076708705587201.json
hash: 28baec58524bf49b
coverage: 0.5
learned_at: 2026-10-16 01:17:14
nodes: [SetNode, SetNode, SetNode, GetNode, GetNode, SolidMask, GetNode, GetNode, GetNode, SetNode, SetNode, LTXVConcatAVLatent, SetNode, SetNode, SetNode, GetNode, SetNode, GetNode, VAELoader, INTConstant, INTConstant, ImageResizeKJv2, SetNode, SetNode, DualCLIPLoader, VAELoader, GetNode, JoinStrings, SetNode, LTXVConditioning, GetNode, GetNode, VAEDecode, LayerUtility: PurgeVRAM, LTXVSeparateAVLatent, LoraLoaderModelOnly, PrimitiveFloat, LTXVCropGuides, INTConstant, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, VAELoaderKJ, SetLatentNoiseMask, SimpleCalculatorKJ, LTXVChunkFeedForward, SetNode, LTXVPreprocess, MelBandRoFormerModelLoader, RandomNoise, GetNode, GetNode, GetNode, SetNode, GetImageSize, ResizeImageMaskNode, SetNode, SetNode, SetNode, SetNode, CLIPTextEncode, CFGGuider, ModelSamplingSD3, SetNode, BasicScheduler, SetNode, ImageResizeKJv2, GetNode, SetNode, LTXVImgToVideoInplaceKJ, LTX2_NAG, GetNode, CLIPTextEncode, LTX2SamplingPreviewOverride, TrimAudioDuration, LatentUpscaleModelLoader, LayerUtility: PurgeVRAM, EmptyLTXVLatentVideo, PathchSageAttentionKJ, LTX2AttentionTunerPatch, Int, SimpleMath+, SimpleMath+, KSamplerSelect, SetNode, SamplerCustomAdvanced, GetNode, GetNode, SetNode, GetNode, ComfySwitchNode, SetNode, SimpleMath+, SetNode, Compare, SetNode, easy showAnything, PrimitiveFloat, UNETLoader, MelBandRoFormerSampler, PrimitiveStringMultiline, TrimAudioDuration, LTXVAudioVAEEncode, InversionDemoLazySwitch, VHS_VideoCombine, IndexTTS2_Basic, SaveAudio, INTConstant, INTConstant, LoadImage, JjkText, LoadAudio, PrimitiveStringMultiline, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/图生视频/数字人带货视频LTX2.3_2083076708705587201.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/数字人带货视频LTX2.3_2083076708705587201.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（118 个）：
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
- `LoraLoaderModelOnly` ★核心
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
- `LTXVChunkFeedForward`
- `SetNode`
- `LTXVPreprocess`
- `MelBandRoFormerModelLoader`
- `RandomNoise`
- `GetNode`
- `GetNode`
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
- `LTXVImgToVideoInplaceKJ`
- `LTX2_NAG`
- `GetNode`
- `CLIPTextEncode` ★核心
- `LTX2SamplingPreviewOverride`
- `TrimAudioDuration`
- `LatentUpscaleModelLoader`
- `LayerUtility: PurgeVRAM`
- `EmptyLTXVLatentVideo`
- `PathchSageAttentionKJ`
- `LTX2AttentionTunerPatch`
- `Int`
- `SimpleMath+`
- `SimpleMath+`
- `KSamplerSelect` ★核心
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `ComfySwitchNode`
- `SetNode`
- `SimpleMath+`
- `SetNode`
- `Compare`
- `SetNode`
- `easy showAnything`
- `PrimitiveFloat`
- `UNETLoader` ★核心
- `MelBandRoFormerSampler` ★核心
- `PrimitiveStringMultiline`
- `TrimAudioDuration`
- `LTXVAudioVAEEncode` ★核心
- `InversionDemoLazySwitch`
- `VHS_VideoCombine`
- `IndexTTS2_Basic`
- `SaveAudio`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `JjkText`
- `LoadAudio`
- `PrimitiveStringMultiline`
- `MarkdownNote`

## 知识

覆盖率 **50%**（59/118）

**有卡**：`SolidMask`、`LTXVConcatAVLatent`、`VAELoader`、`INTConstant`、`ImageResizeKJv2`、`DualCLIPLoader`、`JoinStrings`、`LTXVConditioning`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`LTXVSeparateAVLatent`、`LoraLoaderModelOnly`、`LTXVCropGuides`、`VAELoaderKJ`、`SetLatentNoiseMask`、`SimpleCalculatorKJ`、`LTXVChunkFeedForward`、`LTXVPreprocess`、`MelBandRoFormerModelLoader`、`RandomNoise`、`GetImageSize`、`ResizeImageMaskNode`、`CLIPTextEncode`、`CFGGuider`、`ModelSamplingSD3`、`BasicScheduler`、`LTXVImgToVideoInplaceKJ`、`LTX2_NAG`、`LTX2SamplingPreviewOverride`、`TrimAudioDuration`、`LatentUpscaleModelLoader`、`EmptyLTXVLatentVideo`、`PathchSageAttentionKJ`、`LTX2AttentionTunerPatch`、`Int`、`SimpleMath+`、`KSamplerSelect`、`SamplerCustomAdvanced`、`Compare`、`UNETLoader`、`MelBandRoFormerSampler`、`LTXVAudioVAEEncode`、`InversionDemoLazySwitch`、`VHS_VideoCombine`、`IndexTTS2_Basic`、`SaveAudio`、`LoadImage`、`LoadAudio`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect

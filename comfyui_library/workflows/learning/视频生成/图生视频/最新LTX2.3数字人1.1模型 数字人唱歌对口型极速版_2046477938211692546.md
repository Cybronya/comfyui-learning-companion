---
key: 视频生成/图生视频/最新LTX2.3数字人1.1模型 数字人唱歌对口型极速版_2046477938211692546.json
name: 最新LTX2.3数字人1.1模型 数字人唱歌对口型极速版_2046477938211692546.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2046477938211692546.json
hash: 1697e921f0394203
coverage: 0.495575
learned_at: 2026-10-15 22:36:59
nodes: [SetNode, SetNode, SetNode, GetNode, GetNode, SolidMask, GetNode, SetNode, GetNode, GetNode, SetNode, SetNode, LTXVConcatAVLatent, SetNode, SetNode, SetNode, BasicScheduler, SetNode, KSamplerSelect, GetNode, CFGGuider, GetNode, SetNode, SetLatentNoiseMask, GetNode, LTX2SamplingPreviewOverride, LTXVAudioVAEEncode, SetNode, SetNode, GetImageSize, ResizeImageMaskNode, SetNode, SetNode, GetNode, TrimAudioDuration, SetNode, SimpleCalculatorKJ, RandomNoise, VAELoader, VAELoaderKJ, ComfySwitchNode, SetNode, INTConstant, GetNode, TrimAudioDuration, INTConstant, GetNode, GetNode, SetNode, SetNode, DualCLIPLoader, SetNode, SetNode, SetNode, VAELoader, ImageResizeKJv2, SamplerCustomAdvanced, GetNode, GetNode, PrimitiveStringMultiline, JoinStrings, CLIPTextEncode, SetNode, GetNode, GetNode, GetNode, SimpleCalculatorKJ, GetNode, MelBandRoFormerSampler, LTXVConditioning, SetNode, SimpleCalculatorKJ, GetNode, SetNode, GetNode, VAEDecode, LayerUtility: PurgeVRAM, LTXVCropGuides, LTXVSeparateAVLatent, LoraLoaderModelOnly, EmptyLTXVLatentVideo, MelBandRoFormerModelLoader, LTXVImgToVideoInplaceKJ, LTX2_NAG, CLIPTextEncode, PrimitiveFloat, ModelSamplingSD3, LatentUpscaleModelLoader, SetNode, SetNode, ImageResizeKJv2, UNETLoader, LayerUtility: PurgeVRAM, LTXVPreprocess, INTConstant, GetNode, SetNode, LTX2AttentionTunerPatch, LTXVChunkFeedForward, PathchSageAttentionKJ, SimpleCalculatorKJ, LoadImage, GetAudioDurationFromAudio, INTConstant, PrimitiveFloat, INTConstant, AudioTrim, PrimitiveStringMultiline, GetNode, SetNode, VHS_VideoCombine, Note, LoadAudio]
patterns: []
missing: []
---

# 视频生成/图生视频/最新LTX2.3数字人1.1模型 数字人唱歌对口型极速版_2046477938211692546.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2046477938211692546.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（113 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SolidMask`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `LTXVConcatAVLatent`
- `SetNode`
- `SetNode`
- `SetNode`
- `BasicScheduler`
- `SetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `CFGGuider`
- `GetNode`
- `SetNode`
- `SetLatentNoiseMask`
- `GetNode`
- `LTX2SamplingPreviewOverride`
- `LTXVAudioVAEEncode` ★核心
- `SetNode`
- `SetNode`
- `GetImageSize`
- `ResizeImageMaskNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `TrimAudioDuration`
- `SetNode`
- `SimpleCalculatorKJ`
- `RandomNoise`
- `VAELoader`
- `VAELoaderKJ`
- `ComfySwitchNode`
- `SetNode`
- `INTConstant`
- `GetNode`
- `TrimAudioDuration`
- `INTConstant`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `DualCLIPLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `VAELoader`
- `ImageResizeKJv2`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `PrimitiveStringMultiline`
- `JoinStrings`
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SimpleCalculatorKJ`
- `GetNode`
- `MelBandRoFormerSampler` ★核心
- `LTXVConditioning`
- `SetNode`
- `SimpleCalculatorKJ`
- `GetNode`
- `SetNode`
- `GetNode`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly` ★核心
- `EmptyLTXVLatentVideo`
- `MelBandRoFormerModelLoader`
- `LTXVImgToVideoInplaceKJ`
- `LTX2_NAG`
- `CLIPTextEncode` ★核心
- `PrimitiveFloat`
- `ModelSamplingSD3`
- `LatentUpscaleModelLoader`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `UNETLoader` ★核心
- `LayerUtility: PurgeVRAM`
- `LTXVPreprocess`
- `INTConstant`
- `GetNode`
- `SetNode`
- `LTX2AttentionTunerPatch`
- `LTXVChunkFeedForward`
- `PathchSageAttentionKJ`
- `SimpleCalculatorKJ`
- `LoadImage`
- `GetAudioDurationFromAudio`
- `INTConstant`
- `PrimitiveFloat`
- `INTConstant`
- `AudioTrim`
- `PrimitiveStringMultiline`
- `GetNode`
- `SetNode`
- `VHS_VideoCombine`
- `Note`
- `LoadAudio`

## 知识

覆盖率 **50%**（56/113）

**有卡**：`SolidMask`、`LTXVConcatAVLatent`、`BasicScheduler`、`KSamplerSelect`、`CFGGuider`、`SetLatentNoiseMask`、`LTX2SamplingPreviewOverride`、`LTXVAudioVAEEncode`、`GetImageSize`、`ResizeImageMaskNode`、`TrimAudioDuration`、`SimpleCalculatorKJ`、`RandomNoise`、`VAELoader`、`VAELoaderKJ`、`INTConstant`、`DualCLIPLoader`、`ImageResizeKJv2`、`SamplerCustomAdvanced`、`JoinStrings`、`CLIPTextEncode`、`MelBandRoFormerSampler`、`LTXVConditioning`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LoraLoaderModelOnly`、`EmptyLTXVLatentVideo`、`MelBandRoFormerModelLoader`、`LTXVImgToVideoInplaceKJ`、`LTX2_NAG`、`ModelSamplingSD3`、`LatentUpscaleModelLoader`、`UNETLoader`、`LTXVPreprocess`、`LTX2AttentionTunerPatch`、`LTXVChunkFeedForward`、`PathchSageAttentionKJ`、`LoadImage`、`GetAudioDurationFromAudio`、`AudioTrim`、`VHS_VideoCombine`、`LoadAudio`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect

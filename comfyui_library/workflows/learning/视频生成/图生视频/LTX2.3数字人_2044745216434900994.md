---
key: 视频生成/图生视频/LTX2.3数字人_2044745216434900994.json
name: LTX2.3数字人_2044745216434900994.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3数字人_2044745216434900994.json
hash: a6b5ff389dfd68fb
coverage: 0.519231
learned_at: 2026-10-15 22:36:40
nodes: [GetNode, LatentUpscaleModelLoader, SetNode, SetNode, SetNode, SetNode, SetNode, CLIPTextEncode, CFGGuider, SetNode, INTConstant, INTConstant, SimpleCalculatorKJ, TrimAudioDuration, GetNode, LTX2AttentionTunerPatch, CLIPTextEncode, LTXVConditioning, GetNode, LTX2_NAG, SetNode, SetNode, LTX2SamplingPreviewOverride, GetNode, SetNode, ModelSamplingSD3, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, GetNode, VAEDecode, LayerUtility: PurgeVRAM, SetNode, LTXVAudioVAEEncode, SetLatentNoiseMask, LTXVConcatAVLatent, LTXVImgToVideoInplaceKJ, SimpleCalculatorKJ, SetNode, VAELoaderKJ, UNETLoader, LoraLoaderModelOnly, LayerUtility: PurgeVRAM, VAELoader, DualCLIPLoader, VAELoader, GetNode, SolidMask, GetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, LoadImage, SetNode, MelBandRoFormerModelLoader, EmptyLTXVLatentVideo, GetNode, GetNode, MelBandRoFormerSampler, GetNode, GetNode, BasicScheduler, SetNode, LTXVPreprocess, LTXVChunkFeedForward, PathchSageAttentionKJ, JoinStrings, PrimitiveStringMultiline, GetNode, ComfySwitchNode, SetNode, GetNode, SetNode, TrimAudioDuration, SetNode, SetNode, SimpleCalculatorKJ, GetNode, Note, GetNode, ImageResizeKJv2, GetImageSize, GetNode, SetNode, SetNode, SimpleCalculatorKJ, PrimitiveFloat, SetNode, ImageResizeKJv2, SetNode, GetNode, SetNode, SetNode, ResizeImageMaskNode, SetNode, LoadAudio, INTConstant, INTConstant, RandomNoise, SetNode, KSamplerSelect, PrimitiveStringMultiline, INTConstant]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX2.3数字人_2044745216434900994.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2044745216434900994.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（104 个）：
- `GetNode`
- `LatentUpscaleModelLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `SimpleCalculatorKJ`
- `TrimAudioDuration`
- `GetNode`
- `LTX2AttentionTunerPatch`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `GetNode`
- `LTX2_NAG`
- `SetNode`
- `SetNode`
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `SetNode`
- `ModelSamplingSD3`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `GetNode`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplaceKJ`
- `SimpleCalculatorKJ`
- `SetNode`
- `VAELoaderKJ`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: PurgeVRAM`
- `VAELoader`
- `DualCLIPLoader`
- `VAELoader`
- `GetNode`
- `SolidMask`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `LoadImage`
- `SetNode`
- `MelBandRoFormerModelLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetNode`
- `MelBandRoFormerSampler` ★核心
- `GetNode`
- `GetNode`
- `BasicScheduler`
- `SetNode`
- `LTXVPreprocess`
- `LTXVChunkFeedForward`
- `PathchSageAttentionKJ`
- `JoinStrings`
- `PrimitiveStringMultiline`
- `GetNode`
- `ComfySwitchNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `TrimAudioDuration`
- `SetNode`
- `SetNode`
- `SimpleCalculatorKJ`
- `GetNode`
- `Note`
- `GetNode`
- `ImageResizeKJv2`
- `GetImageSize`
- `GetNode`
- `SetNode`
- `SetNode`
- `SimpleCalculatorKJ`
- `PrimitiveFloat`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `ResizeImageMaskNode`
- `SetNode`
- `LoadAudio`
- `INTConstant`
- `INTConstant`
- `RandomNoise`
- `SetNode`
- `KSamplerSelect` ★核心
- `PrimitiveStringMultiline`
- `INTConstant`

## 知识

覆盖率 **52%**（54/104）

**有卡**：`LatentUpscaleModelLoader`、`CLIPTextEncode`、`CFGGuider`、`INTConstant`、`SimpleCalculatorKJ`、`TrimAudioDuration`、`LTX2AttentionTunerPatch`、`LTXVConditioning`、`LTX2_NAG`、`LTX2SamplingPreviewOverride`、`ModelSamplingSD3`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`LTXVConcatAVLatent`、`LTXVImgToVideoInplaceKJ`、`VAELoaderKJ`、`UNETLoader`、`LoraLoaderModelOnly`、`VAELoader`、`DualCLIPLoader`、`SolidMask`、`VHS_VideoCombine`、`LoadImage`、`MelBandRoFormerModelLoader`、`EmptyLTXVLatentVideo`、`MelBandRoFormerSampler`、`BasicScheduler`、`LTXVPreprocess`、`LTXVChunkFeedForward`、`PathchSageAttentionKJ`、`JoinStrings`、`ImageResizeKJv2`、`GetImageSize`、`ResizeImageMaskNode`、`LoadAudio`、`RandomNoise`、`KSamplerSelect`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect

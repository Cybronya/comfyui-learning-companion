---
key: 视频生成/图生视频/LTX2.3+音频驱动_2084104031198343170.json
name: LTX2.3+音频驱动_2084104031198343170
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3+音频驱动_2084104031198343170.json
hash: 8b33b348022251d5
coverage: 0.490909
learned_at: 2026-10-16 19:17:11
nodes: [SetNode, SetNode, SetNode, GetNode, GetNode, SolidMask, GetNode, GetNode, SetNode, SetNode, LTXVConcatAVLatent, SetNode, SetNode, SetNode, BasicScheduler, SetNode, KSamplerSelect, GetNode, CFGGuider, GetNode, SetLatentNoiseMask, GetNode, LTX2SamplingPreviewOverride, LTXVAudioVAEEncode, SetNode, GetImageSize, ResizeImageMaskNode, SetNode, GetNode, RandomNoise, VAELoader, VAELoaderKJ, TrimAudioDuration, INTConstant, GetNode, GetNode, SetNode, SetNode, DualCLIPLoader, VAELoader, SamplerCustomAdvanced, PathchSageAttentionKJ, LTX2AttentionTunerPatch, LayerUtility: PurgeVRAM, GetNode, JoinStrings, LTXVChunkFeedForward, UNETLoader, SetNode, GetNode, MelBandRoFormerSampler, LTXVConditioning, SetNode, GetNode, SetNode, GetNode, VAEDecode, SetNode, LayerUtility: PurgeVRAM, LTXVCropGuides, LTXVSeparateAVLatent, LoraLoaderModelOnly, EmptyLTXVLatentVideo, INTConstant, MelBandRoFormerModelLoader, PrimitiveFloat, LatentUpscaleModelLoader, ModelSamplingSD3, LTX2_NAG, INTConstant, SetNode, VHS_VideoCombine, GetNode, LTXVImgToVideoInplaceKJ, SetNode, ImageResizeKJv2, LTXVPreprocess, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SimpleCalculatorKJ, SimpleCalculatorKJ, SetNode, ComfySwitchNode, SetNode, SetNode, TrimAudioDuration, ImageResizeKJv2, SimpleCalculatorKJ, GetNode, SetNode, SetNode, INTConstant, GetNode, GetNode, SimpleCalculatorKJ, PrimitiveFloat, SetNode, SetNode, LoadImage, LoadAudio, INTConstant, PrimitiveStringMultiline, PrimitiveStringMultiline, CLIPTextEncode, CLIPTextEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX2.3+音频驱动_2084104031198343170.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.3+音频驱动_2084104031198343170.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（110 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SolidMask`
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
- `SetLatentNoiseMask`
- `GetNode`
- `LTX2SamplingPreviewOverride`
- `LTXVAudioVAEEncode` ★核心
- `SetNode`
- `GetImageSize`
- `ResizeImageMaskNode`
- `SetNode`
- `GetNode`
- `RandomNoise`
- `VAELoader`
- `VAELoaderKJ`
- `TrimAudioDuration`
- `INTConstant`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `DualCLIPLoader`
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `PathchSageAttentionKJ`
- `LTX2AttentionTunerPatch`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `JoinStrings`
- `LTXVChunkFeedForward`
- `UNETLoader` ★核心
- `SetNode`
- `GetNode`
- `MelBandRoFormerSampler` ★核心
- `LTXVConditioning`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `VAEDecode` ★核心
- `SetNode`
- `LayerUtility: PurgeVRAM`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly` ★核心
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `MelBandRoFormerModelLoader`
- `PrimitiveFloat`
- `LatentUpscaleModelLoader`
- `ModelSamplingSD3`
- `LTX2_NAG`
- `INTConstant`
- `SetNode`
- `VHS_VideoCombine`
- `GetNode`
- `LTXVImgToVideoInplaceKJ`
- `SetNode`
- `ImageResizeKJv2`
- `LTXVPreprocess`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SimpleCalculatorKJ`
- `SimpleCalculatorKJ`
- `SetNode`
- `ComfySwitchNode`
- `SetNode`
- `SetNode`
- `TrimAudioDuration`
- `ImageResizeKJv2`
- `SimpleCalculatorKJ`
- `GetNode`
- `SetNode`
- `SetNode`
- `INTConstant`
- `GetNode`
- `GetNode`
- `SimpleCalculatorKJ`
- `PrimitiveFloat`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LoadAudio`
- `INTConstant`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心

## 知识

覆盖率 **49%**（54/110）

**有卡**：`SolidMask`、`LTXVConcatAVLatent`、`BasicScheduler`、`KSamplerSelect`、`CFGGuider`、`SetLatentNoiseMask`、`LTX2SamplingPreviewOverride`、`LTXVAudioVAEEncode`、`GetImageSize`、`ResizeImageMaskNode`、`RandomNoise`、`VAELoader`、`VAELoaderKJ`、`TrimAudioDuration`、`INTConstant`、`DualCLIPLoader`、`SamplerCustomAdvanced`、`PathchSageAttentionKJ`、`LTX2AttentionTunerPatch`、`LayerUtility: PurgeVRAM`、`JoinStrings`、`LTXVChunkFeedForward`、`UNETLoader`、`MelBandRoFormerSampler`、`LTXVConditioning`、`VAEDecode`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LoraLoaderModelOnly`、`EmptyLTXVLatentVideo`、`MelBandRoFormerModelLoader`、`LatentUpscaleModelLoader`、`ModelSamplingSD3`、`LTX2_NAG`、`VHS_VideoCombine`、`LTXVImgToVideoInplaceKJ`、`ImageResizeKJv2`、`LTXVPreprocess`、`SimpleCalculatorKJ`、`LoadImage`、`LoadAudio`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect

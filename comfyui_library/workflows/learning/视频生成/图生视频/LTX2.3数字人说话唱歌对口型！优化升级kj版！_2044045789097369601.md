---
key: 视频生成/图生视频/LTX2.3数字人说话唱歌对口型！优化升级kj版！_2044045789097369601.json
name: LTX2.3数字人说话唱歌对口型！优化升级kj版！_2044045789097369601.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2044045789097369601.json
hash: 68041a1a20d828b5
coverage: 0.486486
learned_at: 2026-10-15 22:36:35
nodes: [SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, SolidMask, GetNode, SetNode, GetNode, GetNode, SetNode, SetNode, LTXVConcatAVLatent, SetNode, SetNode, SetNode, BasicScheduler, SetNode, KSamplerSelect, GetNode, CFGGuider, GetNode, SetNode, SetLatentNoiseMask, GetNode, LTX2SamplingPreviewOverride, LTXVAudioVAEEncode, SetNode, SimpleCalculatorKJ, SetNode, GetImageSize, ResizeImageMaskNode, SetNode, SetNode, GetNode, TrimAudioDuration, SetNode, SimpleCalculatorKJ, RandomNoise, VAELoader, VAELoaderKJ, ComfySwitchNode, SetNode, SetNode, SetNode, INTConstant, GetNode, TrimAudioDuration, GetNode, INTConstant, INTConstant, GetNode, GetNode, ImageResizeKJv2, GetNode, SetNode, SetNode, DualCLIPLoader, SetNode, SetNode, SetNode, VAELoader, ImageResizeKJv2, VHS_VideoCombine, SamplerCustomAdvanced, PathchSageAttentionKJ, LTX2AttentionTunerPatch, LayerUtility: PurgeVRAM, GetNode, GetNode, LTXVPreprocess, PrimitiveStringMultiline, JoinStrings, CLIPTextEncode, LTXVChunkFeedForward, UNETLoader, SetNode, GetNode, GetNode, GetNode, SimpleCalculatorKJ, GetNode, MelBandRoFormerSampler, LTXVConditioning, SetNode, SimpleCalculatorKJ, GetNode, SetNode, GetNode, VAEDecode, SetNode, LayerUtility: PurgeVRAM, LTXVCropGuides, LTXVSeparateAVLatent, LoraLoaderModelOnly, EmptyLTXVLatentVideo, INTConstant, PrimitiveFloat, MelBandRoFormerModelLoader, Note, LoadAudio, INTConstant, LTXVImgToVideoInplaceKJ, LTX2_NAG, PrimitiveStringMultiline, CLIPTextEncode, PrimitiveFloat, LatentUpscaleModelLoader, ModelSamplingSD3, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX2.3数字人说话唱歌对口型！优化升级kj版！_2044045789097369601.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2044045789097369601.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（111 个）：
- `SetNode`
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
- `SimpleCalculatorKJ`
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
- `SetNode`
- `SetNode`
- `INTConstant`
- `GetNode`
- `TrimAudioDuration`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `SetNode`
- `SetNode`
- `DualCLIPLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `VAELoader`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `SamplerCustomAdvanced` ★核心
- `PathchSageAttentionKJ`
- `LTX2AttentionTunerPatch`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `GetNode`
- `LTXVPreprocess`
- `PrimitiveStringMultiline`
- `JoinStrings`
- `CLIPTextEncode` ★核心
- `LTXVChunkFeedForward`
- `UNETLoader` ★核心
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
- `SetNode`
- `LayerUtility: PurgeVRAM`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly` ★核心
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `PrimitiveFloat`
- `MelBandRoFormerModelLoader`
- `Note`
- `LoadAudio`
- `INTConstant`
- `LTXVImgToVideoInplaceKJ`
- `LTX2_NAG`
- `PrimitiveStringMultiline`
- `CLIPTextEncode` ★核心
- `PrimitiveFloat`
- `LatentUpscaleModelLoader`
- `ModelSamplingSD3`
- `LoadImage`

## 知识

覆盖率 **49%**（54/111）

**有卡**：`SolidMask`、`LTXVConcatAVLatent`、`BasicScheduler`、`KSamplerSelect`、`CFGGuider`、`SetLatentNoiseMask`、`LTX2SamplingPreviewOverride`、`LTXVAudioVAEEncode`、`SimpleCalculatorKJ`、`GetImageSize`、`ResizeImageMaskNode`、`TrimAudioDuration`、`RandomNoise`、`VAELoader`、`VAELoaderKJ`、`INTConstant`、`ImageResizeKJv2`、`DualCLIPLoader`、`VHS_VideoCombine`、`SamplerCustomAdvanced`、`PathchSageAttentionKJ`、`LTX2AttentionTunerPatch`、`LayerUtility: PurgeVRAM`、`LTXVPreprocess`、`JoinStrings`、`CLIPTextEncode`、`LTXVChunkFeedForward`、`UNETLoader`、`MelBandRoFormerSampler`、`LTXVConditioning`、`VAEDecode`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LoraLoaderModelOnly`、`EmptyLTXVLatentVideo`、`MelBandRoFormerModelLoader`、`LoadAudio`、`LTXVImgToVideoInplaceKJ`、`LTX2_NAG`、`LatentUpscaleModelLoader`、`ModelSamplingSD3`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect

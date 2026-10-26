---
key: 数字人/数字人/LTX2.3视频改口型加强版 视频生视频 数字人复刻短视频 复刻克隆数字人形象说话_2060596774003367937.json
name: LTX2.3视频改口型加强版 视频生视频 数字人复刻短视频 复刻克隆数字人形象说话_2060596774003367937
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.3视频改口型加强版 视频生视频 数字人复刻短视频 复刻克隆数字人形象说话_2060596774003367937.json
hash: 005d7c6023063881
coverage: 0.524096
learned_at: 2026-10-26 01:56:11
nodes: [LTXVConditioning, SamplerCustomAdvanced, RandomNoise, CFGGuider, KSamplerSelect, BasicScheduler, SetNode, SetNode, GetNode, GetNode, GetNode, RandomNoise, GetNode, LTXVLatentUpsampler, LTXVSeparateAVLatent, LTXVConcatAVLatent, SamplerCustomAdvanced, SetNode, SetNode, LTXVPreprocess, SetNode, GetNode, GetNode, GetImageRangeFromBatch, GetNode, SetNode, SetNode, SetNode, SetNode, VAELoader, LatentUpscaleModelLoader, VAELoaderKJ, SetNode, VAELoader, ManualSigmas, VHS_VideoInfo, SimpleCalculatorKJ, GetNode, GetImageSizeAndCount, GetNode, ImageResizeKJv2, ModelSamplingSD3, VAEEncode, GetNode, GetNode, PrimitiveBoolean, SetNode, GetNode, GetNode, GetNode, SetNode, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, GetNode, GetImageRangeFromBatch, VAEEncode, LTXVCropGuides, PrimitiveFloat, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, MelBandRoFormerModelLoader, MaskToImage, GetImageRangeFromBatch, ResizeImageMaskNode, LTXVImgToVideoInplace, LTXVConcatAVLatent, GetNode, GetNode, easy showAnything, SimpleCalculatorKJ, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, LTX2SamplingPreviewOverride, SetNode, LTX2_NAG, ManualSigmas, Reroute, ResizeImagesByLongerEdge, GetNode, GetNode, GetNode, ResizeImageMaskNode, LTXVSetVideoLatentNoiseMasks, SetNode, SetNode, GetImageSizeAndCount, SetNode, SetNode, LTXVAudioVideoMask, LTXVEmptyLatentAudio, GetNode, LTXVPreprocessMasks, TrimAudioDuration, SetNode, ComfyMathExpression, SetNode, SetNode, SetNode, SetLatentNoiseMask, MelBandRoFormerSampler, GetNode, LTXVAudioVAEDecode, LTXVAddLatentGuide, Float to Int, GetNode, GetNode, LayerUtility: PurgeVRAM, VAEDecode, SetNode, KSamplerSelect, SetNode, LTXVCropGuides, GetNode, easy showAnything, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, SetNode, CFGGuider, GetNode, GetNode, LTXVAudioVAEEncode, SolidMask, SetNode, GetNode, GetNode, LayerUtility: PurgeVRAM, LTXAVTextEncoderLoader, LazySwitchKJ, ResizeImageMaskNode, INTConstant, PrimitiveFloat, easy sam3ModelLoader, INTConstant, SetNode, ResizeImagesByLongerEdge, BlockifyMask, GetNode, GetNode, LTXVImgToVideoInplace, UNETLoader, PathchSageAttentionKJ, LTX2MemoryEfficientSageAttentionPatch, LTX2AttentionTunerPatch, SetNode, GetNode, LTXVSeparateAVLatent, LoraLoaderModelOnly, LoraLoaderModelOnly, easy sam3VideoSegmentation, PrimitiveStringMultiline, VHS_VideoCombine, INTConstant, VHS_LoadVideo, LoadAudio]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 数字人/数字人/LTX2.3视频改口型加强版 视频生视频 数字人复刻短视频 复刻克隆数字人形象说话_2060596774003367937.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.3视频改口型加强版 视频生视频 数字人复刻短视频 复刻克隆数字人形象说话_2060596774003367937.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（166 个）：
- `LTXVConditioning`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `SetNode`
- `LTXVPreprocess`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VAELoader`
- `LatentUpscaleModelLoader`
- `VAELoaderKJ`
- `SetNode`
- `VAELoader`
- `ManualSigmas`
- `VHS_VideoInfo`
- `SimpleCalculatorKJ`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJv2`
- `ModelSamplingSD3`
- `VAEEncode` ★核心
- `GetNode`
- `GetNode`
- `PrimitiveBoolean`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `GetNode`
- `GetImageRangeFromBatch`
- `VAEEncode` ★核心
- `LTXVCropGuides`
- `PrimitiveFloat`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `MelBandRoFormerModelLoader`
- `MaskToImage`
- `GetImageRangeFromBatch`
- `ResizeImageMaskNode`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `SimpleCalculatorKJ`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTX2SamplingPreviewOverride`
- `SetNode`
- `LTX2_NAG`
- `ManualSigmas`
- `Reroute`
- `ResizeImagesByLongerEdge`
- `GetNode`
- `GetNode`
- `GetNode`
- `ResizeImageMaskNode`
- `LTXVSetVideoLatentNoiseMasks`
- `SetNode`
- `SetNode`
- `GetImageSizeAndCount`
- `SetNode`
- `SetNode`
- `LTXVAudioVideoMask`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `LTXVPreprocessMasks`
- `TrimAudioDuration`
- `SetNode`
- `ComfyMathExpression`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetLatentNoiseMask`
- `MelBandRoFormerSampler` ★核心
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `LTXVAddLatentGuide`
- `Float to Int`
- `GetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `SetNode`
- `KSamplerSelect` ★核心
- `SetNode`
- `LTXVCropGuides`
- `GetNode`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `CFGGuider`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `SetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `LTXAVTextEncoderLoader`
- `LazySwitchKJ`
- `ResizeImageMaskNode`
- `INTConstant`
- `PrimitiveFloat`
- `easy sam3ModelLoader`
- `INTConstant`
- `SetNode`
- `ResizeImagesByLongerEdge`
- `BlockifyMask`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoInplace`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `LTX2MemoryEfficientSageAttentionPatch`
- `LTX2AttentionTunerPatch`
- `SetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy sam3VideoSegmentation`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `INTConstant`
- `VHS_LoadVideo`
- `LoadAudio`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **52%**（87/166）

**有卡**：`LTXVConditioning`、`SamplerCustomAdvanced`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`BasicScheduler`、`LTXVLatentUpsampler`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`LTXVPreprocess`、`GetImageRangeFromBatch`、`VAELoader`、`LatentUpscaleModelLoader`、`VAELoaderKJ`、`ManualSigmas`、`VHS_VideoInfo`、`SimpleCalculatorKJ`、`GetImageSizeAndCount`、`ImageResizeKJv2`、`ModelSamplingSD3`、`VAEEncode`、`PrimitiveBoolean`、`ComfyMathExpression`、`LTXVCropGuides`、`MelBandRoFormerModelLoader`、`MaskToImage`、`ResizeImageMaskNode`、`LTXVImgToVideoInplace`、`LTX2SamplingPreviewOverride`、`LTX2_NAG`、`ResizeImagesByLongerEdge`、`LTXVSetVideoLatentNoiseMasks`、`LTXVAudioVideoMask`、`LTXVEmptyLatentAudio`、`LTXVPreprocessMasks`、`TrimAudioDuration`、`SetLatentNoiseMask`、`MelBandRoFormerSampler`、`LTXVAudioVAEDecode`、`LTXVAddLatentGuide`、`Float to Int`、`LayerUtility: PurgeVRAM`、`VAEDecode`、`CLIPTextEncode`、`LTXVAudioVAEEncode`、`SolidMask`、`LTXAVTextEncoderLoader`、`LazySwitchKJ`、`INTConstant`、`easy sam3ModelLoader`、`BlockifyMask`、`UNETLoader`、`PathchSageAttentionKJ`、`LTX2MemoryEfficientSageAttentionPatch`、`LTX2AttentionTunerPatch`、`LoraLoaderModelOnly`、`easy sam3VideoSegmentation`、`VHS_VideoCombine`、`VHS_LoadVideo`、`LoadAudio`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

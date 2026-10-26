---
key: 数字人/数字人/LTX2.3上传视频改口型！B站艾橘溪_2047297756296908801.json
name: LTX2.3上传视频改口型！B站艾橘溪_2047297756296908801
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.3上传视频改口型！B站艾橘溪_2047297756296908801.json
hash: 954b7503635edd6c
coverage: 0.512195
learned_at: 2026-10-26 01:55:56
nodes: [LTXVConditioning, SamplerCustomAdvanced, RandomNoise, CFGGuider, KSamplerSelect, BasicScheduler, SetNode, SetNode, GetNode, GetNode, GetNode, RandomNoise, GetNode, LTXVLatentUpsampler, LTXVSeparateAVLatent, LTXVConcatAVLatent, SamplerCustomAdvanced, SetNode, SetNode, LTXVPreprocess, SetNode, GetNode, GetImageRangeFromBatch, GetNode, SetNode, SetNode, SetNode, SetNode, VAELoader, LatentUpscaleModelLoader, VAELoaderKJ, SetNode, VAELoader, ManualSigmas, VHS_VideoInfo, SimpleCalculatorKJ, GetNode, GetImageSizeAndCount, GetNode, VAEEncode, GetNode, GetNode, PrimitiveBoolean, SetNode, GetNode, SetNode, GetNode, GetImageRangeFromBatch, VAEEncode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, MelBandRoFormerModelLoader, MaskToImage, GetImageRangeFromBatch, ResizeImageMaskNode, GetNode, GetNode, easy showAnything, SimpleCalculatorKJ, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, LTX2SamplingPreviewOverride, SetNode, ManualSigmas, Reroute, ResizeImagesByLongerEdge, GetNode, GetNode, GetNode, ResizeImageMaskNode, LTXVSetVideoLatentNoiseMasks, SetNode, SetNode, GetImageSizeAndCount, LTXVAudioVideoMask, LTXVEmptyLatentAudio, GetNode, LTXVPreprocessMasks, TrimAudioDuration, SetNode, ComfyMathExpression, SetNode, SetNode, SetLatentNoiseMask, MelBandRoFormerSampler, GetNode, LTXVAudioVAEDecode, LTXVAddLatentGuide, GetNode, GetNode, LayerUtility: PurgeVRAM, VAEDecode, KSamplerSelect, SetNode, LTXVCropGuides, GetNode, easy showAnything, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, SetNode, CFGGuider, GetNode, GetNode, LTXVAudioVAEEncode, SolidMask, SetNode, GetNode, VHS_VideoCombine, LazySwitchKJ, ResizeImageMaskNode, INTConstant, PrimitiveStringMultiline, easy sam3ModelLoader, INTConstant, SetNode, ResizeImagesByLongerEdge, BlockifyMask, GetNode, GetNode, MarkdownNote, GetNode, LTXVSeparateAVLatent, easy sam3VideoSegmentation, VHS_LoadVideo, UNETLoader, LTXAVTextEncoderLoader, GetNode, LoadAudio, ModelSamplingSD3, SetNode, GetNode, ComfyMathExpression, ComfyMathExpression, GetNode, LTXVImgToVideoInplace, LTX2_NAG, LTXVConcatAVLatent, PrimitiveFloat, SetNode, SetNode, LTXVImgToVideoInplace, PrimitiveFloat, SetNode, Float to Int, LTXVCropGuides, ComfyMathExpression, GetNode, SetNode, ImageResizeKJv2, PathchSageAttentionKJ, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, INTConstant]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 数字人/数字人/LTX2.3上传视频改口型！B站艾橘溪_2047297756296908801.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.3上传视频改口型！B站艾橘溪_2047297756296908801.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（164 个）：
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
- `VAEEncode` ★核心
- `GetNode`
- `GetNode`
- `PrimitiveBoolean`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `VAEEncode` ★核心
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
- `LTXVAudioVideoMask`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `LTXVPreprocessMasks`
- `TrimAudioDuration`
- `SetNode`
- `ComfyMathExpression`
- `SetNode`
- `SetNode`
- `SetLatentNoiseMask`
- `MelBandRoFormerSampler` ★核心
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `LTXVAddLatentGuide`
- `GetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
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
- `VHS_VideoCombine`
- `LazySwitchKJ`
- `ResizeImageMaskNode`
- `INTConstant`
- `PrimitiveStringMultiline`
- `easy sam3ModelLoader`
- `INTConstant`
- `SetNode`
- `ResizeImagesByLongerEdge`
- `BlockifyMask`
- `GetNode`
- `GetNode`
- `MarkdownNote`
- `GetNode`
- `LTXVSeparateAVLatent`
- `easy sam3VideoSegmentation`
- `VHS_LoadVideo`
- `UNETLoader` ★核心
- `LTXAVTextEncoderLoader`
- `GetNode`
- `LoadAudio`
- `ModelSamplingSD3`
- `SetNode`
- `GetNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `GetNode`
- `LTXVImgToVideoInplace`
- `LTX2_NAG`
- `LTXVConcatAVLatent`
- `PrimitiveFloat`
- `SetNode`
- `SetNode`
- `LTXVImgToVideoInplace`
- `PrimitiveFloat`
- `SetNode`
- `Float to Int`
- `LTXVCropGuides`
- `ComfyMathExpression`
- `GetNode`
- `SetNode`
- `ImageResizeKJv2`
- `PathchSageAttentionKJ`
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly` ★核心
- `INTConstant`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **51%**（84/164）

**有卡**：`LTXVConditioning`、`SamplerCustomAdvanced`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`BasicScheduler`、`LTXVLatentUpsampler`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`LTXVPreprocess`、`GetImageRangeFromBatch`、`VAELoader`、`LatentUpscaleModelLoader`、`VAELoaderKJ`、`ManualSigmas`、`VHS_VideoInfo`、`SimpleCalculatorKJ`、`GetImageSizeAndCount`、`VAEEncode`、`PrimitiveBoolean`、`MelBandRoFormerModelLoader`、`MaskToImage`、`ResizeImageMaskNode`、`LTX2SamplingPreviewOverride`、`ResizeImagesByLongerEdge`、`LTXVSetVideoLatentNoiseMasks`、`LTXVAudioVideoMask`、`LTXVEmptyLatentAudio`、`LTXVPreprocessMasks`、`TrimAudioDuration`、`ComfyMathExpression`、`SetLatentNoiseMask`、`MelBandRoFormerSampler`、`LTXVAudioVAEDecode`、`LTXVAddLatentGuide`、`LayerUtility: PurgeVRAM`、`VAEDecode`、`LTXVCropGuides`、`CLIPTextEncode`、`LTXVAudioVAEEncode`、`SolidMask`、`VHS_VideoCombine`、`LazySwitchKJ`、`INTConstant`、`easy sam3ModelLoader`、`BlockifyMask`、`easy sam3VideoSegmentation`、`VHS_LoadVideo`、`UNETLoader`、`LTXAVTextEncoderLoader`、`LoadAudio`、`ModelSamplingSD3`、`LTXVImgToVideoInplace`、`LTX2_NAG`、`Float to Int`、`ImageResizeKJv2`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

---
key: 视频生成/图生视频/LTX-2.3首尾帧+语音数字人_2036654957595725826.json
name: LTX-2.3首尾帧+语音数字人_2036654957595725826.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX-2.3首尾帧+语音数字人_2036654957595725826.json
hash: ec20543d1fa1c4d1
coverage: 0.503759
learned_at: 2026-10-15 22:35:52
nodes: [GetNode, SimpleCalculatorKJ, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTX2_NAG, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVConcatAVLatent, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, LTXVSeparateAVLatent, CFGGuider, LTXVSeparateAVLatent, CFGGuider, LTXVLatentUpsampler, ImageScaleBy, ImageScaleBy, ImageConcatMulti, GetNode, GetNode, ImageScaleBy, ImageConcatMulti, VHS_VideoCombine, GetNode, SetNode, GetNode, SetNode, GetNode, LTXVScheduler, ManualSigmas, ManualSigmas, SetNode, Fast Groups Bypasser (rgthree), KSamplerSelect, KSamplerSelect, SamplerCustomAdvanced, ResizeImagesByLongerEdge, LTXVPreprocess, GetImageSize, RandomNoise, LTXVPreprocess, SamplerCustomAdvanced, LTXVAudioVAEDecode, LTXVImgToVideoInplace, SetNode, GetNode, VAELoader, GetNode, EmptyLTXVLatentVideo, INTConstant, GetNode, GetNode, GetNode, GetNode, RandomNoise, DualCLIPLoader, VAELoaderKJ, VAELoader, INTConstant, SimpleCalculatorKJ, SimpleCalculatorKJ, MelBandRoFormerModelLoader, SetNode, GetNode, SetNode, SetNode, SetNode, LoadImage, GetNode, UNETLoader, LTX2SamplingPreviewOverride, SetNode, ImageResizeKJv2, SetNode, ComfySwitchNode, ManualSigmas, SetNode, LoraLoaderModelOnly, GetNode, GetNode, GetNode, SetNode, SetLatentNoiseMask, SolidMask, TrimAudioDuration, GetNode, SetNode, INTConstant, PrimitiveFloat, CLIPTextEncode, CLIPTextEncode, MelBandRoFormerSampler, SetNode, LTXVAudioVAEEncode, AudioInfo, SetNode, GetNode, GetNode, ImageResizeKJv2, SetNode, VAEDecodeTiled, VHS_VideoCombine, GetNode, GetNode, LTXVImgToVideoInplaceKJ, ImageScaleBy, ResizeImagesByLongerEdge, LoadImage, LoadAudio, SetNode, GetNode, LTXVConcatAVLatent, LTXVConditioning, SetNode, LatentUpscaleModelLoader, LTXVChunkFeedForward, SetNode, LTXVEmptyLatentAudio]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX-2.3首尾帧+语音数字人_2036654957595725826.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2036654957595725826.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（133 个）：
- `GetNode`
- `SimpleCalculatorKJ`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTX2_NAG`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `CFGGuider`
- `LTXVSeparateAVLatent`
- `CFGGuider`
- `LTXVLatentUpsampler` ★核心
- `ImageScaleBy`
- `ImageScaleBy`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `ImageScaleBy`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `LTXVScheduler`
- `ManualSigmas`
- `ManualSigmas`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `GetImageSize`
- `RandomNoise`
- `LTXVPreprocess`
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVImgToVideoInplace`
- `SetNode`
- `GetNode`
- `VAELoader`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VAELoader`
- `INTConstant`
- `SimpleCalculatorKJ`
- `SimpleCalculatorKJ`
- `MelBandRoFormerModelLoader`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `GetNode`
- `UNETLoader` ★核心
- `LTX2SamplingPreviewOverride`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `ComfySwitchNode`
- `ManualSigmas`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetLatentNoiseMask`
- `SolidMask`
- `TrimAudioDuration`
- `GetNode`
- `SetNode`
- `INTConstant`
- `PrimitiveFloat`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `MelBandRoFormerSampler` ★核心
- `SetNode`
- `LTXVAudioVAEEncode` ★核心
- `AudioInfo`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoInplaceKJ`
- `ImageScaleBy`
- `ResizeImagesByLongerEdge`
- `LoadImage`
- `LoadAudio`
- `SetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `SetNode`
- `LatentUpscaleModelLoader`
- `LTXVChunkFeedForward`
- `SetNode`
- `LTXVEmptyLatentAudio` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **50%**（67/133）

**有卡**：`SimpleCalculatorKJ`、`LTX2_NAG`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`CFGGuider`、`LTXVLatentUpsampler`、`ImageScaleBy`、`ImageConcatMulti`、`VHS_VideoCombine`、`LTXVScheduler`、`ManualSigmas`、`KSamplerSelect`、`SamplerCustomAdvanced`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`GetImageSize`、`RandomNoise`、`LTXVAudioVAEDecode`、`LTXVImgToVideoInplace`、`VAELoader`、`EmptyLTXVLatentVideo`、`INTConstant`、`DualCLIPLoader`、`VAELoaderKJ`、`MelBandRoFormerModelLoader`、`LoadImage`、`UNETLoader`、`LTX2SamplingPreviewOverride`、`ImageResizeKJv2`、`LoraLoaderModelOnly`、`SetLatentNoiseMask`、`SolidMask`、`TrimAudioDuration`、`CLIPTextEncode`、`MelBandRoFormerSampler`、`LTXVAudioVAEEncode`、`AudioInfo`、`VAEDecodeTiled`、`LTXVImgToVideoInplaceKJ`、`LoadAudio`、`LTXVConditioning`、`LatentUpscaleModelLoader`、`LTXVChunkFeedForward`、`LTXVEmptyLatentAudio`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

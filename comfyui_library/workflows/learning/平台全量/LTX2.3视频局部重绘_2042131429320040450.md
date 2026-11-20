---
key: 平台全量/LTX2.3视频局部重绘_2042131429320040450.json
name: LTX2.3视频局部重绘_2042131429320040450
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX2.3视频局部重绘_2042131429320040450.json
hash: 810aa64c6225b575
coverage: 0.47561
learned_at: 2026-11-14 00:38:56
nodes: [GetNode, GetImageSize, SolidMask, LTXVAudioVAEEncode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, VAEDecode, SetNode, LTXVEmptyLatentAudio, SetNode, GetNode, GetNode, LTXVConditioning, SimpleCalculatorKJ, GetNode, GetNode, GetNode, GetNode, GetNode, CreateVideo, GetNode, GetNode, GetNode, SamplerCustomAdvanced, GetNode, LTXVConcatAVLatent, GetNode, LTXVAudioVAEDecode, GetNode, GetNode, LTXVConcatAVLatent, SetLatentNoiseMask, Note, LTXVSeparateAVLatent, SetNode, TrimAudioDuration, Note, GetNode, GetNode, ImageConcanate, GetNode, GetNode, CreateVideo, ImageConcanate, MaskToImage, Reroute, GetNode, GetNode, GetNode, GetNode, EmptyAudio, GetNode, VAEEncode, GetNode, GetNode, GetNode, GetNode, easy cleanGpuUsed, CFGGuider, KSamplerSelect, GetNode, ImageConcanate, ImageConcanate, SetNode, GrowMaskWithBlur, GetNode, easy cleanGpuUsed, ImageScaleBy, MarkdownNote, SetNode, SetNode, SetNode, SetNode, RecordAudio, GetNode, GetNode, GetNode, GetNode, Sam2Segmentation, GetImageRangeFromBatch, ImageCompositeFromMaskBatch+, GetNode, SetNode, GetImageSize+, EmptyImage, ImageInvert, VHS_VideoCombine, GetNode, SamplerCustomAdvanced, LTXVLatentUpsampler, LTXVCropGuides, SetNode, GetNode, GetNode, VAEDecodeTiled, RandomNoise, SetNode, SetNode, BasicScheduler, ImageScaleBy, SetNode, VHS_VideoCombine, SaveVideo, CLIPTextEncode, Note, BlockifyMask, CFGGuider, KSamplerSelect, ManualSigmas, LTXVSeparateAVLatent, GetNode, SetNode, ManualSigmas, GetNode, LTX2SamplingPreviewOverride, RandomNoise, SetNode, SetNode, LTXVCropGuides, SetNode, SetNode, SetNode, DualCLIPLoader, LatentUpscaleModelLoader, LTX2SamplingPreviewOverride, SaveVideo, GetNode, SetNode, SetNode, LoadAudio, INTConstant, INTConstant, PrimitiveFloat, SetNode, PrimitiveFloat, LTXVAudioVAELoader, CheckpointLoaderSimple, VHS_VideoCombine, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, SetNode, DownloadAndLoadSAM2Model, GetNode, GetNode, LTXVAddGuideMulti, LTXVAddGuideMulti, VHS_VideoCombine, SetNode, CLIPTextEncode, GetNode, GetNode, SetNode, LTXVPreprocess, ImageScaleBy, ImageResizeKJv2, VHS_LoadVideo, PointsEditor]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 24, "width": 97}
---

# 平台全量/LTX2.3视频局部重绘_2042131429320040450.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX2.3视频局部重绘_2042131429320040450.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（164 个）：
- `GetNode`
- `GetImageSize`
- `SolidMask`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `SetNode`
- `LTXVEmptyLatentAudio` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVConditioning`
- `SimpleCalculatorKJ`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CreateVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `SetLatentNoiseMask`
- `Note`
- `LTXVSeparateAVLatent`
- `SetNode`
- `TrimAudioDuration`
- `Note`
- `GetNode`
- `GetNode`
- `ImageConcanate`
- `GetNode`
- `GetNode`
- `CreateVideo`
- `ImageConcanate`
- `MaskToImage`
- `Reroute`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyAudio`
- `GetNode`
- `VAEEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `GetNode`
- `ImageConcanate`
- `ImageConcanate`
- `SetNode`
- `GrowMaskWithBlur`
- `GetNode`
- `easy cleanGpuUsed`
- `ImageScaleBy`
- `MarkdownNote`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `RecordAudio`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Sam2Segmentation`
- `GetImageRangeFromBatch`
- `ImageCompositeFromMaskBatch+`
- `GetNode`
- `SetNode`
- `GetImageSize+`
- `EmptyImage`
- `ImageInvert`
- `VHS_VideoCombine`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVCropGuides`
- `SetNode`
- `GetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `RandomNoise`
- `SetNode`
- `SetNode`
- `BasicScheduler`
- `ImageScaleBy`
- `SetNode`
- `VHS_VideoCombine`
- `SaveVideo`
- `CLIPTextEncode` ★核心
- `Note`
- `BlockifyMask`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `GetNode`
- `SetNode`
- `ManualSigmas`
- `GetNode`
- `LTX2SamplingPreviewOverride`
- `RandomNoise`
- `SetNode`
- `SetNode`
- `LTXVCropGuides`
- `SetNode`
- `SetNode`
- `SetNode`
- `DualCLIPLoader`
- `LatentUpscaleModelLoader`
- `LTX2SamplingPreviewOverride`
- `SaveVideo`
- `GetNode`
- `SetNode`
- `SetNode`
- `LoadAudio`
- `INTConstant`
- `INTConstant`
- `PrimitiveFloat`
- `SetNode`
- `PrimitiveFloat`
- `LTXVAudioVAELoader`
- `CheckpointLoaderSimple` ★核心
- `VHS_VideoCombine`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `DownloadAndLoadSAM2Model`
- `GetNode`
- `GetNode`
- `LTXVAddGuideMulti`
- `LTXVAddGuideMulti`
- `VHS_VideoCombine`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `LTXVPreprocess`
- `ImageScaleBy`
- `ImageResizeKJv2`
- `VHS_LoadVideo`
- `PointsEditor`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **48%**（78/164）

**有卡**：`GetImageSize`、`SolidMask`、`LTXVAudioVAEEncode`、`VAEDecode`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`SimpleCalculatorKJ`、`CreateVideo`、`SamplerCustomAdvanced`、`LTXVConcatAVLatent`、`LTXVAudioVAEDecode`、`SetLatentNoiseMask`、`LTXVSeparateAVLatent`、`TrimAudioDuration`、`ImageConcanate`、`MaskToImage`、`EmptyAudio`、`VAEEncode`、`easy cleanGpuUsed`、`CFGGuider`、`KSamplerSelect`、`GrowMaskWithBlur`、`ImageScaleBy`、`RecordAudio`、`Sam2Segmentation`、`GetImageRangeFromBatch`、`ImageCompositeFromMaskBatch+`、`GetImageSize+`、`EmptyImage`、`ImageInvert`、`VHS_VideoCombine`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`VAEDecodeTiled`、`RandomNoise`、`BasicScheduler`、`SaveVideo`、`CLIPTextEncode`、`BlockifyMask`、`ManualSigmas`、`LTX2SamplingPreviewOverride`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`LoadAudio`、`INTConstant`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`DownloadAndLoadSAM2Model`、`LTXVAddGuideMulti`、`LTXVPreprocess`、`ImageResizeKJv2`、`VHS_LoadVideo`、`PointsEditor`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、LTXVLatentUpsampler、SamplerCustomAdvanced

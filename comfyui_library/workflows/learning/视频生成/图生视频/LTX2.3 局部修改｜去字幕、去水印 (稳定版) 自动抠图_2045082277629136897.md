---
key: 视频生成/图生视频/LTX2.3 局部修改｜去字幕、去水印 (稳定版) 自动抠图_2045082277629136897.json
name: LTX2.3 局部修改｜去字幕、去水印 (稳定版) 自动抠图_2045082277629136897.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2045082277629136897.json
hash: a7e55016a05dcfcf
coverage: 0.808081
learned_at: 2026-10-15 22:36:45
nodes: [LTXVCropGuides, BasicScheduler, LTXVLatentUpsampler, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVCropGuides, ImageConcanate, ImageConcanate, SetLatentNoiseMask, PrimitiveFloat, LTXVPreprocess, VHS_VideoCombine, ImageScaleBy, LTXVAudioVAEEncode, EmptyImage, BlockifyMask, GrowMaskWithBlur, SolidMask, LTXVSeparateAVLatent, VAEDecode, ImageConcanate, ImageScaleBy, ManualSigmas, KSamplerSelect, CFGGuider, VHS_VideoCombine, PrimitiveFloat, KSamplerSelect, ImageScaleBy, GetImageSize, Note, Note, CFGGuider, Note, SimpleCalculatorKJ, RandomNoise, SeedGenerator, easy cleanGpuUsed, Note, Note, VAEDecodeTiled, VHS_VideoCombine, LTXVAudioVAEDecode, VHS_VideoCombine, Note, ImageInvert, GetImageSize+, ImageCompositeFromMaskBatch+, MaskToImage, Note, Note, Note, TrimAudioDuration, LoadAudio, Note, GetImageRangeFromBatch, Sam2Segmentation, EmptyAudio, CLIPTextEncode, Note, Note, LTXVEmptyLatentAudio, LTXVConcatAVLatent, LTXVConditioning, easy cleanGpuUsed, INTConstant, CLIPTextEncode, ImageResizeKJv2, easy cleanGpuUsed, SamplerCustomAdvanced, easy cleanGpuUsed, SamplerCustomAdvanced, LoraLoaderModelOnly, easy cleanGpuUsed, VHS_LoadVideo, PreviewImage, DownloadAndLoadSAM2Model, LTXAVTextEncoderLoader, LTXVAudioVAELoader, CheckpointLoaderSimple, VAEEncode, LatentUpscaleModelLoader, CreateVideo, SaveVideo, CreateVideo, PointsEditor, Note, Note, RandomNoise, ImageConcanate, LTX2SamplingPreviewOverride, LTX2SamplingPreviewOverride, SaveVideo, LTXVAddGuideMulti, LTXVAddGuideMulti, easy cleanGpuUsed, Note, LoraLoaderModelOnly, Note]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 24, "width": 97}
---

# 视频生成/图生视频/LTX2.3 局部修改｜去字幕、去水印 (稳定版) 自动抠图_2045082277629136897.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2045082277629136897.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（99 个）：
- `LTXVCropGuides`
- `BasicScheduler`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `ImageConcanate`
- `ImageConcanate`
- `SetLatentNoiseMask`
- `PrimitiveFloat`
- `LTXVPreprocess`
- `VHS_VideoCombine`
- `ImageScaleBy`
- `LTXVAudioVAEEncode` ★核心
- `EmptyImage`
- `BlockifyMask`
- `GrowMaskWithBlur`
- `SolidMask`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `ImageConcanate`
- `ImageScaleBy`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `VHS_VideoCombine`
- `PrimitiveFloat`
- `KSamplerSelect` ★核心
- `ImageScaleBy`
- `GetImageSize`
- `Note`
- `Note`
- `CFGGuider`
- `Note`
- `SimpleCalculatorKJ`
- `RandomNoise`
- `SeedGenerator`
- `easy cleanGpuUsed`
- `Note`
- `Note`
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`
- `Note`
- `ImageInvert`
- `GetImageSize+`
- `ImageCompositeFromMaskBatch+`
- `MaskToImage`
- `Note`
- `Note`
- `Note`
- `TrimAudioDuration`
- `LoadAudio`
- `Note`
- `GetImageRangeFromBatch`
- `Sam2Segmentation`
- `EmptyAudio`
- `CLIPTextEncode` ★核心
- `Note`
- `Note`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `easy cleanGpuUsed`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `easy cleanGpuUsed`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `SamplerCustomAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy cleanGpuUsed`
- `VHS_LoadVideo`
- `PreviewImage`
- `DownloadAndLoadSAM2Model`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `CheckpointLoaderSimple` ★核心
- `VAEEncode` ★核心
- `LatentUpscaleModelLoader`
- `CreateVideo`
- `SaveVideo`
- `CreateVideo`
- `PointsEditor`
- `Note`
- `Note`
- `RandomNoise`
- `ImageConcanate`
- `LTX2SamplingPreviewOverride`
- `LTX2SamplingPreviewOverride`
- `SaveVideo`
- `LTXVAddGuideMulti`
- `LTXVAddGuideMulti`
- `easy cleanGpuUsed`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `Note`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **81%**（80/99）

**有卡**：`LTXVCropGuides`、`BasicScheduler`、`LTXVLatentUpsampler`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`ImageConcanate`、`SetLatentNoiseMask`、`LTXVPreprocess`、`VHS_VideoCombine`、`ImageScaleBy`、`LTXVAudioVAEEncode`、`EmptyImage`、`BlockifyMask`、`GrowMaskWithBlur`、`SolidMask`、`VAEDecode`、`ManualSigmas`、`KSamplerSelect`、`CFGGuider`、`GetImageSize`、`SimpleCalculatorKJ`、`RandomNoise`、`SeedGenerator`、`easy cleanGpuUsed`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`ImageInvert`、`GetImageSize+`、`ImageCompositeFromMaskBatch+`、`MaskToImage`、`TrimAudioDuration`、`LoadAudio`、`GetImageRangeFromBatch`、`Sam2Segmentation`、`EmptyAudio`、`CLIPTextEncode`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`INTConstant`、`ImageResizeKJv2`、`SamplerCustomAdvanced`、`LoraLoaderModelOnly`、`VHS_LoadVideo`、`DownloadAndLoadSAM2Model`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`VAEEncode`、`LatentUpscaleModelLoader`、`CreateVideo`、`SaveVideo`、`PointsEditor`、`LTX2SamplingPreviewOverride`、`LTXVAddGuideMulti`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

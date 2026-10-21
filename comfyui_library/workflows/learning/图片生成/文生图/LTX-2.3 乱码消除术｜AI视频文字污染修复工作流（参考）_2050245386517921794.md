---
key: 图片生成/文生图/LTX-2.3 乱码消除术｜AI视频文字污染修复工作流（参考）_2050245386517921794.json
name: LTX-2.3 乱码消除术｜AI视频文字污染修复工作流（参考）_2050245386517921794
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/LTX-2.3 乱码消除术｜AI视频文字污染修复工作流（参考）_2050245386517921794.json
hash: 582b6a764a6baa1f
coverage: 0.757576
learned_at: 2026-10-21 02:53:27
nodes: [LTXVAudioVAEEncode, SamplerCustomAdvanced, LTXVConditioning, LTXVConcatAVLatent, Reroute, Note, SetNode, CFGGuider, Note, Note, Note, SetNode, LTXVSeparateAVLatent, easy showAnything, VAEDecode, LTXVCropGuides, BasicScheduler, KSamplerSelect, VAELoaderKJ, LTXVEmptyLatentAudio, SetLatentNoiseMask, MarkdownNote, CLIPTextEncode, CLIPTextEncode, easy cleanGpuUsed, ImageFromBatch+, PreviewImage, LoraLoaderModelOnly, GetImageSize, SolidMask, EmptyAudio, VAEEncode, MathExpression|pysssss, UnetLoaderGGUF, VAELoaderKJ, BatchImagesNode, BatchImagesNode, LoraLoaderModelOnly, VHS_VideoCombine, VHS_VideoCombine, LTXVAddGuideMulti, DualCLIPLoaderGGUF, PrimitiveFloat, Note, RandomNoise, VHS_DuplicateMasks, easy showAnything, LTXVPreprocess, PreviewImage, GetImageSize+, ImageCompositeFromMaskBatch+, GetImageRangeFromBatch, easy cleanGpuUsed, BlockifyMask, INTConstant, EmptyImage, ImageFromBatch+, ImageResizeKJv2, Image Batch, VHS_LoadVideo, LoadImage, Int, PrimitiveFloat, JWImageResizeByLongerSide, PrimitiveInt, GetImageSize]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 97}
---

# 图片生成/文生图/LTX-2.3 乱码消除术｜AI视频文字污染修复工作流（参考）_2050245386517921794.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/LTX-2.3 乱码消除术｜AI视频文字污染修复工作流（参考）_2050245386517921794.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（66 个）：
- `LTXVAudioVAEEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVConditioning`
- `LTXVConcatAVLatent`
- `Reroute`
- `Note`
- `SetNode`
- `CFGGuider`
- `Note`
- `Note`
- `Note`
- `SetNode`
- `LTXVSeparateAVLatent`
- `easy showAnything`
- `VAEDecode` ★核心
- `LTXVCropGuides`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `VAELoaderKJ`
- `LTXVEmptyLatentAudio` ★核心
- `SetLatentNoiseMask`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `ImageFromBatch+`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `GetImageSize`
- `SolidMask`
- `EmptyAudio`
- `VAEEncode` ★核心
- `MathExpression|pysssss`
- `UnetLoaderGGUF` ★核心
- `VAELoaderKJ`
- `BatchImagesNode`
- `BatchImagesNode`
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LTXVAddGuideMulti`
- `DualCLIPLoaderGGUF`
- `PrimitiveFloat`
- `Note`
- `RandomNoise`
- `VHS_DuplicateMasks`
- `easy showAnything`
- `LTXVPreprocess`
- `PreviewImage`
- `GetImageSize+`
- `ImageCompositeFromMaskBatch+`
- `GetImageRangeFromBatch`
- `easy cleanGpuUsed`
- `BlockifyMask`
- `INTConstant`
- `EmptyImage`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `Image Batch`
- `VHS_LoadVideo`
- `LoadImage`
- `Int`
- `PrimitiveFloat`
- `JWImageResizeByLongerSide`
- `PrimitiveInt`
- `GetImageSize`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **76%**（50/66）

**有卡**：`LTXVAudioVAEEncode`、`SamplerCustomAdvanced`、`LTXVConditioning`、`LTXVConcatAVLatent`、`CFGGuider`、`LTXVSeparateAVLatent`、`VAEDecode`、`LTXVCropGuides`、`BasicScheduler`、`KSamplerSelect`、`VAELoaderKJ`、`LTXVEmptyLatentAudio`、`SetLatentNoiseMask`、`CLIPTextEncode`、`easy cleanGpuUsed`、`ImageFromBatch+`、`LoraLoaderModelOnly`、`GetImageSize`、`SolidMask`、`EmptyAudio`、`VAEEncode`、`MathExpression|pysssss`、`UnetLoaderGGUF`、`BatchImagesNode`、`VHS_VideoCombine`、`LTXVAddGuideMulti`、`DualCLIPLoaderGGUF`、`RandomNoise`、`VHS_DuplicateMasks`、`LTXVPreprocess`、`GetImageSize+`、`ImageCompositeFromMaskBatch+`、`GetImageRangeFromBatch`、`BlockifyMask`、`INTConstant`、`EmptyImage`、`ImageResizeKJv2`、`Image Batch`、`VHS_LoadVideo`、`LoadImage`、`Int`、`JWImageResizeByLongerSide`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent

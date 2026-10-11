---
key: 视频生成/文生视频/小云雀无痕抹字｜LTX2.3 去水印去字幕视频修复工作流_2053501073624715266.json
name: 小云雀无痕抹字｜LTX2.3 去水印去字幕视频修复工作流_2053501073624715266
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/小云雀无痕抹字｜LTX2.3 去水印去字幕视频修复工作流_2053501073624715266.json
hash: b550b1058925fed4
coverage: 0.647059
learned_at: 2026-10-11 19:49:48
nodes: [LTXVAudioVAEEncode, SamplerCustomAdvanced, LTXVConditioning, LTXVConcatAVLatent, Reroute, Note, SetNode, CFGGuider, Note, Note, Note, SetNode, LTXVSeparateAVLatent, easy showAnything, VAEDecode, LTXVCropGuides, BasicScheduler, KSamplerSelect, VAELoaderKJ, LTXVEmptyLatentAudio, SetLatentNoiseMask, MarkdownNote, CLIPTextEncode, easy cleanGpuUsed, PreviewImage, LoraLoaderModelOnly, GetImageSize, SolidMask, EmptyAudio, UnetLoaderGGUF, VAELoaderKJ, LoraLoaderModelOnly, VHS_VideoCombine, DualCLIPLoaderGGUF, RandomNoise, easy showAnything, ImageFromBatch+, LTXVAddGuideMulti, JWMaskResize, VHS_VideoCombine, CLIPTextEncode, PrimitiveFloat, VAEEncode, LoadImage, ImageResizeKJv2, JWMaskResize, VHS_VideoInfoLoaded, PrimitiveFloat, JWImageResizeByLongerSide, GetImageSize+, ImageCompositeFromMaskBatch+, EmptyImage, BlockifyMask, easy cleanGpuUsed, VHS_DuplicateMasks, Int, INTConstant, LoadImage, LoadImage, PreviewImage, ImageFromBatch+, ImageFromBatch+, Image Batch, easy ifElse, MaskAdd_UTK, VHS_LoadVideo, PrimitiveInt, LoadImage]
patterns: []
missing: [Image Batch, ImageCompositeFromMaskBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, easy cleanGpuUsed, easy cleanGpuUsed, GetImageSize+]
parameters: {"batch_size": 1, "height": 24, "width": 97}
discoveries: [次要节点 `Image Batch` 知识库中没有该节点类型的任何知识, 次要节点 `ImageCompositeFromMaskBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/小云雀无痕抹字｜LTX2.3 去水印去字幕视频修复工作流_2053501073624715266.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/小云雀无痕抹字｜LTX2.3 去水印去字幕视频修复工作流_2053501073624715266.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（68 个）：
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
- `easy cleanGpuUsed`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `GetImageSize`
- `SolidMask`
- `EmptyAudio`
- `UnetLoaderGGUF` ★核心
- `VAELoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `DualCLIPLoaderGGUF`
- `RandomNoise`
- `easy showAnything`
- `ImageFromBatch+`
- `LTXVAddGuideMulti`
- `JWMaskResize`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `PrimitiveFloat`
- `VAEEncode` ★核心
- `LoadImage`
- `ImageResizeKJv2`
- `JWMaskResize`
- `VHS_VideoInfoLoaded`
- `PrimitiveFloat`
- `JWImageResizeByLongerSide`
- `GetImageSize+`
- `ImageCompositeFromMaskBatch+`
- `EmptyImage`
- `BlockifyMask`
- `easy cleanGpuUsed`
- `VHS_DuplicateMasks`
- `Int`
- `INTConstant`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `Image Batch`
- `easy ifElse`
- `MaskAdd_UTK`
- `VHS_LoadVideo`
- `PrimitiveInt`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **65%**（44/68）

**有卡**：`LTXVAudioVAEEncode`、`SamplerCustomAdvanced`、`LTXVConditioning`、`LTXVConcatAVLatent`、`CFGGuider`、`LTXVSeparateAVLatent`、`VAEDecode`、`LTXVCropGuides`、`BasicScheduler`、`KSamplerSelect`、`VAELoaderKJ`、`LTXVEmptyLatentAudio`、`SetLatentNoiseMask`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`GetImageSize`、`SolidMask`、`EmptyAudio`、`UnetLoaderGGUF`、`VHS_VideoCombine`、`DualCLIPLoaderGGUF`、`RandomNoise`、`LTXVAddGuideMulti`、`JWMaskResize`、`VAEEncode`、`LoadImage`、`ImageResizeKJv2`、`VHS_VideoInfoLoaded`、`JWImageResizeByLongerSide`、`EmptyImage`、`BlockifyMask`、`VHS_DuplicateMasks`、`Int`、`INTConstant`、`MaskAdd_UTK`、`VHS_LoadVideo`

**缺卡**（8）：`Image Batch`、`ImageCompositeFromMaskBatch+`、`ImageFromBatch+`、`ImageFromBatch+`、`ImageFromBatch+`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`GetImageSize+`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent

## 学习发现

- 次要节点 `Image Batch` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageCompositeFromMaskBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明

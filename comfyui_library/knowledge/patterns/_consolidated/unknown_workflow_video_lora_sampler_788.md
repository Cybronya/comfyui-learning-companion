---
name: unknown_workflow_video_lora_sampler_788
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7615
common_nodes: [BasicScheduler, BlockifyMask, CFGGuider, CLIPTextEncode, DualCLIPLoaderGGUF, EmptyAudio, EmptyImage, GetImageSize, GetImageSize+, INTConstant, Image Batch, ImageCompositeFromMaskBatch+, ImageFromBatch+, ImageResizeKJv2, Int, JWImageResizeByLongerSide, KSamplerSelect, LTXVAddGuideMulti, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveFloat, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SolidMask, UnetLoaderGGUF, VAEDecode, VAEEncode, VAELoaderKJ, VHS_DuplicateMasks, VHS_LoadVideo, VHS_VideoCombine, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/LTX-2.3 乱码消除术｜AI视频文字污染修复工作流（参考）_2050245386517921794.json, 视频生成/文生视频/小云雀无痕抹字｜LTX2.3 去水印去字幕视频修复工作流_2053501073624715266.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_788

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/LTX-2.3 乱码消除术｜AI视频文字污染修复工作流（参考）_2050245386517921794.json、视频生成/文生视频/小云雀无痕抹字｜LTX2.3 去水印去字幕视频修复工作流_2053501073624715266.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `BlockifyMask`
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoaderGGUF`
- `EmptyAudio`
- `EmptyImage`
- `GetImageSize`
- `GetImageSize+`
- `INTConstant`
- `Image Batch`
- `ImageCompositeFromMaskBatch+`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `Int`
- `JWImageResizeByLongerSide`
- `KSamplerSelect`
- `LTXVAddGuideMulti`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SolidMask`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAEEncode`
- `VAELoaderKJ`
- `VHS_DuplicateMasks`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `BatchImagesNode` —— 1/2 个有
- `GetImageRangeFromBatch` —— 1/2 个有
- `JWMaskResize` —— 1/2 个有
- `LTXVPreprocess` —— 1/2 个有
- `MaskAdd_UTK` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `VHS_VideoInfoLoaded` —— 1/2 个有
- `easy ifElse` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | - | 2 | 100% |
| 高度 | 24 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 24，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

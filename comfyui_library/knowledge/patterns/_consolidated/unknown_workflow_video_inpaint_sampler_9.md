---
name: unknown_workflow_video_inpaint_sampler_9
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9725
common_nodes: [BboxDetectorCombined_v2, CompressImages, Evaluate Integers, GrowMaskWithBlur, INPAINT_InpaintWithModel, INPAINT_LoadInpaintModel, ImageCompositeMasked, LayerUtility: ImageScaleByAspectRatio V2, MaskListToMaskBatch, MaskToImage, SolidMask, UltralyticsDetectorProvider, VHS_LoadVideo, VHS_SelectFilename, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoBlockSwap, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoMiniMaxRemoverEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader, easy imageBatchToImageList, easy int, easy seed]
problems: []
missing: []
members: [平台全量/即梦视频水印去除_1990943866142535682.json, 视频生成/图生视频/全能视频S水印去除(支持新_旧水印_长视频)_1981220170108665857.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_sampler_9

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/即梦视频水印去除_1990943866142535682.json、视频生成/图生视频/全能视频S水印去除(支持新_旧水印_长视频)_1981220170108665857.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 2 个 workflow 都包含：
- `BboxDetectorCombined_v2`
- `CompressImages`
- `Evaluate Integers`
- `GrowMaskWithBlur`
- `INPAINT_InpaintWithModel`
- `INPAINT_LoadInpaintModel`
- `ImageCompositeMasked`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MaskListToMaskBatch`
- `MaskToImage`
- `SolidMask`
- `UltralyticsDetectorProvider`
- `VHS_LoadVideo`
- `VHS_SelectFilename`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanVideoBlockSwap`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoMiniMaxRemoverEmbeds`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVAELoader`
- `easy imageBatchToImageList`
- `easy int`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `ImpactSEGSConcat` —— 1/2 个有
- `MaskToSEGS` —— 1/2 个有
- `SegsToCombinedMask` —— 1/2 个有
- `VHS_DuplicateMasks` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

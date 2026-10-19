---
name: unknown_workflow_video_sampler_vae_173
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.686
common_nodes: [DF_Integer, GetImageRangeFromBatch, ImageCompositeMasked, ImageResizeKJv2, ImageToMask, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskToImage, PreviewImage, RepeatImageBatch, SimpleMath+, SolidMask, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoDecode, WanVideoEncode, WanVideoMiniMaxRemoverEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader, easy batchAnything, easy compare, easy forLoopEnd, easy forLoopStart, easy ifElse, easy showAnything]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, SimpleMath+, WanVideoMiniMaxRemoverEmbeds, easy batchAnything, easy compare, easy forLoopEnd, easy forLoopStart]
members: [视频生成/图生视频/1974664225505325058.json, 视频生成/文生视频/1974664225505325058.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_173

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1974664225505325058.json、视频生成/文生视频/1974664225505325058.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：69%

## 共有节点

全部 2 个 workflow 都包含：
- `DF_Integer`
- `GetImageRangeFromBatch`
- `ImageCompositeMasked`
- `ImageResizeKJv2`
- `ImageToMask`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `RepeatImageBatch`
- `SimpleMath+`
- `SolidMask`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoMiniMaxRemoverEmbeds`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy batchAnything`
- `easy compare`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy ifElse`
- `easy showAnything`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、SimpleMath+、WanVideoMiniMaxRemoverEmbeds、easy batchAnything、easy compare
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

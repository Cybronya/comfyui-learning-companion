---
name: unknown_workflow_video_sampler_vae_213
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.596
common_nodes: [GetImageRangeFromBatch, GetNode, ImageCompositeMasked, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, MaskToImage, PreviewBridge, PreviewImage, SetNode, SolidMask, VHS_DuplicateMasks, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoDecode, WanVideoEncode, WanVideoMiniMaxRemoverEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy compare, easy ifElse, easy imageScaleDownToSize, easy imageSize]
problems: []
missing: []
members: [平台全量/MiniMax Remover视频去水印_1992098448864333826.json, 平台全量/自适应遮罩MMRemover视频去水印_1991749115197616129.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_213

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/MiniMax Remover视频去水印_1992098448864333826.json、平台全量/自适应遮罩MMRemover视频去水印_1991749115197616129.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：60%

## 共有节点

全部 2 个 workflow 都包含：
- `GetImageRangeFromBatch`
- `GetNode`
- `ImageCompositeMasked`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadWanVideoT5TextEncoder`
- `MaskToImage`
- `PreviewBridge`
- `PreviewImage`
- `SetNode`
- `SolidMask`
- `VHS_DuplicateMasks`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoMiniMaxRemoverEmbeds`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy compare`
- `easy ifElse`
- `easy imageScaleDownToSize`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `ImageBatchCopy` —— 1/2 个有
- `ImageBatchJoin` —— 1/2 个有
- `ImageFromBatch` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `ImageToMask` —— 1/2 个有
- `JWImageBatchCount` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `ShowAnything|Mie` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

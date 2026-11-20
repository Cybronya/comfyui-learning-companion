---
name: unknown_workflow_video_sampler_vae_111
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9786
common_nodes: [GrowMaskWithBlur, ImageCompositeMasked, ImageResizeKJv2, LoadWanVideoT5TextEncoder, MaskToImage, SolidMask, VHS_LoadVideo, VHS_VideoCombine, WanVideoDecode, WanVideoEncode, WanVideoMiniMaxRemoverEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/Aiwood-minimaxRemover视频擦除工作流_1935023318582140929.json, 平台全量/Wan2_1-MiniMaxRemover_1_3B_fp16_1935610651618508801.json, 平台全量/视频去文字水印(自动)_1963592678699143169.json, 平台全量/视频去文字水印_1948020479476019202.json, 平台全量/视频擦除工作流_1935234048040304642.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_111

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/Aiwood-minimaxRemover视频擦除工作流_1935023318582140929.json、平台全量/Wan2_1-MiniMaxRemover_1_3B_fp16_1935610651618508801.json、平台全量/视频去文字水印(自动)_1963592678699143169.json、平台全量/视频去文字水印_1948020479476019202.json、平台全量/视频擦除工作流_1935234048040304642.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 5 个 workflow 都包含：
- `GrowMaskWithBlur`
- `ImageCompositeMasked`
- `ImageResizeKJv2`
- `LoadWanVideoT5TextEncoder`
- `MaskToImage`
- `SolidMask`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoMiniMaxRemoverEmbeds`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadSAM2Model` —— 4/5 个有
- `MaskPreview+` —— 4/5 个有
- `PointsEditor` —— 4/5 个有
- `Sam2Segmentation` —— 4/5 个有
- `easy imageRemBg` —— 4/5 个有
- `GetImageSizeAndCount` —— 2/5 个有
- `ImageFromBatch+` —— 2/5 个有
- `LayerMask: SegmentAnythingUltra V2` —— 2/5 个有
- `Masks Combine Regions` —— 2/5 个有
- `MathExpression|pysssss` —— 2/5 个有
- `PrimitiveInt` —— 2/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `LayerMask: LoadSegmentAnythingModels` —— 1/5 个有
- `LayerMask: SegmentAnythingUltra V3` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/5 个有
- `WanVideoTorchCompileSettings` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

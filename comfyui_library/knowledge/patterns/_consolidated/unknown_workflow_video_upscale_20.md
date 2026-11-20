---
name: unknown_workflow_video_upscale_20
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.833333
common_nodes: [GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), ImageBatchGet, ImageToMask, ImageUpscaleWithModel, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: LaMa, LayerUtility: PurgeVRAM V2, LoadImage, MaskToImage, PreviewImage, SAMModelLoader (segment anything), UpscaleModelLoader, VHS_DuplicateMasks, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [平台全量/极速图像水印擦除无损文字_2043539460645724161.json, 平台全量/视频去水印全自动识别_1964637341849669633.json, 视频生成/图生视频/视频去水印全自动识别_1982367593988276225.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_20

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/极速图像水印擦除无损文字_2043539460645724161.json、平台全量/视频去水印全自动识别_1964637341849669633.json、视频生成/图生视频/视频去水印全自动识别_1982367593988276225.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `GroundingDinoModelLoader (segment anything)`
- `GroundingDinoSAMSegment (segment anything)`
- `ImageBatchGet`
- `ImageToMask`
- `ImageUpscaleWithModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: LaMa`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `SAMModelLoader (segment anything)`
- `UpscaleModelLoader`
- `VHS_DuplicateMasks`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `GetImageRangeFromBatch` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `GrowMaskWithBlur` —— 2/3 个有
- `PreviewBridge` —— 2/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

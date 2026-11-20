---
name: unknown_workflow_video_78
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.766
common_nodes: [BboxDetectorCombined_v2, GetImageSizeAndCount, GetNode, GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), ImageBatch, ImageToMask, MaskListToMaskBatch, MaskPreview, MaskToImage, Masks Add, PreviewBridge, PreviewImage, ResizeMask, SAMModelLoader (segment anything), SetNode, SolidMask, UltralyticsDetectorProvider, VHS_LoadVideo, VHS_SelectImages, VHS_SelectMasks, VHS_VideoCombine, VHS_VideoInfo, easy cleanGpuUsed, easy ifElse, easy imageBatchToImageList, easy isMaskEmpty]
problems: []
missing: []
members: [平台全量/去水印-视频去水印-支持全能视频S动态水印-支持抖音_豆包水印-极速版_1987456709083992065.json, 平台全量/去水印-视频去水印-进阶版-支持抖音_豆包水印-支持全能视频S动态水印_2025002312934105089.json, 平台全量/响响-视频去水印_2006362344586223618.json, 平台全量/视频动态去水印_1992202473029038082.json, 平台全量/视频去水印_2030914657971605506.json]
source: knowledge_consolidation
---

# unknown_workflow_video_78

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/去水印-视频去水印-支持全能视频S动态水印-支持抖音_豆包水印-极速版_1987456709083992065.json、平台全量/去水印-视频去水印-进阶版-支持抖音_豆包水印-支持全能视频S动态水印_2025002312934105089.json、平台全量/响响-视频去水印_2006362344586223618.json、平台全量/视频动态去水印_1992202473029038082.json、平台全量/视频去水印_2030914657971605506.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 5 个 workflow 都包含：
- `BboxDetectorCombined_v2`
- `GetImageSizeAndCount`
- `GetNode`
- `GroundingDinoModelLoader (segment anything)`
- `GroundingDinoSAMSegment (segment anything)`
- `ImageBatch`
- `ImageToMask`
- `MaskListToMaskBatch`
- `MaskPreview`
- `MaskToImage`
- `Masks Add`
- `PreviewBridge`
- `PreviewImage`
- `ResizeMask`
- `SAMModelLoader (segment anything)`
- `SetNode`
- `SolidMask`
- `UltralyticsDetectorProvider`
- `VHS_LoadVideo`
- `VHS_SelectImages`
- `VHS_SelectMasks`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `easy cleanGpuUsed`
- `easy ifElse`
- `easy imageBatchToImageList`
- `easy isMaskEmpty`

**可变部分**（部分 workflow 才有）：
- `DiffuEraserLoader` —— 3/5 个有
- `DiffuEraserSampler` —— 3/5 个有
- `FlashVSRNode` —— 3/5 个有
- `GetImageRangeFromBatch` —— 3/5 个有
- `ImageConcanate` —— 3/5 个有
- `LayerUtility: LaMa` —— 3/5 个有
- `SimpleMath+` —— 3/5 个有
- `easy boolean` —— 3/5 个有
- `Fast Groups Muter (rgthree)` —— 2/5 个有
- `ImageResizeKJ` —— 2/5 个有
- `ImpactSwitch` —— 2/5 个有
- `WanVideoImageResizeToClosest` —— 2/5 个有
- `WatermarkDetector` —— 2/5 个有
- `WatermarkDetectorLoader` —— 2/5 个有
- `easy int` —— 2/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

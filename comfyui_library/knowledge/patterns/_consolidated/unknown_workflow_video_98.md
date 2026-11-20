---
name: unknown_workflow_video_98
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.903
common_nodes: [BboxDetectorSEGS, CropMask, FaceRestoreCFWithModel, FaceRestoreModelLoader, ImageComposite+, ImageCrop+, ImageListToImageBatch, ImageResize+, ImpactImageBatchToImageList, LayerColor: Brightness & Contrast, LoadImage, Mask Crop Region, MaskBlur+, PreviewImage, ReActorFaceSwap, SAMDetectorCombined, SAMLoader, UltralyticsDetectorProvider, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/Reactor视频换脸+SAM分割v1_2107472866123014146.json, 平台全量/reactor视频快速换脸（支持侧脸换脸）_1892122251351777282.json, 平台全量/最稳定！Reactor视频换脸_1916314329816170497.json, 视频生成/图生视频/旅拍机-淘汰-视频ReActor稳定版-SAM加载失败_2071227862950170625.json]
source: knowledge_consolidation
---

# unknown_workflow_video_98

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/Reactor视频换脸+SAM分割v1_2107472866123014146.json、平台全量/reactor视频快速换脸（支持侧脸换脸）_1892122251351777282.json、平台全量/最稳定！Reactor视频换脸_1916314329816170497.json、视频生成/图生视频/旅拍机-淘汰-视频ReActor稳定版-SAM加载失败_2071227862950170625.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `BboxDetectorSEGS`
- `CropMask`
- `FaceRestoreCFWithModel`
- `FaceRestoreModelLoader`
- `ImageComposite+`
- `ImageCrop+`
- `ImageListToImageBatch`
- `ImageResize+`
- `ImpactImageBatchToImageList`
- `LayerColor: Brightness & Contrast`
- `LoadImage`
- `Mask Crop Region`
- `MaskBlur+`
- `PreviewImage`
- `ReActorFaceSwap`
- `SAMDetectorCombined`
- `SAMLoader`
- `UltralyticsDetectorProvider`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GPENO Face Restoration` —— 1/4 个有
- `RHHiddenNodes` —— 1/4 个有
- `ReActorBuildFaceModel` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

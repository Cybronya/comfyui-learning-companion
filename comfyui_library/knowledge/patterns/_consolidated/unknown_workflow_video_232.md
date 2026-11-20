---
name: unknown_workflow_video_232
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.792
common_nodes: [DiffuEraserLoader, GroundingDinoModelLoader (segment anything), ImageBatchGet, ImageResizeKJ, ImageToMask, MaskToImage, Note _O, PreviewImage, RHHiddenNodes, RepeatImageBatch, SAMModelLoader (segment anything), VHS_DuplicateMasks, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, easy cleanGpuUsed]
problems: []
missing: []
members: [平台全量/视频全自动无损去水印-去除水印_2033843395117981698.json, 视频生成/图生视频/视频全自动无损去水印-去除水印_1977334580774621186.json]
source: knowledge_consolidation
---

# unknown_workflow_video_232

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/视频全自动无损去水印-去除水印_2033843395117981698.json、视频生成/图生视频/视频全自动无损去水印-去除水印_1977334580774621186.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `DiffuEraserLoader`
- `GroundingDinoModelLoader (segment anything)`
- `ImageBatchGet`
- `ImageResizeKJ`
- `ImageToMask`
- `MaskToImage`
- `Note _O`
- `PreviewImage`
- `RHHiddenNodes`
- `RepeatImageBatch`
- `SAMModelLoader (segment anything)`
- `VHS_DuplicateMasks`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `easy cleanGpuUsed`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

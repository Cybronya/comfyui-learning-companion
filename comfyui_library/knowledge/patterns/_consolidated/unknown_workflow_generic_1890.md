---
name: unknown_workflow_generic_1890
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.938
common_nodes: [CreateVideo, DA3_MultiViewPointCloud, DA3_SavePointCloud, DA3_ToMesh, DA3_ToPointCloud, DepthAnythingV3_MultiView, DepthAnything_V3, DownloadAndLoadDepthAnythingV3Model, Fast Groups Bypasser (rgthree), ImageBatchMulti, Label (rgthree), LoadImage, PreviewImage, SaveVideo, VHS_LoadVideo]
problems: []
missing: []
members: [平台全量/Depth Anything V3_3D重建 深度控制 点云生成_1999265925369036801.json, 平台全量/新节点Depth Anything V3，一键实现3D重建 + ControlNet深度控制！_1998728563337613314.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1890

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Depth Anything V3_3D重建 深度控制 点云生成_1999265925369036801.json、平台全量/新节点Depth Anything V3，一键实现3D重建 + ControlNet深度控制！_1998728563337613314.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `CreateVideo`
- `DA3_MultiViewPointCloud`
- `DA3_SavePointCloud`
- `DA3_ToMesh`
- `DA3_ToPointCloud`
- `DepthAnythingV3_MultiView`
- `DepthAnything_V3`
- `DownloadAndLoadDepthAnythingV3Model`
- `Fast Groups Bypasser (rgthree)`
- `ImageBatchMulti`
- `Label (rgthree)`
- `LoadImage`
- `PreviewImage`
- `SaveVideo`
- `VHS_LoadVideo`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 1/2 个有
- `VHS_VideoInfoLoaded` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

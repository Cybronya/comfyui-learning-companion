---
name: unknown_workflow_video_236
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.718
common_nodes: [BiRefNet_Hugo, ImageFromBatch+, ImageScaleBy, LayerMask: MaskBoxDetect, LayerUtility: ImageBlendAdvance V2, LoadImage, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [平台全量/视频添加小人_2011724459568275458.json, 平台全量/视频添加小小人_1960015433040605185.json]
source: knowledge_consolidation
---

# unknown_workflow_video_236

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/视频添加小人_2011724459568275458.json、平台全量/视频添加小小人_1960015433040605185.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：72%

## 共有节点

全部 2 个 workflow 都包含：
- `BiRefNet_Hugo`
- `ImageFromBatch+`
- `ImageScaleBy`
- `LayerMask: MaskBoxDetect`
- `LayerUtility: ImageBlendAdvance V2`
- `LoadImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `SaveImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

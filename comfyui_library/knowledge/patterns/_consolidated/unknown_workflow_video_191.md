---
name: unknown_workflow_video_191
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9445
common_nodes: [DownloadAndLoadSAM2Model, MaskToImage, PointsEditor, Sam2Segmentation, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoSource]
problems: []
missing: []
members: [平台全量/DiffuEraser生成视频遮罩_1919244433861316610.json, 平台全量/视频手动指定物体抠像_1967139227374903298.json]
source: knowledge_consolidation
---

# unknown_workflow_video_191

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/DiffuEraser生成视频遮罩_1919244433861316610.json、平台全量/视频手动指定物体抠像_1967139227374903298.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `DownloadAndLoadSAM2Model`
- `MaskToImage`
- `PointsEditor`
- `Sam2Segmentation`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoSource`

**可变部分**（部分 workflow 才有）：
- `GrowMask` —— 1/2 个有
- `ImageAndMaskPreview` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

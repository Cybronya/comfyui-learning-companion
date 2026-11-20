---
name: unknown_workflow_video_137
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.705
common_nodes: [CoordinatePlotter, DrawMaskOnImage, ImageConcatMulti, ImageFromBatch, PointsEditor, PreviewImage, PrimitiveInt, SeCModelLoader, SeCVideoSegmentation, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, easy showAnything]
problems: []
missing: []
members: [视频生成/文生视频/SecNodes+Sam2丝滑稳定视频遮罩V2 (切镜版)_1976951725854728193.json, 视频生成/文生视频/SecNodes视频遮罩提取_1977650345428045825.json]
source: knowledge_consolidation
---

# unknown_workflow_video_137

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/SecNodes+Sam2丝滑稳定视频遮罩V2 (切镜版)_1976951725854728193.json、视频生成/文生视频/SecNodes视频遮罩提取_1977650345428045825.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：70%

## 共有节点

全部 2 个 workflow 都包含：
- `CoordinatePlotter`
- `DrawMaskOnImage`
- `ImageConcatMulti`
- `ImageFromBatch`
- `PointsEditor`
- `PreviewImage`
- `PrimitiveInt`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `ImageFromBatch+` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `PDIMAGE_LongerSize` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

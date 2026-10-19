---
name: unknown_workflow_video_29
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.67225
common_nodes: [CoordinatePlotter, DrawMaskOnImage, ImageConcatMulti, ImageFromBatch, PointsEditor, PreviewImage, PrimitiveInt, SeCModelLoader, SeCVideoSegmentation, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, easy showAnything]
problems: []
missing: [ImageFromBatch+, LayerUtility: PurgeVRAM]
members: [视频生成/图生视频/1976951725854728193.json, 视频生成/文生视频/1976951725854728193.json, 视频生成/文生视频/1977650345428045825.json, 视频生成/文生视频/SecNodes视频遮罩提取_2072999508340154368.json]
source: knowledge_consolidation
---

# unknown_workflow_video_29

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1976951725854728193.json、视频生成/文生视频/1976951725854728193.json、视频生成/文生视频/1977650345428045825.json、视频生成/文生视频/SecNodes视频遮罩提取_2072999508340154368.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 4 个 workflow 都包含：
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
- `AddLabel` —— 2/4 个有
- `ImageConcanate` —— 2/4 个有
- `ImageFromBatch+` —— 2/4 个有
- `LayerUtility: PurgeVRAM` —— 2/4 个有
- `PDIMAGE_LongerSize` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：ImageFromBatch+、LayerUtility: PurgeVRAM

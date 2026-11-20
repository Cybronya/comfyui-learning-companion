---
name: unknown_workflow_video_99
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.767
common_nodes: [CoordinatePlotter, DrawMaskOnImage, ImageFromBatch, PointsEditor, PreviewImage, SeCModelLoader, SeCVideoSegmentation, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [平台全量/SEC最强视频分割工作流_1982793259560906753.json, 平台全量/SeC视频分割_2007264703705255937.json, 平台全量/SecNodes+Sam2丝滑稳定视频遮罩V1 (切镜版)_1977745964511416322.json, 视频生成/文生视频/SecNodes+Sam2丝滑稳定视频遮罩V2 (切镜版)_1976951725854728193.json]
source: knowledge_consolidation
---

# unknown_workflow_video_99

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/SEC最强视频分割工作流_1982793259560906753.json、平台全量/SeC视频分割_2007264703705255937.json、平台全量/SecNodes+Sam2丝滑稳定视频遮罩V1 (切镜版)_1977745964511416322.json、视频生成/文生视频/SecNodes+Sam2丝滑稳定视频遮罩V2 (切镜版)_1976951725854728193.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 4 个 workflow 都包含：
- `CoordinatePlotter`
- `DrawMaskOnImage`
- `ImageFromBatch`
- `PointsEditor`
- `PreviewImage`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `ImageFromBatch+` —— 2/4 个有
- `ImageStitch` —— 2/4 个有
- `LayerUtility: PurgeVRAM` —— 2/4 个有
- `MaskToImage` —— 2/4 个有
- `PrimitiveInt` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `PDIMAGE_LongerSize` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

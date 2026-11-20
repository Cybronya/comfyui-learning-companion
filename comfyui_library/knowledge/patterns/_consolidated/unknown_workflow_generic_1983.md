---
name: unknown_workflow_generic_1983
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [INTConstant, ImageFromBatch, SaveImage, VHS_LoadVideo]
problems: []
missing: []
members: [平台全量/视频蒙版_1993148270423851009.json, 平台全量/视频首尾帧提取_1954836386916515842.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1983

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/视频蒙版_1993148270423851009.json、平台全量/视频首尾帧提取_1954836386916515842.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `INTConstant`
- `ImageFromBatch`
- `SaveImage`
- `VHS_LoadVideo`

**可变部分**（部分 workflow 才有）：
- `PointsEditor` —— 1/2 个有
- `VHS_VideoInfo` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

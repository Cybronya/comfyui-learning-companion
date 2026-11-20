---
name: unknown_workflow_generic_735
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.6845
common_nodes: [LoadImage, SDPoseOODLoader, SDPoseOODProcessor, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/万能姿态图 SDPose_1988986163945934849.json, 图片生成/图生图/万能骨骼图 SDPose_1989359431509004289.json, 图片生成/图生图/动作提取+姿势提取+万能骨骼图 SDPose+全节点注释_2054183862510604289.json, 图片生成/图生图/生成骨骼图_2054638352711856130.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_735

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/万能姿态图 SDPose_1988986163945934849.json、图片生成/图生图/万能骨骼图 SDPose_1989359431509004289.json、图片生成/图生图/动作提取+姿势提取+万能骨骼图 SDPose+全节点注释_2054183862510604289.json、图片生成/图生图/生成骨骼图_2054638352711856130.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 4 个 workflow 都包含：
- `LoadImage`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `GroundingDinoModelLoader_SDPose` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `YOLOModelLoader` —— 3/4 个有
- `VHS_LoadVideo` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_generic_727
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.913
common_nodes: [GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), InvertMask, InvertMask (segment anything), LayerUtility: CropByMask, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SAMLoader, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/co 批量裁剪新2_2071504923543556097.json, 图片生成/图生图/co 批量裁剪新3_2071519463295508482.json, 图片生成/图生图/co裁剪1_2075961816714407937.json, 图片生成/图生图/co裁剪_2075131937269829633.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_727

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/co 批量裁剪新2_2071504923543556097.json、图片生成/图生图/co 批量裁剪新3_2071519463295508482.json、图片生成/图生图/co裁剪1_2075961816714407937.json、图片生成/图生图/co裁剪_2075131937269829633.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `GroundingDinoModelLoader (segment anything)`
- `GroundingDinoSAMSegment (segment anything)`
- `InvertMask`
- `InvertMask (segment anything)`
- `LayerUtility: CropByMask`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SAMLoader`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `GroupSwitcher` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_generic_558
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.913
common_nodes: [GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), InvertMask, InvertMask (segment anything), LayerUtility: CropByMask, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SAMLoader, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/co 批量裁剪新2_2071504923543556097.json, 图片生成/图生图/co 批量裁剪新3_2071519463295508482.json, 图片生成/图生图/co裁剪1_2075961816714407937.json, 图片生成/图生图/co裁剪_2075131937269829633.json, 平台全量/cocoon 裁剪1_2071114194623225858.json, 平台全量/co裁剪新_2117807875505606657.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_558

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/co 批量裁剪新2_2071504923543556097.json、图片生成/图生图/co 批量裁剪新3_2071519463295508482.json、图片生成/图生图/co裁剪1_2075961816714407937.json、图片生成/图生图/co裁剪_2075131937269829633.json、平台全量/cocoon 裁剪1_2071114194623225858.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
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
- `GroupSwitcher` —— 3/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

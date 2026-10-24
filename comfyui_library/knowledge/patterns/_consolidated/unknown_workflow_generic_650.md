---
name: unknown_workflow_generic_650
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 1
common_nodes: [LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LoadImage, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/RMBG-2抠图+修边_2063215332772372482.json, 图片生成/图生图/万能急速抠图_2082289989509017601.json, 图片生成/图生图/万能急速抠图_2082295216089952258.json, 图片生成/图生图/抠图_1995412855149277186.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_650

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/RMBG-2抠图+修边_2063215332772372482.json、图片生成/图生图/万能急速抠图_2082289989509017601.json、图片生成/图生图/万能急速抠图_2082295216089952258.json、图片生成/图生图/抠图_1995412855149277186.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 4 个 workflow 都包含：
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LoadImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `GrowMaskWithBlur` —— 1/4 个有
- `ImageCombineAlpha_UTK` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

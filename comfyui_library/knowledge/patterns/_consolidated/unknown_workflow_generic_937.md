---
name: unknown_workflow_generic_937
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.781667
common_nodes: [GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), ImageBatchGet, ImageToMask, LayerUtility: LaMa, LoadImage, MaskToImage, PreviewImage, SAMModelLoader (segment anything), SaveImage]
problems: []
missing: []
members: [图片生成/图生图/图像去水印+放大_1942480718805274626.json, 图片生成/图生图/图像去水印（全自动）_1915291152122318850.json, 图片生成/图生图/图片去水印-稳定高效版_1931584333021118465.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_937

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/图像去水印+放大_1942480718805274626.json、图片生成/图生图/图像去水印（全自动）_1915291152122318850.json、图片生成/图生图/图片去水印-稳定高效版_1931584333021118465.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 3 个 workflow 都包含：
- `GroundingDinoModelLoader (segment anything)`
- `GroundingDinoSAMSegment (segment anything)`
- `ImageBatchGet`
- `ImageToMask`
- `LayerUtility: LaMa`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `SAMModelLoader (segment anything)`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `SetNode` —— 2/3 个有
- `VHS_DuplicateMasks` —— 2/3 个有
- `GetNode` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `PMRF` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

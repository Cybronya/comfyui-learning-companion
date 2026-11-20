---
name: unknown_workflow_generic_901
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.68775
common_nodes: [GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), ImageBatchGet, LayerUtility: LaMa, LoadImage, MaskToImage, PreviewImage, SAMModelLoader (segment anything), SaveImage]
problems: []
missing: []
members: [图片生成/图生图/图像去水印+放大_1942480718805274626.json, 图片生成/图生图/图像去水印（全自动）_1915291152122318850.json, 图片生成/图生图/图片去水印-稳定高效版_1931584333021118465.json, 平台全量/Advance 基础低配去水印工作流_2032850446993334274.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_901

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/图像去水印+放大_1942480718805274626.json、图片生成/图生图/图像去水印（全自动）_1915291152122318850.json、图片生成/图生图/图片去水印-稳定高效版_1931584333021118465.json、平台全量/Advance 基础低配去水印工作流_2032850446993334274.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 4 个 workflow 都包含：
- `GroundingDinoModelLoader (segment anything)`
- `GroundingDinoSAMSegment (segment anything)`
- `ImageBatchGet`
- `LayerUtility: LaMa`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `SAMModelLoader (segment anything)`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `ImageToMask` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `VHS_DuplicateMasks` —— 3/4 个有
- `GetNode` —— 2/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `PMRF` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

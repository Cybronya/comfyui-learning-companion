---
name: unknown_workflow_generic_854
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.831
common_nodes: [FaceAnalysisModels, FaceEmbedDistance, InsertAnythingImageProcessor, InsertAnythingInferencer, InsertAnythingLoader, LayerMask: PersonMaskUltra V2, LoadImage, MaskOption, PreviewImage, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/Nunchaku_InsertAnything换脸_1922491323624935426.json, 图片生成/图生图/快速换脸+一致性｜insertAnything 修图_1922611624191082498.json, 图片生成/图生图/换脸工作流高清出图nsertAnything_1964261096339197954.json, 平台全量/最全案例-InsertAnything极速万物迁移(换脸_换装_换鞋_换人等)_1921844906262740993.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_854

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Nunchaku_InsertAnything换脸_1922491323624935426.json、图片生成/图生图/快速换脸+一致性｜insertAnything 修图_1922611624191082498.json、图片生成/图生图/换脸工作流高清出图nsertAnything_1964261096339197954.json、平台全量/最全案例-InsertAnything极速万物迁移(换脸_换装_换鞋_换人等)_1921844906262740993.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
- `FaceAnalysisModels`
- `FaceEmbedDistance`
- `InsertAnythingImageProcessor`
- `InsertAnythingInferencer`
- `InsertAnythingLoader`
- `LayerMask: PersonMaskUltra V2`
- `LoadImage`
- `MaskOption`
- `PreviewImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 2/4 个有
- `ImageConcatMulti` —— 2/4 个有
- `PreviewMask_` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `LayerMask: LoadSegmentAnythingModels` —— 1/4 个有
- `LayerMask: SegmentAnythingUltra V3` —— 1/4 个有
- `Text Multiline` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

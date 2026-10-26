---
name: unknown_workflow_generic_972
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.821
common_nodes: [FaceAnalysisModels, FaceEmbedDistance, InsertAnythingImageProcessor, InsertAnythingInferencer, InsertAnythingLoader, LayerMask: PersonMaskUltra V2, LoadImage, MaskOption, PreviewImage, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/Nunchaku_InsertAnything换脸_1922491323624935426.json, 图片生成/图生图/快速换脸+一致性｜insertAnything 修图_1922611624191082498.json, 图片生成/图生图/换脸工作流高清出图nsertAnything_1964261096339197954.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_972

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Nunchaku_InsertAnything换脸_1922491323624935426.json、图片生成/图生图/快速换脸+一致性｜insertAnything 修图_1922611624191082498.json、图片生成/图生图/换脸工作流高清出图nsertAnything_1964261096339197954.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
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
- `ImageConcatMulti` —— 2/3 个有
- `ImageConcanate` —— 1/3 个有
- `PreviewMask_` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

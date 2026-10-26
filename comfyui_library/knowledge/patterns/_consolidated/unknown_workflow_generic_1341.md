---
name: unknown_workflow_generic_1341
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.965
common_nodes: [DisplayImageFromURL, GetImageSize, ImageScaleBy, ImageToMask, LayerUtility: CropByMask, LayerUtility: ImageBlendAdvance V3, LayerUtility: TextImage, MaskToImage, MathExpression|pysssss, ResizeImageMaskNode, SaveImage, easy imageConcat]
problems: []
missing: []
members: [图片生成/图生图/7502图片_2089208656658259969.json, 图片生成/图生图/二拼主图_2093954787669798913.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1341

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/7502图片_2089208656658259969.json、图片生成/图生图/二拼主图_2093954787669798913.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 2 个 workflow 都包含：
- `DisplayImageFromURL`
- `GetImageSize`
- `ImageScaleBy`
- `ImageToMask`
- `LayerUtility: CropByMask`
- `LayerUtility: ImageBlendAdvance V3`
- `LayerUtility: TextImage`
- `MaskToImage`
- `MathExpression|pysssss`
- `ResizeImageMaskNode`
- `SaveImage`
- `easy imageConcat`

**可变部分**（部分 workflow 才有）：
- `CR Split String` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `Crop (mtb)` —— 1/2 个有
- `LayerUtility: RoundedRectangle` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

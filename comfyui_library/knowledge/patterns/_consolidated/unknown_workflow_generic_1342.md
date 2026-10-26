---
name: unknown_workflow_generic_1342
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9355
common_nodes: [CR Text, GetImageSize, ImageScaleBy, ImageToMask, LayerUtility: CropByMask, LayerUtility: ImageBlendAdvance V3, LoadImageFromUrl, MaskToImage, MathExpression|pysssss, RHLLMChatNode, SaveImage, TextImage, TextSplitByDelimiterEnhanced]
problems: []
missing: []
members: [图片生成/图生图/8-0_2094739574856704001.json, 图片生成/图生图/9_2094744740368572417.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1342

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/8-0_2094739574856704001.json、图片生成/图生图/9_2094744740368572417.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `GetImageSize`
- `ImageScaleBy`
- `ImageToMask`
- `LayerUtility: CropByMask`
- `LayerUtility: ImageBlendAdvance V3`
- `LoadImageFromUrl`
- `MaskToImage`
- `MathExpression|pysssss`
- `RHLLMChatNode`
- `SaveImage`
- `TextImage`
- `TextSplitByDelimiterEnhanced`

**可变部分**（部分 workflow 才有）：
- `ImageScale` —— 1/2 个有
- `LayerUtility: ColorImage` —— 1/2 个有
- `LoadImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

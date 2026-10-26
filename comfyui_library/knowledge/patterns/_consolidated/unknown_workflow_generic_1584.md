---
name: unknown_workflow_generic_1584
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [CR Prompt Text, ImageScaleToTotalPixels, LoadImage, LongCatImageEdit, LongCatImageModelLoader, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/（自用）LongCat Edit单图像编辑（换装前置）_1997711874340925441.json, 图片生成/文生图/水墨画l图像生成V2-longcat-image-edit_2000828999762931714.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1584

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/（自用）LongCat Edit单图像编辑（换装前置）_1997711874340925441.json、图片生成/文生图/水墨画l图像生成V2-longcat-image-edit_2000828999762931714.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `LongCatImageEdit`
- `LongCatImageModelLoader`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `TT_img_enc` —— 1/2 个有
- `TT_img_enc_v2` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

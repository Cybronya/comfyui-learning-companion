---
name: unknown_workflow_generic_1236
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 1
common_nodes: [CR Prompt Text, ImageScaleToTotalPixels, LoadImage, LongCatImageEdit, LongCatImageModelLoader, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/（自用）LongCat Edit单图像编辑（换装前置）_1997711874340925441.json, 图片生成/文生图/水墨画l图像生成V2-longcat-image-edit_2000828999762931714.json, 平台全量/🦖LongCat Edit单图像编辑（可本地解码）_1998624640870285314.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1236

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/（自用）LongCat Edit单图像编辑（换装前置）_1997711874340925441.json、图片生成/文生图/水墨画l图像生成V2-longcat-image-edit_2000828999762931714.json、平台全量/🦖LongCat Edit单图像编辑（可本地解码）_1998624640870285314.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `CR Prompt Text`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `LongCatImageEdit`
- `LongCatImageModelLoader`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM` —— 2/3 个有
- `TT_img_enc` —— 2/3 个有
- `TT_img_enc_v2` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

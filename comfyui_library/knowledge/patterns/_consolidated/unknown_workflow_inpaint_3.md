---
name: unknown_workflow_inpaint_3
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.877667
common_nodes: [GetImageSize, INPAINT_MaskedFill, ImageBlend, InvertMask, LayerMask: LoadSegformerModel, LayerMask: SegformerClothesSetting, LayerMask: SegformerUltraV3, LayerUtility: ColorImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, Text Multiline]
problems: []
missing: []
members: [平台全量/4K超清全能一键换装_2037003256429289474.json, 平台全量/全能图片V1一键换装（最新版）_1965295910622253058.json, 平台全量/香焦2代—全能图片一键换装，免费换装_2026825695673982977.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_3

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/4K超清全能一键换装_2037003256429289474.json、平台全量/全能图片V1一键换装（最新版）_1965295910622253058.json、平台全量/香焦2代—全能图片一键换装，免费换装_2026825695673982977.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `GetImageSize`
- `INPAINT_MaskedFill`
- `ImageBlend`
- `InvertMask`
- `LayerMask: LoadSegformerModel`
- `LayerMask: SegformerClothesSetting`
- `LayerMask: SegformerUltraV3`
- `LayerUtility: ColorImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `Text Multiline`

**可变部分**（部分 workflow 才有）：
- `MaskToImage` —— 2/3 个有
- `SaveImage` —— 2/3 个有
- `easy promptConcat` —— 2/3 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/3 个有
- `RH_Nano_Banana2_Image2Image` —— 1/3 个有
- `RH_Nano_Banana_Image2Image` —— 1/3 个有
- `SaveImageAndMetadata_` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

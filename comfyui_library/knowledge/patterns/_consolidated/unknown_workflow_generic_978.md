---
name: unknown_workflow_generic_978
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8445
common_nodes: [LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerMask: SegformerB2ClothesUltra, LayerUtility: CropByMask V2, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, RH_Jimeng4_Image2Image, SaveImage]
problems: []
missing: []
members: [平台全量/一键快速 _ 提取服装 _ Seedream 4.0_1905961024795906050.json, 平台全量/提取服装 _ 穿在人体模型上_1890364968515051522.json, 平台全量/提取鞋子 _ 穿在人体模型上_1884524109483884546.json, 平台全量/模特服装一键提取 Seedream   保持衣服不变 最新人物服装提取_2009504525450747906.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_978

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/一键快速 _ 提取服装 _ Seedream 4.0_1905961024795906050.json、平台全量/提取服装 _ 穿在人体模型上_1890364968515051522.json、平台全量/提取鞋子 _ 穿在人体模型上_1884524109483884546.json、平台全量/模特服装一键提取 Seedream   保持衣服不变 最新人物服装提取_2009504525450747906.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerMask: SegformerB2ClothesUltra`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `RH_Jimeng4_Image2Image`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `AddMask` —— 1/4 个有
- `GrowMaskWithBlur` —— 1/4 个有
- `LayerMask: PersonMaskUltra V2` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

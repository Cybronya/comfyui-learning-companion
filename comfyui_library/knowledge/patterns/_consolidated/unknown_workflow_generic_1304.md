---
name: unknown_workflow_generic_1304
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9295
common_nodes: [LoadImage, PreviewImage, RH_Nano_Banana_Image2Image, SaveImage, Textbox]
problems: []
missing: []
members: [图片生成/图生图/一致性+全能图片V1 双人人物合影_1971243555006169090.json, 图片生成/图生图/全能图片V1多图融合编辑2.0_1982503148055085058.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1304

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/一致性+全能图片V1 双人人物合影_1971243555006169090.json、图片生成/图生图/全能图片V1多图融合编辑2.0_1982503148055085058.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `PreviewImage`
- `RH_Nano_Banana_Image2Image`
- `SaveImage`
- `Textbox`

**可变部分**（部分 workflow 才有）：
- `AnyLineArtPreprocessor_aux` —— 1/2 个有
- `ImageBatch` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_upscale_19
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.7705
common_nodes: [DF_Integer, GrowMask, Image Comparer (rgthree), ImageUpscaleWithModel, Int, InvertMask, JoinImageWithAlpha, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LoadImage, PreviewImage, RHHiddenNodes, SaveImage, Upscale Model Loader, YUAN_TXTConvertAny]
problems: []
missing: []
members: [图片生成/图生图/无损放大增强真实感_2112739393718018049.json, 图片生成/图生图/无损放大（人像专用）_2070443876204240898.json, 图片生成/图生图/无损放大（海报专用）_2070443929752924162.json, 图片生成/图生图/磨皮_2070444004679970818.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_19

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/无损放大增强真实感_2112739393718018049.json、图片生成/图生图/无损放大（人像专用）_2070443876204240898.json、图片生成/图生图/无损放大（海报专用）_2070443929752924162.json、图片生成/图生图/磨皮_2070444004679970818.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 4 个 workflow 都包含：
- `DF_Integer`
- `GrowMask`
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `Int`
- `InvertMask`
- `JoinImageWithAlpha`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LoadImage`
- `PreviewImage`
- `RHHiddenNodes`
- `SaveImage`
- `Upscale Model Loader`
- `YUAN_TXTConvertAny`

**可变部分**（部分 workflow 才有）：
- `LG_Color_Match_V2` —— 3/4 个有
- `ImageResize+` —— 1/4 个有
- `JWFloat` —— 1/4 个有
- `KuwaharaBlur` —— 1/4 个有
- `PrimitiveFloat` —— 1/4 个有
- `easy boolean` —— 1/4 个有
- `easy ifElse` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

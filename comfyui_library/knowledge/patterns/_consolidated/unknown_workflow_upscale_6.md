---
name: unknown_workflow_upscale_6
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.609667
common_nodes: [DF_Integer, GrowMask, Image Comparer (rgthree), ImageUpscaleWithModel, Int, InvertMask, JoinImageWithAlpha, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LoadImage, PreviewImage, RHHiddenNodes, SaveImage, Upscale Model Loader, YUAN_TXTConvertAny]
problems: []
missing: [LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, Upscale Model Loader, easy boolean, ImageResize+]
members: [图片生成/图生图/2070443876204240898.json, 图片生成/图生图/2070443929752924162.json, 图片生成/图生图/2070444004679970818.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_6

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/2070443876204240898.json、图片生成/图生图/2070443929752924162.json、图片生成/图生图/2070444004679970818.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 3 个 workflow 都包含：
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
- `LG_Color_Match_V2` —— 2/3 个有
- `ImageResize+` —— 1/3 个有
- `JWFloat` —— 1/3 个有
- `KuwaharaBlur` —— 1/3 个有
- `easy boolean` —— 1/3 个有
- `easy ifElse` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerMask: BiRefNetUltraV2、LayerMask: LoadBiRefNetModelV2、Upscale Model Loader、easy boolean、ImageResize+

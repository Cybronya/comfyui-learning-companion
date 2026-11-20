---
name: unknown_workflow_generic_958
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.952667
common_nodes: [ImageConcatMulti, LoadImage, RH_ComfyFluxKontext, RH_Translator, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/Flux Kontext多图参考模式（电商特供）_1930843229246435330.json, 图片生成/图生图/Flux Kontext多图编辑模式_1929170174723919873.json, 图片生成/图生图/电商产品展示商品替换-产品人像融合_1941683234705195009.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_958

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Flux Kontext多图参考模式（电商特供）_1930843229246435330.json、图片生成/图生图/Flux Kontext多图编辑模式_1929170174723919873.json、图片生成/图生图/电商产品展示商品替换-产品人像融合_1941683234705195009.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `ImageConcatMulti`
- `LoadImage`
- `RH_ComfyFluxKontext`
- `RH_Translator`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RMBG` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

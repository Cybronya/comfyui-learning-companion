---
name: unknown_workflow_generic_190
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.9165
common_nodes: [DeepTranslatorTextNode, ImageConcanate, LoadImage, RH_ComfyFluxKontext, SaveImage]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2]
members: [图片生成/文生图/1931273202180227074.json, 图片生成/文生图/1931550667134185473.json, 图片生成/文生图/1931553605239943170.json, 图片生成/文生图/1931555932394684418.json, 图片生成/文生图/1931560252347756545.json, 图片生成/文生图/1931563283378319361.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_190

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/1931273202180227074.json、图片生成/文生图/1931550667134185473.json、图片生成/文生图/1931553605239943170.json、图片生成/文生图/1931555932394684418.json、图片生成/文生图/1931560252347756545.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 6 个 workflow 都包含：
- `DeepTranslatorTextNode`
- `ImageConcanate`
- `LoadImage`
- `RH_ComfyFluxKontext`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/6 个有
- `BFL_ComfyFluxKontext` —— 2/6 个有
- `Comfly_Flux_Kontext` —— 2/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2

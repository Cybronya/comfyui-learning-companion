---
name: unknown_workflow_generic_647
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.75
common_nodes: [LoadImage, RH_ComfyFluxKontext, RH_Translator, SaveImage]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2]
members: [图片生成/文生图/1930576685161435138.json, 图片生成/文生图/1961644288889307138.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_647

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1930576685161435138.json、图片生成/文生图/1961644288889307138.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `RH_ComfyFluxKontext`
- `RH_Translator`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

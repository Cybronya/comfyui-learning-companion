---
name: unknown_workflow_generic_1626
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.732
common_nodes: [JjkText, LoadImage, RH_ComfyFluxKontext, RH_Translator, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/kontext 服装换颜色四宫格图生成_1938098708426702849.json, 平台全量/Kontext风格参考_1937427956660641794.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1626

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/kontext 服装换颜色四宫格图生成_1938098708426702849.json、平台全量/Kontext风格参考_1937427956660641794.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
- `JjkText`
- `LoadImage`
- `RH_ComfyFluxKontext`
- `RH_Translator`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `ConcatTextOfUtils` —— 1/2 个有
- `JjkConcat` —— 1/2 个有
- `preview_text` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

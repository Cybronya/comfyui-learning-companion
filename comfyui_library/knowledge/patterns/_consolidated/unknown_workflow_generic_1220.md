---
name: unknown_workflow_generic_1220
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.657
common_nodes: [CR Simple Image Compare, LoadImage, PreviewImage, RH_ComfyFluxKontext, RH_Translator, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/Flux-Kontext中文提示词改图工作流_1982368308584423425.json, 图片生成/图生图/Flux-Kontext中文提示词改图稳定版_1926935251522625537.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1220

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flux-Kontext中文提示词改图工作流_1982368308584423425.json、图片生成/图生图/Flux-Kontext中文提示词改图稳定版_1926935251522625537.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：66%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Simple Image Compare`
- `LoadImage`
- `PreviewImage`
- `RH_ComfyFluxKontext`
- `RH_Translator`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_generic_1219
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.796
common_nodes: [CR Integer To String, CR Text, FluxKontextImageScale, FluxResolutionNode, GetImageSize+, ImageConcanate, Int, JoinStrings, LoadImage, PreviewImage, RH_ComfyFluxKontext, RH_LLMAPI_NODE, RH_Translator, SaveImage, easy compare, easy ifElse]
problems: []
missing: []
members: [图片生成/图生图/Flux Kontext Pro_Max单图模式_1949739835357618178.json, 图片生成/图生图/Flux Kontext Pro_Max双图模式_1949765475255410689.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1219

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flux Kontext Pro_Max单图模式_1949739835357618178.json、图片生成/图生图/Flux Kontext Pro_Max双图模式_1949765475255410689.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Integer To String`
- `CR Text`
- `FluxKontextImageScale`
- `FluxResolutionNode`
- `GetImageSize+`
- `ImageConcanate`
- `Int`
- `JoinStrings`
- `LoadImage`
- `PreviewImage`
- `RH_ComfyFluxKontext`
- `RH_LLMAPI_NODE`
- `RH_Translator`
- `SaveImage`
- `easy compare`
- `easy ifElse`

**可变部分**（部分 workflow 才有）：
- `Display Any (rgthree)` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_generic_681
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.849
common_nodes: [CR Text, LoadImage, RH_LLMAPI_Pro_Node, RH_Nano_Banana2_Gemini31Flash, SaveImage, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2038856574608871426.json, 视频生成/图生视频/2034535724053172225.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_681

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2038856574608871426.json、视频生成/图生视频/2034535724053172225.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `LoadImage`
- `RH_LLMAPI_Pro_Node`
- `RH_Nano_Banana2_Gemini31Flash`
- `SaveImage`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `RH_Nano_Banana2_Image2Image` —— 1/2 个有
- `RH_RhartVideoSparkvideo20MultimodalVideo` —— 1/2 个有
- `SaveVideo` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

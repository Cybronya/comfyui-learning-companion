---
name: unknown_workflow_generic_1658
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8
common_nodes: [CR Prompt Text, CR Text Replace, ImpactSwitch, LoadImage, PromptBatchQueue, RH_Nano_Banana2_Gemini31Flash, SaveImage, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/产品批量视觉图（超级矩阵视觉库Agent）_2044036534629834754.json, 平台全量/人像摄影-高定视觉大片-可出系列（完整版）_2044287898492604418.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1658

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/产品批量视觉图（超级矩阵视觉库Agent）_2044036534629834754.json、平台全量/人像摄影-高定视觉大片-可出系列（完整版）_2044287898492604418.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `CR Text Replace`
- `ImpactSwitch`
- `LoadImage`
- `PromptBatchQueue`
- `RH_Nano_Banana2_Gemini31Flash`
- `SaveImage`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `RH_LLMAPI_Pro_Node` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

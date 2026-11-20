---
name: unknown_workflow_generic_1317
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.748
common_nodes: [LoadImage, SaveImage, ShellAgentPluginOutputText, TextInput_, easy showAnything]
problems: []
missing: []
members: [图片生成/反推提示词/室内-Seedance 2.0室内营销号分镜提示词生成工作流_2036075802558730241.json, 图片生成/反推提示词/建筑-Seedance 2.0自建宅营销号分镜提示词生成工作流_2036075786326777857.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1317

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/室内-Seedance 2.0室内营销号分镜提示词生成工作流_2036075802558730241.json、图片生成/反推提示词/建筑-Seedance 2.0自建宅营销号分镜提示词生成工作流_2036075786326777857.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `SaveImage`
- `ShellAgentPluginOutputText`
- `TextInput_`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Comfly_LLm_API` —— 1/2 个有
- `Gemini3MultimodalChatNode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

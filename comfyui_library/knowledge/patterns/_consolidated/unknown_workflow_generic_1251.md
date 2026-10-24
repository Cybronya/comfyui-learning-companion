---
name: unknown_workflow_generic_1251
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.668
common_nodes: [JjkText, LoadImage, ProcessString, RH_LLMAPI_NODE, SaveImage, ShellAgentPluginOutputText, easy promptLine, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/LLM API 图生电影分镜文本一次一RH币_2009067979266334722.json, 图片生成/图生图/根据图片生成不同视角分镜头故事版_2107655869549858817.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1251

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/LLM API 图生电影分镜文本一次一RH币_2009067979266334722.json、图片生成/图生图/根据图片生成不同视角分镜头故事版_2107655869549858817.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：67%

## 共有节点

全部 2 个 workflow 都包含：
- `JjkText`
- `LoadImage`
- `ProcessString`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `ShellAgentPluginOutputText`
- `easy promptLine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `RH_RhartImageG2ImageToImage` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

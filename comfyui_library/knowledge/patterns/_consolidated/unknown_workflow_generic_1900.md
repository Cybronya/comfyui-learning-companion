---
name: unknown_workflow_generic_1900
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.831
common_nodes: [LoadImage, LoadVideo, MiniMaxH3PromptEnhancerT8, SaveImage, ShellAgentPluginOutputText, easy showAnything]
problems: []
missing: []
members: [平台全量/MiniMax H3提示词增强器_2117507975651876866.json, 视频生成/文生视频/最强MiniMax H3提示词增强器｜Qwen3.8本地版_2095652482700627969.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1900

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/MiniMax H3提示词增强器_2117507975651876866.json、视频生成/文生视频/最强MiniMax H3提示词增强器｜Qwen3.8本地版_2095652482700627969.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `LoadVideo`
- `MiniMaxH3PromptEnhancerT8`
- `SaveImage`
- `ShellAgentPluginOutputText`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `MuyeTextEditOutput` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_generic_422
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.609167
common_nodes: [ComfySwitchNode, MinimaxHailuo03ContextIRNode, MinimaxHailuo03RegenerateNode, PrimitiveBoolean, PrimitiveStringMultiline, SaveText, SaveVideo]
problems: []
missing: []
members: [comfyui-workflow-templates-json/api_minimax_h3_max_flf2v.json, comfyui-workflow-templates-json/api_minimax_h3_max_i2v.json, comfyui-workflow-templates-json/api_minimax_h3_max_r2v.json, comfyui-workflow-templates-json/api_minimax_h3_max_t2v.json, comfyui-workflow-templates-json/api_minimax_h3_max_turbo_i2v.json, comfyui-workflow-templates-json/api_minimax_h3_max_turbo_t2v.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_422

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（comfyui-workflow-templates-json/api_minimax_h3_max_flf2v.json、comfyui-workflow-templates-json/api_minimax_h3_max_i2v.json、comfyui-workflow-templates-json/api_minimax_h3_max_r2v.json、comfyui-workflow-templates-json/api_minimax_h3_max_t2v.json、comfyui-workflow-templates-json/api_minimax_h3_max_turbo_i2v.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 6 个 workflow 都包含：
- `ComfySwitchNode`
- `MinimaxHailuo03ContextIRNode`
- `MinimaxHailuo03RegenerateNode`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `SaveText`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 4/6 个有
- `MinimaxHailuo03FirstLastFrameNode` —— 3/6 个有
- `MinimaxHailuo03TextToVideoNode` —— 2/6 个有
- `MinimaxHailuo03ReferenceNode` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

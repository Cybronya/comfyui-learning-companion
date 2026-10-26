---
name: unknown_workflow_generic_1298
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.824
common_nodes: [LoadImage, PreviewAny, QwenPECanvasT8, QwenPERewriteT8, SaveImage, ShellAgentPluginOutputText]
problems: []
missing: []
members: [图片生成/反推提示词/Qwen Image 2.1 PE提示词强化（T8节点版）_2102224088881258498.json, 图片生成/反推提示词/Qwen Image 2.1 Uncensor PE图像编辑提示词强化_2104563522247151617.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1298

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/Qwen Image 2.1 PE提示词强化（T8节点版）_2102224088881258498.json、图片生成/反推提示词/Qwen Image 2.1 Uncensor PE图像编辑提示词强化_2104563522247151617.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `PreviewAny`
- `QwenPECanvasT8`
- `QwenPERewriteT8`
- `SaveImage`
- `ShellAgentPluginOutputText`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

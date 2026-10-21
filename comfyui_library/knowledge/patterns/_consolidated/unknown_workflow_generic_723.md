---
name: unknown_workflow_generic_723
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.833
common_nodes: [LoadImage, PreviewAny, SaveImage, easy saveText, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: []
missing: []
members: [图片生成/反推提示词/qwen3.8-27B反推图片提示词_2103825737462673409.json, 图片生成/反推提示词/qwen3.8-27B反推图片提示词_2104868396172140545.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_723

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/qwen3.8-27B反推图片提示词_2103825737462673409.json、图片生成/反推提示词/qwen3.8-27B反推图片提示词_2104868396172140545.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `PreviewAny`
- `SaveImage`
- `easy saveText`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_generic_609
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5145
common_nodes: [LoadImage, MaskPreview, PreviewImage]
problems: []
missing: []
members: [comfyui-workflow-templates-json/utility_birefnet_remove_background.json, comfyui-workflow-templates-json/utility_moge_depth_estimation.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_609

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（comfyui-workflow-templates-json/utility_birefnet_remove_background.json、comfyui-workflow-templates-json/utility_moge_depth_estimation.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：51%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `MaskPreview`
- `PreviewImage`

**可变部分**（部分 workflow 才有）：
- `5b40ca21-ba1a-41d5-b403-4d2d7acdc195` —— 1/2 个有
- `ca1fac5f-abe5-4729-b7fe-2299f6630a65` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

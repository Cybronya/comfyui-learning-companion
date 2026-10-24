---
name: unknown_workflow_generic_1181
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.667
common_nodes: [ImageScaleToMaxDimension, LoadImage, SaveImage, f754a936-daaf-4b6e-9658-41fdc54d301d]
problems: []
missing: []
members: [comfyui-workflow-templates-json/image_qwen_image_layered.json, comfyui-workflow-templates-json/image_qwen_image_layered_control.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1181

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（comfyui-workflow-templates-json/image_qwen_image_layered.json、comfyui-workflow-templates-json/image_qwen_image_layered_control.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：67%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageScaleToMaxDimension`
- `LoadImage`
- `SaveImage`
- `f754a936-daaf-4b6e-9658-41fdc54d301d`

**可变部分**（部分 workflow 才有）：
- `1ea4fa01-a81b-4420-a03c-f60019e69a92` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

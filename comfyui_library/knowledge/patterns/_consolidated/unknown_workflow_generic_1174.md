---
name: unknown_workflow_generic_1174
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7335
common_nodes: [ImageScaleToTotalPixels, LoadImage, SaveImage]
problems: []
missing: []
members: [comfyui-workflow-templates-json/image_flux2.json, comfyui-workflow-templates-json/image_qwen_image_edit.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1174

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（comfyui-workflow-templates-json/image_flux2.json、comfyui-workflow-templates-json/image_qwen_image_edit.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageScaleToTotalPixels`
- `LoadImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `74a8e1e2-9cb8-4112-978e-06ce1b5793f1` —— 1/2 个有
- `7651d2ae-5471-47b0-b064-b34ee62343c1` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

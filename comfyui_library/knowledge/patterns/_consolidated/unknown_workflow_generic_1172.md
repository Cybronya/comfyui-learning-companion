---
name: unknown_workflow_generic_1172
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7525
common_nodes: [147b517e-5ea6-4fba-84f7-46851be6e4ce, GetImageSize, ImageCompare, LoadImage, PreviewImage, ResizeImageMaskNode, SaveImage]
problems: []
missing: []
members: [comfyui-workflow-templates-json/image_anima_lllite_any_control_to_image.json, comfyui-workflow-templates-json/image_anima_lllite_depth_control_to_image.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1172

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（comfyui-workflow-templates-json/image_anima_lllite_any_control_to_image.json、comfyui-workflow-templates-json/image_anima_lllite_depth_control_to_image.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `147b517e-5ea6-4fba-84f7-46851be6e4ce`
- `GetImageSize`
- `ImageCompare`
- `LoadImage`
- `PreviewImage`
- `ResizeImageMaskNode`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `28eb0ec0-5d35-42e9-8cb3-d1161dc5a231` —— 1/2 个有
- `Canny` —— 1/2 个有
- `ImageInvert` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

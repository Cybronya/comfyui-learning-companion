---
name: unknown_workflow_upscale_7
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9
common_nodes: [ImageCompare, LoadImage, SaveImage]
problems: []
missing: []
members: [comfyui-workflow-templates-json/api_flux_erase_image.json, comfyui-workflow-templates-json/api_magnific_image_upscale_creative.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_7

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（comfyui-workflow-templates-json/api_flux_erase_image.json、comfyui-workflow-templates-json/api_magnific_image_upscale_creative.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageCompare`
- `LoadImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `FluxEraseNode` —— 1/2 个有
- `MagnificImageUpscalerCreativeNode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

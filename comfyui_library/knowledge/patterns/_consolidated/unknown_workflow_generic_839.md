---
name: unknown_workflow_generic_839
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.802333
common_nodes: [ImageCompare, ImageScaleBy, LoadImage, SaveImage]
problems: []
missing: []
members: [comfyui-workflow-templates-json/utility-topaz_landscape_upscaler.json, comfyui-workflow-templates-json/utility_interpolation_image_upscale.json, comfyui-workflow-templates-json/utility_topaz_illustration_upscale.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_839

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（comfyui-workflow-templates-json/utility-topaz_landscape_upscaler.json、comfyui-workflow-templates-json/utility_interpolation_image_upscale.json、comfyui-workflow-templates-json/utility_topaz_illustration_upscale.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 3 个 workflow 都包含：
- `ImageCompare`
- `ImageScaleBy`
- `LoadImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 2/3 个有
- `TopazImageEnhance` —— 1/3 个有
- `TopazImageEnhanceV2` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

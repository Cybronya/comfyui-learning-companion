---
name: unknown_workflow_generic_490
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.778
common_nodes: [GetImageSize, ImageCompare, LoadImage, ResizeImageMaskNode]
problems: []
missing: []
members: [comfyui-workflow-templates-json/api_topaz_image_enhance.json, comfyui-workflow-templates-json/image_boogu_image_0_1_edit.json, comfyui-workflow-templates-json/image_boogu_image_0_1_edit_int8.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_490

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（comfyui-workflow-templates-json/api_topaz_image_enhance.json、comfyui-workflow-templates-json/image_boogu_image_0_1_edit.json、comfyui-workflow-templates-json/image_boogu_image_0_1_edit_int8.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 3 个 workflow 都包含：
- `GetImageSize`
- `ImageCompare`
- `LoadImage`
- `ResizeImageMaskNode`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 2/3 个有
- `fd5d0097-8a1d-4dc2-86f2-1d5869b3f0eb` —— 2/3 个有
- `SaveImageAdvanced` —— 1/3 个有
- `TopazImageEnhanceV2` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

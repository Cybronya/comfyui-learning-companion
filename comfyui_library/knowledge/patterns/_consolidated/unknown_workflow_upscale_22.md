---
name: unknown_workflow_upscale_22
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.755667
common_nodes: [ImageCompare, LoadImage, SaveImage]
problems: []
missing: []
members: [comfyui-workflow-templates-json/utility_recraft_crisp_image_upscale.json, comfyui-workflow-templates-json/utility_seedvr2_3b_int8_upscale_image.json, comfyui-workflow-templates-json/utility_seedvr2_7b_int8_upscale_image.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_22

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（comfyui-workflow-templates-json/utility_recraft_crisp_image_upscale.json、comfyui-workflow-templates-json/utility_seedvr2_3b_int8_upscale_image.json、comfyui-workflow-templates-json/utility_seedvr2_7b_int8_upscale_image.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 3 个 workflow 都包含：
- `ImageCompare`
- `LoadImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `1970dcb4-982a-4c01-a373-4d239a3041e4` —— 2/3 个有
- `RecraftCrispUpscaleNode` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

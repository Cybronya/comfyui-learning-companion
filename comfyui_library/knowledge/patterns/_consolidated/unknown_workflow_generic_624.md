---
name: unknown_workflow_generic_624
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.9
common_nodes: [ImageCompare, LoadImage, SaveImageAdvanced]
problems: []
missing: []
members: [comfyui-workflow-templates-json/api_nano_banana_2_1_image_edit.json, comfyui-workflow-templates-json/api_nano_banana_2_lite_image_edit.json, comfyui-workflow-templates-json/api_topaz_image_enhance_bloom2.json, comfyui-workflow-templates-json/api_topaz_image_enhance_wonder3_5.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_624

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（comfyui-workflow-templates-json/api_nano_banana_2_1_image_edit.json、comfyui-workflow-templates-json/api_nano_banana_2_lite_image_edit.json、comfyui-workflow-templates-json/api_topaz_image_enhance_bloom2.json、comfyui-workflow-templates-json/api_topaz_image_enhance_wonder3_5.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `ImageCompare`
- `LoadImage`
- `SaveImageAdvanced`

**可变部分**（部分 workflow 才有）：
- `GeminiNanoBanana2V2` —— 2/4 个有
- `TopazImageEnhanceV2` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

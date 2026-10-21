---
name: unknown_workflow_generic_341
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.78025
common_nodes: [ByteDanceSeedreamNodeV3, SaveImageAdvanced]
problems: []
missing: []
members: [comfyui-workflow-templates-json/api_bytedance_seedream_5_0_flash_image_edit.json, comfyui-workflow-templates-json/api_bytedance_seedream_5_0_flash_t2i.json, comfyui-workflow-templates-json/api_bytedance_seedream_5_0_lite_image_edit.json, comfyui-workflow-templates-json/api_bytedance_seedream_5_0_pro_image_edit.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_341

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（comfyui-workflow-templates-json/api_bytedance_seedream_5_0_flash_image_edit.json、comfyui-workflow-templates-json/api_bytedance_seedream_5_0_flash_t2i.json、comfyui-workflow-templates-json/api_bytedance_seedream_5_0_lite_image_edit.json、comfyui-workflow-templates-json/api_bytedance_seedream_5_0_pro_image_edit.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 4 个 workflow 都包含：
- `ByteDanceSeedreamNodeV3`
- `SaveImageAdvanced`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 3/4 个有
- `Painter` —— 1/4 个有
- `PreviewImage` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

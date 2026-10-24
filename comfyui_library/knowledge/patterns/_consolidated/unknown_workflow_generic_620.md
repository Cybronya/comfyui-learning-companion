---
name: unknown_workflow_generic_620
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.80175
common_nodes: [LoadVideo, SaveVideo]
problems: []
missing: []
members: [comfyui-workflow-templates-json/api_google_gemini_omni_flash_1_1_edit.json, comfyui-workflow-templates-json/api_google_gemini_omni_flash_1_1_extend.json, comfyui-workflow-templates-json/api_seedance2_5_video_editing.json, comfyui-workflow-templates-json/api_seedance2_5_video_extend.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_620

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（comfyui-workflow-templates-json/api_google_gemini_omni_flash_1_1_edit.json、comfyui-workflow-templates-json/api_google_gemini_omni_flash_1_1_extend.json、comfyui-workflow-templates-json/api_seedance2_5_video_editing.json、comfyui-workflow-templates-json/api_seedance2_5_video_extend.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 4 个 workflow 都包含：
- `LoadVideo`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `Video Slice` —— 3/4 个有
- `ByteDance2ReferenceNodeV2` —— 2/4 个有
- `GeminiVideoOmniV2` —— 2/4 个有
- `d9aa59a4-3784-4796-9f1b-5b467fb41fa1` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

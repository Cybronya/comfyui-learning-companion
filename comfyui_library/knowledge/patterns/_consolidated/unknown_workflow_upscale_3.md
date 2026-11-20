---
name: unknown_workflow_upscale_3
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.911111
common_nodes: [SaveImage]
problems: []
missing: []
members: [comfyui-workflow-templates-json/api_openai_fashion_billboard_generator.json, comfyui-workflow-templates-json/api_openai_gpt_image_25_flare_t2i.json, comfyui-workflow-templates-json/api_openai_gpt_image_25_sunburst_t2i.json, comfyui-workflow-templates-json/api_openai_gpt_image_2_image_edit.json, comfyui-workflow-templates-json/api_openai_gpt_image_2_t2i.json, comfyui-workflow-templates-json/api_openai_image_1_i2i.json, comfyui-workflow-templates-json/api_openai_image_1_inpaint.json, comfyui-workflow-templates-json/api_wavespeed_image_upscale.json, comfyui-workflow-templates-json/api_wavespeed_seedvr2_ai_image_fix.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_3

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（comfyui-workflow-templates-json/api_openai_fashion_billboard_generator.json、comfyui-workflow-templates-json/api_openai_gpt_image_25_flare_t2i.json、comfyui-workflow-templates-json/api_openai_gpt_image_25_sunburst_t2i.json、comfyui-workflow-templates-json/api_openai_gpt_image_2_image_edit.json、comfyui-workflow-templates-json/api_openai_gpt_image_2_t2i.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 9 个 workflow 都包含：
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `OpenAIGPTImageNodeV2` —— 7/9 个有
- `LoadImage` —— 6/9 个有
- `ImageCompare` —— 4/9 个有
- `WavespeedImageUpscaleNode` —— 2/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_generic_679
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.6
common_nodes: [CLIPLoader, PreviewAny, TextGenerate]
problems: []
missing: []
members: [comfyui-workflow-templates-json/llm_qwen3_5_text_gen.json, comfyui-workflow-templates-json/llm_qwen3_text_gen.json, comfyui-workflow-templates-json/llm_qwen3vl_text_gen.json, 图片生成/反推提示词/图像反推提示词_qwen3.5_2063048577647202305.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_679

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（comfyui-workflow-templates-json/llm_qwen3_5_text_gen.json、comfyui-workflow-templates-json/llm_qwen3_text_gen.json、comfyui-workflow-templates-json/llm_qwen3vl_text_gen.json、图片生成/反推提示词/图像反推提示词_qwen3.5_2063048577647202305.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：60%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `PreviewAny`
- `TextGenerate`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 3/4 个有
- `easy saveText` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

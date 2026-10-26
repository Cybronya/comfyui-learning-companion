---
name: unknown_workflow_generic_1269
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.4375
common_nodes: [PrimitiveStringMultiline, SaveImage, StringConcatenate]
problems: []
missing: []
members: [comfyui-workflow-templates-json/template_qwen_Image_2512_360_lora.json, 图片生成/文生图/krea2_turbo_t2i_int8_角色三视图_2076487283330600962.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1269

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（comfyui-workflow-templates-json/template_qwen_Image_2512_360_lora.json、图片生成/文生图/krea2_turbo_t2i_int8_角色三视图_2076487283330600962.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：44%

## 共有节点

全部 2 个 workflow 都包含：
- `PrimitiveStringMultiline`
- `SaveImage`
- `StringConcatenate`

**可变部分**（部分 workflow 才有）：
- `c3c58f7e-2004-43ae-8b06-a956294bf7f4` —— 1/2 个有
- `workflow>krea2` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

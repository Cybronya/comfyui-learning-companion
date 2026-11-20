---
name: unknown_workflow_video_176
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8265
common_nodes: [ShowText|pysssss, StringFunction|pysssss, Text Multiline, easy positive, easy saveText, easy seed]
problems: []
missing: []
members: [图片生成/反推提示词/推理-文生图提示词-qwen2.5_1972214593177251841.json, 平台全量/推理-角色-Qwen3VL_1988240730667835394.json]
source: knowledge_consolidation
---

# unknown_workflow_video_176

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/推理-文生图提示词-qwen2.5_1972214593177251841.json、平台全量/推理-角色-Qwen3VL_1988240730667835394.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `ShowText|pysssss`
- `StringFunction|pysssss`
- `Text Multiline`
- `easy positive`
- `easy saveText`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `Qwen3_VQA` —— 1/2 个有
- `QwenLoader` —— 1/2 个有
- `WanVideoPromptExtender` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_generic_1487
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.639
common_nodes: [LoadImage, RH_LLMAPI_NODE, SaveImage, ShowText|pysssss]
problems: []
missing: []
members: [图片生成/文生图/【阡陌】 Comfyui Qwen-Image调用deepseek优化提示词生图_1960218348674035713.json, 视频生成/图生视频/图生视频提示词优化_1989332533642973186.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1487

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/【阡陌】 Comfyui Qwen-Image调用deepseek优化提示词生图_1960218348674035713.json、视频生成/图生视频/图生视频提示词优化_1989332533642973186.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `ShowText|pysssss`

**可变部分**（部分 workflow 才有）：
- `QwenImageNode` —— 1/2 个有
- `easy imageConcat` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

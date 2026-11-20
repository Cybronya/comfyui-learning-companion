---
name: unknown_workflow_lora_6
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.857
common_nodes: [LoadImage, LoraLoaderModelOnly, RH_LLMAPI_NODE, SaveImage, ShowText|pysssss, String Literal, Text]
problems: []
missing: []
members: [图片生成/反推提示词/260110007.提示词生成_2011257487067975682.json, 图片生成/反推提示词/AI赋能安全管理-你的工作小助手_2011752051327377410.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_6

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/260110007.提示词生成_2011257487067975682.json、图片生成/反推提示词/AI赋能安全管理-你的工作小助手_2011752051327377410.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `LoraLoaderModelOnly`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `ShowText|pysssss`
- `String Literal`
- `Text`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_generic_1448
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.717
common_nodes: [CR Combine Prompt, Image Comparer (rgthree), LoadImage, Qwen3_VQA, RH_Nano_Banana2_Image2Image, SaveImage, ShowText|pysssss, Text, ToString]
problems: []
missing: []
members: [图片生成/图生图/产品替换工作流（+反推固定产品规格）_2038602585648668673.json, 图片生成/图生图/软包产品材质替换_2027554475094839298.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1448

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/产品替换工作流（+反推固定产品规格）_2038602585648668673.json、图片生成/图生图/软包产品材质替换_2027554475094839298.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：72%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Combine Prompt`
- `Image Comparer (rgthree)`
- `LoadImage`
- `Qwen3_VQA`
- `RH_Nano_Banana2_Image2Image`
- `SaveImage`
- `ShowText|pysssss`
- `Text`
- `ToString`

**可变部分**（部分 workflow 才有）：
- `PrimitiveBoolean` —— 1/2 个有
- `Qwen3VL_Chat` —— 1/2 个有
- `SeargePromptCombiner` —— 1/2 个有
- `easy ifElse` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

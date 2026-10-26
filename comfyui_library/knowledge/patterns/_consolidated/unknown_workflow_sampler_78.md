---
name: unknown_workflow_sampler_78
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9165
common_nodes: [CR Prompt Text, ImageConcanate, JWInteger, LoadImage, Note Plus (mtb), RunningHub_UNO_Loadmodel, RunningHub_UNO_Sampler, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/UNO双图融合主题一致性工作流V1_1910340168090615809.json, 图片生成/图生图/Uno单图主题编辑一致性工作流_1910317954465001473.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_78

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/UNO双图融合主题一致性工作流V1_1910340168090615809.json、图片生成/图生图/Uno单图主题编辑一致性工作流_1910317954465001473.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `ImageConcanate`
- `JWInteger`
- `LoadImage`
- `Note Plus (mtb)`
- `RunningHub_UNO_Loadmodel`
- `RunningHub_UNO_Sampler`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `ImageBatch` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

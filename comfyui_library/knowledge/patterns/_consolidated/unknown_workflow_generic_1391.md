---
name: unknown_workflow_generic_1391
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.696
common_nodes: [CR Prompt Text, Comfly_api_set, Comfly_qwen_image, SaveImage, SeedVR2, SeedVR2BlockSwap]
problems: []
missing: []
members: [图片生成/图生图/Qwen Image 满血版API洗图高清放大流V1_1957309776436850690.json, 图片生成/文生图/Qwen Image 满血版API文生图高清放大流V1_1957311556746932225.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1391

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Qwen Image 满血版API洗图高清放大流V1_1957309776436850690.json、图片生成/文生图/Qwen Image 满血版API文生图高清放大流V1_1957311556746932225.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：70%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `Comfly_api_set`
- `Comfly_qwen_image`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

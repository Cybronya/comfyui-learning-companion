---
name: unknown_workflow_sampler_vae_39
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.671
common_nodes: [DualCLIPLoader, DyPE_Condition, DyPE_Encode, DyPE_KSampler, DyPE_Model, SaveImage, VAEDecode, VAELoader]
problems: []
missing: [CR Prompt Text, LayerUtility: ImageScaleByAspectRatio V2]
members: [图片生成/文生图/1984246530523742209.json, 图片生成/文生图/1984409596913664002.json, 图片生成/文生图/1984816251937636354.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_39

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1984246530523742209.json、图片生成/文生图/1984409596913664002.json、图片生成/文生图/1984816251937636354.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 3 个 workflow 都包含：
- `DualCLIPLoader`
- `DyPE_Condition`
- `DyPE_Encode`
- `DyPE_KSampler`
- `DyPE_Model`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 2/3 个有
- `JWInteger` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `DeepTranslatorTextNode` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Prompt Text、LayerUtility: ImageScaleByAspectRatio V2

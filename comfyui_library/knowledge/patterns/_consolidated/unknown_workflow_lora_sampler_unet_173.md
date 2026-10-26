---
name: unknown_workflow_lora_sampler_unet_173
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.91825
common_nodes: [CFGNorm, CLIPLoader, CR Text, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader, easy imageScaleDownToSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-2509-全能换背景_2003643161689899010.json, 图片生成/图生图/qwen-edit-2509-电商换背景_1989217669691879425.json, 图片生成/图生图/qwen-edit-2509双图编辑万物迁移_1978724036937191426.json, 图片生成/图生图/qwen-edit-图片精修_1988195106761129986.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_173

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen-2509-全能换背景_2003643161689899010.json、图片生成/图生图/qwen-edit-2509-电商换背景_1989217669691879425.json、图片生成/图生图/qwen-edit-2509双图编辑万物迁移_1978724036937191426.json、图片生成/图生图/qwen-edit-图片精修_1988195106761129986.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Text`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageScaleDownToSize`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/4 个有
- `ImageConcanate` —— 2/4 个有
- `LayerUtility: ImageReel` —— 2/4 个有
- `LayerUtility: ImageReelComposit` —— 2/4 个有
- `ConditioningClamp` —— 1/4 个有
- `LayerMask: BiRefNetUltraV2` —— 1/4 个有
- `LayerMask: LoadBiRefNetModel` —— 1/4 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/4 个有
- `easy imageRemBg` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | 8 - 20 | 4 | 57% |
| Prompt 约束强度(CFG) | 1.75 | 1 - 2.5 | 4 | 57% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | beta57 | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，观测区间 8 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 1.75，观测区间 1 - 2.5，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 beta57，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足

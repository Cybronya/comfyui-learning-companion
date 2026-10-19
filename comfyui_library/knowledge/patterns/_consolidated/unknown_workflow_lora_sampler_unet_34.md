---
name: unknown_workflow_lora_sampler_unet_34
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.78625
common_nodes: [CLIPLoader, ConditioningZeroOut, ConstrainImage|pysssss, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, TextInput_, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [ConstrainImage|pysssss, LayerUtility: ExtendCanvas, Seed (rgthree)]
members: [图片生成/文生图/1980915356590100482.json, 图片生成/文生图/1983003529390489602.json, 图片生成/文生图/1988816202585747457.json, 图片生成/文生图/1989589101206753282.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_34

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1980915356590100482.json、图片生成/文生图/1983003529390489602.json、图片生成/文生图/1988816202585747457.json、图片生成/文生图/1989589101206753282.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `ConstrainImage|pysssss`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BiRefNetRMBG` —— 3/4 个有
- `LayerUtility: ExtendCanvas` —— 3/4 个有
- `Seed (rgthree)` —— 3/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta57 | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta57，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：ConstrainImage|pysssss、LayerUtility: ExtendCanvas、Seed (rgthree)

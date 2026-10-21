---
name: unknown_workflow_sampler_clip_unet_77
type: Unknown Workflow
frequency: 8
level: weak
coverage: 0.926875
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/AA--缓存加速Zimage-base-MeanCache5种加速模式对比_2019746684867190785.json, 图片生成/文生图/Qwen image pruning——权重瘦身版_2073209712295899137.json, 图片生成/文生图/Qwen-Image 2steps 超极速生图_2028108869695709185.json, 图片生成/文生图/Qwen-Image 角色图工作流_2088869274373943298.json, 图片生成/文生图/Z - IMAGE - Distill loRa 速度对比工作流_2024672851546083330.json, 图片生成/文生图/Z-distill lora对比工作流_2082076301388767234.json, 图片生成/文生图/Zimage base 4步8步Lora对比_2021782849505992705.json, 图片生成/文生图/最高20倍提速！Z-distill lora对比工作流_2021664209846673409.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_77

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/AA--缓存加速Zimage-base-MeanCache5种加速模式对比_2019746684867190785.json、图片生成/文生图/Qwen image pruning——权重瘦身版_2073209712295899137.json、图片生成/文生图/Qwen-Image 2steps 超极速生图_2028108869695709185.json、图片生成/文生图/Qwen-Image 角色图工作流_2088869274373943298.json、图片生成/文生图/Z - IMAGE - Distill loRa 速度对比工作流_2024672851546083330.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 5/8 个有
- `ImageConcatMulti` —— 5/8 个有
- `ConditioningZeroOut` —— 4/8 个有
- `Image Comparer (rgthree)` —— 4/8 个有
- `LoraLoaderModelOnly` —— 4/8 个有
- `easy globalSeed` —— 4/8 个有
- `easy promptList` —— 4/8 个有
- `LayerUtility: PurgeVRAM` —— 1/8 个有
- `MeanCache_ZImage` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | 2 - 50 | 8 | 17% |
| Prompt 约束强度(CFG) | 1.75 | 1 - 4 | 8 | 41% |
| 采样算法 | res_multistep | - | 8 | 38% |
| 调度器 | simple | - | 8 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，观测区间 2 - 50，8 个样本，取值分散，一致性仅 17%
- Prompt 约束强度(CFG) 中位数 1.75，观测区间 1 - 4，8 个样本，取值分散，一致性仅 41%
- 采样算法 最常用 res_multistep，8 个样本，一致性 38%
- 调度器 最常用 simple，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（10/8 个样本）：Steps较低可能导致细节不足

---
name: unknown_workflow_sampler_checkpoint_vae_37
type: Unknown Workflow
frequency: 3
level: strong
coverage: 1
common_nodes: [CFGNorm, CheckpointLoaderSimple, ConditioningZeroOut, EmptyLatentImage, KSampler, LoadImage, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人物三视图_2032614113515409410.json, 图片生成/图生图/最新LTX 2.3  Seedance2.0 人物设定三视图_2037384136079450113.json, 图片生成/图生图/电商-模特服装融图用_2046237840547254273.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_37

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/人物三视图_2032614113515409410.json、图片生成/图生图/最新LTX 2.3  Seedance2.0 人物设定三视图_2037384136079450113.json、图片生成/图生图/电商-模特服装融图用_2046237840547254273.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1440 | 1024 - 1440 | 3 | 85% |
| 高度 | 1920 | 1792 - 1920 | 3 | 97% |
| 采样步数 | 4 | 4 - 8 | 3 | 65% |
| Prompt 约束强度(CFG) | 1.2 | 1 - 1.2 | 3 | 92% |
| 采样算法 | euler_ancestral | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1440，观测区间 1024 - 1440，3 个样本，取值集中（一致性 85%）
- 高度 中位数 1920，观测区间 1792 - 1920，3 个样本，取值集中（一致性 97%）
- 采样步数 中位数 4，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1.2，观测区间 1 - 1.2，3 个样本，取值集中（一致性 92%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足

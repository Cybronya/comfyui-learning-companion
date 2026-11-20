---
name: unknown_workflow_sampler_checkpoint_vae_34
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 1
common_nodes: [CheckpointLoaderSimple, ConditioningZeroOut, EmptyLatentImage, KSampler, LoadImage, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人物三视图_2032614113515409410.json, 图片生成/图生图/最新LTX 2.3  Seedance2.0 人物设定三视图_2037384136079450113.json, 图片生成/图生图/电商-模特服装融图用_2046237840547254273.json, 平台全量/Qwen-Edit-Rapid-AIO单图编辑_1977698403817771009.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_34

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/人物三视图_2032614113515409410.json、图片生成/图生图/最新LTX 2.3  Seedance2.0 人物设定三视图_2037384136079450113.json、图片生成/图生图/电商-模特服装融图用_2046237840547254273.json、平台全量/Qwen-Edit-Rapid-AIO单图编辑_1977698403817771009.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 4 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `CLIPLoader` —— 2/4 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/4 个有
- `ModelSamplingAuraFlow` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1232 | 512 - 1440 | 4 | 65% |
| 高度 | 1856 | 512 - 1920 | 4 | 61% |
| 采样步数 | 4 | 4 - 8 | 4 | 65% |
| Prompt 约束强度(CFG) | 1.1 | 1 - 1.2 | 4 | 91% |
| 采样算法 | euler_ancestral | - | 4 | 50% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1232，观测区间 512 - 1440，4 个样本
- 高度 中位数 1856，观测区间 512 - 1920，4 个样本
- 采样步数 中位数 4，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1.1，观测区间 1 - 1.2，4 个样本，取值集中（一致性 91%）
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足

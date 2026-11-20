---
name: unknown_workflow_sampler_vae_57
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.984
common_nodes: [CFGNorm, ConditioningZeroOut, EmptyLatentImage, KSampler, LoadImage, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QwenAIO动漫转真人三视图_2035514846493544449.json, 图片生成/图生图/QwenEdit2511-融图-去塑料感-v5.0_2046110169540599810.json, 图片生成/图生图/qwen 最新2026多视角生成保持一致性_2013805117430042625.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_57

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/QwenAIO动漫转真人三视图_2035514846493544449.json、图片生成/图生图/QwenEdit2511-融图-去塑料感-v5.0_2046110169540599810.json、图片生成/图生图/qwen 最新2026多视角生成保持一致性_2013805117430042625.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 2/3 个有
- `CheckpointLoaderSimple` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/3 个有
- `QWenVL_API_S_Multi_Zho` —— 1/3 个有
- `Qwen2.5VL` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `UNETLoader` —— 1/3 个有
- `VAELoader` —— 1/3 个有
- `easy promptLine` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 3 | 65% |
| Prompt 约束强度(CFG) | 1.2 | 1 - 1.2 | 3 | 92% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 512 - 1024 | 3 | 72% |
| 高度 | 1536 | 512 - 1792 | 3 | 57% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1.2，观测区间 1 - 1.2，3 个样本，取值集中（一致性 92%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 512 - 1024，3 个样本
- 高度 中位数 1536，观测区间 512 - 1792，3 个样本
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足

---
name: unknown_workflow_sampler_vae_61
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.972
common_nodes: [CFGNorm, ConditioningZeroOut, EmptyLatentImage, KSampler, LoadImage, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QwenAIO动漫转真人三视图_2035514846493544449.json, 图片生成/图生图/QwenEdit2511-融图-去塑料感-v5.0_2046110169540599810.json, 图片生成/图生图/b-光影溶图融图qwen edit 2509_2005252378804842497.json, 图片生成/图生图/ktv公主_1991635135160336386.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_61

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/QwenAIO动漫转真人三视图_2035514846493544449.json、图片生成/图生图/QwenEdit2511-融图-去塑料感-v5.0_2046110169540599810.json、图片生成/图生图/b-光影溶图融图qwen edit 2509_2005252378804842497.json、图片生成/图生图/ktv公主_1991635135160336386.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `ModelSamplingAuraFlow` —— 3/4 个有
- `CheckpointLoaderSimple` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `UNETLoader` —— 2/4 个有
- `VAELoader` —— 2/4 个有
- `CR Simple Image Compare` —— 1/4 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/4 个有
- `GetImageSize` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 20 | 4 | 27% |
| Prompt 约束强度(CFG) | 1.2 | 1 - 1.5 | 4 | 85% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 976 | 512 - 1024 | 4 | 76% |
| 高度 | 1332 | 512 - 1792 | 4 | 59% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 20，4 个样本，取值分散，一致性仅 27%
- Prompt 约束强度(CFG) 中位数 1.2，观测区间 1 - 1.5，4 个样本，取值集中（一致性 85%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 976，观测区间 512 - 1024，4 个样本
- 高度 中位数 1332，观测区间 512 - 1792，4 个样本
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足

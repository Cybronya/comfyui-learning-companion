---
name: unknown_workflow_sampler_clip_unet_18
type: Unknown Workflow
frequency: 15
level: weak
coverage: 0.8318
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageReel, LayerUtility: ImageReelComposit, CR Text, CR SDXL Aspect Ratio]
members: [图片生成/文生图/1954222888989683714.json, 图片生成/文生图/1954423623698280449.json, 图片生成/文生图/1954463793558515714.json, 图片生成/文生图/1954559302579187713.json, 图片生成/文生图/1954757119348240386.json, 图片生成/文生图/1954798087374987266.json, 图片生成/文生图/1954817663203721218.json, 图片生成/文生图/1954915934088544258.json, 图片生成/文生图/1954932387395223553.json, 图片生成/文生图/1954932461516963842.json, 图片生成/文生图/1955290519761928194.json, 图片生成/文生图/1955342392250417153.json, 图片生成/文生图/1956936946464296962.json, 图片生成/文生图/1959887822478061569.json, 图片生成/文生图/1961085397939982338.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_18

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/文生图/1954222888989683714.json、图片生成/文生图/1954423623698280449.json、图片生成/文生图/1954463793558515714.json、图片生成/文生图/1954559302579187713.json、图片生成/文生图/1954757119348240386.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 15 个 workflow 都包含：
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
- `LoraLoaderModelOnly` —— 14/15 个有
- `PreviewImage` —— 8/15 个有
- `LayerUtility: ImageReel` —— 6/15 个有
- `LayerUtility: ImageReelComposit` —— 6/15 个有
- `CR SDXL Aspect Ratio` —— 4/15 个有
- `CR Text` —— 4/15 个有
- `ConditioningZeroOut` —— 1/15 个有
- `DF_Get_image_size` —— 1/15 个有
- `Float` —— 1/15 个有
- `ImpactInt` —— 1/15 个有
- `Int` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 30 | 15 | 33% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 15 | 28% |
| 采样算法 | euler | - | 15 | 87% |
| 调度器 | simple | - | 15 | 93% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 27/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 30，15 个样本，取值分散，一致性仅 33%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，15 个样本，取值分散，一致性仅 28%
- 采样算法 最常用 euler，15 个样本，一致性 87%
- 调度器 最常用 simple，15 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（27/15 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageReel、LayerUtility: ImageReelComposit、CR Text、CR SDXL Aspect Ratio

---
name: unknown_workflow_sampler_clip_unet_62
type: Unknown Workflow
frequency: 9
level: weak
coverage: 0.812556
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [SDXL Resolutions (JPS)]
members: [图片生成/文生图/1971904444222926850.json, 图片生成/文生图/Z-IMAGE文生图_2017069432048193538.json, 图片生成/文生图/Z-Image Turbo 文生图_2012561031096176642.json, 图片生成/文生图/Z-Image Turbo 文生图_2013174546978836481.json, 图片生成/文生图/Z-Image-BEYOND REALITY SUPER Z IMAGE 3.0 淡妆浓抹_2018826875602214914.json, 图片生成/文生图/Z-Image-Base - 文生图 官方基础版_2016349336380121090.json, 图片生成/文生图/Z-Image-Base-Text to Image_2016308651929116673.json, 图片生成/文生图/Z-Image-Base文生图-自然美学v260128_2016358691083128834.json, 图片生成/文生图/文生图对比Z-Image-bf16 res vs bf16 euler vs turbo_2016748618899787777.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_62

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/1971904444222926850.json、图片生成/文生图/Z-IMAGE文生图_2017069432048193538.json、图片生成/文生图/Z-Image Turbo 文生图_2012561031096176642.json、图片生成/文生图/Z-Image Turbo 文生图_2013174546978836481.json、图片生成/文生图/Z-Image-BEYOND REALITY SUPER Z IMAGE 3.0 淡妆浓抹_2018826875602214914.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 8/9 个有
- `SDXL Resolutions (JPS)` —— 4/9 个有
- `ConditioningZeroOut` —— 3/9 个有
- `easy cleanGpuUsed` —— 3/9 个有
- `LayerUtility: ImageReel` —— 2/9 个有
- `LayerUtility: ImageReelComposit` —— 2/9 个有
- `EmptyChromaRadianceLatentImage` —— 1/9 个有
- `LoadImage` —— 1/9 个有
- `MuyeTextEditOutput` —— 1/9 个有
- `T5TokenizerOptions` —— 1/9 个有
- `easy seed` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 50 | 9 | 19% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 9 | 36% |
| 采样算法 | euler | - | 9 | 78% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 50，9 个样本，取值分散，一致性仅 19%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，9 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 euler，9 个样本，一致性 78%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：SDXL Resolutions (JPS)

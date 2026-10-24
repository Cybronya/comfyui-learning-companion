---
name: unknown_workflow_sampler_clip_vae_10
type: Unknown Workflow
frequency: 14
level: weak
coverage: 0.827429
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/AA--缓存加速Zimage-base-MeanCache5种加速模式对比_2019746684867190785.json, 图片生成/文生图/LH-DMT版本-2.生图片类-022.Z_image_turbo文生图_2016484426032619521.json, 图片生成/文生图/LH-DMT版本-2.生图片类-044.Qwen-Image-10步蒸馏-Q版3D人物_2016524825891704833.json, 图片生成/文生图/Neta Lumina新版Sota级动漫模型文生图_1948069349862060033.json, 图片生成/文生图/Nunchaku Rank128版本Qwen-Image极速版文生图V1_1959689364051800066.json, 图片生成/文生图/Nunchaku Rank128版本Qwen-Image极速版文生图V1_2038785728322215938.json, 图片生成/文生图/Nunchaku Rank128版本Qwen-Image极速版文生图V1_2039505785788567554.json, 图片生成/文生图/Nunchaku Rank128版本Qwen-Image极速版文生图V1_2039620069642211330.json, 图片生成/文生图/Nunchaku Rank128版本Qwen-Image极速版文生图V1_2042481267639328769.json, 图片生成/文生图/Nunchaku-Qwen-image-8步极速出图_1960003368511025153.json, 图片生成/文生图/Z-ImageBase-MeanCache加速-文生图_2019218139791237121.json, 图片生成/文生图/Z-image对比测试工作流_2068508638993534977.json, 图片生成/文生图/Z-image模型 与 Engineer v6 交叉对比-测试工作流_2065276186162458626.json, 图片生成/文生图/Z-turbo Engineer v6对比工作流_2064619941457907714.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_10

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/AA--缓存加速Zimage-base-MeanCache5种加速模式对比_2019746684867190785.json、图片生成/文生图/LH-DMT版本-2.生图片类-022.Z_image_turbo文生图_2016484426032619521.json、图片生成/文生图/LH-DMT版本-2.生图片类-044.Qwen-Image-10步蒸馏-Q版3D人物_2016524825891704833.json、图片生成/文生图/Neta Lumina新版Sota级动漫模型文生图_1948069349862060033.json、图片生成/文生图/Nunchaku Rank128版本Qwen-Image极速版文生图V1_1959689364051800066.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 8/14 个有
- `LayerUtility: PurgeVRAM` —— 6/14 个有
- `NunchakuQwenImageDiTLoader` —— 6/14 个有
- `AddLabel` —— 4/14 个有
- `CR Prompt Text` —— 4/14 个有
- `ImageConcatMulti` —— 4/14 个有
- `easy seed` —— 3/14 个有
- `ClipLoaderGGUF` —— 2/14 个有
- `ConditioningZeroOut` —— 2/14 个有
- `GetNode` —— 2/14 个有
- `LoraLoaderModelOnly` —— 2/14 个有
- `MeanCache_ZImage` —— 2/14 个有
- `SetNode` —— 2/14 个有
- `PreviewImage` —— 1/14 个有
- `TeaCache` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 50 | 14 | 33% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 5.5 | 14 | 44% |
| 采样算法 | euler | - | 14 | 50% |
| 调度器 | simple | - | 14 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 50，14 个样本，取值分散，一致性仅 33%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 5.5，14 个样本，取值分散，一致性仅 44%
- 采样算法 最常用 euler，14 个样本，一致性 50%
- 调度器 最常用 simple，14 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（10/14 个样本）：Steps较低可能导致细节不足

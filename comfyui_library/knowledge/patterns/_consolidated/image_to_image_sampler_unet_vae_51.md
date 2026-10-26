---
name: image_to_image_sampler_unet_vae_51
type: Image To Image
frequency: 3
level: moderate
coverage: 0.843667
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, ReferenceLatent, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/多图编辑Flux.2 Klein自用_2093617848798244866.json, 图片生成/文生图/Qwen Image Edit 2511 基础图像编辑_2003694338204942337.json, 图片生成/文生图/Qwen-Image-Edit-2511图片人物+场景+打光+全节点注释_2055894861483651073.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_51

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/多图编辑Flux.2 Klein自用_2093617848798244866.json、图片生成/文生图/Qwen Image Edit 2511 基础图像编辑_2003694338204942337.json、图片生成/文生图/Qwen-Image-Edit-2511图片人物+场景+打光+全节点注释_2055894861483651073.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `ConstrainImage|pysssss` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `ImageScale` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `SDXL Empty Latent Image (rgthree)` —— 1/3 个有
- `SeedVR2` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 4 - 20 | 3 | 24% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 4 - 20，3 个样本，取值分散，一致性仅 24%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足

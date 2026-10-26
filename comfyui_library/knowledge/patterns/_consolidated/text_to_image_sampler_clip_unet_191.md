---
name: text_to_image_sampler_clip_unet_191
type: Text To Image
frequency: 3
level: moderate
coverage: 0.927667
common_nodes: [AddLabel, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, ImageConcanate, KSampler, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader, easy globalSeed, easy promptList]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen image 2512 文生图_2006546319086723074.json, 图片生成/文生图/Z image_VS_Qwen image2512对比_2006540775126994945.json, 图片生成/文生图/既生瑜何生亮，Zimage_VS_2512_2006333323450261505.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_191

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Qwen image 2512 文生图_2006546319086723074.json、图片生成/文生图/Z image_VS_Qwen image2512对比_2006540775126994945.json、图片生成/文生图/既生瑜何生亮，Zimage_VS_2512_2006333323450261505.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `AddLabel`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImageConcanate`
- `KSampler`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy globalSeed`
- `easy promptList`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImageScaleBy` —— 1/3 个有
- `MemoryCleaner` —— 1/3 个有
- `SeedVR2LoadDiTModel` —— 1/3 个有
- `SeedVR2LoadVAEModel` —— 1/3 个有
- `SeedVR2VideoUpscaler` —— 1/3 个有
- `easy clearCacheAll` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 8 - 30 | 3 | 35% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 3 | 29% |
| 采样算法 | euler_ancestral | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 928 | 928 - 1080 | 3 | 93% |
| 高度 | 1664 | 1664 - 1920 | 3 | 93% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 8 - 30，3 个样本，取值分散，一致性仅 35%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，3 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 928，观测区间 928 - 1080，3 个样本，取值集中（一致性 93%）
- 高度 中位数 1664，观测区间 1664 - 1920，3 个样本，取值集中（一致性 93%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足

---
name: text_to_image_sampler_clip_unet_168
type: Text To Image
frequency: 4
level: moderate
coverage: 0.923
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen image 2512 文生图_2006546319086723074.json, 图片生成/文生图/Qwen-image-2.1-文生图_2101847911167520770.json, 图片生成/文生图/Z image_VS_Qwen image2512对比_2006540775126994945.json, 图片生成/文生图/既生瑜何生亮，Zimage_VS_2512_2006333323450261505.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_168

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Qwen image 2512 文生图_2006546319086723074.json、图片生成/文生图/Qwen-image-2.1-文生图_2101847911167520770.json、图片生成/文生图/Z image_VS_Qwen image2512对比_2006540775126994945.json、图片生成/文生图/既生瑜何生亮，Zimage_VS_2512_2006333323450261505.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 3/4 个有
- `ImageConcanate` —— 3/4 个有
- `easy globalSeed` —— 3/4 个有
- `easy promptList` —— 3/4 个有
- `Fast Groups Muter (rgthree)` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `ImageScaleBy` —— 1/4 个有
- `MemoryCleaner` —— 1/4 个有
- `QwenImage21Cache` —— 1/4 个有
- `SeedVR2LoadDiTModel` —— 1/4 个有
- `SeedVR2LoadVAEModel` —— 1/4 个有
- `SeedVR2VideoUpscaler` —— 1/4 个有
- `easy clearCacheAll` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 17 | 8 - 30 | 4 | 46% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 4 | 26% |
| 采样算法 | euler_ancestral | - | 4 | 75% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 976 | 928 - 1080 | 4 | 93% |
| 高度 | 1664 | 1024 - 1920 | 4 | 79% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 17，观测区间 8 - 30，4 个样本，取值分散，一致性仅 46%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，4 个样本，取值分散，一致性仅 26%
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 976，观测区间 928 - 1080，4 个样本，取值集中（一致性 93%）
- 高度 中位数 1664，观测区间 1024 - 1920，4 个样本
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足

---
name: text_to_image_sampler_clip_vae_4
type: Text To Image
frequency: 15
level: moderate
coverage: 0.883133
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/N-Super Z-image 3.0+lota文生图_2020339880995332097.json, 图片生成/文生图/None Z-image-Turbo CFG解锁版（提高高频信息）_1999533655208980481.json, 图片生成/文生图/Nunchaku极速版Z-image文生图_2005527503991177218.json, 图片生成/文生图/Nunchaku超级加速版Z-image文生图v1_2005116765585764354.json, 图片生成/文生图/Red-Z image Distilled Base加速版文生图V1_2018000841084506113.json, 图片生成/文生图/Super Z-image 3.0文生图_2018000830837825538.json, 图片生成/文生图/Super Z-image 3.0文生图批量跑 浮云2.6_2019676814746066946.json, 图片生成/文生图/Super Z-image 文生图_2018521699486015489.json, 图片生成/文生图/Z-Image Turbo VS De-Turbo VS Re-Turbo对比_2073390583678332930.json, 图片生成/文生图/Z-Image-Base Turbo  Art distilled  super图像对比_2018274455566426114.json, 图片生成/文生图/Z-Image-Base Vs Turbo Vs Art vs distilled vs super_2017968997358112769.json, 图片生成/文生图/Z-Image-Base Vs Turbo Vs Art_2017613257602768897.json, 图片生成/文生图/Z-Image-Base Vs Turbo Vs Art图像对比_2017854026301317122.json, 图片生成/文生图/Z-Image-Base 多种加速方式对比_2019021050884923393.json, 图片生成/文生图/boogu-trubo VS boogu-base VS Z-image-trubo—图像对比_2068142561574866946.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_4

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/文生图/N-Super Z-image 3.0+lota文生图_2020339880995332097.json、图片生成/文生图/None Z-image-Turbo CFG解锁版（提高高频信息）_1999533655208980481.json、图片生成/文生图/Nunchaku极速版Z-image文生图_2005527503991177218.json、图片生成/文生图/Nunchaku超级加速版Z-image文生图v1_2005116765585764354.json、图片生成/文生图/Red-Z image Distilled Base加速版文生图V1_2018000841084506113.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 14/15 个有
- `CR Prompt Text` —— 13/15 个有
- `PrimitiveInt` —— 10/15 个有
- `LayerUtility: PurgeVRAM` —— 9/15 个有
- `ImageConcatMulti` —— 7/15 个有
- `AddLabel` —— 6/15 个有
- `EmptySD3LatentImage` —— 6/15 个有
- `ModelSamplingAuraFlow` —— 6/15 个有
- `ConditioningZeroOut` —— 5/15 个有
- `LoraLoaderModelOnly` —— 3/15 个有
- `easy promptLine` —— 3/15 个有
- `NunchakuZImageDiTLoader` —— 2/15 个有
- `DuckHideNode` —— 1/15 个有
- `Int` —— 1/15 个有
- `MeanCache_ZImage` —— 1/15 个有
- `PreviewImage` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1024 - 1920 | 15 | 76% |
| 高度 | 1920 | 1080 - 1920 | 15 | 82% |
| 采样步数 | 15 | 8 - 50 | 15 | 25% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 15 | 33% |
| 采样算法 | euler | - | 15 | 60% |
| 调度器 | simple | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 1024 - 1920，15 个样本
- 高度 中位数 1920，观测区间 1080 - 1920，15 个样本，取值集中（一致性 82%）
- 采样步数 中位数 15，观测区间 8 - 50，15 个样本，取值分散，一致性仅 25%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，15 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 euler，15 个样本，一致性 60%
- 调度器 最常用 simple，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（15/15 个样本）：Steps较低可能导致细节不足

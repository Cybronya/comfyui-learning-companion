---
name: text_to_image_sampler_clip_unet_123
type: Text To Image
frequency: 6
level: moderate
coverage: 0.865833
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptyLatentImage, KSampler, LayerUtility: PurgeVRAM, PrimitiveInt, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image-Base Turbo  Art distilled  super图像对比_2018274455566426114.json, 图片生成/文生图/Z-Image-Base Vs Turbo Vs Art vs distilled vs super_2017968997358112769.json, 图片生成/文生图/Z-Image-Base Vs Turbo Vs Art_2017613257602768897.json, 图片生成/文生图/Z-Image-Base Vs Turbo Vs Art图像对比_2017854026301317122.json, 图片生成/文生图/Z-Image-Base 多种加速方式对比_2019021050884923393.json, 图片生成/文生图/贞贞lora多重z-image版本对比_2018006131871846401.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_123

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Z-Image-Base Turbo  Art distilled  super图像对比_2018274455566426114.json、图片生成/文生图/Z-Image-Base Vs Turbo Vs Art vs distilled vs super_2017968997358112769.json、图片生成/文生图/Z-Image-Base Vs Turbo Vs Art_2017613257602768897.json、图片生成/文生图/Z-Image-Base Vs Turbo Vs Art图像对比_2017854026301317122.json、图片生成/文生图/Z-Image-Base 多种加速方式对比_2019021050884923393.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptyLatentImage`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `PrimitiveInt`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 5/6 个有
- `EmptySD3LatentImage` —— 5/6 个有
- `ImageConcatMulti` —— 5/6 个有
- `ModelSamplingAuraFlow` —— 5/6 个有
- `LoraLoaderModelOnly` —— 2/6 个有
- `MeanCache_ZImage` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 15 | 8 - 50 | 6 | 31% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 6 | 29% |
| 采样算法 | res_multistep | - | 6 | 67% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1080 | 1080 - 1080 | 6 | 100% |
| 高度 | 1920 | 1920 - 1920 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 15，观测区间 8 - 50，6 个样本，取值分散，一致性仅 31%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，6 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 res_multistep，6 个样本，一致性 67%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 1080 - 1080，6 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，6 个样本，取值集中（一致性 100%）
- 高发问题（17/6 个样本）：Steps较低可能导致细节不足

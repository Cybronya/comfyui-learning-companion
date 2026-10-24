---
name: text_to_image_sampler_clip_unet_119
type: Text To Image
frequency: 6
level: weak
coverage: 0.869667
common_nodes: [AddLabel, CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, ModelSamplingAuraFlow, PrimitiveInt, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image-Base Turbo  Art distilled  super图像对比_2018274455566426114.json, 图片生成/文生图/Z-Image-Base Vs Turbo Vs Art vs distilled vs super_2017968997358112769.json, 图片生成/文生图/Z-Image-Base Vs Turbo Vs Art_2017613257602768897.json, 图片生成/文生图/Z-Image-Base Vs Turbo Vs Art图像对比_2017854026301317122.json, 图片生成/文生图/Z-Image-Base 多种加速方式对比_2019021050884923393.json, 图片生成/文生图/动漫生图｜Anima base v1官方文生图直出_2089769718608650241.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_119

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Z-Image-Base Turbo  Art distilled  super图像对比_2018274455566426114.json、图片生成/文生图/Z-Image-Base Vs Turbo Vs Art vs distilled vs super_2017968997358112769.json、图片生成/文生图/Z-Image-Base Vs Turbo Vs Art_2017613257602768897.json、图片生成/文生图/Z-Image-Base Vs Turbo Vs Art图像对比_2017854026301317122.json、图片生成/文生图/Z-Image-Base 多种加速方式对比_2019021050884923393.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `AddLabel`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `PrimitiveInt`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 5/6 个有
- `EmptySD3LatentImage` —— 5/6 个有
- `ImageConcatMulti` —— 5/6 个有
- `LayerUtility: PurgeVRAM` —— 5/6 个有
- `LoraLoaderModelOnly` —— 2/6 个有
- `JjkText` —— 1/6 个有
- `MeanCache_ZImage` —— 1/6 个有
- `solarL_SaveImagesToZip` —— 1/6 个有
- `孤海注释` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 15 | 4 - 50 | 6 | 20% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4.5 | 6 | 38% |
| 采样算法 | res_multistep | - | 6 | 67% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1080 | 80 - 1080 | 6 | 59% |
| 高度 | 1920 | 80 - 1920 | 6 | 57% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 15，观测区间 4 - 50，6 个样本，取值分散，一致性仅 20%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4.5，6 个样本，取值分散，一致性仅 38%
- 采样算法 最常用 res_multistep，6 个样本，一致性 67%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 80 - 1080，6 个样本
- 高度 中位数 1920，观测区间 80 - 1920，6 个样本
- 高发问题（12/6 个样本）：Steps较低可能导致细节不足

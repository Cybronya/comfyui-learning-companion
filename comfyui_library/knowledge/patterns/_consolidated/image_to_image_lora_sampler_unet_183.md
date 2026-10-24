---
name: image_to_image_lora_sampler_unet_183
type: Image To Image
frequency: 3
level: moderate
coverage: 0.801667
common_nodes: [CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【楚心钟陌】返璞归真基础流_2019019903289794561.json, 图片生成/图生图/一键生成Hello Kitty中国风头像_2013190174729052161.json, 图片生成/图生图/一键美瞳_2009605418158399489.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_183

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/【楚心钟陌】返璞归真基础流_2019019903289794561.json、图片生成/图生图/一键生成Hello Kitty中国风头像_2013190174729052161.json、图片生成/图生图/一键美瞳_2009605418158399489.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 2/3 个有
- `FluxKontextMultiReferenceLatentMethod` —— 2/3 个有
- `LayerUtility: ImageReel` —— 2/3 个有
- `LayerUtility: ImageReelComposit` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `ImageScale` —— 1/3 个有
- `Text` —— 1/3 个有
- `TextEncodeQwenImageEdit` —— 1/3 个有
- `Textbox` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 3 | 53% |
| Prompt 约束强度(CFG) | 1 | 0.99 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 0.8 - 1 | 3 | 90% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 0.99 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.8 - 1，3 个样本，取值集中（一致性 90%）
- 风险：Prompt 约束强度(CFG) 观测到 0.99，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足

---
name: image_to_image_lora_sampler_unet_222
type: Image To Image
frequency: 3
level: moderate
coverage: 0.956667
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图片转刺绣风格加抠图new_2043883856301920257.json, 图片生成/图生图/电商产品多视角_1992474545672220673.json, 图片生成/图生图/🐱Qwen-image-edit2509图案提取器v3_言灵ru😼_2005647151185227777.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_222

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/图片转刺绣风格加抠图new_2043883856301920257.json、图片生成/图生图/电商产品多视角_1992474545672220673.json、图片生成/图生图/🐱Qwen-image-edit2509图案提取器v3_言灵ru😼_2005647151185227777.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerMask: BiRefNetUltraV2` —— 2/3 个有
- `LayerMask: LoadBiRefNetModelV2` —— 2/3 个有
- `easy imageSize` —— 2/3 个有
- `FastCanvas` —— 1/3 个有
- `FastCanvasTool` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImageCompositeMasked` —— 1/3 个有
- `InvertMask` —— 1/3 个有
- `JoinImageWithAlpha` —— 1/3 个有
- `LayerUtility: ColorImage` —— 1/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 3 | 65% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 3 | 65% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 0.99 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.99 - 1，3 个样本，取值集中（一致性 100%）

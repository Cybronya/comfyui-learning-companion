---
name: image_to_image_lora_sampler_unet_125
type: Image To Image
frequency: 5
level: moderate
coverage: 0.8818
common_nodes: [CFGNorm, CLIPLoader, CR Text, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen edit+SRL光影增强_轮廓光_1965037498328076289.json, 图片生成/图生图/Qwen_edit+SRL光影增强_轮廓光_2097888446189760513.json, 图片生成/图生图/Qwen_edit+SRL光影增强_轮廓光_2099415976717672449.json, 图片生成/图生图/光影增强_轮廓光_发丝灯_V4_1961853735989350401.json, 图片生成/图生图/千问Edit重新打光_1965112456316076033.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_125

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen edit+SRL光影增强_轮廓光_1965037498328076289.json、图片生成/图生图/Qwen_edit+SRL光影增强_轮廓光_2097888446189760513.json、图片生成/图生图/Qwen_edit+SRL光影增强_轮廓光_2099415976717672449.json、图片生成/图生图/光影增强_轮廓光_发丝灯_V4_1961853735989350401.json、图片生成/图生图/千问Edit重新打光_1965112456316076033.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Text`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 4/5 个有
- `HSLColorNode` —— 4/5 个有
- `LayerColor: ColorTemperature` —— 4/5 个有
- `easy imageConcat` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `LayerUtility: PurgeVRAM` —— 3/5 个有
- `SeedVR2` —— 3/5 个有
- `SeedVR2BlockSwap` —— 3/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 5 | 54% |
| Prompt 约束强度(CFG) | 2.5 | 2.5 - 2.5 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，5 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 2.5 - 2.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足

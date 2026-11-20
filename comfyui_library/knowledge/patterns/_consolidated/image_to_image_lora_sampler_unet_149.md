---
name: image_to_image_lora_sampler_unet_149
type: Image To Image
frequency: 4
level: strong
coverage: 0.8785
common_nodes: [CFGNorm, CLIPLoader, CR Text, ColorMatch, HSLColorNode, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LayerColor: ColorTemperature, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageConcat]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen edit+SRL光影增强_轮廓光_1965037498328076289.json, 图片生成/图生图/Qwen_edit+SRL光影增强_轮廓光_2097888446189760513.json, 图片生成/图生图/Qwen_edit+SRL光影增强_轮廓光_2099415976717672449.json, 图片生成/图生图/光影增强_轮廓光_发丝灯_V4_1961853735989350401.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_149

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen edit+SRL光影增强_轮廓光_1965037498328076289.json、图片生成/图生图/Qwen_edit+SRL光影增强_轮廓光_2097888446189760513.json、图片生成/图生图/Qwen_edit+SRL光影增强_轮廓光_2099415976717672449.json、图片生成/图生图/光影增强_轮廓光_发丝灯_V4_1961853735989350401.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Text`
- `ColorMatch`
- `HSLColorNode`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LayerColor: ColorTemperature`
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
- `easy imageConcat`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `LayerUtility: PurgeVRAM` —— 3/4 个有
- `SeedVR2` —— 3/4 个有
- `SeedVR2BlockSwap` —— 3/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 2.5 | 2.5 - 2.5 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 2.5 - 2.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足

---
name: image_to_image_lora_sampler_unet_141
type: Image To Image
frequency: 5
level: moderate
coverage: 0.933
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/小象URL_2013143198536835074.json, 图片生成/图生图/小象URL_2014201425718415362.json, 图片生成/图生图/建筑夜景转换  qwen_image_edit_2511_2007012600965505025.json, 图片生成/图生图/美颜-化妆编辑-妆容增强-FireRed-Image-Edit工作流_2030558270418591745.json, 图片生成/文生图/2030095760506753026.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_141

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/小象URL_2013143198536835074.json、图片生成/图生图/小象URL_2014201425718415362.json、图片生成/图生图/建筑夜景转换  qwen_image_edit_2511_2007012600965505025.json、图片生成/图生图/美颜-化妆编辑-妆容增强-FireRed-Image-Edit工作流_2030558270418591745.json、图片生成/文生图/2030095760506753026.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
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
- `FluxKontextImageScale` —— 4/5 个有
- `Image Comparer (rgthree)` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `ImpactInt` —— 2/5 个有
- `LoadRembgByBiRefNetModel` —— 2/5 个有
- `RembgByBiRefNet` —— 2/5 个有
- `CR Prompt Text` —— 1/5 个有
- `EmptyLatentImage` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `LoadImagesFromURL` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 25 | 5 | 57% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 5 | 61% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | karras | - | 5 | 40% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1920 | - | 1 | 100% |
| 高度 | 1080 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 25，5 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 karras，5 个样本，一致性 40%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足

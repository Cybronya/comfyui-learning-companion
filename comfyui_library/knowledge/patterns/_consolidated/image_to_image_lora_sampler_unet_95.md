---
name: image_to_image_lora_sampler_unet_95
type: Image To Image
frequency: 8
level: moderate
coverage: 0.876375
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen edit 图像编辑_1970750998853677057.json, 图片生成/图生图/Qwen 图片编辑（提示词改图）_1982720861146882049.json, 图片生成/图生图/Qwen 生成产品包裹类场景_1995337597046153217.json, 图片生成/图生图/Qwen 白底图 电商产品换背景_1998035851756077058.json, 图片生成/图生图/☯️Qwen 产品一键白底换背景_1987620274281582594.json, 图片生成/图生图/千问Edit重新打光_1965112456316076033.json, 图片生成/图生图/🥨Qwen 白底换背景 电商换背景🥨_1986265387476144129.json, 图片生成/图生图/🥯Qwen edit一句话改变图片！国产之光 千问图片编辑🥯_1958089759602126850.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_95

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Qwen edit 图像编辑_1970750998853677057.json、图片生成/图生图/Qwen 图片编辑（提示词改图）_1982720861146882049.json、图片生成/图生图/Qwen 生成产品包裹类场景_1995337597046153217.json、图片生成/图生图/Qwen 白底图 电商产品换背景_1998035851756077058.json、图片生成/图生图/☯️Qwen 产品一键白底换背景_1987620274281582594.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 7/8 个有
- `ImageScaleToTotalPixels` —— 7/8 个有
- `CR Text` —— 6/8 个有
- `ImageResizeKJv2` —— 4/8 个有
- `PreviewImage` —— 4/8 个有
- `StringFunction|pysssss` —— 4/8 个有
- `TextEncodeQwenImageEdit` —— 4/8 个有
- `TextEncodeQwenImageEditPlus` —— 4/8 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 4/8 个有
- `ImpactInt` —— 3/8 个有
- `Note Plus (mtb)` —— 3/8 个有
- `easy imageRemBg` —— 3/8 个有
- `LoadImageFromUrl` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | 8 - 20 | 8 | 57% |
| Prompt 约束强度(CFG) | 1.75 | 1 - 3 | 8 | 54% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 0.8 - 1 | 8 | 93% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，观测区间 8 - 20，8 个样本
- Prompt 约束强度(CFG) 中位数 1.75，观测区间 1 - 3，8 个样本
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.8 - 1，8 个样本，取值集中（一致性 93%）
- 高发问题（4/8 个样本）：Steps较低可能导致细节不足

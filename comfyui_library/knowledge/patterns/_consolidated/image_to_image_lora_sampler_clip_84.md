---
name: image_to_image_lora_sampler_clip_84
type: Image To Image
frequency: 3
level: strong
coverage: 0.716333
common_nodes: [Any Switch (rgthree), CFGNorm, CLIPLoader, CLIPTextEncode, CR Latent Input Switch, CR Text Concatenate, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), Fast Groups Muter (rgthree), FastCanvas, FastCanvasTool, ImageConcatMulti, ImageScaleToMegapixels, Int, JjkText, KSampler, LayerUtility: PurgeVRAM V2, LoadImage, Lora Loader Stack (rgthree), ModelSamplingAuraFlow, PreviewImage, PrimitiveStringMultiline, SaveImage, SeedVR2GGUF, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageConcat, easy imageRemBg]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/AI短剧角色站位-Qwen-image-edit2509 Plus自动or手动调整位置 多图融合生图_1961293749953433602.json, 图片生成/图生图/AI短剧角色站位-Qwen-image-edit2509 Plus自动or手动调整位置 多图融合生图_2010366718249537538.json, 图片生成/图生图/电商模特商品展示（可任意调整人物、物品位置大小）Qwen-image-edit2509_1993354492504637442.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_84

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/AI短剧角色站位-Qwen-image-edit2509 Plus自动or手动调整位置 多图融合生图_1961293749953433602.json、图片生成/图生图/AI短剧角色站位-Qwen-image-edit2509 Plus自动or手动调整位置 多图融合生图_2010366718249537538.json、图片生成/图生图/电商模特商品展示（可任意调整人物、物品位置大小）Qwen-image-edit2509_1993354492504637442.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Latent Input Switch`
- `CR Text Concatenate`
- `EmptySD3LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Muter (rgthree)`
- `FastCanvas`
- `FastCanvasTool`
- `ImageConcatMulti`
- `ImageScaleToMegapixels`
- `Int`
- `JjkText`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `Lora Loader Stack (rgthree)`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `SaveImage`
- `SeedVR2GGUF`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageConcat`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `Wuji360Panorama` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足

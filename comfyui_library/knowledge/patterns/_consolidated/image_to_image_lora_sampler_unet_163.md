---
name: image_to_image_lora_sampler_unet_163
type: Image To Image
frequency: 3
level: weak
coverage: 0.830333
common_nodes: [CFGNorm, CLIPLoader, FluxKontextImageScale, GetImageSize, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/69.tonnie-2511扩图_2010311843973177346.json, 图片生成/图生图/73.tonnie-2511换脸（效果不好）_2010883623301419009.json, 图片生成/图生图/Qwen edit 2511无像素偏移_2004837793459306497.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_163

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/69.tonnie-2511扩图_2010311843973177346.json、图片生成/图生图/73.tonnie-2511换脸（效果不好）_2010883623301419009.json、图片生成/图生图/Qwen edit 2511无像素偏移_2004837793459306497.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextImageScale`
- `GetImageSize`
- `Image Comparer (rgthree)`
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
- `CLIPTextEncode` —— 2/3 个有
- `Image Blank` —— 2/3 个有
- `ImageCompositeMasked` —— 2/3 个有
- `JoinImageWithAlpha` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `ReferenceLatent` —— 2/3 个有
- `CropFace` —— 1/3 个有
- `DifferentialDiffusion` —— 1/3 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/3 个有
- `ImagePadForOutpaint` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `Mask Fill Holes` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 1 - 10 | 3 | 25% |
| Prompt 约束强度(CFG) | 1 | 1 - 10 | 3 | 0% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 1 - 10，3 个样本，取值分散，一致性仅 25%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 10，3 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足

---
name: text_to_image_upscale_sampler_clip_24
type: Text To Image
frequency: 5
level: strong
coverage: 0.896
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Image Comparer (rgthree), KSampler, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/2号特工：Z-image-base文生图+人脸Lora+seedvr2超分放大_2076991277698211841.json, 图片生成/文生图/Krea 2文生图+高清4K放大_2069681674400653314.json, 图片生成/文生图/Qwen-2512 直出最强电影艺术照片_2033840471654539266.json, 图片生成/文生图/Z-Image + 4K超清放大_1995496468943396865.json, 图片生成/文生图/自-z image turbo文生图_2080539022929260546.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_24

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/2号特工：Z-image-base文生图+人脸Lora+seedvr2超分放大_2076991277698211841.json、图片生成/文生图/Krea 2文生图+高清4K放大_2069681674400653314.json、图片生成/文生图/Qwen-2512 直出最强电影艺术照片_2033840471654539266.json、图片生成/文生图/Z-Image + 4K超清放大_1995496468943396865.json、图片生成/文生图/自-z image turbo文生图_2080539022929260546.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `ImageScaleBy` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `ModelSamplingAuraFlow` —— 2/5 个有
- `Int` —— 1/5 个有
- `LayerUtility: ImageReel` —— 1/5 个有
- `LayerUtility: ImageReelComposit` —— 1/5 个有
- `SaveImagePlus` —— 1/5 个有
- `Text` —— 1/5 个有
- `easy seed` —— 1/5 个有
- `easy stylesSelector` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1280 | 5 | 70% |
| 高度 | 1536 | 512 - 1920 | 5 | 64% |
| 采样步数 | 9 | 8 - 10 | 5 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1280，5 个样本
- 高度 中位数 1536，观测区间 512 - 1920，5 个样本
- 采样步数 中位数 9，观测区间 8 - 10，5 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（3/5 个样本）：Steps较低可能导致细节不足

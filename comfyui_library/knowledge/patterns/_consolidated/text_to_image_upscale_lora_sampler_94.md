---
name: text_to_image_upscale_lora_sampler_94
type: Text To Image
frequency: 3
level: moderate
coverage: 0.890667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Image Comparer (rgthree), KSampler, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/2号特工：Z-image-base文生图+人脸Lora+seedvr2超分放大_2076991277698211841.json, 图片生成/文生图/Krea 2文生图+高清4K放大_2069681674400653314.json, 图片生成/文生图/Qwen-2512 直出最强电影艺术照片_2033840471654539266.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_94

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/2号特工：Z-image-base文生图+人脸Lora+seedvr2超分放大_2076991277698211841.json、图片生成/文生图/Krea 2文生图+高清4K放大_2069681674400653314.json、图片生成/文生图/Qwen-2512 直出最强电影艺术照片_2033840471654539266.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `ImageScaleBy` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `Int` —— 1/3 个有
- `LayerUtility: ImageReel` —— 1/3 个有
- `LayerUtility: ImageReelComposit` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `SaveImagePlus` —— 1/3 个有
- `Text` —— 1/3 个有
- `easy seed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 720 | 512 - 1280 | 3 | 61% |
| 高度 | 1280 | 512 - 1920 | 3 | 53% |
| 采样步数 | 10 | 8 - 10 | 3 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | res_multistep | - | 3 | 33% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 720，观测区间 512 - 1280，3 个样本
- 高度 中位数 1280，观测区间 512 - 1920，3 个样本
- 采样步数 中位数 10，观测区间 8 - 10，3 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，3 个样本，一致性 33%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）

---
name: image_to_image_upscale_sampler_clip_5
type: Image To Image
frequency: 3
level: moderate
coverage: 0.788667
common_nodes: [CLIPTextEncode, Florence2ModelLoader, Florence2Run, Image Comparer (rgthree), ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, LoadImage, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch]
problems: [发现KSampler但没有VAEDecode, Steps较低可能导致细节不足]
missing: [easy imageBatchToImageList, easy imageListToImageBatch, Latent Noise Injection]
members: [图片生成/文生图/1987808205147451394.json, 图片生成/文生图/1988253883254358017.json, 图片生成/文生图/Z-Image-base放大_2016768153547710466.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_5

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1987808205147451394.json、图片生成/文生图/1988253883254358017.json、图片生成/文生图/Z-Image-base放大_2016768153547710466.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `Florence2ModelLoader`
- `Florence2Run`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 2/3 个有
- `ConditioningZeroOut` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `CFGNorm` —— 1/3 个有
- `DualCLIPLoader` —— 1/3 个有
- `DyPE_FLUX` —— 1/3 个有
- `Latent Noise Injection` —— 1/3 个有
- `ModelPatchTorchSettings` —— 1/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `Seed (rgthree)` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 3 | 53% |
| Prompt 约束强度(CFG) | 1.1 | 1 - 3 | 3 | 46% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 0.3 | 0.25 - 0.35 | 3 | 86% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 3/3 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 1.1，观测区间 1 - 3，3 个样本，取值分散，一致性仅 46%
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 0.3，观测区间 0.25 - 0.35，3 个样本，取值集中（一致性 86%）
- 高发问题（3/3 个样本）：发现KSampler但没有VAEDecode
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：easy imageBatchToImageList、easy imageListToImageBatch、Latent Noise Injection

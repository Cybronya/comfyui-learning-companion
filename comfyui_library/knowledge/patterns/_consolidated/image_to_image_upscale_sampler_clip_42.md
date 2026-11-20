---
name: image_to_image_upscale_sampler_clip_42
type: Image To Image
frequency: 4
level: moderate
coverage: 0.877
common_nodes: [CLIPTextEncode, Image Comparer (rgthree), ImageListToImageBatch, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, LoadImage, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/TTP放大_2037113135659749378.json, 平台全量/人像高清放大TTP+WAN 2.2修复皮肤质感和面部细节V1_2025844790520188929.json, 平台全量/高清放大-ttp-klein_2091312070460534785.json, 平台全量/（TTP+Wan2.2）批量去油放大精修增加写实质感_1990616290475872258.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_42

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/TTP放大_2037113135659749378.json、平台全量/人像高清放大TTP+WAN 2.2修复皮肤质感和面部细节V1_2025844790520188929.json、平台全量/高清放大-ttp-klein_2091312070460534785.json、平台全量/（TTP+Wan2.2）批量去油放大精修增加写实质感_1990616290475872258.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `Image Comparer (rgthree)`
- `ImageListToImageBatch`
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
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `ImpactImageBatchToImageList` —— 2/4 个有
- `ModelSamplingSD3` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `easy imageBatchToImageList` —— 2/4 个有
- `DualCLIPLoader` —— 1/4 个有
- `Flux2KleinEditTextEncode_EditUtils` —— 1/4 个有
- `ImageResize+` —— 1/4 个有
- `JJC_JoyCaption` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `LoraLoader` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `easy imageSize` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |
| 采样步数 | 7 | 2 - 10 | 4 | 45% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 50% |
| 调度器 | beta | - | 4 | 50% |
| 重绘幅度 | 0.19 | 0.1 - 0.4 | 4 | 42% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7，观测区间 2 - 10，4 个样本，取值分散，一致性仅 45%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 50%
- 调度器 最常用 beta，4 个样本，一致性 50%
- 重绘幅度 中位数 0.19，观测区间 0.1 - 0.4，4 个样本，取值分散，一致性仅 42%
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足

---
name: image_to_image_upscale_sampler_clip_10
type: Image To Image
frequency: 10
level: weak
coverage: 0.9167
common_nodes: [CLIPTextEncode, Image Comparer (rgthree), ImageUpscaleWithModel, KSampler, LoadImage, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/4K无损人像放大_1970494670352621570.json, 图片生成/图生图/FLUX TTP分块高清放大_1910944667330932737.json, 图片生成/图生图/FULX高清放大-提速增质_2068164749141037057.json, 图片生成/图生图/Klein_一致性高清放大_2081656038633332738.json, 图片生成/图生图/Klein_一致性高清放大_2083363280915099649.json, 图片生成/图生图/Klein_一致性高清放大_2083375107824771074.json, 图片生成/图生图/Klein_一致性高清放大_2087385336187023362.json, 图片生成/图生图/Klein_多角度视角切换_2083359034417172482.json, 图片生成/图生图/Klein_多角度视角切换_2083369368465002497.json, 图片生成/图生图/全能万物迁移（产品、颜色、服装、饰品、光影迁移）_2088527787975069697.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_10

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/4K无损人像放大_1970494670352621570.json、图片生成/图生图/FLUX TTP分块高清放大_1910944667330932737.json、图片生成/图生图/FULX高清放大-提速增质_2068164749141037057.json、图片生成/图生图/Klein_一致性高清放大_2081656038633332738.json、图片生成/图生图/Klein_一致性高清放大_2083363280915099649.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `Image Comparer (rgthree)`
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

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 9/10 个有
- `FluxGuidance` —— 9/10 个有
- `ImageListToImageBatch` —— 9/10 个有
- `LoraLoaderModelOnly` —— 9/10 个有
- `CLIPLoader` —— 8/10 个有
- `ImageScaleToTotalPixels` —— 8/10 个有
- `ImpactImageBatchToImageList` —— 8/10 个有
- `VAEEncodeTiled` —— 8/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/10 个有
- `PrimitiveInt` —— 7/10 个有
- `ReferenceLatent` —— 7/10 个有
- `SZ_KleinTiledKSampler` —— 7/10 个有
- `DualCLIPLoader` —— 3/10 个有
- `GetImageSize+` —— 3/10 个有
- `PainterFluxImageEdit` —— 3/10 个有
- `VAEDecode` —— 3/10 个有
- `Fast Groups Muter (rgthree)` —— 2/10 个有
- `ImageResizeKJ` —— 2/10 个有
- `JoinStrings` —— 2/10 个有
- `LayerUtility: TextBox` —— 2/10 个有
- `QwenMultiangleCameraNode` —— 2/10 个有
- `easy imageBatchToImageList` —— 2/10 个有
- `Anything Everywhere` —— 1/10 个有
- `CR Text` —— 1/10 个有
- `Fast Groups Bypasser (rgthree)` —— 1/10 个有
- `ImageResize+` —— 1/10 个有
- `LoraLoader` —— 1/10 个有
- `ModelSamplingSD3` —— 1/10 个有
- `PixaromaLabel` —— 1/10 个有
- `PreviewImage` —— 1/10 个有
- `easy imageListToImageBatch` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 25 | 10 | 18% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.1 | 10 | 96% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | kl_optimal | - | 10 | 50% |
| 重绘幅度 | 0.4 | 0.1 - 1 | 10 | 41% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 24/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 7/10 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 25，10 个样本，取值分散，一致性仅 18%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.1，10 个样本，取值集中（一致性 96%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 kl_optimal，10 个样本，一致性 50%
- 重绘幅度 中位数 0.4，观测区间 0.1 - 1，10 个样本，取值分散，一致性仅 41%
- 高发问题（24/10 个样本）：Steps较低可能导致细节不足
- 高发问题（7/10 个样本）：发现KSampler但没有VAEDecode

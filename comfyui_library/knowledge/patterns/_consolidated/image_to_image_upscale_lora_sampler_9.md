---
name: image_to_image_upscale_lora_sampler_9
type: Image To Image
frequency: 15
level: moderate
coverage: 0.876533
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, GrowMaskWithBlur, Image Comparer (rgthree), ImageListToImageBatch, ImageScaleToTotalPixels, ImageUpscaleWithModel, ImpactImageBatchToImageList, KSampler, LayerUtility: ImageMaskScaleAs, LoadImage, LoraLoaderModelOnly, MaskToImage, Mix Images By Mask, PreviewImage, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy imageColorMatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Klein_亚秒级渲染精修_2083361847742394370.json, 图片生成/图生图/Klein_亚秒级渲染精修_2083373013055139841.json, 图片生成/图生图/Klein_渲染级精修V5自动白底像素对齐_2080934004727046145.json, 图片生成/图生图/Klein_渲染级精修V5自动白底像素对齐_2083360526314328065.json, 图片生成/图生图/Klein_渲染级精修V5自动白底像素对齐_2083371919650410497.json, 图片生成/图生图/Klein_珠宝首饰渲染级精修_2085627429598617602.json, 图片生成/图生图/Klein_珠宝首饰渲染级精修_2085639627188293633.json, 图片生成/图生图/Klein_珠宝首饰渲染级精修_2085909747752062977.json, 图片生成/图生图/Klein_珠宝首饰渲染级精修_2085927494745673730.json, 图片生成/图生图/Klein_珠宝首饰渲染级精修_2087368908192960513.json, 图片生成/图生图/Klein_珠宝首饰渲染级精修去除粘胶_2085911313288622082.json, 图片生成/图生图/Klein_珠宝首饰渲染级精修去除粘胶_2085928521888784385.json, 图片生成/图生图/⭐️  渲染级精修-Klein 9b_2072982724671008770.json, 图片生成/图生图/渲染级精修-Klein_9b_2090094291338223617.json, 图片生成/图生图/蒜香卡普Klein9b_亚秒级产品渲染精修_2018625687455801345.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_9

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/Klein_亚秒级渲染精修_2083361847742394370.json、图片生成/图生图/Klein_亚秒级渲染精修_2083373013055139841.json、图片生成/图生图/Klein_渲染级精修V5自动白底像素对齐_2080934004727046145.json、图片生成/图生图/Klein_渲染级精修V5自动白底像素对齐_2083360526314328065.json、图片生成/图生图/Klein_渲染级精修V5自动白底像素对齐_2083371919650410497.json…）

- **类型**：Image To Image
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageListToImageBatch`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `ImpactImageBatchToImageList`
- `KSampler`
- `LayerUtility: ImageMaskScaleAs`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `Mix Images By Mask`
- `PreviewImage`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageColorMatch`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 13/15 个有
- `CFGGuider` —— 10/15 个有
- `EmptyFlux2LatentImage` —— 10/15 个有
- `Flux2Scheduler` —— 10/15 个有
- `GetImageSize` —— 10/15 个有
- `KSamplerSelect` —— 10/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/15 个有
- `RandomNoise` —— 10/15 个有
- `ReferenceLatent` —— 10/15 个有
- `SamplerCustomAdvanced` —— 10/15 个有
- `GetImageSize+` —— 7/15 个有
- `PainterFluxImageEdit` —— 7/15 个有
- `CR Prompt Text` —— 5/15 个有
- `CR Text Input Switch (4 way)` —— 5/15 个有
- `ImageLoader` —— 5/15 个有
- `PixaromaLabel` —— 5/15 个有
- `ResizeImagesByLongerEdge` —— 4/15 个有
- `ConstrainImage|pysssss` —— 3/15 个有
- `easy textSwitch` —— 3/15 个有
- `GrowMask` —— 2/15 个有
- `InvertMask` —— 2/15 个有
- `JoinImageWithAlpha` —— 2/15 个有
- `LoadRembgByBiRefNetModel` —— 2/15 个有
- `RembgByBiRefNetAdvanced` —— 2/15 个有
- `孤海图像裁剪按比例` —— 2/15 个有
- `忽略多组孤海` —— 2/15 个有
- `Label (rgthree)` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 2 - 6 | 15 | 74% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 15 | 70% |
| 采样算法 | euler | - | 15 | 100% |
| 调度器 | kl_optimal | - | 15 | 53% |
| 重绘幅度 | 0.4 | 0.4 - 1 | 15 | 56% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 22/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 2 - 6，15 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，15 个样本
- 采样算法 最常用 euler，15 个样本，一致性 100%
- 调度器 最常用 kl_optimal，15 个样本，一致性 53%
- 重绘幅度 中位数 0.4，观测区间 0.4 - 1，15 个样本
- 高发问题（22/15 个样本）：Steps较低可能导致细节不足

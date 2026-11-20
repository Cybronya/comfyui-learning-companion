---
name: image_to_image_upscale_lora_sampler_13
type: Image To Image
frequency: 16
level: moderate
coverage: 0.94625
common_nodes: [CLIPTextEncode, FluxGuidance, Image Comparer (rgthree), ImageListToImageBatch, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX2-室内设计模型+参考生成效果图V1_2083444914024706050.json, 图片生成/图生图/KONTEXET质感提升+TTP_1994360100020232194.json, 图片生成/图生图/Klein_专业级自然无缝扩图_2031754954209239041.json, 图片生成/图生图/Kontext电商产品质感提升细节增强_2053311580279975937.json, 图片生成/图生图/Kontext电商产品质感提升细节增强_2055996250503303170.json, 图片生成/图生图/Kontext电商产品质感提升细节增强_2057118295471509505.json, 图片生成/图生图/Kontext电商产品质感提升细节增强_2097153668264062978.json, 图片生成/图生图/Kontext电商产品质感提升细节增强_2097494951763464193.json, 图片生成/图生图/kontext全能质感提升细节增强_2045329112276930561.json, 图片生成/图生图/一键产品精修（万物皆可修）_2054010513645948929.json, 图片生成/图生图/万物质感提升 - 包装、室内建筑、效果炸裂_2009249948952436737.json, 图片生成/图生图/万物质感提升+真实感+立体感_1995423421632851970.json, 图片生成/图生图/万物质感提升（包装室内建筑方向效果更佳）_1994345615612125185.json, 图片生成/图生图/全能质感提升 _ 细节增强_v1_2015006699500867585.json, 平台全量/电商产品去瑕疵精修 自动矫正透视产品精修   质感优化 全能质感提升 TTP分块放大修复 细节增强_2031546719275585538.json, 平台全量/超级无缝扩图Flux2Klein + SeedVR2.5 & TTP分块高清修复放大_2046417687810678786.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_13

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/FLUX2-室内设计模型+参考生成效果图V1_2083444914024706050.json、图片生成/图生图/KONTEXET质感提升+TTP_1994360100020232194.json、图片生成/图生图/Klein_专业级自然无缝扩图_2031754954209239041.json、图片生成/图生图/Kontext电商产品质感提升细节增强_2053311580279975937.json、图片生成/图生图/Kontext电商产品质感提升细节增强_2055996250503303170.json…）

- **类型**：Image To Image
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPTextEncode`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageListToImageBatch`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
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

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 15/16 个有
- `ConstrainImage|pysssss` —— 15/16 个有
- `DualCLIPLoader` —— 15/16 个有
- `GetImageSize+` —— 15/16 个有
- `BasicGuider` —— 14/16 个有
- `BasicScheduler` —— 14/16 个有
- `FluxKontextImageScale` —— 14/16 个有
- `ImageBlend` —— 13/16 个有
- `ImagePosterize+` —— 13/16 个有
- `NoiseImage` —— 13/16 个有
- `easy cleanGpuUsed` —— 13/16 个有
- `easy imageBatchToImageList` —— 13/16 个有
- `PreviewImage` —— 11/16 个有
- `LoraLoader` —— 5/16 个有
- `LayerUtility: PurgeVRAM` —— 4/16 个有
- `CLIPLoader` —— 3/16 个有
- `Fast Groups Bypasser (rgthree)` —— 3/16 个有
- `ImpactImageBatchToImageList` —— 3/16 个有
- `CFGGuider` —— 2/16 个有
- `Flux2Scheduler` —— 2/16 个有
- `ImpactInt` —— 2/16 个有
- `ImagePadForOutpaint` —— 1/16 个有
- `ImageResizeKJv2` —— 1/16 个有
- `LayerColor: AutoAdjustV2` —— 1/16 个有
- `LayerUtility: ExtendCanvasV2` —— 1/16 个有
- `SDVN Apply Kontext Reference` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 6 - 30 | 16 | 64% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 16 | 100% |
| 采样算法 | euler | - | 16 | 100% |
| 调度器 | simple | - | 16 | 88% |
| 重绘幅度 | 1 | 0.4 - 1 | 16 | 79% |
| LoRA 模型强度 | 0.45 | 0.45 - 1 | 5 | 61% |
| LoRA 文本强度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 6 - 30，16 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，16 个样本，一致性 100%
- 调度器 最常用 simple，16 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 0.4 - 1，16 个样本
- LoRA 模型强度 中位数 0.45，观测区间 0.45 - 1，5 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）

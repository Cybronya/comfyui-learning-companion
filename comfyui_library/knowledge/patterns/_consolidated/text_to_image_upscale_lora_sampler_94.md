---
name: text_to_image_upscale_lora_sampler_94
type: Text To Image
frequency: 3
level: strong
coverage: 0.878
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ColorMatch, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, Fast Groups Bypasser (rgthree), Flux2Scheduler, GetImageSize, Image Comparer (rgthree), ImageScaleToTotalPixels, JjkText, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageSize, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/krea2图生图加flux2加klein三采极｜James008出品_2100852119631912961.json, 图片生成/图生图/图像放大图生图工作流，小图无损拉大细节依旧清晰_2112626658086838273.json, 图片生成/图生图/图像放大工作流｜老图无损变高清大图细节保留_2112428265683120130.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_94

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/krea2图生图加flux2加klein三采极｜James008出品_2100852119631912961.json、图片生成/图生图/图像放大图生图工作流，小图无损拉大细节依旧清晰_2112626658086838273.json、图片生成/图生图/图像放大工作流｜老图无损变高清大图细节保留_2112428265683120130.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageSize`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `FlashVSRNode` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `ImageScale` —— 2/3 个有
- `ImageSharpen` —— 2/3 个有
- `Load Image From Url (mtb)` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `easy imageBatchToImageList` —— 2/3 个有
- `easy imageListToImageBatch` —— 2/3 个有
- `easy imageSizeBySide` —— 2/3 个有
- `AILab_QwenVL` —— 1/3 个有
- `BasicGuider` —— 1/3 个有
- `BasicScheduler` —— 1/3 个有
- `EmptyImage` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `ImageScaleBy` —— 1/3 个有
- `ImageUpscaleWithModel` —— 1/3 个有
- `KSamplerAdvanced` —— 1/3 个有
- `LoraLoader` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `UpscaleModelLoader` —— 1/3 个有
- `VAEDecodeTiled` —— 1/3 个有
- `VAEEncodeTiled` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `easy imageColorMatch` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足

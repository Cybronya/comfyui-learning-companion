---
name: text_to_image_upscale_lora_sampler_57
type: Text To Image
frequency: 4
level: strong
coverage: 0.86975
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, INTConstant, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/4K图像高清放大｜SeedVR 2.5+TTP清晰图片处理_2092925104920555521.json, 图片生成/图生图/SeedVR 2.5精修工作流，图生图高清修复细节增强工具_2105778806178013185.json, 图片生成/图生图/图像放大图生图工作流，小图无损拉大细节依旧清晰_2112626658086838273.json, 图片生成/图生图/图像放大工作流｜老图无损变高清大图细节保留_2112428265683120130.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_57

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/4K图像高清放大｜SeedVR 2.5+TTP清晰图片处理_2092925104920555521.json、图片生成/图生图/SeedVR 2.5精修工作流，图生图高清修复细节增强工具_2105778806178013185.json、图片生成/图生图/图像放大图生图工作流，小图无损拉大细节依旧清晰_2112626658086838273.json、图片生成/图生图/图像放大工作流｜老图无损变高清大图细节保留_2112428265683120130.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `INTConstant`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/4 个有
- `ImageScale` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `TTP_Image_Assy` —— 3/4 个有
- `TTP_Image_Tile_Batch` —— 3/4 个有
- `TTP_Tile_image_size` —— 3/4 个有
- `easy imageBatchToImageList` —— 3/4 个有
- `easy imageListToImageBatch` —— 3/4 个有
- `easy imageSize` —— 3/4 个有
- `easy imageSizeBySide` —— 3/4 个有
- `CFGGuider` —— 2/4 个有
- `ColorMatch` —— 2/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `EmptyFlux2LatentImage` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `FlashVSRNode` —— 2/4 个有
- `Flux2Scheduler` —— 2/4 个有
- `GetImageSize` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 2/4 个有
- `ImageSharpen` —— 2/4 个有
- `KSamplerSelect` —— 2/4 个有
- `Load Image From Url (mtb)` —— 2/4 个有
- `RandomNoise` —— 2/4 个有
- `ReferenceLatent` —— 2/4 个有
- `SamplerCustomAdvanced` —— 2/4 个有
- `VAEEncode` —— 2/4 个有
- `SetNode` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足

---
name: unknown_workflow_sampler_clip_unet_352
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.821667
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), ImageScale, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch, easy imageSize, easy imageSizeBySide]
problems: []
missing: []
members: [图片生成/图生图/Klein-9B电商产品精修_2027744018473426945.json, 图片生成/图生图/产品精修SeedVR2 .5放大一键金属电器化妆品精修 FLUX2-Klein-9B产品精修升级版_2101492202433236993.json, 图片生成/图生图/图像放大_2020915083957772290.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_352

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Klein-9B电商产品精修_2027744018473426945.json、图片生成/图生图/产品精修SeedVR2 .5放大一键金属电器化妆品精修 FLUX2-Klein-9B产品精修升级版_2101492202433236993.json、图片生成/图生图/图像放大_2020915083957772290.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScale`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `easy imageSize`
- `easy imageSizeBySide`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `JWInteger` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `SeedVR2LoadDiTModel` —— 2/3 个有
- `SeedVR2LoadVAEModel` —— 2/3 个有
- `SeedVR2VideoUpscaler` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `easy imageScaleDownToSize` —— 2/3 个有
- `ColorMatch` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `FlashVSRNode` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `ImageSharpen` —— 1/3 个有
- `LayerUtility: ImageReel` —— 1/3 个有
- `LayerUtility: ImageReelComposit` —— 1/3 个有
- `Load Image From Url (mtb)` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `SeedVR2BlockSwap` —— 1/3 个有
- `SeedVR2ExtraArgs` —— 1/3 个有
- `SeedVR2GGUF` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

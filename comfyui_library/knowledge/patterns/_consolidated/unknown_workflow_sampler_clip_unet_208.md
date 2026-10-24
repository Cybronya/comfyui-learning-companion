---
name: unknown_workflow_sampler_clip_unet_208
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.865333
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux--Klein--产品精修高清放大_2054921194004074498.json, 图片生成/图生图/Flux-Klein-产品精修-高清放大_2055848149163495425.json, 图片生成/图生图/Flux-Klein产品精修高清放大（爆显用plus模式）_2055471694915096578.json, 图片生成/图生图/Klein-9B电商产品精修_2027744018473426945.json, 图片生成/图生图/产品精修SeedVR2 .5放大一键金属电器化妆品精修 FLUX2-Klein-9B产品精修升级版_2101492202433236993.json, 图片生成/图生图/图像放大_2020915083957772290.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_208

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Flux--Klein--产品精修高清放大_2054921194004074498.json、图片生成/图生图/Flux-Klein-产品精修-高清放大_2055848149163495425.json、图片生成/图生图/Flux-Klein产品精修高清放大（爆显用plus模式）_2055471694915096578.json、图片生成/图生图/Klein-9B电商产品精修_2027744018473426945.json、图片生成/图生图/产品精修SeedVR2 .5放大一键金属电器化妆品精修 FLUX2-Klein-9B产品精修升级版_2101492202433236993.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JWInteger` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `easy cleanGpuUsed` —— 5/6 个有
- `easy imageScaleDownToSize` —— 5/6 个有
- `SeedVR2BlockSwap` —— 4/6 个有
- `SeedVR2ExtraArgs` —— 4/6 个有
- `AILab_QwenVL` —— 3/6 个有
- `DF_Integer` —— 3/6 个有
- `ImageScale` —— 3/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/6 个有
- `SeedVR2` —— 3/6 个有
- `SimpleMath+` —— 3/6 个有
- `TTP_Image_Assy` —— 3/6 个有
- `TTP_Image_Tile_Batch` —— 3/6 个有
- `TTP_Tile_image_size` —— 3/6 个有
- `easy imageBatchToImageList` —— 3/6 个有
- `easy imageListToImageBatch` —— 3/6 个有
- `easy imageSize` —— 3/6 个有
- `easy imageSizeBySide` —— 3/6 个有
- `CR Text` —— 2/6 个有
- `INTConstant` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `SeedVR2LoadDiTModel` —— 2/6 个有
- `SeedVR2LoadVAEModel` —— 2/6 个有
- `SeedVR2VideoUpscaler` —— 2/6 个有
- `SetNode` —— 2/6 个有
- `ColorMatch` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `FlashVSRNode` —— 1/6 个有
- `GetNode` —— 1/6 个有
- `ImageScaleToTotalPixels` —— 1/6 个有
- `ImageSharpen` —— 1/6 个有
- `LayerUtility: ImageReel` —— 1/6 个有
- `LayerUtility: ImageReelComposit` —— 1/6 个有
- `Load Image From Url (mtb)` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `SeedVR2GGUF` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

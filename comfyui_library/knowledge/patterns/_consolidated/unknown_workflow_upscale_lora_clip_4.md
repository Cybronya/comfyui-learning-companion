---
name: unknown_workflow_upscale_lora_clip_4
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.64
common_nodes: [CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), GetImageSize, GetNode, Image Comparer (rgthree), ImageCASharpening+, ImageResize+, ImageScaleToTotalPixels, ImageSharpen, ImpactMinMax, IterativeImageUpscale, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PDIMAGE_LongerSize, PixelKSampleUpscalerProvider, PreviewImage, ReferenceLatent, SaveImage, SeedVR2, SeedVR2BlockSwap, SetNode, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, UNETLoader, Upscale Model Loader, VAEDecode, VAEEncode, VAELoader, VOSR2ModelLoader, VOSR2Upscale, easy cleanGpuUsed, easy int, workflow>自定义采样器]
problems: []
missing: [ImageCASharpening+, SimpleMath+, easy cleanGpuUsed, easy int, ImageResize+, Upscale Model Loader, workflow>自定义采样器]
members: [图片生成/图生图/2019374754297290754.json, 图片生成/文生图/高清放大V4_保持一致性_四合一_2098309851838509057.json, 图片生成/文生图/高清放大V4_保持一致性_四合一_2108398270673412098.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_clip_4

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/2019374754297290754.json、图片生成/文生图/高清放大V4_保持一致性_四合一_2098309851838509057.json、图片生成/文生图/高清放大V4_保持一致性_四合一_2108398270673412098.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageCASharpening+`
- `ImageResize+`
- `ImageScaleToTotalPixels`
- `ImageSharpen`
- `ImpactMinMax`
- `IterativeImageUpscale`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PDIMAGE_LongerSize`
- `PixelKSampleUpscalerProvider`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SetNode`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `UNETLoader`
- `Upscale Model Loader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `easy cleanGpuUsed`
- `easy int`
- `workflow>自定义采样器`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：ImageCASharpening+、SimpleMath+、easy cleanGpuUsed、easy int、ImageResize+

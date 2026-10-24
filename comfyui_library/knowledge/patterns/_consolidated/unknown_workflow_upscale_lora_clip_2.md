---
name: unknown_workflow_upscale_lora_clip_2
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.70575
common_nodes: [CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), GetImageSize, GetNode, Image Comparer (rgthree), ImageCASharpening+, ImageResize+, ImageScaleToTotalPixels, ImageSharpen, ImpactMinMax, IterativeImageUpscale, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PixelKSampleUpscalerProvider, PreviewImage, ReferenceLatent, SaveImage, SeedVR2, SeedVR2BlockSwap, SetNode, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, UNETLoader, Upscale Model Loader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy int, workflow>自定义采样器]
problems: []
missing: []
members: [图片生成/图生图/图片高清放大V4 保持一致性 四合一_2097998465761632257.json, 图片生成/图生图/图片高清放大V4_保持一致性_四合一_2098221530831482882.json, 图片生成/图生图/高清放大V3 + 三合一 + 完美一致性_2070346770542059521.json, 图片生成/图生图/高清放大V3_+_三合一_+_完美一致性_2095765972950016002.json, 图片生成/图生图/高清放大V3_+_三合一_+_完美一致性_2096060602690129921.json, 图片生成/图生图/高清放大V4_保持一致性_四合一_2019374754297290754.json, 图片生成/图生图/高清放大V4_保持一致性_四合一_2098315206148575234.json, 图片生成/图生图/高清放大V4_保持一致性_四合一_2099055315647025154.json, 图片生成/图生图/高清放大V4_保持一致性_四合一_2099660267905970178.json, 图片生成/图生图/高清放大V4_保持一致性_四合一_2100167156053921794.json, 图片生成/文生图/高清放大V4_保持一致性_四合一_2098309851838509057.json, 图片生成/文生图/高清放大V4_保持一致性_四合一_2108398270673412098.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_clip_2

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/图片高清放大V4 保持一致性 四合一_2097998465761632257.json、图片生成/图生图/图片高清放大V4_保持一致性_四合一_2098221530831482882.json、图片生成/图生图/高清放大V3 + 三合一 + 完美一致性_2070346770542059521.json、图片生成/图生图/高清放大V3_+_三合一_+_完美一致性_2095765972950016002.json、图片生成/图生图/高清放大V3_+_三合一_+_完美一致性_2096060602690129921.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 12 个 workflow 都包含：
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
- `easy cleanGpuUsed`
- `easy int`
- `workflow>自定义采样器`

**可变部分**（部分 workflow 才有）：
- `PDIMAGE_LongerSize` —— 9/12 个有
- `VOSR2ModelLoader` —— 9/12 个有
- `VOSR2Upscale` —— 9/12 个有
- `EmptyImage` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

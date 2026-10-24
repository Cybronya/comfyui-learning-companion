---
name: unknown_workflow_upscale_sampler_clip_30
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8655
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, GetImageSize+, Image Comparer (rgthree), ImageResize+, ImageScaleBy, KSamplerSelect, LoadImage, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Flux.2-Klein：富士Pro400H_2079555927270838274.json, 图片生成/图生图/Klein-9B_canny硬边缘控制图片编辑_2071437841372110850.json, 图片生成/图生图/Klein-9B深度控制图片编辑_2071412091562577921.json, 图片生成/图生图/flux2-klein-换头_2080885547890991106.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_30

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux.2-Klein：富士Pro400H_2079555927270838274.json、图片生成/图生图/Klein-9B_canny硬边缘控制图片编辑_2071437841372110850.json、图片生成/图生图/Klein-9B深度控制图片编辑_2071412091562577921.json、图片生成/图生图/flux2-klein-换头_2080885547890991106.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `KSamplerSelect`
- `LoadImage`
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
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `Get Image Size` —— 2/4 个有
- `ImageCASharpening+` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 2/4 个有
- `LayerUtility: ImageReel` —— 2/4 个有
- `LayerUtility: ImageReelComposit` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `easy imageScaleToNormPixels` —— 2/4 个有
- `图像缩放V2_孤海` —— 2/4 个有
- `数学运算_孤海` —— 2/4 个有
- `Any To String (mtb)` —— 1/4 个有
- `ConditioningCombine` —— 1/4 个有
- `ControlNetLoader` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `FluxUnionControlNetApply` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `PrimitiveFloat` —— 1/4 个有
- `RHLLMChatNode` —— 1/4 个有
- `SetUnionControlNetType` —— 1/4 个有
- `easy int` —— 1/4 个有
- `easy seed` —— 1/4 个有
- `easy setNode` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | canny | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_sampler_clip_unet_339
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.944
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, GetImageSize, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/11.高清放大，质感提升_2050782119433129985.json, 图片生成/图生图/13.老照片修复_2051995992244932609.json, 图片生成/图生图/Flux2 Klein Multi-Image Edit_2018198139378864129.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_339

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/11.高清放大，质感提升_2050782119433129985.json、图片生成/图生图/13.老照片修复_2051995992244932609.json、图片生成/图生图/Flux2 Klein Multi-Image Edit_2018198139378864129.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `GetImageSize`
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
- `EmptyFlux2LatentImage` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `ResizeImagesByLongerEdge` —— 2/3 个有
- `SeedVR2LoadDiTModel` —— 2/3 个有
- `SeedVR2LoadVAEModel` —— 2/3 个有
- `SeedVR2VideoUpscaler` —— 2/3 个有
- `AIO_Preprocessor` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `INTConstant` —— 1/3 个有
- `Image Padding` —— 1/3 个有
- `ImageAddNoise` —— 1/3 个有
- `ImageCASharpening+` —— 1/3 个有
- `ImageColorMatch+` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `LoaderGGUF` —— 1/3 个有
- `RTXVideoSuperResolution` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

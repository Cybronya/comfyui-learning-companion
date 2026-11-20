---
name: unknown_workflow_sampler_clip_unet_286
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.924
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, GetImageSize, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/11.高清放大，质感提升_2050782119433129985.json, 图片生成/图生图/13.老照片修复_2051995992244932609.json, 图片生成/图生图/AI多功能  老照片修复、去水印、偏色曝光_2115976429346320386.json, 图片生成/图生图/Flux2 Klein Multi-Image Edit_2018198139378864129.json, 平台全量/Flux2 Klein 重新打光，照片过曝，光斑，上色，偏色，老照片修复，万能P图，去水印_2098670522694455297.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_286

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/11.高清放大，质感提升_2050782119433129985.json、图片生成/图生图/13.老照片修复_2051995992244932609.json、图片生成/图生图/AI多功能  老照片修复、去水印、偏色曝光_2115976429346320386.json、图片生成/图生图/Flux2 Klein Multi-Image Edit_2018198139378864129.json、平台全量/Flux2 Klein 重新打光，照片过曝，光斑，上色，偏色，老照片修复，万能P图，去水印_2098670522694455297.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `GetImageSize`
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
- `EmptyFlux2LatentImage` —— 4/5 个有
- `Image Comparer (rgthree)` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `SeedVR2LoadDiTModel` —— 4/5 个有
- `SeedVR2LoadVAEModel` —— 4/5 个有
- `SeedVR2VideoUpscaler` —— 4/5 个有
- `Flux2Scheduler` —— 3/5 个有
- `ImageScaleToTotalPixels` —— 3/5 个有
- `KSamplerSelect` —— 3/5 个有
- `Fast Groups Bypasser (rgthree)` —— 2/5 个有
- `ImageScaleBy` —— 2/5 个有
- `RHHiddenNodes` —— 2/5 个有
- `ResizeImagesByLongerEdge` —— 2/5 个有
- `AIO_Preprocessor` —— 1/5 个有
- `INTConstant` —— 1/5 个有
- `Image Padding` —— 1/5 个有
- `ImageAddNoise` —— 1/5 个有
- `ImageCASharpening+` —— 1/5 个有
- `ImageColorMatch+` —— 1/5 个有
- `LayerUtility: PurgeVRAM` —— 1/5 个有
- `LoaderGGUF` —— 1/5 个有
- `RTXVideoSuperResolution` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

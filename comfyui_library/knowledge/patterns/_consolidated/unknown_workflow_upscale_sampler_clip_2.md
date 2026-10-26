---
name: unknown_workflow_upscale_sampler_clip_2
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.707
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, Image Comparer (rgthree), KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX-Klein版 电商产品可控构图换背景+融图_2013853557090426881.json, 图片生成/图生图/FLUX2 KLEIN True-V2底模升级-单图编辑_2049082691332612097.json, 图片生成/图生图/FLUX2+KLEIN+True-V2-单图编辑_2050236956377923586.json, 图片生成/图生图/Flux.2 [Klein]图像扩图+4K放大_2012429239328444417.json, 图片生成/图生图/Flux2 Klein 多图万能编辑工作流（局部重绘、扩图、单图、双图、三图编辑）_2012017503123283970.json, 图片生成/图生图/Flux2 Klein 超级多合一_文生图、单图多图编辑、重绘、完美扩图_2058397027016466433.json, 图片生成/图生图/Flux2 Klein 超级多合一_文生图、单图多图编辑、重绘、完美扩图_2100023809893031937.json, 图片生成/图生图/Flux2_Klein_超级多合一_文生图、单图多图编辑、重绘、完美扩图_2101484677134635010.json, 图片生成/图生图/Flux2_Klein_超级多合一_文生图、单图多图编辑、重绘、完美扩图_2102214802272776194.json, 图片生成/图生图/krea 2 and flux klein__文生图_2100026938537627650.json, 图片生成/图生图/krea 2 and flux klein__文生图_2100263128801038337.json, 图片生成/文生图/Flux2 Klein 超级多合一_文生图、单图多图编辑、重绘、完美扩图_2014259943414697985.json, 图片生成/文生图/Flux2 Klein 超级多合一_文生图、单图多图编辑、重绘、完美扩图自用_2012776375110868994.json, 图片生成/文生图/Flux2_Klein_超级多合一_文生图、单图多图编辑、重绘、完美扩图_2098909534654914562.json, 图片生成/文生图/Flux2_Klein_超级多合一_文生图、单图多图编辑、重绘、完美扩图_2098971198804807681.json, 图片生成/文生图/YZ金鱼-Flux2 Klein 超级多合一_文生图、单图多图编辑、重绘、完美扩图_2012136788260823041.json, 图片生成/文生图/krea_2_and_flux_klein_文生图_2_2101081616683716610.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_2

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/FLUX-Klein版 电商产品可控构图换背景+融图_2013853557090426881.json、图片生成/图生图/FLUX2 KLEIN True-V2底模升级-单图编辑_2049082691332612097.json、图片生成/图生图/FLUX2+KLEIN+True-V2-单图编辑_2050236956377923586.json、图片生成/图生图/Flux.2 [Klein]图像扩图+4K放大_2012429239328444417.json、图片生成/图生图/Flux2 Klein 多图万能编辑工作流（局部重绘、扩图、单图、双图、三图编辑）_2012017503123283970.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 17 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 16/17 个有
- `Fast Groups Bypasser (rgthree)` —— 15/17 个有
- `GetImageSize` —— 15/17 个有
- `ImageScaleToTotalPixels` —— 15/17 个有
- `PreviewImage` —— 15/17 个有
- `ImagePadForOutpaint` —— 14/17 个有
- `PlaySound|pysssss` —— 14/17 个有
- `easy cleanGpuUsed` —— 14/17 个有
- `DifferentialDiffusion` —— 13/17 个有
- `GrowMaskWithBlur` —— 13/17 个有
- `InpaintModelConditioning` —— 13/17 个有
- `LanPaint_MaskBlend` —— 13/17 个有
- `CR SDXL Aspect Ratio` —— 12/17 个有
- `GetNode` —— 12/17 个有
- `SetNode` —— 12/17 个有
- `EmptyImage` —— 2/17 个有
- `PrimitiveStringMultiline` —— 2/17 个有
- `CR Text Input Switch (4 way)` —— 1/17 个有
- `ColorMatch` —— 1/17 个有
- `FastCanvas` —— 1/17 个有
- `FastCanvasTool` —— 1/17 个有
- `ImpactInt` —— 1/17 个有
- `LayerMask: BiRefNetUltraV2` —— 1/17 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/17 个有
- `LayerUtility: PurgeVRAM V2` —— 1/17 个有
- `MuyeSizeSelector` —— 1/17 个有
- `TextInput_` —— 1/17 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

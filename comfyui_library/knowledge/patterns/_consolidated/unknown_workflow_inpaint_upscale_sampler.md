---
name: unknown_workflow_inpaint_upscale_sampler
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.628571
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR SDXL Aspect Ratio, ConditioningZeroOut, DifferentialDiffusion, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), Flux2Scheduler, GetImageSize, GetNode, GrowMaskWithBlur, Image Comparer (rgthree), ImagePadForOutpaint, ImageScaleToTotalPixels, InpaintModelConditioning, KSamplerSelect, LanPaint_MaskBlend, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PlaySound|pysssss, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, PlaySound|pysssss, easy cleanGpuUsed, CR SDXL Aspect Ratio]
members: [图片生成/图生图/2102214802272776194.json, 图片生成/文生图/Flux2 Klein 超级多合一_文生图、单图多图编辑、重绘、完美扩图_2014259943414697985.json, 图片生成/文生图/Flux2 Klein 超级多合一_文生图、单图多图编辑、重绘、完美扩图自用_2012776375110868994.json, 图片生成/文生图/Flux2_Klein_超级多合一_文生图、单图多图编辑、重绘、完美扩图_2098909534654914562.json, 图片生成/文生图/Flux2_Klein_超级多合一_文生图、单图多图编辑、重绘、完美扩图_2098971198804807681.json, 图片生成/文生图/YZ金鱼-Flux2 Klein 超级多合一_文生图、单图多图编辑、重绘、完美扩图_2012136788260823041.json, 图片生成/文生图/krea_2_and_flux_klein_文生图_2_2101081616683716610.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_upscale_sampler

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/2102214802272776194.json、图片生成/文生图/Flux2 Klein 超级多合一_文生图、单图多图编辑、重绘、完美扩图_2014259943414697985.json、图片生成/文生图/Flux2 Klein 超级多合一_文生图、单图多图编辑、重绘、完美扩图自用_2012776375110868994.json、图片生成/文生图/Flux2_Klein_超级多合一_文生图、单图多图编辑、重绘、完美扩图_2098909534654914562.json、图片生成/文生图/Flux2_Klein_超级多合一_文生图、单图多图编辑、重绘、完美扩图_2098971198804807681.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `EmptyFlux2LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `GetImageSize`
- `GetNode`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImagePadForOutpaint`
- `ImageScaleToTotalPixels`
- `InpaintModelConditioning`
- `KSamplerSelect`
- `LanPaint_MaskBlend`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PlaySound|pysssss`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 2/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、PlaySound|pysssss、easy cleanGpuUsed、CR SDXL Aspect Ratio

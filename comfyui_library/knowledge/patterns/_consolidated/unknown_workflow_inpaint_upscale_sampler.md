---
name: unknown_workflow_inpaint_upscale_sampler
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.835308
common_nodes: [CFGGuider, CLIPTextEncode, CR Latent Input Switch, CannyEdgePreprocessor, ConditioningZeroOut, DepthAnythingPreprocessor, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), ImagePadForOutpaint, ImageScaleBy, ImageScaleToTotalPixels, ImpactGaussianBlurMask, InpaintModelConditioning, KSamplerSelect, LoadImage, Mask Fill Holes, MaskPreview+, OpenposePreprocessor, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, VAEDecode, VAEEncode, VAELoader, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/Flux2 Klein 六合一多功能工作流_2045672281417981954.json, 图片生成/图生图/Flux2 Klein 超强多功能工作流 林耀_2013647507200417794.json, 图片生成/图生图/Flux2 Klein 超强多功能工作流_2015391524393062402.json, 图片生成/图生图/Flux2 Klein多合一编辑—— 文生图、局部重绘、CN控制、扩图_2037339316598349825.json, 图片生成/图生图/Flux2+Klein+超强多功能工作流_2016689043509088258.json, 图片生成/图生图/最新Flux2 Klein 2.0超强多功能工作流 ！_2027560403449946114.json, 图片生成/图生图/蒜香卡普-Flux2+Klein9b_ 超强材质替换工作流_2033472142460850177.json, 图片生成/图生图/超强多功能工作流 -邻家AI大女孩_2047356701464072194.json, 图片生成/文生图/Flux2 Klein 多功能工作流（文生图，局部重绘，CN控制，扩图）_2014253655599353858.json, 图片生成/文生图/Flux2 Klein 文生图，局部重绘，CN控制，扩图。多合一_2014269646165254145.json, 图片生成/文生图/Flux2 Klein 超强多功能工作流_2013285336390045697.json, 图片生成/文生图/Flux2 Klein 超强多功能工作流_2014234115482066945.json, 图片生成/文生图/Flux2-Klein工作流_2014628146850570241.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_upscale_sampler

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/Flux2 Klein 六合一多功能工作流_2045672281417981954.json、图片生成/图生图/Flux2 Klein 超强多功能工作流 林耀_2013647507200417794.json、图片生成/图生图/Flux2 Klein 超强多功能工作流_2015391524393062402.json、图片生成/图生图/Flux2 Klein多合一编辑—— 文生图、局部重绘、CN控制、扩图_2037339316598349825.json、图片生成/图生图/Flux2+Klein+超强多功能工作流_2016689043509088258.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CR Latent Input Switch`
- `CannyEdgePreprocessor`
- `ConditioningZeroOut`
- `DepthAnythingPreprocessor`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImagePadForOutpaint`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `ImpactGaussianBlurMask`
- `InpaintModelConditioning`
- `KSamplerSelect`
- `LoadImage`
- `Mask Fill Holes`
- `MaskPreview+`
- `OpenposePreprocessor`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 12/13 个有
- `UNETLoader` —— 12/13 个有
- `PrimitiveInt` —— 10/13 个有
- `Fast Groups Bypasser (rgthree)` —— 4/13 个有
- `Int` —— 3/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/13 个有
- `Text` —— 3/13 个有
- `LoraLoaderModelOnly` —— 2/13 个有
- `ImageResizeKJv2` —— 1/13 个有
- `LoadDiffusionModelShared //Inspire` —— 1/13 个有
- `LoadTextEncoderShared //Inspire` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

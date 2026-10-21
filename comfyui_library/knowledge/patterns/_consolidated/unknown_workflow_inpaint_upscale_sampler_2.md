---
name: unknown_workflow_inpaint_upscale_sampler_2
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8392
common_nodes: [CFGGuider, CLIPTextEncode, CR Latent Input Switch, CannyEdgePreprocessor, ConditioningZeroOut, DepthAnythingPreprocessor, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), ImagePadForOutpaint, ImageScaleBy, ImageScaleToTotalPixels, ImpactGaussianBlurMask, InpaintModelConditioning, KSamplerSelect, LoadImage, Mask Fill Holes, MaskPreview+, OpenposePreprocessor, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, VAEDecode, VAEEncode, VAELoader, easy imageSize]
problems: []
missing: []
members: [图片生成/文生图/Flux2 Klein 多功能工作流（文生图，局部重绘，CN控制，扩图）_2014253655599353858.json, 图片生成/文生图/Flux2 Klein 文生图，局部重绘，CN控制，扩图。多合一_2014269646165254145.json, 图片生成/文生图/Flux2 Klein 超强多功能工作流_2013285336390045697.json, 图片生成/文生图/Flux2 Klein 超强多功能工作流_2014234115482066945.json, 图片生成/文生图/Flux2-Klein工作流_2014628146850570241.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_upscale_sampler_2

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Flux2 Klein 多功能工作流（文生图，局部重绘，CN控制，扩图）_2014253655599353858.json、图片生成/文生图/Flux2 Klein 文生图，局部重绘，CN控制，扩图。多合一_2014269646165254145.json、图片生成/文生图/Flux2 Klein 超强多功能工作流_2013285336390045697.json、图片生成/文生图/Flux2 Klein 超强多功能工作流_2014234115482066945.json、图片生成/文生图/Flux2-Klein工作流_2014628146850570241.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
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
- `CLIPLoader` —— 4/5 个有
- `UNETLoader` —— 4/5 个有
- `PrimitiveInt` —— 3/5 个有
- `Fast Groups Bypasser (rgthree)` —— 2/5 个有
- `Int` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `Text` —— 2/5 个有
- `LoadDiffusionModelShared //Inspire` —— 1/5 个有
- `LoadTextEncoderShared //Inspire` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_inpaint_upscale_sampler_15
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.826
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, DWPreprocessor, EmptyFlux2LatentImage, Fast Bypasser (rgthree), Fast Groups Bypasser (rgthree), Flux2Scheduler, GetImageSize, Image Comparer (rgthree), ImageScaleBy, ImpactMakeAnyList, InpaintCropImproved, KSamplerSelect, LayerMask: LoadSegmentAnythingModels, LayerMask: SegmentAnythingUltra V3, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy positive]
problems: []
missing: []
members: [图片生成/图生图/模特图-换脸-换头-换模特-换肤色 产品不变_2015686911104393218.json, 平台全量/flux2-klein-服装模特图-换脸-换头-换模特-换肤色_2013990963538042881.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_upscale_sampler_15

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/模特图-换脸-换头-换模特-换肤色 产品不变_2015686911104393218.json、平台全量/flux2-klein-服装模特图-换脸-换头-换模特-换肤色_2013990963538042881.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `DWPreprocessor`
- `EmptyFlux2LatentImage`
- `Fast Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImpactMakeAnyList`
- `InpaintCropImproved`
- `KSamplerSelect`
- `LayerMask: LoadSegmentAnythingModels`
- `LayerMask: SegmentAnythingUltra V3`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
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
- `easy positive`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

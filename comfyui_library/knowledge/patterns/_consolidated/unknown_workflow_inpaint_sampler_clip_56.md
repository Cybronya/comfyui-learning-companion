---
name: unknown_workflow_inpaint_sampler_clip_56
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9285
common_nodes: [AdvancedLyingSigmaSampler, BasicGuider, BasicScheduler, CLIPTextEncode, Colored Image (mtb), FaceParse(FaceParsing), FaceParsingModelLoader(FaceParsing), FaceParsingProcessorLoader(FaceParsing), FaceParsingResultsParser(FaceParsing), Image Comparer (rgthree), ImageToMask, ImpactGaussianBlurMask, InpaintModelConditioning, KSamplerSelect, LayerUtility: ImageBlendAdvance, LoadImage, MaskPreview+, MaskToImage, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/FLUX.krea真实皮肤质感_1971483655719862274.json, 图片生成/图生图/Flux2-klein+zimage单图人像编辑去ai感_2012155674465144834.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_56

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/FLUX.krea真实皮肤质感_1971483655719862274.json、图片生成/图生图/Flux2-klein+zimage单图人像编辑去ai感_2012155674465144834.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `AdvancedLyingSigmaSampler`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `Colored Image (mtb)`
- `FaceParse(FaceParsing)`
- `FaceParsingModelLoader(FaceParsing)`
- `FaceParsingProcessorLoader(FaceParsing)`
- `FaceParsingResultsParser(FaceParsing)`
- `Image Comparer (rgthree)`
- `ImageToMask`
- `ImpactGaussianBlurMask`
- `InpaintModelConditioning`
- `KSamplerSelect`
- `LayerUtility: ImageBlendAdvance`
- `LoadImage`
- `MaskPreview+`
- `MaskToImage`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `CFGGuider` —— 1/2 个有
- `CLIPLoader` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `EmptyFlux2LatentImage` —— 1/2 个有
- `Flux2Scheduler` —— 1/2 个有
- `FluxGuidance` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `LayerMask: MaskPreview` —— 1/2 个有
- `LayerMask: PersonMaskUltra V2` —— 1/2 个有
- `NunchakuFluxDiTLoader` —— 1/2 个有
- `NunchakuTextEncoderLoaderV2` —— 1/2 个有
- `ReferenceLatent` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `VAEEncode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_inpaint_upscale_sampler_16
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8185
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DifferentialDiffusion, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), ImagePadForOutpaint, ImageScaleToTotalPixels, InpaintModelConditioning, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy clearCacheAll, easy imageSize]
problems: []
missing: []
members: [平台全量/完美扩图_单图放大_批量放大（有用）_2067177141007118337.json, 平台全量/无限扩图优化版-Flux2-Klein_2021049091278512130.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_upscale_sampler_16

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/完美扩图_单图放大_批量放大（有用）_2067177141007118337.json、平台全量/无限扩图优化版-Flux2-Klein_2021049091278512130.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImagePadForOutpaint`
- `ImageScaleToTotalPixels`
- `InpaintModelConditioning`
- `KSamplerSelect`
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
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `HAIGC_SaveImagesToZip` —— 1/2 个有
- `JoinImageWithAlpha` —— 1/2 个有
- `PlaySound|pysssss` —— 1/2 个有
- `RHUploadZip_V2` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `easy int` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_upscale_sampler_clip_49
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.841
common_nodes: [CLIPTextEncode, Image Comparer (rgthree), ImageAndMaskPreview, ImageScaleToTotalPixels, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Mask Fill Holes, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy clearCacheAll, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/万物消除_2033893854461566977.json, 平台全量/万物消除-祛水印-字幕-Logo等原图直出加强版-直出4K-Flux2-klein_2013785198252527618.json, 平台全量/万物消除手动画遮罩-去水印-去字幕-速度快--直出4K-Flux-kontext_1996828886056980481.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_49

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/万物消除_2033893854461566977.json、平台全量/万物消除-祛水印-字幕-Logo等原图直出加强版-直出4K-Flux2-klein_2013785198252527618.json、平台全量/万物消除手动画遮罩-去水印-去字幕-速度快--直出4K-Flux-kontext_1996828886056980481.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `Image Comparer (rgthree)`
- `ImageAndMaskPreview`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Mask Fill Holes`
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
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 2/3 个有
- `BasicScheduler` —— 2/3 个有
- `CFGGuider` —— 2/3 个有
- `CLIPLoader` —— 2/3 个有
- `ConditioningZeroOut` —— 2/3 个有
- `Convert Masks to Images` —— 2/3 个有
- `EmptyFlux2LatentImage` —— 2/3 个有
- `EmptySD3LatentImage` —— 2/3 个有
- `Flux2Scheduler` —— 2/3 个有
- `FluxGuidance` —— 2/3 个有
- `FluxKontextImageScale` —— 2/3 个有
- `GetImageSize+` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `Image To Mask` —— 2/3 个有
- `ImageScale` —— 2/3 个有
- `ModelSamplingFlux` —— 2/3 个有
- `NunchakuFluxDiTLoader` —— 2/3 个有
- `NunchakuTextEncoderLoaderV2` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

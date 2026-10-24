---
name: unknown_workflow_sampler_clip_unet_334
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.927
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2 Klein 双图_2035898098593046530.json, 图片生成/图生图/Flux2 Klein 局部重绘_2015810312481542146.json, 图片生成/图生图/Flux2 Klein 超强局部参考重绘 颜色区域_2015807913335463937.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_334

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Flux2 Klein 双图_2035898098593046530.json、图片生成/图生图/Flux2 Klein 局部重绘_2015810312481542146.json、图片生成/图生图/Flux2 Klein 超强局部参考重绘 颜色区域_2015807913335463937.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
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
- `ConditioningZeroOut` —— 2/3 个有
- `EmptyFlux2LatentImage` —— 2/3 个有
- `ImpactGaussianBlurMask` —— 2/3 个有
- `InpaintModelConditioning` —— 2/3 个有
- `Mask Fill Holes` —— 2/3 个有
- `MaskPreview+` —— 2/3 个有
- `GetImageSize+` —— 1/3 个有
- `Image Blank` —— 1/3 个有
- `ImageCompositeMasked` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `JoinImageWithAlpha` —— 1/3 个有
- `LayerUtility: CropByMask V2` —— 1/3 个有
- `Number to Float` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `Text Dictionary Get` —— 1/3 个有
- `Text Dictionary New` —— 1/3 个有
- `Text to Number` —— 1/3 个有
- `easy imageSize` —— 1/3 个有
- `scale` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

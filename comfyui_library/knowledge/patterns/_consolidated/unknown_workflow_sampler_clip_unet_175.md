---
name: unknown_workflow_sampler_clip_unet_175
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.823667
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: [LayerMask: BiRefNetUltra, LayerUtility: ImageScaleByAspectRatio V2]
members: [图片生成/图生图/2089629118886404097.json, 图片生成/文生图/Bfs Klein人物换脸V1_2019423087078412290.json, 图片生成/文生图/FLUX-2-klein 文生图+图片编辑汇总_2012040681329532930.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_175

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/2089629118886404097.json、图片生成/文生图/Bfs Klein人物换脸V1_2019423087078412290.json、图片生成/文生图/FLUX-2-klein 文生图+图片编辑汇总_2012040681329532930.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `GetImageSize` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `DifferentialDiffusion` —— 1/3 个有
- `FluxGuidance` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `ImpactImageInfo` —— 1/3 个有
- `ImpactInt` —— 1/3 个有
- `LayerMask: BiRefNetUltra` —— 1/3 个有
- `ModelPatchTorchSettings` —— 1/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有
- `easy int` —— 1/3 个有
- `孤海注释` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerMask: BiRefNetUltra、LayerUtility: ImageScaleByAspectRatio V2

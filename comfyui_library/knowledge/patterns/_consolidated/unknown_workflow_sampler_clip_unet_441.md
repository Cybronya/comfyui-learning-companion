---
name: unknown_workflow_sampler_clip_unet_441
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7675
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), Flux2Scheduler, Image Comparer (rgthree), KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/FLUX-2-klein 文生图+图片编辑汇总_2012040681329532930.json, 图片生成/文生图/FLUX2-Klein多图编辑_2042101150391996418.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_441

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/FLUX-2-klein 文生图+图片编辑汇总_2012040681329532930.json、图片生成/文生图/FLUX2-Klein多图编辑_2042101150391996418.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `Image Comparer (rgthree)`
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
- `FluxGuidance` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `ImpactImageInfo` —— 1/2 个有
- `ModelPatchTorchSettings` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `PlaySound|pysssss` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `easy int` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

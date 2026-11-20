---
name: unknown_workflow_sampler_clip_unet_425
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.941
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, Get resolution [Crystools], KSamplerSelect, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, Seed (rgthree), TTResolutionSelector, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2 Klein 人物替换_2018215637369233409.json, 图片生成/图生图/图生图三视图_2016147740836761602.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_425

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flux2 Klein 人物替换_2018215637369233409.json、图片生成/图生图/图生图三视图_2016147740836761602.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `Get resolution [Crystools]`
- `KSamplerSelect`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `TTResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BboxDetectorSEGS` —— 1/2 个有
- `DWPreprocessor` —— 1/2 个有
- `GrowMaskWithBlur` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageCompositeMasked` —— 1/2 个有
- `InpaintModelConditioning` —— 1/2 个有
- `MaskToImage` —— 1/2 个有
- `SAMDetectorCombined` —— 1/2 个有
- `SAMLoader` —— 1/2 个有
- `SDPoseOODLoader` —— 1/2 个有
- `SDPoseOODProcessor` —— 1/2 个有
- `UltralyticsDetectorProvider` —— 1/2 个有
- `easy getNode` —— 1/2 个有
- `easy imageSwitch` —— 1/2 个有
- `easy setNode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

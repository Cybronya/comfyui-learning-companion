---
name: unknown_workflow_sampler_clip_unet_428
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.865
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), KSamplerSelect, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/换脸换装 真实高度一致 多图编辑 加强版_2089609145862414337.json, 图片生成/图生图/最新Flux2-Klein 9B-换脸换头_2013812519105728513.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_428

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/换脸换装 真实高度一致 多图编辑 加强版_2089609145862414337.json、图片生成/图生图/最新Flux2-Klein 9B-换脸换头_2013812519105728513.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 1/2 个有
- `ConstrainImage|pysssss` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `FluxKontextImageScale` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `RH_AlibabaQwenImage30ProImageEdit` —— 1/2 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/2 个有
- `SegmentV2` —— 1/2 个有
- `easy imageColorMatch` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

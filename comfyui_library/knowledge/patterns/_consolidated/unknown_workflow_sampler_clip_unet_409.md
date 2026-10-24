---
name: unknown_workflow_sampler_clip_unet_409
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8685
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), ImageConcanate, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2 Klein 双图编辑 极速4步模特换衣换装溶图光影融合_2014176840830685186.json, 图片生成/图生图/Flux2-Klein-9b(仅启用图片编辑，可转角度重打光）_2012726330126766082.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_409

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flux2 Klein 双图编辑 极速4步模特换衣换装溶图光影融合_2014176840830685186.json、图片生成/图生图/Flux2-Klein-9b(仅启用图片编辑，可转角度重打光）_2012726330126766082.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

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
- `ImageConcanate`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
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
- `BiRefNetRMBG` —— 1/2 个有
- `DetailTransfer` —— 1/2 个有
- `FastCanvas` —— 1/2 个有
- `FastCanvasTool` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `LayerMask: BiRefNetUltraV2` —— 1/2 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/2 个有
- `LayerMask: MaskGrow` —— 1/2 个有
- `LayerMask: MaskPreview` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `QwenMultiangleCameraNode` —— 1/2 个有
- `QwenMultiangleLightningNode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

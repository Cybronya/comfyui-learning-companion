---
name: unknown_workflow_sampler_clip_unet_435
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.987
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, ImageResizeKJv2, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, Seed Everywhere, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy promptLine]
problems: []
missing: []
members: [图片生成/图生图/klein专用_2021769783435337730.json, 图片生成/图生图/klein单图-大头照-抠图_2016821224147521538.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_435

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/klein专用_2021769783435337730.json、图片生成/图生图/klein单图-大头照-抠图_2016821224147521538.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：99%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed Everywhere`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy promptLine`

**可变部分**（部分 workflow 才有）：
- `Int` —— 1/2 个有
- `InvertMask` —— 1/2 个有
- `JoinImageWithAlpha` —— 1/2 个有
- `LayerUtility: CropByMask` —— 1/2 个有
- `LayerUtility: ExtendCanvasV2` —— 1/2 个有
- `LoadBackgroundRemovalModel` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RemoveBackground` —— 1/2 个有
- `SAM3Segment` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `easy anythingIndexSwitch` —— 1/2 个有
- `easy int` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

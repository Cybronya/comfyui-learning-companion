---
name: unknown_workflow_sampler_clip_unet_410
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.921
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, Image Comparer (rgthree), KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/Flux2-klein移除_局部重绘工作流_2013104344488480770.json, 图片生成/图生图/Klein单图像编辑（头发飘动版）_2052707351915966465.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_410

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flux2-klein移除_局部重绘工作流_2013104344488480770.json、图片生成/图生图/Klein单图像编辑（头发飘动版）_2052707351915966465.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 1/2 个有
- `LayerUtility: ColorImage V2` —— 1/2 个有
- `LayerUtility: CropByMask V2` —— 1/2 个有
- `LayerUtility: ImageBlend` —— 1/2 个有
- `Mask Fill Holes` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `Text Concatenate` —— 1/2 个有
- `取色器_孤海` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

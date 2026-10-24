---
name: unknown_workflow_sampler_unet_vae_306
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9425
common_nodes: [CFGGuider, CLIPLoader, ConditioningZeroOut, Flux2Scheduler, Image Comparer (rgthree), KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/双图编辑（解禁模型）：Flux.2 Klein 9B_2051467007492665345.json, 图片生成/图生图/局部重绘（解禁模型）：Flux.2 Klein 9B_2051475126302064642.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_306

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/双图编辑（解禁模型）：Flux.2 Klein 9B_2051467007492665345.json、图片生成/图生图/局部重绘（解禁模型）：Flux.2 Klein 9B_2051475126302064642.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DrawMaskOnImage` —— 1/2 个有
- `LayerMask: MaskGrow` —— 1/2 个有
- `Mask Fill Holes` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_sampler_clip_unet_421
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.845
common_nodes: [Anything Everywhere3, BasicGuider, CLIPLoader, CLIPTextEncode, CR Latent Input Switch, CR SDXL Aspect Ratio, CR Text, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), Flux2Scheduler, FluxGuidance, KSamplerSelect, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/FLUX.2- klein单图图编辑_2012069959744098306.json, 图片生成/图生图/FLUX.2- klein好多图编辑_2011996211644993537.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_421

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/FLUX.2- klein单图图编辑_2012069959744098306.json、图片生成/图生图/FLUX.2- klein好多图编辑_2011996211644993537.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere3`
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Latent Input Switch`
- `CR SDXL Aspect Ratio`
- `CR Text`
- `EmptyFlux2LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `FluxGuidance`
- `KSamplerSelect`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
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
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 1/2 个有
- `CR Text Concatenate` —— 1/2 个有
- `FluxKontextImageScale` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `Qwen3_VQA` —— 1/2 个有
- `SDPoseOODLoader` —— 1/2 个有
- `SDPoseOODProcessor` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

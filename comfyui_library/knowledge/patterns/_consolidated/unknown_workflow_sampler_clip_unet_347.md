---
name: unknown_workflow_sampler_clip_unet_347
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.814
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, KSamplerSelect, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux.2 Klein 9B 局部重绘+换头换脸+更换服装+万能图像编辑+极速版_2023278303158738945.json, 图片生成/图生图/第二个成熟AI城市设计-klein生成城市设计工作流_2026550405894774785.json, 图片生成/图生图/第二个成熟AI景观设计-klein景观_2022131857361477633.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_347

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Flux.2 Klein 9B 局部重绘+换头换脸+更换服装+万能图像编辑+极速版_2023278303158738945.json、图片生成/图生图/第二个成熟AI城市设计-klein生成城市设计工作流_2026550405894774785.json、图片生成/图生图/第二个成熟AI景观设计-klein景观_2022131857361477633.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `Flux2Scheduler`
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

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `Anything Everywhere3` —— 1/3 个有
- `CR Text` —— 1/3 个有
- `DifferentialDiffusion` —— 1/3 个有
- `GrowMaskWithBlur` —— 1/3 个有
- `ImageAndMaskPreview` —— 1/3 个有
- `InpaintModelConditioning` —— 1/3 个有
- `Int` —— 1/3 个有
- `KOOK_SaveJPGImage` —— 1/3 个有
- `Mask Fill Holes` —— 1/3 个有
- `easy imageSize` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

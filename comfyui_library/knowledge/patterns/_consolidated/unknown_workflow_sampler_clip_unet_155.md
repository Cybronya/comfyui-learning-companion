---
name: unknown_workflow_sampler_clip_unet_155
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.70725
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), Flux2Scheduler, GetImageSize, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/文生图/FLUX2-KLEIN _ 文生图+多图编辑大合集_2012077337252204546.json, 图片生成/文生图/FLUX2-KLEIN _ 文生图+多图编辑大合集_2012132446178910209.json, 图片生成/文生图/FLUX2-KLEIN _ 文生图+多图编辑大合集_2015497456603111426.json, 图片生成/文生图/Flux2-Klein全家桶-多功能版_2016042987171614722.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_155

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/FLUX2-KLEIN _ 文生图+多图编辑大合集_2012077337252204546.json、图片生成/文生图/FLUX2-KLEIN _ 文生图+多图编辑大合集_2012132446178910209.json、图片生成/文生图/FLUX2-KLEIN _ 文生图+多图编辑大合集_2015497456603111426.json、图片生成/文生图/Flux2-Klein全家桶-多功能版_2016042987171614722.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `GetImageSize`
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
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 3/4 个有
- `INTConstant` —— 3/4 个有
- `LayerUtility: ImageReel` —— 3/4 个有
- `LayerUtility: ImageReelComposit` —— 3/4 个有
- `CR Latent Input Switch` —— 1/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `ImageScaleToTotalPixels` —— 1/4 个有
- `InpaintModelConditioning` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

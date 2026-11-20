---
name: unknown_workflow_sampler_clip_unet_354
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.69275
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, Fast Groups Bypasser (rgthree), Flux2Scheduler, Image Comparer (rgthree), KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/FLUX-2-klein 文生图+图片编辑汇总_2012040681329532930.json, 图片生成/文生图/FLUX2-Klein多图编辑_2042101150391996418.json, 平台全量/Flux2-Klein-9B 图像编辑+图像扩图+局部重绘_2077957321824755713.json, 平台全量/影视二创换装流_2015710039327117314.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_354

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/FLUX-2-klein 文生图+图片编辑汇总_2012040681329532930.json、图片生成/文生图/FLUX2-Klein多图编辑_2042101150391996418.json、平台全量/Flux2-Klein-9B 图像编辑+图像扩图+局部重绘_2077957321824755713.json、平台全量/影视二创换装流_2015710039327117314.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
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
- `ConditioningZeroOut` —— 3/4 个有
- `EmptyFlux2LatentImage` —— 3/4 个有
- `GetNode` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `PreviewImage` —— 2/4 个有
- `easy int` —— 2/4 个有
- `Anything Everywhere` —— 1/4 个有
- `FancyTimerNode` —— 1/4 个有
- `FluxGuidance` —— 1/4 个有
- `INTConstant` —— 1/4 个有
- `ImpactImageInfo` —— 1/4 个有
- `ModelPatchTorchSettings` —— 1/4 个有
- `PathchSageAttentionKJ` —— 1/4 个有
- `PlaySound|pysssss` —— 1/4 个有
- `孤海外补画板按方向` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_sampler_clip_unet_380
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.771
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, Image Comparer (rgthree), KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/FLUX-2-klein 文生图+图片编辑汇总_2012040681329532930.json, 图片生成/文生图/FLUX2-Klein多图编辑_2042101150391996418.json, 数字人/数字人/Flux2 Klein 增强细节 动漫转真实照片_2048302003553570818.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_380

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/FLUX-2-klein 文生图+图片编辑汇总_2012040681329532930.json、图片生成/文生图/FLUX2-Klein多图编辑_2042101150391996418.json、数字人/数字人/Flux2 Klein 增强细节 动漫转真实照片_2048302003553570818.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 3 个 workflow 都包含：
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
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `easy int` —— 2/3 个有
- `FluxGuidance` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `ImpactImageInfo` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `ModelPatchTorchSettings` —— 1/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有
- `PlaySound|pysssss` —— 1/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

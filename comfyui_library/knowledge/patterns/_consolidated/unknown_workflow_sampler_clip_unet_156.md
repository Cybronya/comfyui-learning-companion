---
name: unknown_workflow_sampler_clip_unet_156
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.82
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux2-Klein 光速文生图&图生图&多图编辑大合集_2012036300836179970.json, 图片生成/文生图/人像换脸丨Flux2-Klein 9B丨面部发型替换_2105644038434152450.json, 图片生成/文生图/图片生成和编辑_Flux-2-Klein_2012115517577891842.json, 图片生成/文生图/😼FLUX2-KLEIN 文生图、单图、多图编辑合集@言灵ru_2014708517436919810.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_156

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Flux2-Klein 光速文生图&图生图&多图编辑大合集_2012036300836179970.json、图片生成/文生图/人像换脸丨Flux2-Klein 9B丨面部发型替换_2105644038434152450.json、图片生成/文生图/图片生成和编辑_Flux-2-Klein_2012115517577891842.json、图片生成/文生图/😼FLUX2-KLEIN 文生图、单图、多图编辑合集@言灵ru_2014708517436919810.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `KSamplerSelect`
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
- `Image Comparer (rgthree)` —— 3/4 个有
- `GetNode` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `LayerUtility: PurgeVRAM V2` —— 2/4 个有
- `Seed (rgthree)` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `easy int` —— 2/4 个有
- `AILab_QwenVL` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/4 个有
- `ModelSamplingAuraFlow` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `TTResolutionSelector` —— 1/4 个有
- `Text` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

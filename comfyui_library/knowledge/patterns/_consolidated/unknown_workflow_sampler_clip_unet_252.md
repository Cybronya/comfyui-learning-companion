---
name: unknown_workflow_sampler_clip_unet_252
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9116
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, Int, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/打光_溶图_改透视_提升画质_100%不偏移_细节迁移_klein_9b_2091710740364349442.json, 图片生成/图生图/打光_溶图_改透视_提升画质_100%不偏移_细节迁移_klein_9b_2091842911334912001.json, 图片生成/图生图/换脸Flux2Klein多图编辑9B加速版Flux2Klein多图编辑9B加速版+_2025838254557237250.json, 图片生成/图生图/换脸Flux2Klein多图编辑9B加速版_2031581292579528705.json, 图片生成/文生图/Klein 9B单、双、多图编辑_2018506313860386818.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_252

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/打光_溶图_改透视_提升画质_100%不偏移_细节迁移_klein_9b_2091710740364349442.json、图片生成/图生图/打光_溶图_改透视_提升画质_100%不偏移_细节迁移_klein_9b_2091842911334912001.json、图片生成/图生图/换脸Flux2Klein多图编辑9B加速版Flux2Klein多图编辑9B加速版+_2025838254557237250.json、图片生成/图生图/换脸Flux2Klein多图编辑9B加速版_2031581292579528705.json、图片生成/文生图/Klein 9B单、双、多图编辑_2018506313860386818.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `Int`
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
- `CR Text` —— 3/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `Image Comparer (rgthree)` —— 3/5 个有
- `easy imageConcat` —— 3/5 个有
- `ImageBatchConcatNode` —— 2/5 个有
- `LayerMask: BiRefNetUltraV2` —— 2/5 个有
- `LayerMask: LoadBiRefNetModelV2` —— 2/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `XinbaoPintu` —— 2/5 个有
- `easy imageDetailTransfer` —— 2/5 个有
- `easy seed` —— 2/5 个有
- `ImageResize+` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

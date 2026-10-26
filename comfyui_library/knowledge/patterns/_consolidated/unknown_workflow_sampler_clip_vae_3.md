---
name: unknown_workflow_sampler_clip_vae_3
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.90425
common_nodes: [CFGGuider, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/1.人物换装_2050619333541412866.json, 图片生成/图生图/20260722一致性personal_2079764596788912130.json, 图片生成/图生图/9.批量精修白底图_2050773369066401794.json, 图片生成/图生图/F.2Klein9B万物迁移_2066737707379945473.json, 图片生成/图生图/FLUX-Klein-图像编辑-10秒急速出图_2012126304631529473.json, 图片生成/图生图/FLUX.Klein-9B一致性lora单图编辑_2033155455794548737.json, 图片生成/图生图/Flux-2-Klein-9b 万物迁移_2065056521217728513.json, 图片生成/图生图/Klein - 万物迁移_2051859267984084993.json, 图片生成/图生图/Klein - 万物迁移_2065714934046089217.json, 图片生成/图生图/Klein - 万物迁移光影_2065342945917755393.json, 图片生成/图生图/Klein_-_万物迁移重新打光_2082641469969616898.json, 图片生成/图生图/Klein_-_万物迁移重新打光_2082650177730600962.json, 图片生成/图生图/万物迁移-Flux-2Klein-9b_2064567178598371329.json, 图片生成/图生图/光影迁移-打光色调复刻_kelin打光工作流_2068244841733115905.json, 图片生成/文生图/Klein - 万物迁移自用_2064658422053818370.json, 图片生成/文生图/Klein-一致性_2096434383749210114.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_3

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/1.人物换装_2050619333541412866.json、图片生成/图生图/20260722一致性personal_2079764596788912130.json、图片生成/图生图/9.批量精修白底图_2050773369066401794.json、图片生成/图生图/F.2Klein9B万物迁移_2066737707379945473.json、图片生成/图生图/FLUX-Klein-图像编辑-10秒急速出图_2012126304631529473.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 16 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 15/16 个有
- `ConditioningZeroOut` —— 15/16 个有
- `GetImageSize` —— 15/16 个有
- `ImageScaleToTotalPixels` —— 15/16 个有
- `LoadImage` —— 15/16 个有
- `LoraLoaderModelOnly` —— 15/16 个有
- `PreviewImage` —— 15/16 个有
- `UNETLoader` —— 15/16 个有
- `CR Text` —— 14/16 个有
- `LayerUtility: ImageReel` —— 14/16 个有
- `LayerUtility: ImageReelComposit` —— 14/16 个有
- `Image Comparer (rgthree)` —— 12/16 个有
- `ImageStitch` —— 11/16 个有
- `PrimitiveFloat` —— 10/16 个有
- `ImageScaleToMaxDimension` —— 2/16 个有
- `JWFloat` —— 2/16 个有
- `ClothesSegment` —— 1/16 个有
- `ColorMatchToReference` —— 1/16 个有
- `CustomAddLabel` —— 1/16 个有
- `HAIGC_LoadImagesFromZip` —— 1/16 个有
- `ImageCompositeMasked` —— 1/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/16 个有
- `LoadDiffusionModelShared //Inspire` —— 1/16 个有
- `LoadTextEncoderShared //Inspire` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

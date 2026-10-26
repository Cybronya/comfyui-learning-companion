---
name: unknown_workflow_sampler_clip_unet_59
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.915214
common_nodes: [CLIPLoader, CLIPTextEncode, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/F.2 - klein9b - 自动溶图打光一致性_2057337249720782849.json, 图片生成/图生图/F.2Klein9bBFS最强换脸保持一致性_2063776218675245057.json, 图片生成/图生图/F.2Klein9b全能图像编辑超强一致性_2056202050345684993.json, 图片生成/图生图/F.2Klein9b全能图像编辑超强一致性_2057338153110953986.json, 图片生成/图生图/F.2Klein9b全能图像编辑超强证件照一致性_2053752493900873729.json, 图片生成/图生图/F.2klein9b自动溶图打光一致性_2053386790131773442.json, 图片生成/图生图/F.2klein9b自动溶图打光一致性_2056051923589058561.json, 图片生成/图生图/F.2klein9b自动溶图打光一致性_2056259309541089281.json, 图片生成/图生图/F.2klein9b自动溶图打光一致性_2057329599301902337.json, 图片生成/图生图/F2K图像编辑_2091763181373976577.json, 图片生成/图生图/Flux2图像编辑换装局部重绘_2092444261538160642.json, 图片生成/图生图/Klein-9b-高一致性图像编辑可娱乐_2053013506131279873.json, 图片生成/图生图/Klein-9b-高一致性图像编辑（可娱乐）_2032259159961374721.json, 图片生成/图生图/flux2 Klein图像编辑-改背景，改颜色_2059198574604414977.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_59

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/F.2 - klein9b - 自动溶图打光一致性_2057337249720782849.json、图片生成/图生图/F.2Klein9bBFS最强换脸保持一致性_2063776218675245057.json、图片生成/图生图/F.2Klein9b全能图像编辑超强一致性_2056202050345684993.json、图片生成/图生图/F.2Klein9b全能图像编辑超强一致性_2057338153110953986.json、图片生成/图生图/F.2Klein9b全能图像编辑超强证件照一致性_2053752493900873729.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
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
- `CFGGuider` —— 9/14 个有
- `ConditioningZeroOut` —— 9/14 个有
- `EmptyFlux2LatentImage` —— 9/14 个有
- `ImageScaleToTotalPixels` —— 9/14 个有
- `Int` —— 9/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/14 个有
- `LoraLoaderModelOnly` —— 8/14 个有
- `LayerUtility: PurgeVRAM V2` —— 6/14 个有
- `Seed (rgthree)` —— 6/14 个有
- `BasicGuider` —— 5/14 个有
- `ColorMatch` —— 5/14 个有
- `easy positive` —— 5/14 个有
- `CR Text` —— 3/14 个有
- `Fast Groups Bypasser (rgthree)` —— 3/14 个有
- `ImageResizeKJv2` —— 3/14 个有
- `PreviewImage` —— 3/14 个有
- `HAIGC_SaveImagesToZip` —— 2/14 个有
- `LoadLatent` —— 2/14 个有
- `SaveLatent` —— 2/14 个有
- `easy imageConcat` —— 2/14 个有
- `PreviewAny` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_sampler_clip_unet_22
type: Unknown Workflow
frequency: 25
level: moderate
coverage: 0.81404
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2-Klein9b证件照 - AI一键生成专业证件照_2039260252654280706.json, 图片生成/图生图/Flux2-klein 单双图编辑_2012469809119764482.json, 图片生成/图生图/Flux2-klein 单图编辑之胸围调节器_2021575947543121921.json, 图片生成/图生图/Flux2-klein 双图编辑_2013531882973040642.json, 图片生成/图生图/Flux2-klein-4B单图+双图编辑工作流_2013144477556285442.json, 图片生成/图生图/Flux2-klein-9B单图+双图编辑 多风格转换 多角色多视觉创作设计_2025761285224271874.json, 图片生成/图生图/Flux2-klein-单图编辑+双图编辑_2012099023846514690.json, 图片生成/图生图/Flux2-klein-双图编辑-换脸换颜色换背景_2012118660227272706.json, 图片生成/图生图/Flux2Klein9b万物迁移_2050069477714345986.json, 图片生成/图生图/Flux2Klein9b万物迁移_2051441888972029954.json, 图片生成/图生图/Flux2Klein9b换装换物万物迁移_2059100959283965953.json, 图片生成/图生图/Klein -风格转绘_2090068733799784450.json, 图片生成/图生图/Klein-双图 可换脸换颜色换背景_2014216991204188162.json, 图片生成/图生图/f2k_9B_IP转三视图_2023738211675152385.json, 图片生成/图生图/f2k_9b_anything change clothes 3.0 万物迁移_2048647017747976194.json, 图片生成/图生图/f2k_9b_anything change clothes _万物迁移_2018950444059467777.json, 图片生成/图生图/flux2+klein+9B真人转动漫极速版 卡通动画角色设定  漫画手绘卡通 极速出图_2055626421451665410.json, 图片生成/图生图/flux2+klein+9B真人转动漫极速版 卡通动画角色设定  漫画手绘卡通 极速出图_2056274420871815169.json, 图片生成/图生图/flux2_klein_9b_动漫转实景_2016022089664307202.json, 图片生成/图生图/flux2_klein_漫画转实景_2013834475771269122.json, 图片生成/图生图/【真人转动漫】FLUX.2.0_Klein9B_2032008428285075458.json, 图片生成/图生图/一键生成+真人转动漫+卡通动画角色设定+flux2+klein+9B+漫画手绘卡通网剧_2058708137649205250.json, 图片生成/图生图/一键生成+真人转动漫+卡通动画角色设定+flux2+klein+9B+漫画手绘卡通网剧_2090695210543181826.json, 图片生成/图生图/丰胸效果 美女模特身材优化 胸部增强胸部放大_2081213931091218434.json, 图片生成/图生图/丰胸效果( Flux-2-klein-9B)+胸部增强胸部放大+美女模特身材优化_2070384154809815042.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_22

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（图片生成/图生图/Flux2-Klein9b证件照 - AI一键生成专业证件照_2039260252654280706.json、图片生成/图生图/Flux2-klein 单双图编辑_2012469809119764482.json、图片生成/图生图/Flux2-klein 单图编辑之胸围调节器_2021575947543121921.json、图片生成/图生图/Flux2-klein 双图编辑_2013531882973040642.json、图片生成/图生图/Flux2-klein-4B单图+双图编辑工作流_2013144477556285442.json…）

- **类型**：Unknown Workflow
- **样本数**：25
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 25 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
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
- `Flux2Scheduler` —— 24/25 个有
- `GetImageSize` —— 24/25 个有
- `CR Text` —— 20/25 个有
- `LayerUtility: ImageReel` —— 19/25 个有
- `LayerUtility: ImageReelComposit` —— 19/25 个有
- `GetNode` —— 18/25 个有
- `LoraLoaderModelOnly` —— 18/25 个有
- `SetNode` —— 18/25 个有
- `Image Comparer (rgthree)` —— 16/25 个有
- `easy imageScaleDownToSize` —— 15/25 个有
- `Fast Groups Bypasser (rgthree)` —— 12/25 个有
- `Int` —— 10/25 个有
- `easy cleanGpuUsed` —— 8/25 个有
- `ImageScaleToTotalPixels` —— 7/25 个有
- `JWInteger` —— 5/25 个有
- `图像缩放V2_孤海` —— 3/25 个有
- `PreviewImage` —— 2/25 个有
- `easy promptConcat` —— 2/25 个有
- `easy showAnything` —— 2/25 个有
- `BasicScheduler` —— 1/25 个有
- `PrimitiveFloat` —— 1/25 个有
- `PrimitiveStringMultiline` —— 1/25 个有
- `Text` —— 1/25 个有
- `Text Load Line From File` —— 1/25 个有
- `easy mathInt` —— 1/25 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_sampler_clip_unet_18
type: Unknown Workflow
frequency: 28
level: moderate
coverage: 0.983893
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2-Klein9b证件照 - AI一键生成专业证件照_2039260252654280706.json, 图片生成/图生图/Flux2-klein 一次性多图 电商产品迁移_2046045595718131714.json, 图片生成/图生图/Flux2-klein 双图编辑_2013531882973040642.json, 图片生成/图生图/Flux2-klein-4B单图+双图编辑工作流_2013144477556285442.json, 图片生成/图生图/Flux2-klein三图编辑_2014894419652120577.json, 图片生成/图生图/Flux2-klein单图+双图编辑工作流_2012077133371281410.json, 图片生成/图生图/Flux2-klein单图+双图编辑工作流_2012490858884505601.json, 图片生成/图生图/Flux2-klein单图+双图编辑工作流。两张照片，可以单图编辑，也可以双图融合，效果不错，值得推_2032745452604493825.json, 图片生成/图生图/Flux2-klein双图编辑_2014262671088029698.json, 图片生成/图生图/Flux2-klein双图编辑_2071856786591801345.json, 图片生成/图生图/Flux2-klein双图编辑_2094963496629923841.json, 图片生成/图生图/Flux2-klein双图编辑_2099463529001738242.json, 图片生成/图生图/Flux2-klein编辑工作流_2012818467442921473.json, 图片生成/图生图/Flux2.Klein_KV 4steps_2046833812876824578.json, 图片生成/图生图/Flux2Klein-4B 一致性人物替换加速版_2015600860935491586.json, 图片生成/图生图/Flux2Klein-4B 人物一致性换装_2043595835887329282.json, 图片生成/图生图/Flux2Klein-换内衣-9B版_2013862581559107585.json, 图片生成/图生图/Flux2Klein-换内衣_2084936137038188546.json, 图片生成/图生图/Flux2Klein-换装_2015725097327267841.json, 图片生成/图生图/Flux2Klein-换装工作流-高级版_1938439504737034241.json, 图片生成/图生图/Flux2Klein9B动漫转写实真人_2061651201707569153.json, 图片生成/图生图/Flux2Klein人物换脸+多图编辑_2018928471556235265.json, 图片生成/图生图/Flux2Klein人物换脸高清快速版_2047599085003218946.json, 图片生成/图生图/Flux2Klein多图编辑4B加速版Flux2Klein多图编辑4B加速版_2012067711764926466.json, 图片生成/图生图/Flux2Klein多图编辑4B加速版本_2012148311343501314.json, 图片生成/图生图/FluxKlein场景替换_人物替换加速高质量_2033122074021076994.json, 图片生成/图生图/Klein -风格转绘_2090068733799784450.json, 图片生成/图生图/全能证件照Flux2-Klein9b，一致性最强_2020492624783740930.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_18

> 由 `engine/knowledge_consolidation` 从 28 个 workflow 归纳得出（图片生成/图生图/Flux2-Klein9b证件照 - AI一键生成专业证件照_2039260252654280706.json、图片生成/图生图/Flux2-klein 一次性多图 电商产品迁移_2046045595718131714.json、图片生成/图生图/Flux2-klein 双图编辑_2013531882973040642.json、图片生成/图生图/Flux2-klein-4B单图+双图编辑工作流_2013144477556285442.json、图片生成/图生图/Flux2-klein三图编辑_2014894419652120577.json…）

- **类型**：Unknown Workflow
- **样本数**：28
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 28 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
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
- `ImageScaleToTotalPixels` —— 27/28 个有
- `Flux2Scheduler` —— 26/28 个有
- `EmptyFlux2LatentImage` —— 23/28 个有
- `ConditioningZeroOut` —— 22/28 个有
- `CR Text` —— 21/28 个有
- `GetImageSize` —— 15/28 个有
- `ImageConcanate` —— 11/28 个有
- `JWFloat` —— 10/28 个有
- `easy imageSize` —— 6/28 个有
- `LoraLoaderModelOnly` —— 5/28 个有
- `easy promptConcat` —— 3/28 个有
- `easy showAnything` —— 3/28 个有
- `BasicScheduler` —— 2/28 个有
- `Int` —— 2/28 个有
- `Image Comparer (rgthree)` —— 1/28 个有
- `ImpactMakeAnyList` —— 1/28 个有
- `JWInteger` —— 1/28 个有
- `PrimitiveFloat` —— 1/28 个有
- `PrimitiveStringMultiline` —— 1/28 个有
- `Text Load Line From File` —— 1/28 个有
- `Text Multiline` —— 1/28 个有
- `easy imageScaleDownToSize` —— 1/28 个有
- `easy mathInt` —— 1/28 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

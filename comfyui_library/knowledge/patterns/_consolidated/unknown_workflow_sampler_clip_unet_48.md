---
name: unknown_workflow_sampler_clip_unet_48
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.622062
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/AI漫剧 分镜一键生成（免费版）_2049505485845434370.json, 图片生成/图生图/AI漫剧 分镜一键生成（免费版）_2049512732680003585.json, 图片生成/图生图/F2 klein 9b多角度漫剧分镜三视图_2061788380777762818.json, 图片生成/图生图/F2_klein_9b多角度漫剧分镜三视图_2087347699246002178.json, 图片生成/图生图/FLUX2-KLEIN 双图编辑 超真实一键换头换_2016348870447472642.json, 图片生成/图生图/Flux2-KLEIN 三图编辑_2016421909616922626.json, 图片生成/图生图/flux2-klein多功能单图_双图编辑_2068895971546845186.json, 图片生成/图生图/flux2-klein多功能单图_双图编辑_2068990679107325953.json, 图片生成/图生图/【Supermate】自用测试白里透红极致皮肤FLUX2-KLEIN _ 文生图+多图编辑大合集_2013554748233883650.json, 图片生成/图生图/一键漫剧分镜流(免费版)-邻家AI大女孩_2049665338568130561.json, 图片生成/图生图/一键漫剧分镜流（免费版）_2013908081847046145.json, 图片生成/图生图/建筑与室内效果图渲染_2021215392135389186.json, 图片生成/文生图/FLUX2-KLEIN _ 文生图+多图编辑大合集_2012077337252204546.json, 图片生成/文生图/FLUX2-KLEIN _ 文生图+多图编辑大合集_2012132446178910209.json, 图片生成/文生图/FLUX2-KLEIN _ 文生图+多图编辑大合集_2015497456603111426.json, 图片生成/文生图/一键漫剧分镜出图（免费版）_2046497420153982978.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_48

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/AI漫剧 分镜一键生成（免费版）_2049505485845434370.json、图片生成/图生图/AI漫剧 分镜一键生成（免费版）_2049512732680003585.json、图片生成/图生图/F2 klein 9b多角度漫剧分镜三视图_2061788380777762818.json、图片生成/图生图/F2_klein_9b多角度漫剧分镜三视图_2087347699246002178.json、图片生成/图生图/FLUX2-KLEIN 双图编辑 超真实一键换头换_2016348870447472642.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：62%

## 共有节点

全部 16 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptyFlux2LatentImage`
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

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 14/16 个有
- `INTConstant` —— 14/16 个有
- `easy cleanGpuUsed` —— 13/16 个有
- `GetNode` —— 9/16 个有
- `LayerUtility: ImageReel` —— 9/16 个有
- `LayerUtility: ImageReelComposit` —— 9/16 个有
- `SetNode` —— 9/16 个有
- `CR Text Concatenate` —— 7/16 个有
- `List of strings [Crystools]` —— 7/16 个有
- `PromptBatchQueue` —— 7/16 个有
- `ShowText|pysssss` —— 7/16 个有
- `SomethingToString` —— 7/16 个有
- `Split String` —— 7/16 个有
- `ConditioningZeroOut` —— 2/16 个有
- `Label (rgthree)` —— 2/16 个有
- `LoraLoaderModelOnly` —— 2/16 个有
- `TTResolutionSelector` —— 2/16 个有
- `Image Comparer (rgthree)` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_lora_sampler_clip_23
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.754467
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, GetNode, Image Comparer (rgthree), KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/flux.2 klein 9b-重打光·照片光源重新照明着色_2027329955582976001.json, 平台全量/flux.2 klein 9b-重打光·照片光源重新照明着色_2034629810638557186.json, 平台全量/万物迁移 换脸换装换背景 局部重绘FLUX 2 9b anything change_2052551456070348802.json, 平台全量/丰胸效果 Flux-2-klein-9B 胸部放大 美女模特身材优化_2029785490177658882.json, 平台全量/丰胸效果 胸部增强 Flux-2-klein-9B 胸部放大 美女模特身材优化_2037054850244022274.json, 平台全量/丰胸效果 胸部增强 Flux-2-klein-9B 胸部放大 美女模特身材优化_2055119095477088258.json, 平台全量/产品换背景 重新打光融图 FLUX2-Klein电商产品主图编辑 自动匹配场景_2030874130374987777.json, 平台全量/换脸换装 万物迁移 换背景 局部重绘FLUX 2 9b anything change_2052625343177084929.json, 平台全量/服饰换装 换装换脸 风格统一  Flux2-klein-9B 万物迁移_2029383671819538433.json, 平台全量/电商模特  完美身材  大大大_2060989070385438722.json, 平台全量/真人转动漫 Real life to Animation Flux2-Klein 9B_2033411114142277633.json, 平台全量/真人转动漫 flux2 klein 9B  漫画手绘卡通网剧_2030149737764098050.json, 平台全量/真人转动漫 极速版 flux2 klein 9B 漫画手绘卡通网剧_2035946693237153794.json, 平台全量/身材优化 丰胸效果 胸部增强 Flux-2-klein-9B 胸部放大 美女模特_2049353833167458305.json, 平台全量/身材优化 丰胸效果(+Flux-2-klein-9B)+胸部增强胸部放大 美女模特身材优化_2071412790501400577.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_23

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（平台全量/flux.2 klein 9b-重打光·照片光源重新照明着色_2027329955582976001.json、平台全量/flux.2 klein 9b-重打光·照片光源重新照明着色_2034629810638557186.json、平台全量/万物迁移 换脸换装换背景 局部重绘FLUX 2 9b anything change_2052551456070348802.json、平台全量/丰胸效果 Flux-2-klein-9B 胸部放大 美女模特身材优化_2029785490177658882.json、平台全量/丰胸效果 胸部增强 Flux-2-klein-9B 胸部放大 美女模特身材优化_2037054850244022274.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 15 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `GetNode`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 14/15 个有
- `LayerUtility: ImageReel` —— 13/15 个有
- `LayerUtility: ImageReelComposit` —— 13/15 个有
- `easy imageScaleDownToSize` —— 13/15 个有
- `easy cleanGpuUsed` —— 9/15 个有
- `JWInteger` —— 6/15 个有
- `Int` —— 3/15 个有
- `Anything Everywhere` —— 2/15 个有
- `Float` —— 2/15 个有
- `ImpactSwitch` —— 2/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/15 个有
- `QwenMultiangleLightningNode` —— 2/15 个有
- `RebatchLatents` —— 2/15 个有
- `RepeatLatentBatch` —— 2/15 个有
- `easy showAnything` —— 2/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

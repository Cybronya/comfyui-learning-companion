---
name: image_to_image_sampler_clip_unet_115
type: Image To Image
frequency: 5
level: strong
coverage: 0.936
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, CR Text Concatenate, ConditioningZeroOut, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), Flux2Scheduler, Image Comparer (rgthree), ImageCASharpening+, ImageListToImageBatch, ImageScaleBy, ImpactImageBatchToImageList, JanusImageUnderstanding, JanusModelLoader, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: NumberCalculatorV2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAEEncodeTiled, VAELoader, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2 Klein-9B 衣服提取与换装双工作流 开源最夯_2070025165500669954.json, 图片生成/图生图/Flux2_klein_9B_4K_8K_去油腻进阶超分高清放大工作流_好用_2077207085812637697.json, 图片生成/图生图/Flux2_klein_9B_4K_8K_去油腻进阶超分高清放大工作流_好用_2077211493933862914.json, 平台全量/Flux2 Klein 9B BFS开源最强换脸工作流_2070580513798189057.json, 平台全量/Flux2 klein 9B 4K 8K 去油腻进阶超分高清放大工作流 （好用）_2058482736050036738.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_115

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Flux2 Klein-9B 衣服提取与换装双工作流 开源最夯_2070025165500669954.json、图片生成/图生图/Flux2_klein_9B_4K_8K_去油腻进阶超分高清放大工作流_好用_2077207085812637697.json、图片生成/图生图/Flux2_klein_9B_4K_8K_去油腻进阶超分高清放大工作流_好用_2077211493933862914.json、平台全量/Flux2 Klein 9B BFS开源最强换脸工作流_2070580513798189057.json、平台全量/Flux2 klein 9B 4K 8K 去油腻进阶超分高清放大工作流 （好用）_2058482736050036738.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `Image Comparer (rgthree)`
- `ImageCASharpening+`
- `ImageListToImageBatch`
- `ImageScaleBy`
- `ImpactImageBatchToImageList`
- `JanusImageUnderstanding`
- `JanusModelLoader`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: NumberCalculatorV2`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAEEncodeTiled`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 4/5 个有
- `ImageColorMatchAdobe+` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `CR Text Input Switch (4 way)` —— 3/5 个有
- `ImpactInt` —— 3/5 个有
- `easy int` —— 3/5 个有
- `ColorMatch` —— 1/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `ModelMemoryUsageFactorOverride` —— 1/5 个有
- `PathchSageAttentionKJ` —— 1/5 个有
- `PixaromaLabel` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `RHHiddenNodes` —— 1/5 个有
- `RMBG` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 5 - 6 | 5 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 0.73 | 0.5 - 0.73 | 5 | 82% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 5 - 6，5 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 0.73，观测区间 0.5 - 0.73，5 个样本，取值集中（一致性 82%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足

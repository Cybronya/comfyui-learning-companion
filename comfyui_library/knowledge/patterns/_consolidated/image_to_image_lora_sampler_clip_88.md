---
name: image_to_image_lora_sampler_clip_88
type: Image To Image
frequency: 3
level: strong
coverage: 0.935333
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, CR Text Concatenate, ConditioningZeroOut, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), Flux2Scheduler, Image Comparer (rgthree), ImageCASharpening+, ImageListToImageBatch, ImageScaleBy, ImpactImageBatchToImageList, JanusImageUnderstanding, JanusModelLoader, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: NumberCalculatorV2, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAEEncodeTiled, VAELoader, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2 Klein-9B 衣服提取与换装双工作流 开源最夯_2070025165500669954.json, 图片生成/图生图/Flux2_klein_9B_4K_8K_去油腻进阶超分高清放大工作流_好用_2077207085812637697.json, 图片生成/图生图/Flux2_klein_9B_4K_8K_去油腻进阶超分高清放大工作流_好用_2077211493933862914.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_88

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Flux2 Klein-9B 衣服提取与换装双工作流 开源最夯_2070025165500669954.json、图片生成/图生图/Flux2_klein_9B_4K_8K_去油腻进阶超分高清放大工作流_好用_2077207085812637697.json、图片生成/图生图/Flux2_klein_9B_4K_8K_去油腻进阶超分高清放大工作流_好用_2077211493933862914.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
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
- `LoraLoaderModelOnly`
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
- `CR Text` —— 2/3 个有
- `CR Text Input Switch (4 way)` —— 2/3 个有
- `ImageColorMatchAdobe+` —— 2/3 个有
- `ImpactInt` —— 2/3 个有
- `easy int` —— 2/3 个有
- `ColorMatch` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 5 - 6 | 3 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 0.73 | 0.5 - 0.73 | 3 | 83% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 5 - 6，3 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 0.73，观测区间 0.5 - 0.73，3 个样本，取值集中（一致性 83%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足

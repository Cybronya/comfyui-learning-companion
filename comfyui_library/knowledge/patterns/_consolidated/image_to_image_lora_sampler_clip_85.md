---
name: image_to_image_lora_sampler_clip_85
type: Image To Image
frequency: 5
level: moderate
coverage: 0.898
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImageResize+, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy float, easy getNode, easy imageBatchToImageList, easy imageListToImageBatch, easy setNode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人像修复_1.0_2075034041816014849.json, 图片生成/图生图/人像修复_1.0_2075042147572731905.json, 图片生成/图生图/人像修复_1.0_2076042842564284418.json, 平台全量/场景中的透明瓶身（包含磨砂）精修，包含场景修图_2064636498149990401.json, 平台全量/透明、实色、金属、磨砂 精修_2065731513416769537.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_85

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/人像修复_1.0_2075034041816014849.json、图片生成/图生图/人像修复_1.0_2075042147572731905.json、图片生成/图生图/人像修复_1.0_2076042842564284418.json、平台全量/场景中的透明瓶身（包含磨砂）精修，包含场景修图_2064636498149990401.json、平台全量/透明、实色、金属、磨砂 精修_2065731513416769537.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy float`
- `easy getNode`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `easy setNode`

**可变部分**（部分 workflow 才有）：
- `FluxGuidance` —— 4/5 个有
- `ImageAutoSelector` —— 4/5 个有
- `Int` —— 4/5 个有
- `RepeatLatentBatch` —— 4/5 个有
- `GetImageSize` —— 3/5 个有
- `SDVN Image Color Match` —— 3/5 个有
- `SimpleMath+` —— 3/5 个有
- `easy seed` —— 3/5 个有
- `ImpactMinMax` —— 2/5 个有
- `JjkText` —— 2/5 个有
- `PrimitiveFloat` —— 2/5 个有
- `PrimitiveInt` —— 2/5 个有
- `SeedVR2LoadDiTModel` —— 2/5 个有
- `SeedVR2LoadVAEModel` —— 2/5 个有
- `SeedVR2VideoUpscaler` —— 2/5 个有
- `easy cleanGpuUsed` —— 2/5 个有
- `easy imageSize` —— 2/5 个有
- `CR Text Concatenate` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 16 | 5 | 35% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 0.95 - 1 | 5 | 98% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 16，5 个样本，取值分散，一致性仅 35%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.95 - 1，5 个样本，取值集中（一致性 98%）
- 高发问题（7/5 个样本）：Steps较低可能导致细节不足

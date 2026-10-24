---
name: image_to_image_lora_sampler_clip_104
type: Image To Image
frequency: 3
level: strong
coverage: 0.964
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Fast Groups Bypasser (rgthree), FluxGuidance, GetImageSize, Image Comparer (rgthree), ImageAutoSelector, ImageResize+, Int, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, RepeatLatentBatch, SDVN Image Color Match, SaveImage, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy float, easy getNode, easy imageBatchToImageList, easy imageListToImageBatch, easy seed, easy setNode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人像修复_1.0_2075034041816014849.json, 图片生成/图生图/人像修复_1.0_2075042147572731905.json, 图片生成/图生图/人像修复_1.0_2076042842564284418.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_104

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/人像修复_1.0_2075034041816014849.json、图片生成/图生图/人像修复_1.0_2075042147572731905.json、图片生成/图生图/人像修复_1.0_2076042842564284418.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageAutoSelector`
- `ImageResize+`
- `Int`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `RepeatLatentBatch`
- `SDVN Image Color Match`
- `SaveImage`
- `SimpleMath+`
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
- `easy seed`
- `easy setNode`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（6/3 个样本）：Steps较低可能导致细节不足

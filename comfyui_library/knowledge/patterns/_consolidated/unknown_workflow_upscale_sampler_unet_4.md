---
name: unknown_workflow_upscale_sampler_unet_4
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.706
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetNode, Image Comparer (rgthree), ImageResize+, ImageScaleBy, KSampler, LoadImage, QwenImage21Cache, ResolutionSelector, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: [ImageResize+, easy imageSize, Label (rgthree), LayerUtility: ImageReel, LayerUtility: ImageReelComposit]
members: [图片生成/图生图/2102576678341009409.json, 图片生成/图生图/2102617237571067905.json, 图片生成/文生图/Qwen2.1文生图_图生视频高清工作流合集V2_2103104839063531521.json, 图片生成/文生图/Qwen2.1文生图_图生视频高清工作流合集_2102020890262331394.json, 图片生成/文生图/千问Qwen2.1文生图_图像编辑合集_t2i_i2i-edit-Collection_2102576678341009409.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_unet_4

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/2102576678341009409.json、图片生成/图生图/2102617237571067905.json、图片生成/文生图/Qwen2.1文生图_图生视频高清工作流合集V2_2103104839063531521.json、图片生成/文生图/Qwen2.1文生图_图生视频高清工作流合集_2102020890262331394.json、图片生成/文生图/千问Qwen2.1文生图_图像编辑合集_t2i_i2i-edit-Collection_2102576678341009409.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 4/5 个有
- `Label (rgthree)` —— 3/5 个有
- `ImageConcatMulti` —— 2/5 个有
- `Int` —— 2/5 个有
- `PrimitiveStringMultiline` —— 2/5 个有
- `DWPreprocessor` —— 1/5 个有
- `DepthAnythingV2Preprocessor` —— 1/5 个有
- `LayerUtility: ImageReel` —— 1/5 个有
- `LayerUtility: ImageReelComposit` —— 1/5 个有
- `LineArtPreprocessor` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `PreviewImage` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1024 | 1024 - 1024 | 5 | 100% |
| 采样步数 | 50 | 4 - 50 | 5 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 50，观测区间 4 - 50，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：ImageResize+、easy imageSize、Label (rgthree)、LayerUtility: ImageReel、LayerUtility: ImageReelComposit

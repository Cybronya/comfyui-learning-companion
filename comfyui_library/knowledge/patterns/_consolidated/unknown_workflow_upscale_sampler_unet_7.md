---
name: unknown_workflow_upscale_sampler_unet_7
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.778667
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetNode, Image Comparer (rgthree), ImageResize+, ImageScaleBy, KSampler, QwenImage21Cache, ResolutionSelector, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问Qwen2.1文生图_图像编辑合集_t2i_i2i-edit-Collection_2102576678341009409.json, 图片生成/文生图/Qwen-Image-2.1 亚洲人像 _ 摄影胶片_2112163425462865921.json, 图片生成/文生图/Qwen-Image-2.1-Turbo 亚洲人像 摄影专用_2112038053098377218.json, 图片生成/文生图/Qwen2.1 亚洲摄影 _ 人像写真 (4K高清）_2112186702088462337.json, 图片生成/文生图/Qwen2.1文生图_图生视频高清工作流合集V2_2103104839063531521.json, 图片生成/文生图/Qwen2.1文生图_图生视频高清工作流合集_2102020890262331394.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_unet_7

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/千问Qwen2.1文生图_图像编辑合集_t2i_i2i-edit-Collection_2102576678341009409.json、图片生成/文生图/Qwen-Image-2.1 亚洲人像 _ 摄影胶片_2112163425462865921.json、图片生成/文生图/Qwen-Image-2.1-Turbo 亚洲人像 摄影专用_2112038053098377218.json、图片生成/文生图/Qwen2.1 亚洲摄影 _ 人像写真 (4K高清）_2112186702088462337.json、图片生成/文生图/Qwen2.1文生图_图生视频高清工作流合集V2_2103104839063531521.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
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
- `LoraLoaderModelOnly` —— 4/6 个有
- `Any Switch (rgthree)` —— 3/6 个有
- `CR Prompt Text` —— 3/6 个有
- `Color Grading JK` —— 3/6 个有
- `LayerUtility: PurgeVRAM` —— 3/6 个有
- `LoadImage` —— 3/6 个有
- `PreviewImage` —— 3/6 个有
- `ImageConcatMulti` —— 2/6 个有
- `Label (rgthree)` —— 2/6 个有
- `Int` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 6 | 100% |
| 高度 | 1024 | 1024 - 1024 | 6 | 100% |
| 采样步数 | 8.5 | 4 - 50 | 6 | 5% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8.5，观测区间 4 - 50，6 个样本，取值分散，一致性仅 5%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（5/6 个样本）：Steps较低可能导致细节不足

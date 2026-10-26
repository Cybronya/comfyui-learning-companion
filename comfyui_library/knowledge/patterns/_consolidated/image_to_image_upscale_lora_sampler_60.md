---
name: image_to_image_upscale_lora_sampler_60
type: Image To Image
frequency: 3
level: strong
coverage: 0.83
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, GetImageSize, GetImageSize+, Image Comparer (rgthree), ImageResize+, ImageScaleBy, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人物换脸（真实美感）专用工作流 DB（f2k9b+Kook）_2035942152928235521.json, 图片生成/图生图/放大_2057392876400758786.json, 图片生成/图生图/最强人物换脸 双方法_2055255871818616834.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_60

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/人物换脸（真实美感）专用工作流 DB（f2k9b+Kook）_2035942152928235521.json、图片生成/图生图/放大_2057392876400758786.json、图片生成/图生图/最强人物换脸 双方法_2055255871818616834.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `GetImageSize`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `ImageCASharpening+` —— 2/3 个有
- `ImageConcatMulti` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 2/3 个有
- `LayerUtility: PurgeVRAM V2` —— 2/3 个有
- `RunningHub Deepcleaner` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `easy imageConcat` —— 2/3 个有
- `CR Image Input Switch` —— 1/3 个有
- `CR Text` —— 1/3 个有
- `ImageScaleToMaxDimension` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LazySwitch1way` —— 1/3 个有
- `PrimitiveBoolean` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 3 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足

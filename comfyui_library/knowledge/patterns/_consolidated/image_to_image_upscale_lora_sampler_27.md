---
name: image_to_image_upscale_lora_sampler_27
type: Image To Image
frequency: 6
level: moderate
coverage: 0.894333
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, GetImageSize+, Image Comparer (rgthree), ImageResize+, ImageScaleBy, ImageUpscaleWithModel, KOOK_ImageCompression, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image 图生图一键优化洗图 高清8K出图，最完美的洗图流，细节爆棚！_2048563802806951938.json, 图片生成/图生图/Z-image 图生图一键优化洗图 高清8K出图，最完美的洗图流，细节爆棚！_2048597151487365121.json, 图片生成/图生图/极客组合：模糊图“重生”超清放大工作流（Qwen + TTP + Z-image）_2006256542605119489.json, 图片生成/图生图/（自用）ZT8K洗图_2037033662457323522.json, 图片生成/图生图/🦁Z-image 图生图一键优化洗图 高清8K出图_2004147923271204865.json, 图片生成/图生图/🦁Z-image 图生图一键优化洗图 高清8K出图_2011768773262446594.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_27

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Z-image 图生图一键优化洗图 高清8K出图，最完美的洗图流，细节爆棚！_2048563802806951938.json、图片生成/图生图/Z-image 图生图一键优化洗图 高清8K出图，最完美的洗图流，细节爆棚！_2048597151487365121.json、图片生成/图生图/极客组合：模糊图“重生”超清放大工作流（Qwen + TTP + Z-image）_2006256542605119489.json、图片生成/图生图/（自用）ZT8K洗图_2037033662457323522.json、图片生成/图生图/🦁Z-image 图生图一键优化洗图 高清8K出图_2004147923271204865.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KOOK_ImageCompression`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 5/6 个有
- `ImpactFloat` —— 5/6 个有
- `RH_LLMAPI_NODE` —— 5/6 个有
- `RandomNoise` —— 5/6 个有
- `RepeatLatentBatch` —— 5/6 个有
- `easy int` —— 5/6 个有
- `Note Plus (mtb)` —— 2/6 个有
- `CR Value Cycler` —— 1/6 个有
- `GetImageSize` —— 1/6 个有
- `ImageListToBatch+` —— 1/6 个有
- `KSamplerAdvanced` —— 1/6 个有
- `MathExpression|pysssss` —— 1/6 个有
- `ModelSamplingAuraFlow` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `ReferenceLatent` —— 1/6 个有
- `RunningHub Deepcleaner` —— 1/6 个有
- `ShowAnything|Mie` —— 1/6 个有
- `TextEncodeQwenImageEditPlus` —— 1/6 个有
- `easy imageBatchToImageList` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 9 - 10 | 5 | 96% |
| Prompt 约束强度(CFG) | 1 | 1 - 10 | 6 | 0% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 9 - 10，5 个样本，取值集中（一致性 96%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 10，6 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/6 个样本）：Steps较低可能导致细节不足

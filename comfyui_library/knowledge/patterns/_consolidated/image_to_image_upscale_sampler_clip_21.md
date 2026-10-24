---
name: image_to_image_upscale_sampler_clip_21
type: Image To Image
frequency: 5
level: moderate
coverage: 0.8108
common_nodes: [CLIPTextEncode, ConditioningZeroOut, Image Comparer (rgthree), ImageResize+, ImageScaleBy, KSampler, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/GRAVES-质感优化+高清放大_2110566614830764034.json, 图片生成/图生图/修复细节，还原真实度、去AI感_2094694132613734402.json, 图片生成/图生图/修复细节，还原真实度、去AI感，反推提示词，洗图高清放大_2095323694716514305.json, 图片生成/图生图/修复细节，还原真实度、去AI感，反推提示词，洗图高清放大_2095427272378503169.json, 图片生成/文生图/Krea2-ControlNet 洗图_2080982528030236673.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_21

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/GRAVES-质感优化+高清放大_2110566614830764034.json、图片生成/图生图/修复细节，还原真实度、去AI感_2094694132613734402.json、图片生成/图生图/修复细节，还原真实度、去AI感，反推提示词，洗图高清放大_2095323694716514305.json、图片生成/图生图/修复细节，还原真实度、去AI感，反推提示词，洗图高清放大_2095427272378503169.json、图片生成/文生图/Krea2-ControlNet 洗图_2080982528030236673.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
- `LoadImage`
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
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `Qwen3_VQA` —— 4/5 个有
- `ImpactInt` —— 3/5 个有
- `LayerUtility: PurgeVRAM` —— 3/5 个有
- `ShowText|pysssss` —— 3/5 个有
- `GetNode` —— 2/5 个有
- `MuyeTextEditOutput` —— 2/5 个有
- `SetNode` —— 2/5 个有
- `AIO_Preprocessor` —— 1/5 个有
- `CLIPLoaderGGUF` —— 1/5 个有
- `DepthAnything_V3` —— 1/5 个有
- `DownloadAndLoadDepthAnythingV3Model` —— 1/5 个有
- `Krea2ControlApply` —— 1/5 个有
- `Krea2ControlImageEncode` —— 1/5 个有
- `Krea2ControlLoRALoader` —— 1/5 个有
- `ModelSamplingAuraFlow` —— 1/5 个有
- `PrimitiveFloat` —— 1/5 个有
- `Text` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 6 - 10 | 5 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 0.7 | 0.25 - 1 | 5 | 64% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 6 - 10，5 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 0.7，观测区间 0.25 - 1，5 个样本

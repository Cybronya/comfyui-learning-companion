---
name: text_to_image_lora_sampler_clip_269
type: Text To Image
frequency: 4
level: strong
coverage: 0.84525
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, FlashVSR_SM_KSampler, FlashVSR_SM_Model, Get Image Size, GetImageRangeFromBatch, Image Comparer (rgthree), ImageCASharpening+, ImageConcanate, ImageResize+, ImpactMinMax, JWInteger, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, PreviewImage, SaveImage, SeedVR2, TTP_Image_Assy, TTP_Image_Tile_Batch, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image turbo文生图+高清放大(FlashVSR+SeedVR2.5)_1999312098377203714.json, 图片生成/文生图/Z-image文生图+高清放大修复FlashVSR+SeedVR2.5_1996233743738224641.json, 图片生成/文生图/真8K超清Z-image文生图（3分40秒）_1994812513348935681.json, 图片生成/文生图/真8K超清Z-image文生图（3分40秒）_1994988686821535746.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_269

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Z-image turbo文生图+高清放大(FlashVSR+SeedVR2.5)_1999312098377203714.json、图片生成/文生图/Z-image文生图+高清放大修复FlashVSR+SeedVR2.5_1996233743738224641.json、图片生成/文生图/真8K超清Z-image文生图（3分40秒）_1994812513348935681.json、图片生成/文生图/真8K超清Z-image文生图（3分40秒）_1994988686821535746.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `FlashVSR_SM_KSampler`
- `FlashVSR_SM_Model`
- `Get Image Size`
- `GetImageRangeFromBatch`
- `Image Comparer (rgthree)`
- `ImageCASharpening+`
- `ImageConcanate`
- `ImageResize+`
- `ImpactMinMax`
- `JWInteger`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `SeedVR2`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 2/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `LoadImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 8 - 10 | 4 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1500 | 1080 - 1920 | 4 | 72% |
| 高度 | 1272 | 1080 - 1920 | 4 | 75% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 8 - 10，4 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1500，观测区间 1080 - 1920，4 个样本
- 高度 中位数 1272，观测区间 1080 - 1920，4 个样本
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足

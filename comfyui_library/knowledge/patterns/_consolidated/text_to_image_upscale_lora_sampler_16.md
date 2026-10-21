---
name: text_to_image_upscale_lora_sampler_16
type: Text To Image
frequency: 6
level: moderate
coverage: 0.8455
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, ConstrainImage|pysssss, EmptyLatentImage, Fast Groups Bypasser (rgthree), Get Image Size, Image Comparer (rgthree), ImageResize+, ImageScaleBy, KSampler, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, VAEDecode, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image-AIO版-文生图+SeedVR高清放大_2060974165913587713.json, 图片生成/文生图/Z-Image-Turbo _ PiD高清4K直出版 - 更快_2060968816380833794.json, 图片生成/文生图/Z-Image-Turbo+_+PiD高清4K直出版+-+更快_2070635052102414338.json, 图片生成/文生图/ZImageTurbo+PiD高清4K直出版更快_2065947456470347778.json, 图片生成/文生图/姿势复制 动作迁移 洗图 模特角色替换 Z-Image 高清4K   高清放大 SeedVR2_2063427520002879490.json, 图片生成/文生图/高清4K直出更快｜ZImageTurbo+PiD文生图_2092931963811352578.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_16

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Z-Image-AIO版-文生图+SeedVR高清放大_2060974165913587713.json、图片生成/文生图/Z-Image-Turbo _ PiD高清4K直出版 - 更快_2060968816380833794.json、图片生成/文生图/Z-Image-Turbo+_+PiD高清4K直出版+-+更快_2070635052102414338.json、图片生成/文生图/ZImageTurbo+PiD高清4K直出版更快_2065947456470347778.json、图片生成/文生图/姿势复制 动作迁移 洗图 模特角色替换 Z-Image 高清4K   高清放大 SeedVR2_2063427520002879490.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `ConstrainImage|pysssss`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Get Image Size`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `VAEDecode`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 5/6 个有
- `ModelSamplingAuraFlow` —— 5/6 个有
- `PiDFinalize` —— 5/6 个有
- `PiDKSamplerCapture` —— 5/6 个有
- `PiDPrepare` —— 5/6 个有
- `PiDSample` —— 5/6 个有
- `PiDTextPrompt` —— 5/6 个有
- `VAEDecodeTiled` —— 5/6 个有
- `Label (rgthree)` —— 3/6 个有
- `CLIPLoader` —— 1/6 个有
- `ImageScaleToTotalPixels` —— 1/6 个有
- `JjkText` —— 1/6 个有
- `LoadImage` —— 1/6 个有
- `PreviewAny` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `RH_Captioner` —— 1/6 个有
- `SeedVR2` —— 1/6 个有
- `SeedVR2BlockSwap` —— 1/6 个有
- `SeedVR2ExtraArgs` —— 1/6 个有
- `UNETLoader` —— 1/6 个有
- `VAELoader` —— 1/6 个有
- `solarL_SaveImagesToZip` —— 1/6 个有
- `孤海注释` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 4 - 9 | 6 | 77% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 6 | 18% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | beta | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1024 | 80 - 1024 | 6 | 59% |
| 高度 | 1536 | 80 - 1536 | 6 | 58% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 4 - 9，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，6 个样本，取值分散，一致性仅 18%
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 beta，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 80 - 1024，6 个样本
- 高度 中位数 1536，观测区间 80 - 1536，6 个样本

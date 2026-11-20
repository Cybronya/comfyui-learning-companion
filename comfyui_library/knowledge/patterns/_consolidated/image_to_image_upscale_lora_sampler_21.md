---
name: image_to_image_upscale_lora_sampler_21
type: Image To Image
frequency: 8
level: strong
coverage: 0.67675
common_nodes: [CFGNorm, CLIPLoader, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen 2511 双图编辑人物与场景融合_2008893097933021186.json, 图片生成/图生图/Qwen-Edit-2511-单图双图编辑_2005573346026811393.json, 图片生成/图生图/YZ金鱼-Qwen-Edit-2511-单图双图编辑_2003739155073015810.json, 图片生成/图生图/双图编辑人物与场景融合_2008739607826927617.json, 图片生成/图生图/星绘-超强一致性-Qwen2511-老照片超清修复_2009457667147833346.json, 图片生成/图生图/老照片超清修复Qwen2511-老照片修复_2007722366050242561.json, 图片生成/文生图/Qwen-Edit 2511 单_多图编辑，人物换装，解决偏色和像素偏移，SeedVR2高清修复_2004097023886434305.json, 平台全量/Qwen2511老照片超清修复_2009502216033406978.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_21

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Qwen 2511 双图编辑人物与场景融合_2008893097933021186.json、图片生成/图生图/Qwen-Edit-2511-单图双图编辑_2005573346026811393.json、图片生成/图生图/YZ金鱼-Qwen-Edit-2511-单图双图编辑_2003739155073015810.json、图片生成/图生图/双图编辑人物与场景融合_2008739607826927617.json、图片生成/图生图/星绘-超强一致性-Qwen2511-老照片超清修复_2009457667147833346.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageReel` —— 7/8 个有
- `LayerUtility: ImageReelComposit` —— 7/8 个有
- `PreviewImage` —— 7/8 个有
- `INTConstant` —— 6/8 个有
- `ConditioningZeroOut` —— 5/8 个有
- `GetImageSize+` —— 5/8 个有
- `GetNode` —— 5/8 个有
- `ImageResize+` —— 5/8 个有
- `ImageScaleBy` —— 5/8 个有
- `PlaySound|pysssss` —— 5/8 个有
- `SetNode` —— 5/8 个有
- `TTP_Image_Assy` —— 5/8 个有
- `TTP_Image_Tile_Batch` —— 5/8 个有
- `TTP_Tile_image_size` —— 5/8 个有
- `UNETLoader` —— 5/8 个有
- `VAELoader` —— 5/8 个有
- `easy cleanGpuUsed` —— 5/8 个有
- `easy showAnything` —— 5/8 个有
- `Fast Groups Bypasser (rgthree)` —— 4/8 个有
- `CR Prompt Text` —— 3/8 个有
- `CheckpointLoaderSimple` —— 3/8 个有
- `ImageScaleToTotalPixels` —— 3/8 个有
- `EmptyLatentImage` —— 2/8 个有
- `EmptySD3LatentImage` —— 1/8 个有
- `Image Rembg (Remove Background)` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler_ancestral | - | 8 | 75% |
| 调度器 | simple | - | 8 | 62% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 1500 | - | 2 | 72% |
| 高度 | 1500 | - | 2 | 72% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，8 个样本，一致性 75%
- 调度器 最常用 simple，8 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 1500，样本不足，未给区间，2 个样本
- 高度 中位数 1500，样本不足，未给区间，2 个样本
- 高发问题（12/8 个样本）：Steps较低可能导致细节不足

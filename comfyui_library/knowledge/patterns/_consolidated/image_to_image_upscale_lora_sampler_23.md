---
name: image_to_image_upscale_lora_sampler_23
type: Image To Image
frequency: 6
level: strong
coverage: 0.6435
common_nodes: [CFGNorm, CLIPLoader, Image Comparer (rgthree), KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, ReferenceLatent, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen 2511 双图编辑人物与场景融合_2008893097933021186.json, 图片生成/图生图/Qwen-Edit-2511-单图双图编辑_2005573346026811393.json, 图片生成/图生图/YZ金鱼-Qwen-Edit-2511-单图双图编辑_2003739155073015810.json, 图片生成/图生图/双图编辑人物与场景融合_2008739607826927617.json, 图片生成/图生图/星绘-超强一致性-Qwen2511-老照片超清修复_2009457667147833346.json, 图片生成/图生图/老照片超清修复Qwen2511-老照片修复_2007722366050242561.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_23

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen 2511 双图编辑人物与场景融合_2008893097933021186.json、图片生成/图生图/Qwen-Edit-2511-单图双图编辑_2005573346026811393.json、图片生成/图生图/YZ金鱼-Qwen-Edit-2511-单图双图编辑_2003739155073015810.json、图片生成/图生图/双图编辑人物与场景融合_2008739607826927617.json、图片生成/图生图/星绘-超强一致性-Qwen2511-老照片超清修复_2009457667147833346.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：64%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 5/6 个有
- `ConditioningZeroOut` —— 4/6 个有
- `GetImageSize+` —— 4/6 个有
- `GetNode` —— 4/6 个有
- `ImageResize+` —— 4/6 个有
- `ImageScaleBy` —— 4/6 个有
- `PlaySound|pysssss` —— 4/6 个有
- `SetNode` —— 4/6 个有
- `TTP_Image_Assy` —— 4/6 个有
- `TTP_Image_Tile_Batch` —— 4/6 个有
- `TTP_Tile_image_size` —— 4/6 个有
- `UNETLoader` —— 4/6 个有
- `VAELoader` —— 4/6 个有
- `easy cleanGpuUsed` —— 4/6 个有
- `easy showAnything` —— 4/6 个有
- `Fast Groups Bypasser (rgthree)` —— 3/6 个有
- `CR Prompt Text` —— 2/6 个有
- `CheckpointLoaderSimple` —— 2/6 个有
- `EmptyLatentImage` —— 2/6 个有
- `ImageScaleToTotalPixels` —— 2/6 个有
- `Image Rembg (Remove Background)` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler_ancestral | - | 6 | 67% |
| 调度器 | simple | - | 6 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1500 | - | 2 | 72% |
| 高度 | 1500 | - | 2 | 72% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，6 个样本，一致性 67%
- 调度器 最常用 simple，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 1500，样本不足，未给区间，2 个样本
- 高度 中位数 1500，样本不足，未给区间，2 个样本
- 高发问题（10/6 个样本）：Steps较低可能导致细节不足

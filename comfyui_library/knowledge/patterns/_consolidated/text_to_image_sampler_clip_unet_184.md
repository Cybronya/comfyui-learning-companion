---
name: text_to_image_sampler_clip_unet_184
type: Text To Image
frequency: 3
level: strong
coverage: 0.896333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Get Image Size, ImageCASharpening+, ImageResize+, ImpactMinMax, KSampler, SaveImage, SeedVR2, TTP_Image_Assy, TTP_Image_Tile_Batch, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/WH-AI-Studio-Z-Image完美高清文生图（SeedVR2高清放大）_2021584958199959554.json, 图片生成/文生图/Z-IMAGE 文生图_1994795379038281729.json, 图片生成/文生图/Z-image文生图+base洗图+超高清放大_1996010927327756290.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_184

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/WH-AI-Studio-Z-Image完美高清文生图（SeedVR2高清放大）_2021584958199959554.json、图片生成/文生图/Z-IMAGE 文生图_1994795379038281729.json、图片生成/文生图/Z-image文生图+base洗图+超高清放大_1996010927327756290.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Get Image Size`
- `ImageCASharpening+`
- `ImageResize+`
- `ImpactMinMax`
- `KSampler`
- `SaveImage`
- `SeedVR2`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 2/3 个有
- `ConditioningZeroOut` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LayerUtility: JoyCaption2ExtraOptions` —— 1/3 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/3 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `LoraLoader` —— 1/3 个有
- `PrimitiveBoolean` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `SeedVR2BlockSwap` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `ZML_SwitchOutput` —— 1/3 个有
- `easy imageBatchToImageList` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 9 - 10 | 3 | 95% |
| Prompt 约束强度(CFG) | 1 | 0.8 - 1 | 3 | 90% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1080 | 1080 - 1680 | 3 | 78% |
| 高度 | 1920 | 904 - 1920 | 3 | 70% |
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 9 - 10，3 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 0.8 - 1，3 个样本，取值集中（一致性 90%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 1080 - 1680，3 个样本
- 高度 中位数 1920，观测区间 904 - 1920，3 个样本
- 风险：Prompt 约束强度(CFG) 观测到 0.8，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足

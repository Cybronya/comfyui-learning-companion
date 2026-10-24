---
name: text_to_image_sampler_clip_unet_130
type: Text To Image
frequency: 5
level: moderate
coverage: 0.691
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, EmptyLatentImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImpactInt, ImpactMinMax, ImpactSwitch, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, RHHiddenNodes, SaveImage, UNETLoader, VAEDecode, VAELoader, easy imageSize, easy int, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2极致美学-turbo+8步极速出文生图！反推洗图2K直出-MJ平替+可选4K高清放大--_2070022513152843777.json, 图片生成/文生图/Krea2极速出文生图！反推洗图，4K高清放大_2070104206756892674.json, 图片生成/文生图/Qwen Image 2512文生图！图生图反推！+可选4K高清放大_1900359010674159618.json, 图片生成/文生图/Z-Image-Base文生图！图生图反推！一键生成逼真写实照片！加可选4K高清放大_1921436231337705474.json, 图片生成/文生图/z-image文生图！洗图！真实感有点吊打超强逼真！目前开源生图模型里ai味最少的一个模型，没有之一_1993881798801293314.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_130

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Krea2极致美学-turbo+8步极速出文生图！反推洗图2K直出-MJ平替+可选4K高清放大--_2070022513152843777.json、图片生成/文生图/Krea2极速出文生图！反推洗图，4K高清放大_2070104206756892674.json、图片生成/文生图/Qwen Image 2512文生图！图生图反推！+可选4K高清放大_1900359010674159618.json、图片生成/文生图/Z-Image-Base文生图！图生图反推！一键生成逼真写实照片！加可选4K高清放大_1921436231337705474.json、图片生成/文生图/z-image文生图！洗图！真实感有点吊打超强逼真！目前开源生图模型里ai味最少的一个模型，没有之一_1993881798801293314.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImpactInt`
- `ImpactMinMax`
- `ImpactSwitch`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `RHHiddenNodes`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 4/5 个有
- `SeedVR2LoadDiTModel` —— 4/5 个有
- `SeedVR2LoadVAEModel` —— 4/5 个有
- `SeedVR2VideoUpscaler` —— 4/5 个有
- `ImageListToImageBatch` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `ModelSamplingSD3` —— 3/5 个有
- `PathchSageAttentionKJ` —— 3/5 个有
- `SeedVR2BlockSwap` —— 3/5 个有
- `SeedVR2ExtraArgs` —— 3/5 个有
- `SeedVR2GGUF` —— 3/5 个有
- `TTP_Image_Assy` —— 3/5 个有
- `TTP_Image_Tile_Batch` —— 3/5 个有
- `TTP_Tile_image_size` —— 3/5 个有
- `VAEDecodeTiled` —— 3/5 个有
- `VAEEncode` —— 3/5 个有
- `easy imageBatchToImageList` —— 3/5 个有
- `ConditioningZeroOut` —— 2/5 个有
- `GetNode` —— 2/5 个有
- `ImageCASharpening+` —— 2/5 个有
- `MathExpression|pysssss` —— 2/5 个有
- `SetNode` —— 2/5 个有
- `TTResolutionSelector` —— 2/5 个有
- `easy cleanGpuUsed` —— 2/5 个有
- `ModelSamplingAuraFlow` —— 1/5 个有
- `SeedVR2` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1080 - 1080 | 5 | 100% |
| 高度 | 1920 | 1920 - 1920 | 5 | 100% |
| 采样步数 | 8 | 4 - 25 | 5 | 31% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 5 | 54% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | beta | - | 5 | 40% |
| 重绘幅度 | 1 | 0.15 - 1 | 5 | 59% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 1080 - 1080，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 4 - 25，5 个样本，取值分散，一致性仅 31%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 beta，5 个样本，一致性 40%
- 重绘幅度 中位数 1，观测区间 0.15 - 1，5 个样本
- 高发问题（6/5 个样本）：Steps较低可能导致细节不足

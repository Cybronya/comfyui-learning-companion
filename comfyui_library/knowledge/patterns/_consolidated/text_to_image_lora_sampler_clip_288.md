---
name: text_to_image_lora_sampler_clip_288
type: Text To Image
frequency: 3
level: moderate
coverage: 0.757667
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, EmptyLatentImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImageListToImageBatch, ImpactInt, ImpactMinMax, ImpactSwitch, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, RHHiddenNodes, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageSize, easy int, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, ImageCASharpening+, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, easy cleanGpuUsed, easy imageBatchToImageList, easy int, easy imageSize]
members: [图片生成/文生图/1921436231337705474.json, 图片生成/文生图/Qwen Image 2512文生图！图生图反推！+可选4K高清放大_1900359010674159618.json, 图片生成/文生图/z-image文生图！洗图！真实感有点吊打超强逼真！目前开源生图模型里ai味最少的一个模型，没有之一_1993881798801293314.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_288

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1921436231337705474.json、图片生成/文生图/Qwen Image 2512文生图！图生图反推！+可选4K高清放大_1900359010674159618.json、图片生成/文生图/z-image文生图！洗图！真实感有点吊打超强逼真！目前开源生图模型里ai味最少的一个模型，没有之一_1993881798801293314.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImageListToImageBatch`
- `ImpactInt`
- `ImpactMinMax`
- `ImpactSwitch`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `RHHiddenNodes`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageSize`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `ImageCASharpening+` —— 2/3 个有
- `SeedVR2BlockSwap` —— 2/3 个有
- `SeedVR2ExtraArgs` —— 2/3 个有
- `SeedVR2GGUF` —— 2/3 个有
- `SeedVR2LoadDiTModel` —— 2/3 个有
- `SeedVR2LoadVAEModel` —— 2/3 个有
- `SeedVR2VideoUpscaler` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `SeedVR2` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 25 | 3 | 26% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 3 | 53% |
| 采样算法 | res_multistep | - | 3 | 33% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 0.15 - 1 | 3 | 44% |
| 宽度 | 1080 | 1080 - 1080 | 3 | 100% |
| 高度 | 1920 | 1920 - 1920 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 25，3 个样本，取值分散，一致性仅 26%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，3 个样本
- 采样算法 最常用 res_multistep，3 个样本，一致性 33%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.15 - 1，3 个样本，取值分散，一致性仅 44%
- 宽度 中位数 1080，观测区间 1080 - 1080，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，3 个样本，取值集中（一致性 100%）
- 高发问题（4/3 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、ImageCASharpening+、LayerUtility: ImageScaleByAspectRatio V2、LayerUtility: PurgeVRAM V2、easy cleanGpuUsed

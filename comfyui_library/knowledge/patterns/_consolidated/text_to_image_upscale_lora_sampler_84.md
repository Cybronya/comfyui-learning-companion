---
name: text_to_image_upscale_lora_sampler_84
type: Text To Image
frequency: 3
level: moderate
coverage: 0.796
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, GetNode, Image Comparer (rgthree), ImageListToImageBatch, ImageScaleToTotalPixels, ImageUpscaleWithModel, Joy_caption_two, Joy_caption_two_load, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, RH_LLMAPI_Pro_Node, SaveImage, SetNode, ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageBatchToImageList]
problems: []
missing: []
members: [图片生成/图生图/Z-image-文生图（提示词扩写）+图生图（提示词反推）+SeedVR2放大+SRPO-TTP放大_1996115460401872897.json, 图片生成/文生图/Z-image-文生图（提示词扩写）+图生图（提示词反推）+SeedVR2放大+SRPO-TTP放大_1993833404275818498.json, 图片生成/文生图/Z-image文生图_洗图（三种提示词反推）自动化+SRPO--TTP放大_1994257461567750146.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_84

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Z-image-文生图（提示词扩写）+图生图（提示词反推）+SeedVR2放大+SRPO-TTP放大_1996115460401872897.json、图片生成/文生图/Z-image-文生图（提示词扩写）+图生图（提示词反推）+SeedVR2放大+SRPO-TTP放大_1993833404275818498.json、图片生成/文生图/Z-image文生图_洗图（三种提示词反推）自动化+SRPO--TTP放大_1994257461567750146.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageListToImageBatch`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RH_LLMAPI_Pro_Node`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `SeedVR2GGUF` —— 2/3 个有
- `AILab_QwenVL` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `ImpactConditionalBranch` —— 1/3 个有
- `MaraScottIsEmptyOrNone_v1` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `SeedVR2LoadDiTModel` —— 1/3 个有
- `SeedVR2LoadVAEModel` —— 1/3 个有
- `SeedVR2VideoUpscaler` —— 1/3 个有
- `Text Concatenate` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1280 | 1280 - 1280 | 3 | 100% |
| 高度 | 1920 | 1920 - 1920 | 3 | 100% |
| 采样步数 | 10 | 10 - 10 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 0.16 | 0.16 - 1 | 3 | 10% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1280，观测区间 1280 - 1280，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，观测区间 10 - 10，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 0.16，观测区间 0.16 - 1，3 个样本，取值分散，一致性仅 10%

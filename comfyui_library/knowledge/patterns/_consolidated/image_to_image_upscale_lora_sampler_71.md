---
name: image_to_image_upscale_lora_sampler_71
type: Image To Image
frequency: 3
level: moderate
coverage: 0.732333
common_nodes: [BRIA_RMBG_ModelLoader_Zho, BRIA_RMBG_Zho, CLIPTextEncode, CR Text Input Switch (4 way), CheckpointLoaderSimple, Display Any (rgthree), Display Int (rgthree), GetImageSizeAndCount, GetNode, GrowMask, HivisionNode, ImageResize+, ImageResizeKJ, ImageUpscaleWithModel, ImpactInt, InvertMask, KSampler, LayerColor: ColorAdapter, LayerUtility: ColorImage, LayerUtility: ColorPicker, LayerUtility: ImageBlendAdvance V2, LoadImage, MaskBlur+, PreviewImage, SUPIR_conditioner, SUPIR_decode, SUPIR_encode, SUPIR_first_stage, SUPIR_model_loader_v2, SUPIR_sample, SaveImage, Seed (rgthree), SetNode, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, ZHHivisionParamsNode]
problems: []
missing: []
members: [图片生成/图生图/一张正面照片生成各种尺寸各种背景高清证件照_1964555264521289730.json, 平台全量/【无痕换底】【快速出图】证件照_1890358368555683841.json, 平台全量/一张照片生成多规格高清证件照(背景颜色随意修改)_1834120666105933826.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_71

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/一张正面照片生成各种尺寸各种背景高清证件照_1964555264521289730.json、平台全量/【无痕换底】【快速出图】证件照_1890358368555683841.json、平台全量/一张照片生成多规格高清证件照(背景颜色随意修改)_1834120666105933826.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 3 个 workflow 都包含：
- `BRIA_RMBG_ModelLoader_Zho`
- `BRIA_RMBG_Zho`
- `CLIPTextEncode`
- `CR Text Input Switch (4 way)`
- `CheckpointLoaderSimple`
- `Display Any (rgthree)`
- `Display Int (rgthree)`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMask`
- `HivisionNode`
- `ImageResize+`
- `ImageResizeKJ`
- `ImageUpscaleWithModel`
- `ImpactInt`
- `InvertMask`
- `KSampler`
- `LayerColor: ColorAdapter`
- `LayerUtility: ColorImage`
- `LayerUtility: ColorPicker`
- `LayerUtility: ImageBlendAdvance V2`
- `LoadImage`
- `MaskBlur+`
- `PreviewImage`
- `SUPIR_conditioner`
- `SUPIR_decode`
- `SUPIR_encode`
- `SUPIR_first_stage`
- `SUPIR_model_loader_v2`
- `SUPIR_sample`
- `SaveImage`
- `Seed (rgthree)`
- `SetNode`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `ZHHivisionParamsNode`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 1/3 个有
- `ChinesePrompt_Mix` —— 1/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `DualCLIPLoader` —— 1/3 个有
- `FluxGuidance` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImageListToImageBatch` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LayerUtility: TextJoin` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `ModelSamplingSD3` —— 1/3 个有
- `ReferenceLatent` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `TTP_Image_Assy` —— 1/3 个有
- `TTP_Image_Tile_Batch` —— 1/3 个有
- `TTP_Tile_image_size` —— 1/3 个有
- `UNETLoader` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `easy imageBatchToImageList` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 3 | 80% |
| Prompt 约束强度(CFG) | 6.97 | 1 - 6.97 | 3 | 43% |
| 采样算法 | dpmpp_2m | - | 3 | 67% |
| 调度器 | karras | - | 3 | 67% |
| 重绘幅度 | 0.55 | 0.55 - 1 | 3 | 70% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，3 个样本
- Prompt 约束强度(CFG) 中位数 6.97，观测区间 1 - 6.97，3 个样本，取值分散，一致性仅 43%
- 采样算法 最常用 dpmpp_2m，3 个样本，一致性 67%
- 调度器 最常用 karras，3 个样本，一致性 67%
- 重绘幅度 中位数 0.55，观测区间 0.55 - 1，3 个样本

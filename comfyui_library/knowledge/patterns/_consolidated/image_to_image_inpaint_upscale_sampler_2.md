---
name: image_to_image_inpaint_upscale_sampler_2
type: Image To Image
frequency: 3
level: strong
coverage: 0.838
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionLoader, CR Upscale Image, DualCLIPLoader, Florence2ModelLoader, Florence2Run, FluxGuidance, GetImageSize+, Image Filter Adjustments, ImageConcanate, ImageCrop+, ImageListToImageBatch, ImageScaleToTotalPixels, ImageToMask, ImpactImageBatchToImageList, InpaintCrop, InpaintModelConditioning, InpaintStitch, InspyrenetRembg, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LyingSigmaSampler, MaskToImage, RandomNoise, ReduxAdvanced, SamplerCustomAdvanced, SaveImage, StringFunction|pysssss, StyleModelLoader, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy cleanGpuUsed, easy clearCacheAll]
problems: []
missing: []
members: [图片生成/图生图/FILL Redux一键换装_1932444199151398913.json, 平台全量/F1专业换装+TTP放大_1910941039279177730.json, 平台全量/一键换装模型，2分钟时间，可以选择服装_1905568782834929665.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_upscale_sampler_2

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/FILL Redux一键换装_1932444199151398913.json、平台全量/F1专业换装+TTP放大_1910941039279177730.json、平台全量/一键换装模型，2分钟时间，可以选择服装_1905568782834929665.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CR Upscale Image`
- `DualCLIPLoader`
- `Florence2ModelLoader`
- `Florence2Run`
- `FluxGuidance`
- `GetImageSize+`
- `Image Filter Adjustments`
- `ImageConcanate`
- `ImageCrop+`
- `ImageListToImageBatch`
- `ImageScaleToTotalPixels`
- `ImageToMask`
- `ImpactImageBatchToImageList`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `InspyrenetRembg`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LyingSigmaSampler`
- `MaskToImage`
- `RandomNoise`
- `ReduxAdvanced`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StringFunction|pysssss`
- `StyleModelLoader`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy clearCacheAll`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 2/3 个有
- `CLIPVisionEncode` —— 2/3 个有
- `DifferentialDiffusion` —— 2/3 个有
- `ImpactInt` —— 2/3 个有
- `SetLatentNoiseMask` —— 2/3 个有
- `StyleModelApply` —— 2/3 个有
- `easy imageSwitch` —— 2/3 个有
- `CheckpointLoaderSimple` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）

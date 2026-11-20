---
name: image_to_image_upscale_lora_sampler_43
type: Image To Image
frequency: 5
level: moderate
coverage: 0.9052
common_nodes: [CLIPTextEncode, ConditioningZeroOut, ConstrainImage|pysssss, Get Image Size, Image Comparer (rgthree), ImageResize+, ImageScaleBy, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/移除主体、水印 并 修复放大_1943295900598870017.json, 平台全量/移除水印+图片高清放大 TTP分块 高清无损放大_2063901354850078721.json, 平台全量/移除水印+图片高清放大_TTP分块_高清无损放大_2096168366250745858.json, 平台全量/移除水印+图片高清放大_TTP分块_高清无损放大_2096401521415114754.json, 平台全量/融图 _ 千问-edit-2511_1890275420535762945.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_43

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/移除主体、水印 并 修复放大_1943295900598870017.json、平台全量/移除水印+图片高清放大 TTP分块 高清无损放大_2063901354850078721.json、平台全量/移除水印+图片高清放大_TTP分块_高清无损放大_2096168366250745858.json、平台全量/移除水印+图片高清放大_TTP分块_高清无损放大_2096401521415114754.json、平台全量/融图 _ 千问-edit-2511_1890275420535762945.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ConstrainImage|pysssss`
- `Get Image Size`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 4/5 个有
- `FluxGuidance` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `CFGNorm` —— 2/5 个有
- `CLIPLoader` —— 2/5 个有
- `ImageResizeKJv2` —— 2/5 个有
- `KSamplerAdvanced` —— 2/5 个有
- `ModelSamplingAuraFlow` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `TextEncodeQwenImageEditPlus` —— 2/5 个有
- `easy imageColorMatch` —— 2/5 个有
- `FluxKontextImageScale` —— 1/5 个有
- `GetImageSize` —— 1/5 个有
- `GrowMaskWithBlur` —— 1/5 个有
- `Image Overlay` —— 1/5 个有
- `ImageScale` —— 1/5 个有
- `LayerMask: MaskPreview` —— 1/5 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 5 | 25% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，5 个样本，取值分散，一致性仅 25%
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）

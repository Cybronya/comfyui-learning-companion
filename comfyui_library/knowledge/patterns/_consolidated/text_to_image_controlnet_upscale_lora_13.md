---
name: text_to_image_controlnet_upscale_lora_13
type: Text To Image
frequency: 2
level: weak
coverage: 0.843
common_nodes: [CLIPLoader, CLIPTextEncode, CannyEdgePreprocessor, ColorMatch, ConditioningZeroOut, EmptyLatentImage, GetImageSize, Image Comparer (rgthree), ImageListToImageBatch, ImageResizeKJv2, ImageScaleDownToSize, ImageSharpen, ImageUpscaleWithModel, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, PreviewImage, Qwen2.5VL, QwenImageDiffsynthControlnet, Saturation, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, VRAM_Debug, easy imageBatchToImageList, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-Image去伪存真工作流｜高清洗图摄影细节放大_2098211853074784257.json, 图片生成/图生图/高清洗图去伪存真｜Z-Image人像写真高清放大_2090927321711730689.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_upscale_lora_13

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Z-Image去伪存真工作流｜高清洗图摄影细节放大_2098211853074784257.json、图片生成/图生图/高清洗图去伪存真｜Z-Image人像写真高清放大_2090927321711730689.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CannyEdgePreprocessor`
- `ColorMatch`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageListToImageBatch`
- `ImageResizeKJv2`
- `ImageScaleDownToSize`
- `ImageSharpen`
- `ImageUpscaleWithModel`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `PreviewImage`
- `Qwen2.5VL`
- `QwenImageDiffsynthControlnet`
- `Saturation`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowText|pysssss`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VRAM_Debug`
- `easy imageBatchToImageList`
- `solarL_SaveImagesToZip`
- `孤海注释`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 80 | - | 2 | 100% |
| 高度 | 80 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: image_to_image_controlnet_upscale_lora_11
type: Image To Image
frequency: 2
level: weak
coverage: 0.866
common_nodes: [AIO_Preprocessor, Any Switch (rgthree), CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, ClipLoaderGGUF, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, GetNode, INTConstant, Image Comparer (rgthree), ImageResize+, ImageScaleBy, ImageScaleToTotalPixels, KSampler, KSamplerAdvanced, KSamplerSelect, LCSColorAnchor, LCSLoadData, LCSSharpnessCalibrate, LCSSharpnessIntervene, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MemoryCleaner, ModelPatchLoader, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader, ZImageFunControlnet, easy imageSize, easy setNode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image+Klein三采极致洗图_2067910429233471490.json, 图片生成/图生图/z-image+flux2-klein三采洗图极致超清！_2067268056879034369.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_upscale_lora_11

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Z-image+Klein三采极致洗图_2067910429233471490.json、图片生成/图生图/z-image+flux2-klein三采洗图极致超清！_2067268056879034369.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `Any Switch (rgthree)`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ClipLoaderGGUF`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `GetNode`
- `INTConstant`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `KSampler`
- `KSamplerAdvanced`
- `KSamplerSelect`
- `LCSColorAnchor`
- `LCSLoadData`
- `LCSSharpnessCalibrate`
- `LCSSharpnessIntervene`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MemoryCleaner`
- `ModelPatchLoader`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `ZImageFunControlnet`
- `easy imageSize`
- `easy setNode`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `ImageReceiver` —— 1/2 个有
- `ImageSender` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `孤海注释` —— 1/2 个有
- `忽略多组孤海` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 22% |
| 采样算法 | 1 | - | 1 | 100% |
| 调度器 | euler | - | 2 | 50% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 22%
- 调度器 最常用 euler，2 个样本，一致性 50%
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

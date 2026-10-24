---
name: text_to_image_upscale_lora_sampler_109
type: Text To Image
frequency: 2
level: weak
coverage: 0.905
common_nodes: [AIO_Preprocessor, CFGNorm, CLIPLoader, CLIPTextEncode, CR Text, CR Text Concatenate, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, Image Comparer (rgthree), Image Tiled, ImageConcanateOfUtils, ImageFromBatch, ImageListToBatch+, ImageScaleBy, ImageUpscaleWithModel, Images to RGB, Int, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: JoyCaptionBeta1, LayerUtility: LoadJoyCaptionBeta1Model, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, PrimitiveInt, ReferenceLatent, SaveImage, SeedVR2, SeedVR2BlockSwap, ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TeaCache, TextEncodeQwenImageEditPlus, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageBatchToImageList]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image Edit Plus 分块高清放大 多参考图像编辑工作流 -StarAI_1970737085378404353.json, 图片生成/图生图/Qwen Image Edit Plus 多参考图像编辑工作流-test_2046780751697420289.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_109

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Qwen Image Edit Plus 分块高清放大 多参考图像编辑工作流 -StarAI_1970737085378404353.json、图片生成/图生图/Qwen Image Edit Plus 多参考图像编辑工作流-test_2046780751697420289.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `Image Tiled`
- `ImageConcanateOfUtils`
- `ImageFromBatch`
- `ImageListToBatch+`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `Images to RGB`
- `Int`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: JoyCaptionBeta1`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `PrimitiveInt`
- `ReferenceLatent`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `ShowText|pysssss`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TeaCache`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageBatchToImageList`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |
| 采样步数 | 16.5 | - | 2 | 48% |
| Prompt 约束强度(CFG) | 1.05 | - | 2 | 95% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.575 | - | 2 | 26% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 16.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 48%
- Prompt 约束强度(CFG) 中位数 1.05，样本不足，未给区间，2 个样本，取值集中（一致性 95%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.575，样本不足，未给区间，2 个样本，取值分散，一致性仅 26%
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

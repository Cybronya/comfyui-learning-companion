---
name: image_to_image_upscale_lora_sampler_104
type: Image To Image
frequency: 2
level: weak
coverage: 0.9095
common_nodes: [ACE_ImageFaceCrop, AILab_QwenVL, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, CreateShapeMask, Fast Groups Bypasser (rgthree), GetImageSize, ImageFromBatch+, ImageListToBatch+, ImageResize+, ImageScaleBy, ImageUpscaleWithModel, KSampler, LayerUtility: ColorImage, LayerUtility: ImageBlendAdvance, LayerUtility: NumberCalculator, LayerUtility: XY to Percent, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, RH_Captioner, SaveImageAndMetadata_, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy forLoopEnd, easy forLoopStart, easy ifElse, easy int, easy positive, easy promptConcat, easy promptLine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/套图写真+换脸_2010917166970834946.json, 图片生成/图生图/套图写真-双z采样版_2019622743326593026.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_104

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/套图写真+换脸_2010917166970834946.json、图片生成/图生图/套图写真-双z采样版_2019622743326593026.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `ACE_ImageFaceCrop`
- `AILab_QwenVL`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `CreateShapeMask`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `ImageFromBatch+`
- `ImageListToBatch+`
- `ImageResize+`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSampler`
- `LayerUtility: ColorImage`
- `LayerUtility: ImageBlendAdvance`
- `LayerUtility: NumberCalculator`
- `LayerUtility: XY to Percent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `RH_Captioner`
- `SaveImageAndMetadata_`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy ifElse`
- `easy int`
- `easy positive`
- `easy promptConcat`
- `easy promptLine`

**可变部分**（部分 workflow 才有）：
- `AnyIsEmpty` —— 1/2 个有
- `CFGNorm` —— 1/2 个有
- `DrawGaussianNoiseOnImage` —— 1/2 个有
- `FeishuBitableConfigNode` —— 1/2 个有
- `FeishuBitableFieldNode` —— 1/2 个有
- `FeishuBitablePushNode` —— 1/2 个有
- `GrowMaskWithBlur` —— 1/2 个有
- `ImageAddNoise` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `InvertMask` —— 1/2 个有
- `KSamplerAdvanced` —— 1/2 个有
- `Latent Noise Injection` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `ProcessString` —— 1/2 个有
- `QwenEditConfigPreparer` —— 1/2 个有
- `RegexReplace` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `ShowText` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `TextEncodeQwenImageEditPlus` —— 1/2 个有
- `TextEncodeQwenImageEditPlusCustom_lrzjason` —— 1/2 个有
- `easy boolean` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy imageRemBg` —— 1/2 个有
- `easy seed` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 5.5 | - | 2 | 18% |
| 采样算法 | 1 | - | 1 | 100% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 0.9 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- Prompt 约束强度(CFG) 中位数 5.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 18%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 高发问题（6/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

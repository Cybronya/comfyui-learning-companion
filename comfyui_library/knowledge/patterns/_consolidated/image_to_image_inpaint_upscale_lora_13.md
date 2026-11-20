---
name: image_to_image_inpaint_upscale_lora_13
type: Image To Image
frequency: 2
level: weak
coverage: 0.6895
common_nodes: [AddMask, Anything Everywhere3, BasicGuider, BasicScheduler, CLIPTextEncode, CLIPTextEncodeFlux, CR Text Concatenate, ConditioningCombine, ConditioningZeroOut, DeepTranslatorTextNode, DifferentialDiffusion, DisableNoise, DualCLIPLoader, Fast Groups Bypasser (rgthree), FluxGuidance, GetNode, GrowMaskWithBlur, Image Comparer (rgthree), ImageAndMaskPreview, ImageListToImageBatch, ImageResizeKJ, ImageScaleToTotalPixels, ImageUpscaleWithModel, InjectLatentNoise+, InpaintCrop, InpaintModelConditioning, InpaintResize, InpaintStitch, KSampler, KSamplerSelect, LayerMask: SegmentAnythingUltra V2, LayerUtility: ImageRemoveAlpha, LoadImage, LoraLoaderModelOnly, MaskPreview+, PreviewBridge, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, SetNode, SplitSigmasDenoise, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, Text Concatenate, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageBatchToImageList, easy positive]
problems: []
missing: []
members: [平台全量/CK-虚拟摄影FLUX版_1924360528250982402.json, 平台全量/一键原片换脸工作流V2.0_1917151238893273089.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_upscale_lora_13

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/CK-虚拟摄影FLUX版_1924360528250982402.json、平台全量/一键原片换脸工作流V2.0_1917151238893273089.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：69%

## 共有节点

全部 2 个 workflow 都包含：
- `AddMask`
- `Anything Everywhere3`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPTextEncodeFlux`
- `CR Text Concatenate`
- `ConditioningCombine`
- `ConditioningZeroOut`
- `DeepTranslatorTextNode`
- `DifferentialDiffusion`
- `DisableNoise`
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `GetNode`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageAndMaskPreview`
- `ImageListToImageBatch`
- `ImageResizeKJ`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `InjectLatentNoise+`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintResize`
- `InpaintStitch`
- `KSampler`
- `KSamplerSelect`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: ImageRemoveAlpha`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `PreviewBridge`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `SplitSigmasDenoise`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `Text Concatenate`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageBatchToImageList`
- `easy positive`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `Any Switch (rgthree)` —— 1/2 个有
- `Anything Everywhere` —— 1/2 个有
- `ApplyPulidFlux` —— 1/2 个有
- `BNK_CLIPTextEncodeAdvanced` —— 1/2 个有
- `CLIPVisionLoader` —— 1/2 个有
- `CheckpointLoaderSimple` —— 1/2 个有
- `ControlNetApplyAdvanced` —— 1/2 个有
- `ControlNetLoader` —— 1/2 个有
- `EmptySD3LatentImage` —— 1/2 个有
- `InpaintPreprocessor` —— 1/2 个有
- `Joy_caption_two` —— 1/2 个有
- `Joy_caption_two_load` —— 1/2 个有
- `LatentInterpolate` —— 1/2 个有
- `LayerMask: PersonMaskUltra V2` —— 1/2 个有
- `LayerUtility: ImageBlendAdvance` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/2 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `PulidFluxEvaClipLoader` —— 1/2 个有
- `PulidFluxInsightFaceLoader` —— 1/2 个有
- `PulidFluxModelLoader` —— 1/2 个有
- `ReduxAdvanced` —— 1/2 个有
- `SDXLPromptStyler` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `StyleModelLoader` —— 1/2 个有
- `WD14Tagger|pysssss` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4 | - | 2 | 25% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| ControlNet 权重 | 0.55 | - | 1 | 100% |
| LoRA 模型强度 | 0.7 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，样本不足，未给区间，2 个样本，取值分散，一致性仅 25%
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

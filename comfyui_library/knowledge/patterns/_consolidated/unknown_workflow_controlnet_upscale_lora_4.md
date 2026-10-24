---
name: unknown_workflow_controlnet_upscale_lora_4
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.588
common_nodes: [ArgosTranslateTextNode, BasicGuider, BasicScheduler, BboxDetectorSEGS, CLIPTextEncode, CR Text Concatenate, CR Text Replace, CR Upscale Image, ConditioningZeroOut, ControlNetLoader, CoreMLDetailerHookProvider, DepthAnythingPreprocessor, DetailerForEach, DisableNoise, DualCLIPLoader, EmptySD3LatentImage, FS: Crop Image Into Even Pieces, Fast Groups Muter (rgthree), Float, FluxGuidance, GetNode, ImageResizeKJ, ImageScaleToTotalPixels, ImageUpscaleWithModel, ImpactSegsAndMask, ImpactSwitch, Int, KSamplerSelect, LayerFilter: FilmV2, LoadImage, LoraLoaderModelOnly, MaskPreview+, ModelSamplingFlux, PlaySound|pysssss, PreviewImage, RH_Captioner, RandomNoise, SAMDetectorCombined, SAMLoader, SamplerCustomAdvanced, SaveImage, SetNode, ShowText|pysssss, SplitSigmasDenoise, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TeaCache, UNETLoader, UltralyticsDetectorProvider, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy cleanGpuUsed, easy globalSeed, easy imageBatchToImageList, easy imageSize, easy positive, easy promptConcat, easy promptReplace, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/FLUX网红美女批量制造机_1920761055910232066.json, 图片生成/图生图/人物一致性，不同pose制造（衣服背景相似，有换脸和放大修复）_1904583752117616642.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_lora_4

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/FLUX网红美女批量制造机_1920761055910232066.json、图片生成/图生图/人物一致性，不同pose制造（衣服背景相似，有换脸和放大修复）_1904583752117616642.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：59%

## 共有节点

全部 2 个 workflow 都包含：
- `ArgosTranslateTextNode`
- `BasicGuider`
- `BasicScheduler`
- `BboxDetectorSEGS`
- `CLIPTextEncode`
- `CR Text Concatenate`
- `CR Text Replace`
- `CR Upscale Image`
- `ConditioningZeroOut`
- `ControlNetLoader`
- `CoreMLDetailerHookProvider`
- `DepthAnythingPreprocessor`
- `DetailerForEach`
- `DisableNoise`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FS: Crop Image Into Even Pieces`
- `Fast Groups Muter (rgthree)`
- `Float`
- `FluxGuidance`
- `GetNode`
- `ImageResizeKJ`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `ImpactSegsAndMask`
- `ImpactSwitch`
- `Int`
- `KSamplerSelect`
- `LayerFilter: FilmV2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `ModelSamplingFlux`
- `PlaySound|pysssss`
- `PreviewImage`
- `RH_Captioner`
- `RandomNoise`
- `SAMDetectorCombined`
- `SAMLoader`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `SplitSigmasDenoise`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TeaCache`
- `UNETLoader`
- `UltralyticsDetectorProvider`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy globalSeed`
- `easy imageBatchToImageList`
- `easy imageSize`
- `easy positive`
- `easy promptConcat`
- `easy promptReplace`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ApplyIPAdapterFlux` —— 1/2 个有
- `CLIPVisionEncode` —— 1/2 个有
- `CLIPVisionLoader` —— 1/2 个有
- `ControlNetApplySD3` —— 1/2 个有
- `DWPreprocessor` —— 1/2 个有
- `IPAdapterFluxLoader` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `OpenposePreprocessor` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `ReActorBuildFaceModel` —— 1/2 个有
- `ReActorFaceBoost` —— 1/2 个有
- `ReActorFaceSwap` —— 1/2 个有
- `StyleModelApply` —— 1/2 个有
- `StyleModelLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.7 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

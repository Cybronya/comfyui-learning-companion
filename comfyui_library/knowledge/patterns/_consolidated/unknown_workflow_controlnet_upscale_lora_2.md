---
name: unknown_workflow_controlnet_upscale_lora_2
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.5808
common_nodes: [BasicGuider, BasicScheduler, BboxDetectorSEGS, CLIPTextEncode, CR Text Replace, CR Upscale Image, ConditioningZeroOut, ControlNetLoader, CoreMLDetailerHookProvider, DepthAnythingPreprocessor, DetailerForEach, DisableNoise, DualCLIPLoader, EmptySD3LatentImage, FS: Crop Image Into Even Pieces, Fast Groups Muter (rgthree), FluxGuidance, GetNode, ImageResizeKJ, ImageScaleToTotalPixels, ImageUpscaleWithModel, ImpactSegsAndMask, ImpactSwitch, Int, KSamplerSelect, LayerFilter: FilmV2, LoadImage, LoraLoaderModelOnly, MaskPreview+, ModelSamplingFlux, PlaySound|pysssss, PreviewImage, RH_Captioner, RandomNoise, SAMDetectorCombined, SAMLoader, SamplerCustomAdvanced, SaveImage, SetNode, ShowText|pysssss, SplitSigmasDenoise, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UltralyticsDetectorProvider, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageBatchToImageList, easy imageSize, easy positive, easy promptConcat]
problems: []
missing: []
members: [图片生成/图生图/FLUX网红美女批量制造机_1920761055910232066.json, 图片生成/图生图/人物一致性，不同pose制造（衣服背景相似，有换脸和放大修复）_1904583752117616642.json, 平台全量/FLUX网红九连拍_1852683538775613442.json, 平台全量/FLUX网红美女批量制造机（可添加提示词）加速TPP放大，面部修复，直接拿成品，抖音，小红书涨粉神器_1901839026838773762.json, 平台全量/图生图，角色一致性，三视图_1915763094046576642.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_lora_2

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/FLUX网红美女批量制造机_1920761055910232066.json、图片生成/图生图/人物一致性，不同pose制造（衣服背景相似，有换脸和放大修复）_1904583752117616642.json、平台全量/FLUX网红九连拍_1852683538775613442.json、平台全量/FLUX网红美女批量制造机（可添加提示词）加速TPP放大，面部修复，直接拿成品，抖音，小红书涨粉神器_1901839026838773762.json、平台全量/图生图，角色一致性，三视图_1915763094046576642.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：58%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `BboxDetectorSEGS`
- `CLIPTextEncode`
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
- `UNETLoader`
- `UltralyticsDetectorProvider`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageBatchToImageList`
- `easy imageSize`
- `easy positive`
- `easy promptConcat`

**可变部分**（部分 workflow 才有）：
- `ArgosTranslateTextNode` —— 4/5 个有
- `CR Text Concatenate` —— 4/5 个有
- `ControlNetApplySD3` —— 4/5 个有
- `Float` —— 4/5 个有
- `TeaCache` —— 4/5 个有
- `easy globalSeed` —— 4/5 个有
- `easy promptReplace` —— 4/5 个有
- `easy showAnything` —— 4/5 个有
- `OpenposePreprocessor` —— 3/5 个有
- `ApplyIPAdapterFlux` —— 2/5 个有
- `CLIPVisionEncode` —— 2/5 个有
- `CLIPVisionLoader` —— 2/5 个有
- `DWPreprocessor` —— 2/5 个有
- `IPAdapterFluxLoader` —— 2/5 个有
- `LayerUtility: PurgeVRAM` —— 2/5 个有
- `ReActorBuildFaceModel` —— 2/5 个有
- `ReActorFaceBoost` —— 2/5 个有
- `ReActorFaceSwap` —— 2/5 个有
- `StyleModelApply` —— 2/5 个有
- `StyleModelLoader` —— 2/5 个有
- `RHHiddenNodes` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.7 | 0.6 - 1 | 4 | 80% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.7，观测区间 0.6 - 1，4 个样本

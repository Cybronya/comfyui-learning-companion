---
name: unknown_workflow_upscale_lora_sampler_103
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6115
common_nodes: [AIO_Preprocessor, AnyLineArtPreprocessor_aux, BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, CR Image Grid Panel, CR Simple Text Watermark, CannyEdgePreprocessor, ConditioningZeroOut, CropFace, DSINE-NormalMapPreprocessor, DWPreprocessor, DepthAnythingV2Preprocessor, EmptyFlux2LatentImage, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImageSize, GetNode, Image Comparer (rgthree), ImageConcatMulti, ImageFlip+, ImagePass, ImageScaleToTotalPixels, ImpactStringSelector, JoinStringMulti, KSamplerSelect, LCSColorAnchor, LCSLoadData, LCSSharpnessCalibrate, LCSSharpnessIntervene, LCSToneAdjust, LayerMask: LoadSegformerModel, LayerMask: SegformerFashionSetting, LayerMask: SegformerUltraV3, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: SaveImagePlus, LensBlur, LoadImage, LoaderGGUF, LoraLoaderModelOnly, ModelPassThrough, OpenposePreprocessor, PlaySound|pysssss, PreviewImage, ProcessString, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, SomethingToString, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy int, easy promptLine, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [图片生成/图生图/Flux2 Klein-TureV3+图片编辑实用工具合集 控制LoRA_2082728296479019009.json, 平台全量/⓬ Flux2 Klein-TureV3+控制LoRA 实测案例+工具合集 7.28_2080678976808378370.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_103

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flux2 Klein-TureV3+图片编辑实用工具合集 控制LoRA_2082728296479019009.json、平台全量/⓬ Flux2 Klein-TureV3+控制LoRA 实测案例+工具合集 7.28_2080678976808378370.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：61%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `AnyLineArtPreprocessor_aux`
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Image Grid Panel`
- `CR Simple Text Watermark`
- `CannyEdgePreprocessor`
- `ConditioningZeroOut`
- `CropFace`
- `DSINE-NormalMapPreprocessor`
- `DWPreprocessor`
- `DepthAnythingV2Preprocessor`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageConcatMulti`
- `ImageFlip+`
- `ImagePass`
- `ImageScaleToTotalPixels`
- `ImpactStringSelector`
- `JoinStringMulti`
- `KSamplerSelect`
- `LCSColorAnchor`
- `LCSLoadData`
- `LCSSharpnessCalibrate`
- `LCSSharpnessIntervene`
- `LCSToneAdjust`
- `LayerMask: LoadSegformerModel`
- `LayerMask: SegformerFashionSetting`
- `LayerMask: SegformerUltraV3`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: SaveImagePlus`
- `LensBlur`
- `LoadImage`
- `LoaderGGUF`
- `LoraLoaderModelOnly`
- `ModelPassThrough`
- `OpenposePreprocessor`
- `PlaySound|pysssss`
- `PreviewImage`
- `ProcessString`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `Seed (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `SomethingToString`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy int`
- `easy promptLine`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

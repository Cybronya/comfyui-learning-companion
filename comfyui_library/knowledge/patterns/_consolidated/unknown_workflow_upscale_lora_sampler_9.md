---
name: unknown_workflow_upscale_lora_sampler_9
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.399
common_nodes: [Any Switch (rgthree), CFGGuider, CLIPLoader, CLIPTextEncode, CR Simple Text Watermark, ColorMatch, ConditioningZeroOut, DrawMaskOnImage, EmptyFlux2LatentImage, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), Flux2Scheduler, GetNode, Image Comparer (rgthree), ImageBlend, ImagePass, ImageResize+, ImageScaleBy, ImageUpscaleWithModel, KOOK_ImageCompression, KOOK_SaveJPGImage, KSamplerAdvanced, KSamplerSelect, LCSColorAnchor, LCSLoadData, LCSSharpnessCalibrate, LCSSharpnessIntervene, LayerColor: ColorAdapter, LayerMask: LoadSegformerModel, LayerMask: SegformerClothesSetting, LayerMask: SegformerUltraV3, LayerUtility: ImageBlendAdvance V3, LayerUtility: ImageScaleByAspectRatio V2, LazyCache, LensBlur, LoadImage, LoraLoaderModelOnly, ModelPassThrough, ModelSamplingAuraFlow, PhotoShakeNode, PlaySound|pysssss, PreviewImage, PrimitiveString, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SaveText|pysssss, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, SomethingToString, StringConcatenate, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextInput_, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageSize, easy int, easy saveText, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: [CR Simple Text Watermark, LayerMask: LoadSegformerModel, LayerMask: SegformerClothesSetting, LayerMask: SegformerUltraV3, LayerUtility: ImageBlendAdvance V3, LayerUtility: ImageScaleByAspectRatio V2, PlaySound|pysssss, easy cleanGpuUsed, easy int, ImageResize+, LayerColor: ColorAdapter, SaveText|pysssss, Seed (rgthree), easy imageSize, easy saveText]
members: [图片生成/图生图/2102319165112672257.json, 图片生成/文生图/❾「写真V3」Z双采  K质感+Edit TTP-HD「9.19」_2056754627374309378.json, 图片生成/文生图/「写真V3」Z双采  K质感+Edit TTP-HD_2103020992871358466.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_9

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/2102319165112672257.json、图片生成/文生图/❾「写真V3」Z双采  K质感+Edit TTP-HD「9.19」_2056754627374309378.json、图片生成/文生图/「写真V3」Z双采  K质感+Edit TTP-HD_2103020992871358466.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：40%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Simple Text Watermark`
- `ColorMatch`
- `ConditioningZeroOut`
- `DrawMaskOnImage`
- `EmptyFlux2LatentImage`
- `EmptySD3LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageBlend`
- `ImagePass`
- `ImageResize+`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KOOK_ImageCompression`
- `KOOK_SaveJPGImage`
- `KSamplerAdvanced`
- `KSamplerSelect`
- `LCSColorAnchor`
- `LCSLoadData`
- `LCSSharpnessCalibrate`
- `LCSSharpnessIntervene`
- `LayerColor: ColorAdapter`
- `LayerMask: LoadSegformerModel`
- `LayerMask: SegformerClothesSetting`
- `LayerMask: SegformerUltraV3`
- `LayerUtility: ImageBlendAdvance V3`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LazyCache`
- `LensBlur`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPassThrough`
- `ModelSamplingAuraFlow`
- `PhotoShakeNode`
- `PlaySound|pysssss`
- `PreviewImage`
- `PrimitiveString`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SaveText|pysssss`
- `Seed (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `SomethingToString`
- `StringConcatenate`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TextInput_`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageSize`
- `easy int`
- `easy saveText`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 15 | 15 - 15 | 3 | 100% |
| 采样算法 | 2 | 2 - 2 | 3 | 100% |
| 调度器 | sa_solver | - | 3 | 100% |
| 重绘幅度 | bong_tangent | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 15，观测区间 15 - 15，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 2，观测区间 2 - 2，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 sa_solver，3 个样本，一致性 100%
- 重绘幅度 最常用 bong_tangent，3 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 15，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 这些节点还没有知识卡，系统对它们的理解有限：CR Simple Text Watermark、LayerMask: LoadSegformerModel、LayerMask: SegformerClothesSetting、LayerMask: SegformerUltraV3、LayerUtility: ImageBlendAdvance V3

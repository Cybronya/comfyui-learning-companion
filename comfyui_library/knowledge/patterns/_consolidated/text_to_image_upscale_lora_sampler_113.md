---
name: text_to_image_upscale_lora_sampler_113
type: Text To Image
frequency: 2
level: weak
coverage: 0.448
common_nodes: [Any Switch (rgthree), CFGGuider, CLIPLoader, CLIPTextEncode, CR Simple Text Watermark, ColorMatch, ConditioningZeroOut, DrawMaskOnImage, EmptyFlux2LatentImage, EmptyLatentImage, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), Flux2Scheduler, GetNode, Image Comparer (rgthree), ImageUpscaleWithModel, JjkText, KOOK_ImageCompression, KOOK_SaveJPGImage, KSampler, KSamplerSelect, LCSColorAnchor, LCSLoadData, LCSSharpnessCalibrate, LCSSharpnessIntervene, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelPassThrough, PlaySound|pysssss, PreviewImage, PrimitiveString, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, SomethingToString, StringConcatenate, TextInput_, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageSize, easy int, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z+K自动反推15宫格分镜多角度扩图拼接文生图处理工具_2102188986180657154.json, 图片生成/文生图/Z双采K质感Edit TTP-HD写真V3文生图处理工作流_2101716704056397826.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_113

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Z+K自动反推15宫格分镜多角度扩图拼接文生图处理工具_2102188986180657154.json、图片生成/文生图/Z双采K质感Edit TTP-HD写真V3文生图处理工作流_2101716704056397826.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：45%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Simple Text Watermark`
- `ColorMatch`
- `ConditioningZeroOut`
- `DrawMaskOnImage`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `EmptySD3LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `JjkText`
- `KOOK_ImageCompression`
- `KOOK_SaveJPGImage`
- `KSampler`
- `KSamplerSelect`
- `LCSColorAnchor`
- `LCSLoadData`
- `LCSSharpnessCalibrate`
- `LCSSharpnessIntervene`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPassThrough`
- `PlaySound|pysssss`
- `PreviewImage`
- `PrimitiveString`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `SomethingToString`
- `StringConcatenate`
- `TextInput_`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageSize`
- `easy int`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Bookmark (rgthree)` —— 1/2 个有
- `CR Prompt Text` —— 1/2 个有
- `CR Text Concatenate` —— 1/2 个有
- `FL_ImageBatch` —— 1/2 个有
- `FromListGetStrings` —— 1/2 个有
- `ImageBlend` —— 1/2 个有
- `ImageFlip+` —— 1/2 个有
- `ImagePadForOutpaint` —— 1/2 个有
- `ImagePass` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `ImageScaleBy` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `ImageStitch` —— 1/2 个有
- `ImagesConcanateToGrid` —— 1/2 个有
- `KSamplerAdvanced` —— 1/2 个有
- `LayerColor: ColorAdapter` —— 1/2 个有
- `LayerMask: LoadSegformerModel` —— 1/2 个有
- `LayerMask: SegformerClothesSetting` —— 1/2 个有
- `LayerMask: SegformerUltraV3` —— 1/2 个有
- `LayerUtility: ImageBlendAdvance V3` —— 1/2 个有
- `LazyCache` —— 1/2 个有
- `LensBlur` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `Mute / Bypass Relay (rgthree)` —— 1/2 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/2 个有
- `PhotoShakeNode` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `ProcessString` —— 1/2 个有
- `QwenMultiangleCameraNode` —— 1/2 个有
- `SaveText|pysssss` —— 1/2 个有
- `Seed (rgthree)` —— 1/2 个有
- `TTP_Image_Assy` —— 1/2 个有
- `TTP_Image_Tile_Batch` —— 1/2 个有
- `TTP_Tile_image_size` —— 1/2 个有
- `easy promptLine` —— 1/2 个有
- `easy saveText` —— 1/2 个有

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
| Steps较低可能导致细节不足 | 3/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（3/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

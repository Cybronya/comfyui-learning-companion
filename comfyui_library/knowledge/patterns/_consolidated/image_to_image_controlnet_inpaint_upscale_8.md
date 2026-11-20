---
name: image_to_image_controlnet_inpaint_upscale_8
type: Image To Image
frequency: 2
level: weak
coverage: 0.8565
common_nodes: [ACE_TextTranslate, AdaptiveLongestEdge_EditUtils, ApplyInstantID, CFGGuider, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ColorTransfer, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, CropWithPadInfo_EditUtils, DF_Get_image_size, EditTextEncode_EditUtils, EmptySD3LatentImage, Flux2KleinConfigPreparer_EditUtils, Flux2KleinModelConfig_EditUtils, Flux2KleinOutputExtractor_EditUtils, Flux2Scheduler, GetImageSize+, Image Comparer (rgthree), ImageScale, ImageScaleToTotalPixels, ImageUpscaleWithModel, InpaintModelConditioning, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, KSamplerSelect, LayerMask: MaskGrow, LayerUtility: CropByMask V2, LayerUtility: PurgeVRAM V2, LayerUtility: RestoreCropBox, LoadImage, LoraLoaderModelOnly, PreviewAny, PreviewImage, PrimitiveInt, RandomNoise, ResolutionSelector, SAM3_Detect, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, Text, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy float, easy promptConcat, easy promptReplace, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一键写真复刻_2102415152149778434.json, 平台全量/超高人脸一致性写真制作工作流_2080955365289713666.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_upscale_8

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/一键写真复刻_2102415152149778434.json、平台全量/超高人脸一致性写真制作工作流_2080955365289713666.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `ACE_TextTranslate`
- `AdaptiveLongestEdge_EditUtils`
- `ApplyInstantID`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ColorTransfer`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `CropWithPadInfo_EditUtils`
- `DF_Get_image_size`
- `EditTextEncode_EditUtils`
- `EmptySD3LatentImage`
- `Flux2KleinConfigPreparer_EditUtils`
- `Flux2KleinModelConfig_EditUtils`
- `Flux2KleinOutputExtractor_EditUtils`
- `Flux2Scheduler`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageScale`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `InpaintModelConditioning`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler`
- `KSamplerSelect`
- `LayerMask: MaskGrow`
- `LayerUtility: CropByMask V2`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `PreviewImage`
- `PrimitiveInt`
- `RandomNoise`
- `ResolutionSelector`
- `SAM3_Detect`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `Text`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy float`
- `easy promptConcat`
- `easy promptReplace`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 1/2 个有
- `ComfySwitchNode` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `ImageBlend` —— 1/2 个有
- `ImageRGBToYUV` —— 1/2 个有
- `KOOK_SaveJPGImage` —— 1/2 个有
- `Krea2EditGroundedEncode` —— 1/2 个有
- `Krea2EditModelPatch` —— 1/2 个有
- `LayerMask: MaskPreview` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `PrimitiveBoolean` —— 1/2 个有
- `SDPoseOODLoader` —— 1/2 个有
- `SDPoseOODProcessor` —— 1/2 个有
- `TextEncodeQwenImageEditPlus` —— 1/2 个有
- `easy imageConcat` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.1 | - | 2 | 100% |
| 采样步数 | 8 | - | 2 | 50% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 50% |
| 调度器 | exponential | - | 2 | 50% |
| 重绘幅度 | 0.9 | - | 2 | 89% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 0.1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 50%
- 调度器 最常用 exponential，2 个样本，一致性 50%
- 重绘幅度 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

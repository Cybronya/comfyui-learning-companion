---
name: text_to_image_video_inpaint_upscale
type: Text To Image
frequency: 2
level: weak
coverage: 0.888
common_nodes: [AddLabel, BasicGuider, BasicScheduler, CLIPTextEncode, CLIPTextEncodeFlux, CLIPVisionEncode, CLIPVisionLoader, CR Image Grid Panel, ConditioningZeroOut, DF_Image_scale_to_side, DifferentialDiffusion, DownloadAndLoadGIMMVFIModel, DualCLIPLoader, EmptyLatentImage, ExpressionEditor, Fast Groups Bypasser (rgthree), FluxGuidance, GIMMVFI_interpolate, Image Blank, Image Comparer (rgthree), ImageConcanate, ImageCrop+, ImageListToBatch+, ImagePadForOutpaint, ImageResize+, ImageResizeKJ, ImageScale, ImageToMask, ImpactInt, InpaintModelConditioning, InspyrenetRembg, Int, JoinStrings, Joy_caption_two, Joy_caption_two_load, KSampler, KSamplerSelect, LayerUtility: ColorImage V2, LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LayerUtility: RestoreCropBox, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, LoraLoader, LoraLoaderModelOnly, LyingSigmaSampler, MaskPreview+, MaskToImage, MathExpression|pysssss, ModelSamplingFlux, PreviewImage, RandomNoise, ReroutePrimitive|pysssss, ResizeMask, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, SomethingToString, StyleModelApply, StyleModelLoader, UNETLoader, UltimateSDUpscaleCustomSample, UpscaleModelLoader, VAEDecode, VAEEncodeForInpaint, VAELoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageClipEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader, easy batchAnything, easy float, easy forLoopEnd, easy forLoopStart, easy imageSize, easy outputToList]
problems: []
missing: []
members: [视频生成/图生视频/击倒_1931524997242925057.json, 视频生成/图生视频/攻击倒下_1931527933436080129.json]
source: knowledge_consolidation
---

# text_to_image_video_inpaint_upscale

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/击倒_1931524997242925057.json、视频生成/图生视频/攻击倒下_1931527933436080129.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `AddLabel`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPTextEncodeFlux`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Image Grid Panel`
- `ConditioningZeroOut`
- `DF_Image_scale_to_side`
- `DifferentialDiffusion`
- `DownloadAndLoadGIMMVFIModel`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `ExpressionEditor`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `GIMMVFI_interpolate`
- `Image Blank`
- `Image Comparer (rgthree)`
- `ImageConcanate`
- `ImageCrop+`
- `ImageListToBatch+`
- `ImagePadForOutpaint`
- `ImageResize+`
- `ImageResizeKJ`
- `ImageScale`
- `ImageToMask`
- `ImpactInt`
- `InpaintModelConditioning`
- `InspyrenetRembg`
- `Int`
- `JoinStrings`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ColorImage V2`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `LyingSigmaSampler`
- `MaskPreview+`
- `MaskToImage`
- `MathExpression|pysssss`
- `ModelSamplingFlux`
- `PreviewImage`
- `RandomNoise`
- `ReroutePrimitive|pysssss`
- `ResizeMask`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `SomethingToString`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `UltimateSDUpscaleCustomSample`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncodeForInpaint`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageClipEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy batchAnything`
- `easy float`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageSize`
- `easy outputToList`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 768 | - | 2 | 100% |
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 0 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

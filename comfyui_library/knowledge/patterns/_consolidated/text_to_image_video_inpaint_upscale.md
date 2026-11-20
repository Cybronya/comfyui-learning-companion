---
name: text_to_image_video_inpaint_upscale
type: Text To Image
frequency: 3
level: strong
coverage: 0.888
common_nodes: [AddLabel, BasicGuider, BasicScheduler, CLIPTextEncode, CLIPTextEncodeFlux, CLIPVisionEncode, CLIPVisionLoader, CR Image Grid Panel, ConditioningZeroOut, DF_Image_scale_to_side, DifferentialDiffusion, DownloadAndLoadGIMMVFIModel, DualCLIPLoader, EmptyLatentImage, ExpressionEditor, Fast Groups Bypasser (rgthree), FluxGuidance, GIMMVFI_interpolate, Image Blank, Image Comparer (rgthree), ImageConcanate, ImageCrop+, ImageListToBatch+, ImagePadForOutpaint, ImageResize+, ImageResizeKJ, ImageScale, ImageToMask, ImpactInt, InpaintModelConditioning, InspyrenetRembg, Int, JoinStrings, Joy_caption_two, Joy_caption_two_load, KSampler, KSamplerSelect, LayerUtility: ColorImage V2, LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LayerUtility: RestoreCropBox, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, LoraLoader, LoraLoaderModelOnly, LyingSigmaSampler, MaskPreview+, MaskToImage, MathExpression|pysssss, ModelSamplingFlux, PreviewImage, RandomNoise, ReroutePrimitive|pysssss, ResizeMask, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, SomethingToString, StyleModelApply, StyleModelLoader, UNETLoader, UltimateSDUpscaleCustomSample, UpscaleModelLoader, VAEDecode, VAEEncodeForInpaint, VAELoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageClipEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader, easy batchAnything, easy float, easy forLoopEnd, easy forLoopStart, easy imageSize, easy outputToList]
problems: []
missing: []
members: [平台全量/多个工作流集合直接下载回去_1930619595797757954.json, 视频生成/图生视频/击倒_1931524997242925057.json, 视频生成/图生视频/攻击倒下_1931527933436080129.json]
source: knowledge_consolidation
---

# text_to_image_video_inpaint_upscale

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/多个工作流集合直接下载回去_1930619595797757954.json、视频生成/图生视频/击倒_1931524997242925057.json、视频生成/图生视频/攻击倒下_1931527933436080129.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
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
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 768 | 768 - 768 | 3 | 100% |
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 0 | 0 - 0 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 768，观测区间 768 - 768，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0，观测区间 0 - 0，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）

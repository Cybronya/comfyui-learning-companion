---
name: image_to_image_controlnet_ipadapter_upscale_11
type: Image To Image
frequency: 2
level: weak
coverage: 0.846
common_nodes: [Anything Everywhere, BasicGuider, BasicScheduler, CLIPSetLastLayer, CLIPTextEncode, CR Prompt Text, CR SDXL Aspect Ratio, CheckpointLoaderSimple, ConditioningAverage, Constant Number, ControlNetApplyAdvanced, ControlNetLoader, DisableNoise, DownloadAndLoadFlorence2Model, DualCLIPLoader, FaceDetailer, Florence2Run, FluxGuidance, Get Image Size, IPAdapterFaceID, IPAdapterNoise, IPAdapterUnifiedLoaderFaceID, Image Comparer (rgthree), Image Inset Crop (rgthree), ImageBatch, ImageScaleBy, ImageScaleToTotalPixels, ImageSharpen, ImpactImageBatchToImageList, KSampler, KSamplerAdvanced, KSamplerSelect, LatentUpscaleBy, LoadImage, LoraLoaderModelOnly, MaskToImage, MeshGraphormer-DepthMapPreprocessor, ModelSamplingFlux, PhotoMakerEncodePlus, PhotoMakerInsightFaceLoader, PhotoMakerLoaderPlus, PhotoMakerStyles, PrepImageForClipVision, PreviewImage, RandomNoise, SAMLoader, SamplerCustomAdvanced, SaveImage, Seed Everywhere, ShowText|pysssss, SplitSigmasDenoise, TTP_CoordinateSplitter, TTP_Image_Tile_Batch, TTP_Tile_image_size, TTP_condsetarea_merge, TTP_condtobatch, Text Concatenate, TextCombinerTwo, TextInput_, UNETLoader, UltralyticsDetectorProvider, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy cleanGpuUsed, smZ CLIPTextEncode, smZ Settings]
problems: []
missing: []
members: [平台全量/屠版流 Internet Celebrity MAKER_网红制作机_1838526209113354241.json, 平台全量/高品质美女抽卡机_1840652362904981506.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_ipadapter_upscale_11

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/屠版流 Internet Celebrity MAKER_网红制作机_1838526209113354241.json、平台全量/高品质美女抽卡机_1840652362904981506.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `BasicGuider`
- `BasicScheduler`
- `CLIPSetLastLayer`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CR SDXL Aspect Ratio`
- `CheckpointLoaderSimple`
- `ConditioningAverage`
- `Constant Number`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DisableNoise`
- `DownloadAndLoadFlorence2Model`
- `DualCLIPLoader`
- `FaceDetailer`
- `Florence2Run`
- `FluxGuidance`
- `Get Image Size`
- `IPAdapterFaceID`
- `IPAdapterNoise`
- `IPAdapterUnifiedLoaderFaceID`
- `Image Comparer (rgthree)`
- `Image Inset Crop (rgthree)`
- `ImageBatch`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `ImageSharpen`
- `ImpactImageBatchToImageList`
- `KSampler`
- `KSamplerAdvanced`
- `KSamplerSelect`
- `LatentUpscaleBy`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `MeshGraphormer-DepthMapPreprocessor`
- `ModelSamplingFlux`
- `PhotoMakerEncodePlus`
- `PhotoMakerInsightFaceLoader`
- `PhotoMakerLoaderPlus`
- `PhotoMakerStyles`
- `PrepImageForClipVision`
- `PreviewImage`
- `RandomNoise`
- `SAMLoader`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed Everywhere`
- `ShowText|pysssss`
- `SplitSigmasDenoise`
- `TTP_CoordinateSplitter`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TTP_condsetarea_merge`
- `TTP_condtobatch`
- `Text Concatenate`
- `TextCombinerTwo`
- `TextInput_`
- `UNETLoader`
- `UltralyticsDetectorProvider`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `smZ CLIPTextEncode`
- `smZ Settings`

**可变部分**（部分 workflow 才有）：
- `RH_Prompter` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 100% |
| Prompt 约束强度(CFG) | 25 | - | 2 | 100% |
| 采样算法 | 5 | - | 2 | 100% |
| 调度器 | dpmpp_2m | - | 2 | 50% |
| 重绘幅度 | karras | - | 2 | 100% |
| ControlNet 权重 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 dpmpp_2m，2 个样本，一致性 50%
- 重绘幅度 最常用 karras，2 个样本，一致性 100%
- ControlNet 权重 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 25，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

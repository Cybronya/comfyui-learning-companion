---
name: text_to_image_controlnet_upscale_face_detailer
type: Text To Image
frequency: 4
level: strong
coverage: 0.656
common_nodes: [AddLabel, Anything Everywhere, AutoCropFaces, AutoDownloadBiRefNetModel, BasicScheduler, BlurImageFast, CFGGuider, CLIPSetLastLayer, CLIPTextEncode, Cfg Literal, CheckpointLoaderSimple, ColorMatch, ControlNetApplyAdvanced, ControlNetLoader, CoreMLDetailerHookProvider, Create Grid Image from Batch, DetailTransfer, DownloadAndLoadFlorence2Model, EmptyLatentImage, ExpressionEditor, FaceDetailerPipe, Fast Groups Muter (rgthree), Florence2Run, FromBasicPipe_v2, GetImageSize+, GetNode, GrowMaskWithBlur, ICLightConditioning, Image Color Palette, Image Comparer (rgthree), ImageBatch, ImageBatchMulti, ImageCompositeMasked, ImageConcanate, ImageFromBatch, ImageGridtoBatch, ImageListToImageBatch, ImagePadForOutpaintMasked, ImageRemoveAlpha+, ImageResizeKJ, ImageScale, ImageScaleBy, ImpactImageBatchToImageList, ImpactMakeImageBatch, ImpactSwitch, Int Literal, JoinStrings, KSampler, KSamplerSelect, LoadAndApplyICLightUnet, LoadImage, LoraLoader, MaskToImage, ModelPassThrough, PreviewImage, RandomNoise, RembgByBiRefNetAdvanced, RepeatImageBatch, SamplerCustomAdvanced, SaveImage, SetNode, SetUnionControlNetType, ShowText|pysssss, SimpleMath+, SolidMask, String Literal, ToBasicPipe, ToDetailerPipe, UltimateSDUpscale, UltralyticsDetectorProvider, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/Flux版生成角色表（指定角色）_1916154640185102338.json, 图片生成/图生图/SDXL - 低显存版生成角色表（指定角色）_1916511896038739969.json, 图片生成/图生图/生成人物 SDXL版生成角色表（指定角色）(六视图生成)_1936425818140626946.json, 图片生成/图生图/生成人物 SDXL版生成角色表（指定角色）_1929057341084221441.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_upscale_face_detailer

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux版生成角色表（指定角色）_1916154640185102338.json、图片生成/图生图/SDXL - 低显存版生成角色表（指定角色）_1916511896038739969.json、图片生成/图生图/生成人物 SDXL版生成角色表（指定角色）(六视图生成)_1936425818140626946.json、图片生成/图生图/生成人物 SDXL版生成角色表（指定角色）_1929057341084221441.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：66%

## 共有节点

全部 4 个 workflow 都包含：
- `AddLabel`
- `Anything Everywhere`
- `AutoCropFaces`
- `AutoDownloadBiRefNetModel`
- `BasicScheduler`
- `BlurImageFast`
- `CFGGuider`
- `CLIPSetLastLayer`
- `CLIPTextEncode`
- `Cfg Literal`
- `CheckpointLoaderSimple`
- `ColorMatch`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `CoreMLDetailerHookProvider`
- `Create Grid Image from Batch`
- `DetailTransfer`
- `DownloadAndLoadFlorence2Model`
- `EmptyLatentImage`
- `ExpressionEditor`
- `FaceDetailerPipe`
- `Fast Groups Muter (rgthree)`
- `Florence2Run`
- `FromBasicPipe_v2`
- `GetImageSize+`
- `GetNode`
- `GrowMaskWithBlur`
- `ICLightConditioning`
- `Image Color Palette`
- `Image Comparer (rgthree)`
- `ImageBatch`
- `ImageBatchMulti`
- `ImageCompositeMasked`
- `ImageConcanate`
- `ImageFromBatch`
- `ImageGridtoBatch`
- `ImageListToImageBatch`
- `ImagePadForOutpaintMasked`
- `ImageRemoveAlpha+`
- `ImageResizeKJ`
- `ImageScale`
- `ImageScaleBy`
- `ImpactImageBatchToImageList`
- `ImpactMakeImageBatch`
- `ImpactSwitch`
- `Int Literal`
- `JoinStrings`
- `KSampler`
- `KSamplerSelect`
- `LoadAndApplyICLightUnet`
- `LoadImage`
- `LoraLoader`
- `MaskToImage`
- `ModelPassThrough`
- `PreviewImage`
- `RandomNoise`
- `RembgByBiRefNetAdvanced`
- `RepeatImageBatch`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `SetUnionControlNetType`
- `ShowText|pysssss`
- `SimpleMath+`
- `SolidMask`
- `String Literal`
- `ToBasicPipe`
- `ToDetailerPipe`
- `UltimateSDUpscale`
- `UltralyticsDetectorProvider`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `DiffusersMVModelMakeup` —— 3/4 个有
- `DiffusersMVSampler` —— 3/4 个有
- `DiffusersMVSchedulerLoader` —— 3/4 个有
- `IPAdapterAdvanced` —— 3/4 个有
- `IPAdapterUnifiedLoader` —— 3/4 个有
- `Image Canny Filter` —— 3/4 个有
- `LdmPipelineLoader` —— 3/4 个有
- `RembgByBiRefNet` —— 3/4 个有
- `FluxGuidance` —— 1/4 个有
- `ImageFromBatch+` —— 1/4 个有
- `easy imageListToImageBatch` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1408 | 1408 - 1408 | 4 | 100% |
| 高度 | 1408 | 1408 - 1408 | 4 | 100% |
| 采样步数 | 25 | 25 - 25 | 4 | 100% |
| Prompt 约束强度(CFG) | 2.98 | 2.98 - 2.98 | 4 | 100% |
| 采样算法 | dpmpp_2m | - | 4 | 100% |
| 调度器 | karras | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| ControlNet 权重 | 0.8 | 0.6 - 0.8 | 4 | 88% |
| LoRA 模型强度 | 0.69 | 0.69 - 0.69 | 4 | 100% |
| LoRA 文本强度 | 0.69 | 0.69 - 0.69 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1408，观测区间 1408 - 1408，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1408，观测区间 1408 - 1408，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.98，观测区间 2.98 - 2.98，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，4 个样本，一致性 100%
- 调度器 最常用 karras，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.8，观测区间 0.6 - 0.8，4 个样本，取值集中（一致性 88%）
- LoRA 模型强度 中位数 0.69，观测区间 0.69 - 0.69，4 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.69，观测区间 0.69 - 0.69，4 个样本，取值集中（一致性 100%）

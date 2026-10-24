---
name: unknown_workflow_video_upscale_latent_upscale_150
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.888
common_nodes: [Anything Everywhere, BasicGuider, BasicScheduler, BetaSamplingScheduler, CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, DWPreprocessor, DisableNoise, DownloadAndLoadWav2VecModel, DualCLIPLoader, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, GetImageSizeAndCount, GetNode, INTConstant, ImageFromBatch, ImageInvert, ImageResizeKJv2, ImageScaleBy, ImageScaleToMaxDimension, Int, JoinStrings, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAddGuide, LTXVAddGuideMulti, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVFirstLastFrameControl_TTP, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, LotusConditioning, ManualSigmas, MemoryCleaner, Power Lora Loader (rgthree), PrimitiveFloat, PrimitiveInt, Qwen3_VQA, RandomNoise, ResizeImageMaskNode, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SetFirstSigma, SetNode, ShowText|pysssss, TextInput_, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, VAELoaderKJ, VHS_LoadVideo, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [视频生成/文生视频/LTX2.0全生态  文生视频｜图生视频｜首尾帧视频｜镜头+_CN控制_2021149152385699842.json, 视频生成/文生视频/LTX2.0文生视频｜图生视频｜首尾帧视频｜镜头+_CN控制_2017161610749550593.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_150

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/LTX2.0全生态  文生视频｜图生视频｜首尾帧视频｜镜头+_CN控制_2021149152385699842.json、视频生成/文生视频/LTX2.0文生视频｜图生视频｜首尾帧视频｜镜头+_CN控制_2017161610749550593.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `BasicGuider`
- `BasicScheduler`
- `BetaSamplingScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `DWPreprocessor`
- `DisableNoise`
- `DownloadAndLoadWav2VecModel`
- `DualCLIPLoader`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageFromBatch`
- `ImageInvert`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `ImageScaleToMaxDimension`
- `Int`
- `JoinStrings`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAddGuide`
- `LTXVAddGuideMulti`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVFirstLastFrameControl_TTP`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `LotusConditioning`
- `ManualSigmas`
- `MemoryCleaner`
- `Power Lora Loader (rgthree)`
- `PrimitiveFloat`
- `PrimitiveInt`
- `Qwen3_VQA`
- `RandomNoise`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SetFirstSigma`
- `SetNode`
- `ShowText|pysssss`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | - | 2 | 100% |
| 高度 | 25 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

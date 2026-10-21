---
name: unknown_workflow_video_upscale_latent_upscale_72
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.6158
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSize, INTConstant, ImageResizeKJv2, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveFloat, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SimpleCalculatorKJ, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2054086859323650049.json, 视频生成/图生视频/2041823999381999617.json, 视频生成/图生视频/2052438647814803458.json, 视频生成/图生视频/2050782618651774978.json, 视频生成/图生视频/2054945607445434370.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_72

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/2054086859323650049.json、视频生成/图生视频/2041823999381999617.json、视频生成/图生视频/2052438647814803458.json、视频生成/图生视频/2050782618651774978.json、视频生成/图生视频/2054945607445434370.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：62%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveFloat`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SimpleCalculatorKJ`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 4/5 个有
- `GetNode` —— 4/5 个有
- `LTXVChunkFeedForward` —— 4/5 个有
- `MathExpression|pysssss` —— 4/5 个有
- `SeedGenerator` —— 4/5 个有
- `SetNode` —— 4/5 个有
- `UNETLoader` —— 4/5 个有
- `UnetLoaderGGUF` —— 4/5 个有
- `AILab_QwenVL` —— 3/5 个有
- `DualCLIPLoaderGGUF` —— 3/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `GetImageRangeFromBatch` —— 3/5 个有
- `PrimitiveBoolean` —— 3/5 个有
- `ResizeImageMaskNode` —— 3/5 个有
- `TTP_text_mix` —— 3/5 个有
- `VHS_GetImageCount` —— 3/5 个有
- `easy convertAnything` —— 3/5 个有
- `ImageScaleBy` —— 2/5 个有
- `LTXVAddGuideMulti` —— 2/5 个有
- `LazySwitchKJ` —— 2/5 个有
- `PreviewAny` —— 2/5 个有
- `PrimitiveStringMultiline` —— 2/5 个有
- `PromptRelayEncodeTimeline` —— 2/5 个有
- `TextGenerateLTX2Prompt` —— 2/5 个有
- `BasicScheduler` —— 1/5 个有
- `GetImagesFromBatchIndexed` —— 1/5 个有
- `ImageBatchMulti` —— 1/5 个有
- `ImageClone` —— 1/5 个有
- `LTXVAddGuide` —— 1/5 个有
- `LTXVAddGuidesFromBatch` —— 1/5 个有
- `LTXVCropGuides` —— 1/5 个有
- `LTXVEnhanceAVideoKJ` —— 1/5 个有
- `LTXVImgToVideoInplaceKJ` —— 1/5 个有
- `ModelPatchTorchSettings` —— 1/5 个有
- `PathchSageAttentionKJ` —— 1/5 个有
- `PromptRelayAdvancedOptions` —— 1/5 个有
- `STGGuiderAdvanced` —— 1/5 个有
- `SaveVideo` —— 1/5 个有
- `Seed (rgthree)` —— 1/5 个有
- `TextInput_` —— 1/5 个有
- `VisualizeSigmasKJ` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 121 | 97 - 121 | 5 | 89% |
| 高度 | 24 | 24 - 25 | 5 | 98% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 121，观测区间 97 - 121，5 个样本，取值集中（一致性 89%）
- 高度 中位数 24，观测区间 24 - 25，5 个样本，取值集中（一致性 98%）

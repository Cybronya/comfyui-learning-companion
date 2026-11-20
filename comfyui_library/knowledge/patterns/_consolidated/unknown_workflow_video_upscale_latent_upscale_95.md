---
name: unknown_workflow_video_upscale_latent_upscale_95
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.5475
common_nodes: [CFGGuider, CLIPTextEncode, CreateVideo, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSize, GetNode, INTConstant, ImageResizeKJv2, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, MathExpression|pysssss, PrimitiveFloat, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SeedGenerator, SetNode, SimpleCalculatorKJ, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/LTX 2.3 Timeline Prompt控制分镜视频生成_2054086859323650049.json, 视频生成/图生视频/LTX2.3 VBVR分镜视频生成I2V_T2V_2052438647814803458.json, 视频生成/图生视频/LTX2.3多帧丝滑转场_2050782618651774978.json, 视频生成/图生视频/Ltx2.3 多图参考人物场景分镜视频_2054945607445434370.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_95

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/LTX 2.3 Timeline Prompt控制分镜视频生成_2054086859323650049.json、视频生成/图生视频/LTX2.3 VBVR分镜视频生成I2V_T2V_2052438647814803458.json、视频生成/图生视频/LTX2.3多帧丝滑转场_2050782618651774978.json、视频生成/图生视频/Ltx2.3 多图参考人物场景分镜视频_2054945607445434370.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：55%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CreateVideo`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `GetNode`
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
- `MathExpression|pysssss`
- `PrimitiveFloat`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SeedGenerator`
- `SetNode`
- `SimpleCalculatorKJ`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `GetImageRangeFromBatch` —— 3/4 个有
- `LTXVChunkFeedForward` —— 3/4 个有
- `PrimitiveBoolean` —— 3/4 个有
- `ResizeImageMaskNode` —— 3/4 个有
- `TTP_text_mix` —— 3/4 个有
- `UNETLoader` —— 3/4 个有
- `UnetLoaderGGUF` —— 3/4 个有
- `VHS_GetImageCount` —— 3/4 个有
- `easy convertAnything` —— 3/4 个有
- `DualCLIPLoaderGGUF` —— 2/4 个有
- `LazySwitchKJ` —— 2/4 个有
- `PreviewAny` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `PromptRelayEncodeTimeline` —— 2/4 个有
- `TextGenerateLTX2Prompt` —— 2/4 个有
- `BasicScheduler` —— 1/4 个有
- `GetImagesFromBatchIndexed` —— 1/4 个有
- `ImageBatchMulti` —— 1/4 个有
- `ImageClone` —— 1/4 个有
- `ImageScaleBy` —— 1/4 个有
- `LTXVAddGuide` —— 1/4 个有
- `LTXVAddGuideMulti` —— 1/4 个有
- `LTXVAddGuidesFromBatch` —— 1/4 个有
- `LTXVEnhanceAVideoKJ` —— 1/4 个有
- `LTXVImgToVideoInplaceKJ` —— 1/4 个有
- `ModelPatchTorchSettings` —— 1/4 个有
- `PathchSageAttentionKJ` —— 1/4 个有
- `PromptRelayAdvancedOptions` —— 1/4 个有
- `STGGuiderAdvanced` —— 1/4 个有
- `SaveVideo` —— 1/4 个有
- `Seed (rgthree)` —— 1/4 个有
- `TextInput_` —— 1/4 个有
- `VisualizeSigmasKJ` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 121 | 97 - 121 | 4 | 91% |
| 高度 | 24 | 24 - 25 | 4 | 98% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 121，观测区间 97 - 121，4 个样本，取值集中（一致性 91%）
- 高度 中位数 24，观测区间 24 - 25，4 个样本，取值集中（一致性 98%）

---
name: unknown_workflow_video_upscale_latent_upscale_95
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.58775
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoader, DualCLIPLoaderGGUF, EmptyLTXVLatentVideo, INTConstant, ImageResizeKJv2, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveFloat, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SimpleCalculatorKJ, UNETLoader, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2041756040752009217.json, 视频生成/文生视频/LTX 2.3 多图首尾帧_2032460701406601217.json, 视频生成/文生视频/LTX-2.3_图生_文生_视频工作流_2029830274397249538.json, 视频生成/文生视频/LTX2.3 Prompt Relay生成多事件时序视频_2046855893886705666.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_95

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2041756040752009217.json、视频生成/文生视频/LTX 2.3 多图首尾帧_2032460701406601217.json、视频生成/文生视频/LTX-2.3_图生_文生_视频工作流_2029830274397249538.json、视频生成/文生视频/LTX2.3 Prompt Relay生成多事件时序视频_2046855893886705666.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：59%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `DualCLIPLoaderGGUF`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
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
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 3/4 个有
- `GetNode` —— 3/4 个有
- `LTX2SamplingPreviewOverride` —— 3/4 个有
- `LTXVChunkFeedForward` —— 3/4 个有
- `LTXVEmptyLatentAudio` —— 3/4 个有
- `PrimitiveBoolean` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `UnetLoaderGGUF` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `LTX2_NAG` —— 2/4 个有
- `Power Lora Loader (rgthree)` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `ResizeImageMaskNode` —— 2/4 个有
- `StringConcatenate` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `ComfyMathExpression` —— 1/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `CreateVideo` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `ImageScaleBy` —— 1/4 个有
- `JWIntegerToString` —— 1/4 个有
- `LTX2AttentionTunerPatch` —— 1/4 个有
- `LTX2MemoryEfficientSageAttentionPatch` —— 1/4 个有
- `LTXVAddGuideMulti` —— 1/4 个有
- `LTXVAudioVAEEncode` —— 1/4 个有
- `LTXVCropGuides` —— 1/4 个有
- `MuyeTextEditOutput` —— 1/4 个有
- `PathchSageAttentionKJ` —— 1/4 个有
- `PromptRelayEncode` —— 1/4 个有
- `SaveImage` —— 1/4 个有
- `SaveVideo` —— 1/4 个有
- `SetLatentNoiseMask` —— 1/4 个有
- `SolidMask` —— 1/4 个有
- `TextGenerateLTX2Prompt` —— 1/4 个有
- `VHS_LoadAudioUpload` —— 1/4 个有
- `easy seed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 121 | 3 | 89% |
| 高度 | 25 | 24 - 25 | 3 | 98% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 121，3 个样本，取值集中（一致性 89%）
- 高度 中位数 25，观测区间 24 - 25，3 个样本，取值集中（一致性 98%）

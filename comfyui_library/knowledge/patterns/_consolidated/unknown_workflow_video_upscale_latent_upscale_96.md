---
name: unknown_workflow_video_upscale_latent_upscale_96
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.4815
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, INTConstant, KSamplerSelect, LTX2AttentionTunerPatch, LTX2MemoryEfficientSageAttentionPatch, LTX2SamplingPreviewOverride, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PathchSageAttentionKJ, PrimitiveFloat, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SetNode, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Sulphur-2 timelinePrompt时序视频_2053346294621589505.json, 视频生成/图生视频/ltx2.3-PromptRelay-4宫格工作流-1.66-24G_2063565423085445122.json, 视频生成/图生视频/ltx2.3-PromptRelay-4宫格工作流-1.80_2073745164908191745.json, 视频生成/文生视频/LTX2.3 Prompt Relay生成多事件时序视频_2046855893886705666.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_96

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Sulphur-2 timelinePrompt时序视频_2053346294621589505.json、视频生成/图生视频/ltx2.3-PromptRelay-4宫格工作流-1.66-24G_2063565423085445122.json、视频生成/图生视频/ltx2.3-PromptRelay-4宫格工作流-1.80_2073745164908191745.json、视频生成/文生视频/LTX2.3 Prompt Relay生成多事件时序视频_2046855893886705666.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：48%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `INTConstant`
- `KSamplerSelect`
- `LTX2AttentionTunerPatch`
- `LTX2MemoryEfficientSageAttentionPatch`
- `LTX2SamplingPreviewOverride`
- `LTXVAudioVAEDecode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SetNode`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LTX2_NAG` —— 3/4 个有
- `PromptRelayEncodeTimeline` —— 3/4 个有
- `UNETLoader` —— 3/4 个有
- `GuHaiAutoImageSplit` —— 2/4 个有
- `ImageFromBatch+` —— 2/4 个有
- `ImageResizeKJv2` —— 2/4 个有
- `LTXVAddGuideMulti` —— 2/4 个有
- `LTXVCropGuides` —— 2/4 个有
- `LTXVImgToVideoInplace` —— 2/4 个有
- `PrimitiveBoolean` —— 2/4 个有
- `ResizeImageMaskNode` —— 2/4 个有
- `SimpleCalculatorKJ` —— 2/4 个有
- `CheckpointLoaderSimple` —— 1/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `CreateVideo` —— 1/4 个有
- `DualCLIPLoaderGGUF` —— 1/4 个有
- `JWIntegerToString` —— 1/4 个有
- `LTXAVTextEncoderLoader` —— 1/4 个有
- `LTXVAudioVAELoader` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `PromptRelayEncode` —— 1/4 个有
- `SaveVideo` —— 1/4 个有
- `SeedGenerator` —— 1/4 个有
- `StringConcatenate` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有
- `easy ckptNames` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 301 | 97 - 361 | 4 | 59% |
| 高度 | 25 | 24 - 25 | 4 | 98% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 301，观测区间 97 - 361，4 个样本
- 高度 中位数 25，观测区间 24 - 25，4 个样本，取值集中（一致性 98%）

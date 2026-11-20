---
name: unknown_workflow_sampler_clip_checkpoint_7
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8461
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, EmptyLTXVLatentVideo, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled]
problems: []
missing: []
members: [图片生成/图生图/LTX2.3首尾帧生视频_2082849413030039554.json, 图片生成/图生图/LTX2.3首尾帧生视频（官流）_2044379185442983938.json, 图片生成/图生图/首尾帧双图生视频_2099481750966718465.json, 图片生成/文生图/LTX-2.3_ICLoRA_Motion_Track运动控制_2073317347884093441.json, 图片生成/文生图/LTX2.3提示词自动优化流_2073313535265951745.json, 图片生成/文生图/LTX2.3提示词自动优化流_2073314279406792706.json, 图片生成/文生图/LTX2.3自动首中尾帧流_2073320995959689218.json, 平台全量/LTX2.3首尾帧_2044349781501288449.json, 视频生成/图生视频/Gemini 3.1 Pro自动提示词+LTX2.3模型 首尾帧生视频工作流_2044864850374955009.json, 视频生成/图生视频/LTX-2.3_ICLoRA_Union_Control视频生视频_2073317124101201921.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_7

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/LTX2.3首尾帧生视频_2082849413030039554.json、图片生成/图生图/LTX2.3首尾帧生视频（官流）_2044379185442983938.json、图片生成/图生图/首尾帧双图生视频_2099481750966718465.json、图片生成/文生图/LTX-2.3_ICLoRA_Motion_Track运动控制_2073317347884093441.json、图片生成/文生图/LTX2.3提示词自动优化流_2073313535265951745.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 9/10 个有
- `CreateVideo` —— 8/10 个有
- `ResizeImageMaskNode` —— 8/10 个有
- `SaveVideo` —— 8/10 个有
- `easy showAnything` —— 8/10 个有
- `KSamplerSelect` —— 7/10 个有
- `PrimitiveStringMultiline` —— 7/10 个有
- `ResizeImagesByLongerEdge` —— 7/10 个有
- `LatentUpscaleModelLoader` —— 6/10 个有
- `RH_LLMAPI_Pro_Node` —— 6/10 个有
- `GetImageSize` —— 5/10 个有
- `LTXVImgToVideoInplace` —— 5/10 个有
- `LTXVLatentUpsampler` —— 5/10 个有
- `ModelPatchTorchSettings` —— 4/10 个有
- `PathchSageAttentionKJ` —— 4/10 个有
- `FloatConstant` —— 3/10 个有
- `LTXVAddGuide` —— 3/10 个有
- `LTXVImgToVideoInplaceKJ` —— 3/10 个有
- `PrimitiveBoolean` —— 3/10 个有
- `SamplerEulerAncestral` —— 3/10 个有
- `Image Resize` —— 2/10 个有
- `ImageResizeKJv2` —— 2/10 个有
- `LTXAddVideoICLoRAGuide` —— 2/10 个有
- `LTXICLoRALoaderModelOnly` —— 2/10 个有
- `LTXVChunkFeedForward` —— 2/10 个有
- `LTXVImgToVideoConditionOnly` —— 2/10 个有
- `SimpleMath+` —— 2/10 个有
- `VHS_VideoCombine` —— 2/10 个有
- `AIO_Preprocessor` —— 1/10 个有
- `CR String To Combo` —— 1/10 个有
- `CustomAddLabel` —— 1/10 个有
- `ImpactStringSelector` —— 1/10 个有
- `Int` —— 1/10 个有
- `LTX2_NAG` —— 1/10 个有
- `LTXVDrawTracks` —— 1/10 个有
- `LTXVScheduler` —— 1/10 个有
- `LTXVSparseTrackEditor` —— 1/10 个有
- `RHHiddenNodes` —— 1/10 个有
- `TTResolutionSelector` —— 1/10 个有
- `VHS_LoadVideo` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 10 | 100% |
| 高度 | 25 | 25 - 25 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，10 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，10 个样本，取值集中（一致性 100%）

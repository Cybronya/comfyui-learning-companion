---
name: unknown_workflow_sampler_clip_checkpoint_3
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.840786
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, EmptyLTXVLatentVideo, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled]
problems: []
missing: []
members: [图片生成/图生图/LTX2.3首尾帧生视频_2082849413030039554.json, 图片生成/图生图/LTX2.3首尾帧生视频（官流）_2044379185442983938.json, 图片生成/图生图/首尾帧双图生视频_2099481750966718465.json, 图片生成/文生图/LTX-2.3_ICLoRA_Motion_Track运动控制_2073317347884093441.json, 图片生成/文生图/LTX2.3提示词自动优化流_2073313535265951745.json, 图片生成/文生图/LTX2.3提示词自动优化流_2073314279406792706.json, 图片生成/文生图/LTX2.3自动首中尾帧流_2073320995959689218.json, 视频生成/图生视频/1FINAL - LTX2.3 _ 单图+提示词=快速出视频_2052231209417232385.json, 视频生成/图生视频/Gemini 3.1 Pro自动提示词+LTX2.3模型 首尾帧生视频工作流_2044864850374955009.json, 视频生成/图生视频/LTX-2.3_ICLoRA_Union_Control视频生视频_2073317124101201921.json, 视频生成/图生视频/LTX2.3 _ 三图-首中尾帧 优化版_2033038199701905410.json, 视频生成/图生视频/LTX2.3 _ 双图-首尾帧 优化版_2033156764371263490.json, 视频生成/图生视频/LTX2.3 _ 双图-首尾帧 优化版_2044341747362304001.json, 视频生成/图生视频/LTX2.3 _ 双图-首尾帧 优化版_2049303254957297665.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_3

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/LTX2.3首尾帧生视频_2082849413030039554.json、图片生成/图生图/LTX2.3首尾帧生视频（官流）_2044379185442983938.json、图片生成/图生图/首尾帧双图生视频_2099481750966718465.json、图片生成/文生图/LTX-2.3_ICLoRA_Motion_Track运动控制_2073317347884093441.json、图片生成/文生图/LTX2.3提示词自动优化流_2073313535265951745.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 14 个 workflow 都包含：
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
- `LoraLoaderModelOnly` —— 13/14 个有
- `easy showAnything` —— 13/14 个有
- `CreateVideo` —— 12/14 个有
- `SaveVideo` —— 12/14 个有
- `KSamplerSelect` —— 11/14 个有
- `PrimitiveStringMultiline` —— 11/14 个有
- `RH_LLMAPI_Pro_Node` —— 11/14 个有
- `ResizeImagesByLongerEdge` —— 11/14 个有
- `LatentUpscaleModelLoader` —— 10/14 个有
- `LTXVImgToVideoInplace` —— 9/14 个有
- `LTXVLatentUpsampler` —— 9/14 个有
- `ResizeImageMaskNode` —— 9/14 个有
- `ModelPatchTorchSettings` —— 8/14 个有
- `PathchSageAttentionKJ` —— 8/14 个有
- `FloatConstant` —— 7/14 个有
- `LTXVImgToVideoInplaceKJ` —— 7/14 个有
- `LTXVChunkFeedForward` —— 6/14 个有
- `SimpleMath+` —— 6/14 个有
- `GetImageSize` —— 5/14 个有
- `ImageResizeKJv2` —— 3/14 个有
- `LTXVAddGuide` —— 3/14 个有
- `PrimitiveBoolean` —— 3/14 个有
- `SamplerEulerAncestral` —— 3/14 个有
- `LTXAddVideoICLoRAGuide` —— 2/14 个有
- `LTXICLoRALoaderModelOnly` —— 2/14 个有
- `LTXVImgToVideoConditionOnly` —— 2/14 个有
- `Resize` —— 2/14 个有
- `VHS_VideoCombine` —— 2/14 个有
- `AILab_QwenVL` —— 1/14 个有
- `AIO_Preprocessor` —— 1/14 个有
- `CR String To Combo` —— 1/14 个有
- `CombineImagesForQwen3VL` —— 1/14 个有
- `Image Resize` —— 1/14 个有
- `ImpactStringSelector` —— 1/14 个有
- `LTX2_NAG` —— 1/14 个有
- `LTXVDrawTracks` —— 1/14 个有
- `LTXVScheduler` —— 1/14 个有
- `LTXVSparseTrackEditor` —— 1/14 个有
- `RHHiddenNodes` —— 1/14 个有
- `VHS_LoadVideo` —— 1/14 个有
- `kkResize` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 14 | 100% |
| 高度 | 25 | 25 - 25 | 14 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，14 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，14 个样本，取值集中（一致性 100%）

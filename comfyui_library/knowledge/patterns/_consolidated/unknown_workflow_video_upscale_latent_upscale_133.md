---
name: unknown_workflow_video_upscale_latent_upscale_133
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.813
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVImgToVideoInplaceKJ, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, MathExpression|pysssss, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveStringMultiline, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, VAEDecodeTiled, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2033729811360780290.json, 视频生成/图生视频/2067597395021623297.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_133

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2033729811360780290.json、视频生成/图生视频/2067597395021623297.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVImgToVideoInplaceKJ`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `FloatConstant` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `LTXVCropGuides` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `RH_LLMAPI_Pro_Node` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `ResizeImageMaskNode` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `SimpleCalculatorKJ` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `VAEDecode` —— 1/2 个有
- `floatToInt _O` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | - | 2 | 100% |
| 高度 | 42.5 | - | 2 | 59% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 42.5，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

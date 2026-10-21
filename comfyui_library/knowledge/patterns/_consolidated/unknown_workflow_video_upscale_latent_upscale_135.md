---
name: unknown_workflow_video_upscale_latent_upscale_135
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.519
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, EmptyLTXVLatentVideo, Float, GetNode, ImageResizeKJv2, Int, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, RandomNoise, SamplerCustomAdvanced, SetNode, Text, VAEDecodeTiled, VHS_VideoCombine, math_calculate]
problems: []
missing: []
members: [视频生成/图生视频/2045362870476607490.json, 视频生成/文生视频/LTX2.3文生视频+图生视频_2034150036669472770.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_135

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2045362870476607490.json、视频生成/文生视频/LTX2.3文生视频+图生视频_2034150036669472770.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：52%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `EmptyLTXVLatentVideo`
- `Float`
- `GetNode`
- `ImageResizeKJv2`
- `Int`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `Text`
- `VAEDecodeTiled`
- `VHS_VideoCombine`
- `math_calculate`

**可变部分**（部分 workflow 才有）：
- `BOOLConstant` —— 1/2 个有
- `Bool` —— 1/2 个有
- `CheckpointLoaderSimple` —— 1/2 个有
- `LTX2SamplingPreviewOverride` —— 1/2 个有
- `LTX2_NAG` —— 1/2 个有
- `LTXVAudioVAELoader` —— 1/2 个有
- `LTXVCropGuides` —— 1/2 个有
- `LTXVImgToVideoInplaceKJ` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `ResizeImagesByLongerEdge` —— 1/2 个有
- `TTResolutionSelector` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `VAELoader` —— 1/2 个有
- `VAELoaderKJ` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | - | 2 | 100% |
| 高度 | 25 | - | 2 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

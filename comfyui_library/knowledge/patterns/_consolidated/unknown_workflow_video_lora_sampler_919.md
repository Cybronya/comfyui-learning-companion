---
name: unknown_workflow_video_lora_sampler_919
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9295
common_nodes: [AudioConcat, CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, DualCLIPLoader, EmptyLTXVLatentVideo, FL_IntToFloat, GetImageRangeFromBatch, ImageSharpen, JWInteger, KSamplerSelect, LTXVAddGuideMulti, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVNormalizingSampler, LTXVPreprocess, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, PathchSageAttentionKJ, PrimitiveInt, RH_LLMAPI_NODE, RH_LLMAPI_Pro_Node, RandomNoise, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/lltx2-视频首尾帧-Video first and last frames_2019971390018953218.json, 视频生成/图生视频/ltx2-图生视频-image to video_2020703327746531330.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_919

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/lltx2-视频首尾帧-Video first and last frames_2019971390018953218.json、视频生成/图生视频/ltx2-图生视频-image to video_2020703327746531330.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioConcat`
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `FL_IntToFloat`
- `GetImageRangeFromBatch`
- `ImageSharpen`
- `JWInteger`
- `KSamplerSelect`
- `LTXVAddGuideMulti`
- `LTXVAudioVAEDecode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVNormalizingSampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `RH_LLMAPI_NODE`
- `RH_LLMAPI_Pro_Node`
- `RandomNoise`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `CR Text Concatenate` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `ManualSigmas` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 93 | - | 2 | 100% |
| 高度 | 20 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 93，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

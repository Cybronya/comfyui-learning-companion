---
name: unknown_workflow_video_lora_sampler_585
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.814333
common_nodes: [Bjornulf_IfElse, CFGGuider, CLIPTextEncode, CR Text, CR Text Concatenate, CheckpointLoaderSimple, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageRangeFromBatch, ImageResizeKJv2, JWInteger, KSamplerSelect, LTXVAddGuideMulti, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LazySwitch1way, LazySwitch2way, LoadImage, LoraLoaderModelOnly, ManualSigmas, MathExpression|pysssss, PathchSageAttentionKJ, PreviewAny, PrimitiveInt, RH_LLMAPI_Pro_Node, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, easy boolean, easy convertAnything, easy float, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2044963252995629058.json, 视频生成/图生视频/2038430942880079873.json, 视频生成/图生视频/2038885933809930241.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_585

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2044963252995629058.json、视频生成/图生视频/2038430942880079873.json、视频生成/图生视频/2038885933809930241.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `Bjornulf_IfElse`
- `CFGGuider`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `CheckpointLoaderSimple`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageRangeFromBatch`
- `ImageResizeKJv2`
- `JWInteger`
- `KSamplerSelect`
- `LTXVAddGuideMulti`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVSeparateAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LazySwitch1way`
- `LazySwitch2way`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MathExpression|pysssss`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `PrimitiveInt`
- `RH_LLMAPI_Pro_Node`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy boolean`
- `easy convertAnything`
- `easy float`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `DapaoGeminiInstructionZhenzhenNode` —— 2/3 个有
- `ImpactSwitch` —— 2/3 个有
- `LTX2SamplingPreviewOverride` —— 2/3 个有
- `LTXVAudioVAEDecode` —— 2/3 个有
- `LTXVEmptyLatentAudio` —— 2/3 个有
- `RTXVideoSuperResolution` —— 2/3 个有
- `VAELoader` —— 2/3 个有
- `AudioCropProcessUTK` —— 1/3 个有
- `CFGNorm` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `LTX2_NAG` —— 1/3 个有
- `LTXVAudioVAEEncode` —— 1/3 个有
- `LTXVChunkFeedForward` —— 1/3 个有
- `LTXVLatentUpsampler` —— 1/3 个有
- `LatentUpscaleModelLoader` —— 1/3 个有
- `LoadAudio` —— 1/3 个有
- `ModelPatchTorchSettings` —— 1/3 个有
- `NormalizeAudioLoudness` —— 1/3 个有
- `PrimitiveBoolean` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `SetLatentNoiseMask` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `SolidMask` —— 1/3 个有
- `TrimAudioDuration` —— 1/3 个有

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

---
name: unknown_workflow_lora_sampler_clip_132
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8295
common_nodes: [Audio Duration (mtb), AudioCrop, CFGGuider, CLIPTextEncode, CreateVideo, DualCLIPLoader, EmptyLTXVLatentVideo, KSamplerSelect, LTX2_NAG, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoInplace, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, MathExpression|pysssss, MelBandRoFormerModelLoader, MelBandRoFormerSampler, RandomNoise, SamplerCustomAdvanced, SaveVideo, SetLatentNoiseMask, SolidMask, UNETLoader, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/图生视频/2032276814873235457.json, 视频生成/图生视频/2051620785973936130.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_132

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2032276814873235457.json、视频生成/图生视频/2051620785973936130.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `Audio Duration (mtb)`
- `AudioCrop`
- `CFGGuider`
- `CLIPTextEncode`
- `CreateVideo`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MathExpression|pysssss`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetLatentNoiseMask`
- `SolidMask`
- `UNETLoader`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `Float` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `Int` —— 1/2 个有
- `JWIntegerToString` —— 1/2 个有
- `LTX2SamplingPreviewOverride` —— 1/2 个有
- `LTXVChunkFeedForward` —— 1/2 个有
- `LTXVImgToVideoConditionOnly` —— 1/2 个有
- `LTXVLatentUpsampler` —— 1/2 个有
- `LTXVPreprocess` —— 1/2 个有
- `LTXVSpatioTemporalTiledVAEDecode` —— 1/2 个有
- `LatentUpscaleModelLoader` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `PrimitiveBoolean` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `VAEDecodeTiled` —— 1/2 个有
- `intToFloat _O` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

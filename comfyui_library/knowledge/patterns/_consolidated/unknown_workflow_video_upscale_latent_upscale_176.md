---
name: unknown_workflow_video_upscale_latent_upscale_176
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.737
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, GetImageSizeAndCount, GetNode, ImageScaleBy, ImpactFloat, JWFloatToString, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, MathExpression|pysssss, PrimitiveFloat, PrimitiveInt, RH_LLMAPI_NODE, RandomNoise, SamplerCustomAdvanced, SetNode, StringFunction|pysssss, VAEDecodeTiled, VHS_VideoCombine, easy anythingIndexSwitch, easy int, easy positive, easy saveText, easy seed, easy showAnything]
problems: []
missing: []
members: [视频生成/文生视频/视频-文生视频扩写-LTX2.0_2009188273779904513.json, 视频生成/文生视频/视频-文生视频扩写-LTX2.3_2037067149814013954.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_176

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/视频-文生视频扩写-LTX2.0_2009188273779904513.json、视频生成/文生视频/视频-文生视频扩写-LTX2.3_2037067149814013954.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CheckpointLoaderSimple`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageScaleBy`
- `ImpactFloat`
- `JWFloatToString`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MathExpression|pysssss`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RH_LLMAPI_NODE`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `StringFunction|pysssss`
- `VAEDecodeTiled`
- `VHS_VideoCombine`
- `easy anythingIndexSwitch`
- `easy int`
- `easy positive`
- `easy saveText`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `LTXVChunkFeedForward` —— 1/2 个有
- `LTXVCropGuides` —— 1/2 个有
- `LTXVImgToVideoConditionOnly` —— 1/2 个有
- `LTXVPreprocess` —— 1/2 个有
- `LTXVScheduler` —— 1/2 个有
- `MemoryCleaner` —— 1/2 个有
- `ModelPatchTorchSettings` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `PrimitiveBoolean` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `VAEDecode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | - | 2 | 100% |
| 高度 | 25 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

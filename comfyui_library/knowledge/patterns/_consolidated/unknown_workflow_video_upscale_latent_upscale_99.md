---
name: unknown_workflow_video_upscale_latent_upscale_99
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.90925
common_nodes: [CFGGuider, CLIPTextEncode, CM_IntToFloat, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, ImpactExecutionOrderController, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVLatentUpsampler, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/文生视频-音频驱动LTX-2_T2V_Audio_Input_2017407860040273922.json, 视频生成/文生视频/文生视频LTX-2_T2V_2017065411149307905.json, 视频生成/文生视频/文生视频（解禁模型）：LTX2.3 Sulphur_2059260196207284225.json, 视频生成/文生视频/文生视频：LTX2.3_2055843716434276354.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_99

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/文生视频-音频驱动LTX-2_T2V_Audio_Input_2017407860040273922.json、视频生成/文生视频/文生视频LTX-2_T2V_2017065411149307905.json、视频生成/文生视频/文生视频（解禁模型）：LTX2.3 Sulphur_2059260196207284225.json、视频生成/文生视频/文生视频：LTX2.3_2055843716434276354.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_IntToFloat`
- `CheckpointLoaderSimple`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageScaleBy`
- `ImpactExecutionOrderController`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVLatentUpsampler`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LTXVEmptyLatentAudio` —— 3/4 个有
- `KepStringLiteral` —— 2/4 个有
- `math_calculate` —— 2/4 个有
- `AudioInfoNode` —— 1/4 个有
- `Int` —— 1/4 个有
- `LTXVAudioVAEEncode` —— 1/4 个有
- `MelBandRoFormerModelLoader` —— 1/4 个有
- `MelBandRoFormerSampler` —— 1/4 个有
- `SetLatentNoiseMask` —— 1/4 个有
- `SolidMask` —— 1/4 个有
- `VHS_LoadAudioUpload` —— 1/4 个有
- `VHS_LoadVideo` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 3 | 100% |
| 高度 | 25 | 25 - 25 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，3 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）

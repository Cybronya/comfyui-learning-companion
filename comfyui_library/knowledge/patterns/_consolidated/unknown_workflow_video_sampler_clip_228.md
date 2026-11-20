---
name: unknown_workflow_video_sampler_clip_228
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.83
common_nodes: [CFGGuider, CLIPTextEncode, DiffusionModelLoaderKJ, DualCLIPLoaderGGUF, ImageResize+, ImpactSwitch, KSamplerSelect, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LTXVSpatioTemporalTiledVAEDecode, ManualSigmas, PathchSageAttentionKJ, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SimpleMath+, VAEEncodeTiled, VAELoader, VAELoaderKJ, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, easy convertAnything]
problems: []
missing: []
members: [平台全量/LTX-2同步嘴型声音_2028638129061629953.json, 平台全量/LTX-2视频放大修复加帧率加声音_2027611418224234498.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_228

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/LTX-2同步嘴型声音_2028638129061629953.json、平台全量/LTX-2视频放大修复加帧率加声音_2027611418224234498.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DiffusionModelLoaderKJ`
- `DualCLIPLoaderGGUF`
- `ImageResize+`
- `ImpactSwitch`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LTXVSpatioTemporalTiledVAEDecode`
- `ManualSigmas`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SimpleMath+`
- `VAEEncodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `easy convertAnything`

**可变部分**（部分 workflow 才有）：
- `EmptyLTXVLatentVideo` —— 1/2 个有
- `Fast Bypasser (rgthree)` —— 1/2 个有
- `GetImageRangeFromBatch` —— 1/2 个有
- `ImageScaleToMaxDimension` —— 1/2 个有
- `ImageSmartSharpen+` —— 1/2 个有
- `LTXVAddGuideMulti` —— 1/2 个有
- `LTXVAudioVAEEncode` —— 1/2 个有
- `LTXVLoopingSampler` —— 1/2 个有
- `Latent Noise Injection` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有
- `RIFE VFI` —— 1/2 个有
- `SetLatentNoiseMask` —— 1/2 个有
- `SolidMask` —— 1/2 个有
- `TrimAudioDuration` —— 1/2 个有
- `VHS_LoadAudioUpload` —— 1/2 个有
- `easy ifElse` —— 1/2 个有

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

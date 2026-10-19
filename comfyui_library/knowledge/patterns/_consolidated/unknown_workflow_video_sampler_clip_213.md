---
name: unknown_workflow_video_sampler_clip_213
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.517
common_nodes: [AudioConcat, CFGGuider, CLIPTextEncode, CR Float To Integer, DualCLIPLoaderGGUF, EmptyImage, EmptyLTXVLatentVideo, GetImageRangeFromBatch, GetImageSize, GetImageSizeAndCount, GetNode, ImageBatchExtendWithOverlap, ImageResizeKJv2, ImpactExecutionOrderController, KSamplerSelect, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LTXVSpatioTemporalTiledVAEDecode, LoadImage, PreviewImage, PrimitiveFloat, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SetNode, SimpleMath+, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2012502570719252481.json, 视频生成/图生视频/2012791378404712449.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_213

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2012502570719252481.json、视频生成/图生视频/2012791378404712449.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：52%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioConcat`
- `CFGGuider`
- `CLIPTextEncode`
- `CR Float To Integer`
- `DualCLIPLoaderGGUF`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageRangeFromBatch`
- `GetImageSize`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageBatchExtendWithOverlap`
- `ImageResizeKJv2`
- `ImpactExecutionOrderController`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LTXVSpatioTemporalTiledVAEDecode`
- `LoadImage`
- `PreviewImage`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `SimpleMath+`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 1/2 个有
- `CheckpointLoaderSimple` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `LTXAVTextEncoderLoader` —— 1/2 个有
- `LTXVGemmaCLIPModelLoader` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `LoaderGGUF` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有
- `VAELoaderKJ` —— 1/2 个有
- `easy ckptNames` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 121 | - | 2 | 100% |
| 高度 | 25 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 121，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

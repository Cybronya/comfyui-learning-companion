---
name: unknown_workflow_video_upscale_latent_upscale_15
type: Unknown Workflow
frequency: 16
level: strong
coverage: 0.759875
common_nodes: [CFGGuider, CLIPTextEncode, CR Text, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, GetNode, ImageResizeKJv2, ImageScaleBy, Int, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SetNode, VAEDecode, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2010965829352955906.json, 视频生成/图生视频/2008794813583331330.json, 视频生成/图生视频/2021544395123724290.json, 视频生成/图生视频/2034099708037173249.json, 视频生成/图生视频/2008570907488423937.json, 视频生成/图生视频/2011219169584353282.json, 视频生成/图生视频/2014635832568717313.json, 视频生成/图生视频/2043520285718093826.json, 视频生成/图生视频/2062391374607118337.json, 视频生成/图生视频/2042089030552133633.json, 视频生成/图生视频/2030021580201402370.json, 视频生成/图生视频/2018853440939630593.json, 视频生成/图生视频/2020093034448293890.json, 视频生成/图生视频/2051947423819411458.json, 视频生成/图生视频/2011639184884244481.json, 视频生成/文生视频/【LTX2.3-图_文双模式视频】全自动台词设计_2030494259446554626.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_15

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/2010965829352955906.json、视频生成/图生视频/2008794813583331330.json、视频生成/图生视频/2021544395123724290.json、视频生成/图生视频/2034099708037173249.json、视频生成/图生视频/2008570907488423937.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 16 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CR Text`
- `CheckpointLoaderSimple`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `GetNode`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `Int`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SetNode`
- `VAEDecode`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LTXVCropGuides` —— 15/16 个有
- `LTXVLatentUpsampler` —— 15/16 个有
- `LTXVScheduler` —— 15/16 个有
- `Compare` —— 14/16 个有
- `LayerUtility: PurgeVRAM V2` —— 14/16 个有
- `ManualSigmas` —— 14/16 个有
- `PreviewImage` —— 14/16 个有
- `RHHiddenNodes` —— 14/16 个有
- `Seed_` —— 14/16 个有
- `easy cleanGpuUsed` —— 14/16 个有
- `easy ifElse` —— 14/16 个有
- `LTXVFirstLastFrameControl_TTP` —— 13/16 个有
- `AudioSeparation` —— 11/16 个有
- `HAIGC_TimestampTextReplace` —— 11/16 个有
- `HAIGC_VideoSubtitleTimestampPro` —— 11/16 个有
- `SubtitleOptimizer` —— 11/16 个有
- `TranscribeConfig` —— 11/16 个有
- `VideoTranscribe` —— 11/16 个有
- `easy showAnything` —— 11/16 个有
- `LTXVImgToVideoInplace` —— 7/16 个有
- `BasicScheduler` —— 6/16 个有
- `VAEDecodeTiled` —— 6/16 个有
- `Float` —— 5/16 个有
- `LTXVChunkFeedForward` —— 5/16 个有
- `ModelPatchTorchSettings` —— 5/16 个有
- `PathchSageAttentionKJ` —— 5/16 个有
- `PrimitiveBoolean` —— 5/16 个有
- `DF_Int_to_Float` —— 2/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/16 个有
- `PrimitiveInt` —— 2/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 16 | 100% |
| 高度 | 24 | 24 - 25 | 16 | 99% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，16 个样本，取值集中（一致性 100%）
- 高度 中位数 24，观测区间 24 - 25，16 个样本，取值集中（一致性 99%）

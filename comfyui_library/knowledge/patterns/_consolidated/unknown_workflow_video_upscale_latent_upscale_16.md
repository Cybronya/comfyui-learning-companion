---
name: unknown_workflow_video_upscale_latent_upscale_16
type: Unknown Workflow
frequency: 15
level: strong
coverage: 0.741067
common_nodes: [CFGGuider, CLIPTextEncode, CR Text, CheckpointLoaderSimple, Compare, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, GetNode, ImageResizeKJv2, ImageScaleBy, Int, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, PreviewImage, RHHiddenNodes, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, Seed_, SetNode, VAEDecode, VHS_VideoCombine, easy cleanGpuUsed, easy ifElse]
problems: []
missing: []
members: [数字人/数字人/种草工作流_2080471415094075394.json, 视频生成/图生视频/LTX2.0-首尾帧变身视频_2010965829352955906.json, 视频生成/图生视频/LTX2.3-图_文双模式视频_2034099708037173249.json, 视频生成/图生视频/【LTX2.0-首尾帧视频】全自动（Plus48G）_2008570907488423937.json, 视频生成/图生视频/【LTX2.0-首尾帧视频】全自动（Plus48G）_2011219169584353282.json, 视频生成/图生视频/【LTX2.0-首尾帧视频】全自动（Plus48G）_2014635832568717313.json, 视频生成/图生视频/【LTX2.0-首尾帧视频】全自动（Plus48G）_2043520285718093826.json, 视频生成/图生视频/【LTX2.3-图_文双模式视频】全自动台词探店电商带货首尾帧图生视频文生视频_2062391374607118337.json, 视频生成/图生视频/【LTX2.3-图_文双模式视频】全自动台词设计首尾帧单图可选择_2042089030552133633.json, 视频生成/图生视频/【LTX2.3-首尾帧频】全自动（1.0版本）_2030021580201402370.json, 视频生成/图生视频/【首尾帧视频LTX2.0】自动生成超流畅_2018853440939630593.json, 视频生成/图生视频/全自动首尾帧视频：LTX2.0_2020093034448293890.json, 视频生成/图生视频/双模式视频自动台词设计_2051947423819411458.json, 视频生成/图生视频/超优质LTX2.0-首尾帧视频，速度快，效果好_2011639184884244481.json, 视频生成/文生视频/【LTX2.3-图_文双模式视频】全自动台词设计_2030494259446554626.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_16

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（数字人/数字人/种草工作流_2080471415094075394.json、视频生成/图生视频/LTX2.0-首尾帧变身视频_2010965829352955906.json、视频生成/图生视频/LTX2.3-图_文双模式视频_2034099708037173249.json、视频生成/图生视频/【LTX2.0-首尾帧视频】全自动（Plus48G）_2008570907488423937.json、视频生成/图生视频/【LTX2.0-首尾帧视频】全自动（Plus48G）_2011219169584353282.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 15 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CR Text`
- `CheckpointLoaderSimple`
- `Compare`
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
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `PreviewImage`
- `RHHiddenNodes`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `Seed_`
- `SetNode`
- `VAEDecode`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy ifElse`

**可变部分**（部分 workflow 才有）：
- `LTXVCropGuides` —— 14/15 个有
- `LTXVFirstLastFrameControl_TTP` —— 14/15 个有
- `LTXVLatentUpsampler` —— 14/15 个有
- `LTXVScheduler` —— 14/15 个有
- `ManualSigmas` —— 13/15 个有
- `AudioSeparation` —— 12/15 个有
- `HAIGC_TimestampTextReplace` —— 12/15 个有
- `HAIGC_VideoSubtitleTimestampPro` —— 12/15 个有
- `SubtitleOptimizer` —— 12/15 个有
- `TranscribeConfig` —— 12/15 个有
- `VideoTranscribe` —— 12/15 个有
- `easy showAnything` —— 12/15 个有
- `BasicScheduler` —— 7/15 个有
- `Float` —— 6/15 个有
- `LTXVChunkFeedForward` —— 6/15 个有
- `LTXVImgToVideoInplace` —— 6/15 个有
- `ModelPatchTorchSettings` —— 6/15 个有
- `PathchSageAttentionKJ` —— 6/15 个有
- `PrimitiveBoolean` —— 6/15 个有
- `VAEDecodeTiled` —— 6/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 15 | 100% |
| 高度 | 24 | 24 - 24 | 15 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，15 个样本，取值集中（一致性 100%）
- 高度 中位数 24，观测区间 24 - 24，15 个样本，取值集中（一致性 100%）

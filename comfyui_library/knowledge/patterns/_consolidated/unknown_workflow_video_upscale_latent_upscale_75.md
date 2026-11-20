---
name: unknown_workflow_video_upscale_latent_upscale_75
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9164
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAddGuide, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VAEDecode, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/文生图/LTX-2 3合 1 控制_2073298485385973761.json, 图片生成/文生图/LTX-2 深度控制_2073298287444193281.json, 平台全量/LTX-2 深度控制生成视频_2008817593309732865.json, 平台全量/LTX2.0深度控制生视频（48G使用）_2008460537599889410.json, 视频生成/图生视频/LTX2.0 Depth深度控制生视频_2008779435071246337.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_75

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/LTX-2 3合 1 控制_2073298485385973761.json、图片生成/文生图/LTX-2 深度控制_2073298287444193281.json、平台全量/LTX-2 深度控制生成视频_2008817593309732865.json、平台全量/LTX2.0深度控制生视频（48G使用）_2008460537599889410.json、视频生成/图生视频/LTX2.0 Depth深度控制生视频_2008779435071246337.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageScaleBy`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAddGuide`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 4/5 个有
- `BasicScheduler` —— 4/5 个有
- `DisableNoise` —— 4/5 个有
- `ImageInvert` —— 4/5 个有
- `ImageResizeKJv2` —— 4/5 个有
- `LotusConditioning` —— 4/5 个有
- `SetFirstSigma` —— 4/5 个有
- `UNETLoader` —— 4/5 个有
- `VAEEncode` —— 4/5 个有
- `VAELoader` —— 4/5 个有
- `CreateVideo` —— 3/5 个有
- `SaveVideo` —— 3/5 个有
- `VAEDecodeTiled` —— 3/5 个有
- `PreviewAny` —— 2/5 个有
- `easy cleanGpuUsed` —— 2/5 个有
- `AIO_Preprocessor` —— 1/5 个有
- `CM_FloatToInt` —— 1/5 个有
- `CR String To Combo` —— 1/5 个有
- `ImpactStringSelector` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `SplitStringByDelimiter` —— 1/5 个有
- `VHS_VideoInfo` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 5 | 100% |
| 高度 | 25 | 25 - 25 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，5 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）

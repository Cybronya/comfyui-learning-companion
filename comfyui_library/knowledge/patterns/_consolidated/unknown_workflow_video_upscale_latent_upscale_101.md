---
name: unknown_workflow_video_upscale_latent_upscale_101
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.898
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, GetImageSize, ImageResizeKJv2, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAddGuide, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VAEDecode, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/文生图/LTX-2 3合 1 控制_2073298485385973761.json, 图片生成/文生图/LTX-2 深度控制_2073298287444193281.json, 视频生成/图生视频/2008779435071246337.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_101

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/LTX-2 3合 1 控制_2073298485385973761.json、图片生成/文生图/LTX-2 深度控制_2073298287444193281.json、视频生成/图生视频/2008779435071246337.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageResizeKJv2`
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
- `BasicGuider` —— 2/3 个有
- `BasicScheduler` —— 2/3 个有
- `CreateVideo` —— 2/3 个有
- `DisableNoise` —— 2/3 个有
- `ImageInvert` —— 2/3 个有
- `LotusConditioning` —— 2/3 个有
- `SaveVideo` —— 2/3 个有
- `SetFirstSigma` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `VAEEncode` —— 2/3 个有
- `VAELoader` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `AIO_Preprocessor` —— 1/3 个有
- `CR String To Combo` —— 1/3 个有
- `ImpactStringSelector` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `SplitStringByDelimiter` —— 1/3 个有
- `VAEDecodeTiled` —— 1/3 个有

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

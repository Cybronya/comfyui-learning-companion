---
name: unknown_workflow_upscale_latent_upscale_lora_30
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.901667
common_nodes: [CFGGuider, CLIPTextEncode, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced]
problems: []
missing: []
members: [视频生成/图生视频/2014646400780345345.json, 视频生成/图生视频/2073311336997675009.json, 视频生成/图生视频/2073311138300911617.json, 视频生成/图生视频/2017463595512111106.json, 视频生成/图生视频/2009155672465743874.json, 视频生成/图生视频/2008482127481933826.json, 视频生成/图生视频/2008532910646763522.json, 视频生成/图生视频/2009279040347185153.json, 视频生成/图生视频/2039311541685719041.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_30

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/2014646400780345345.json、视频生成/图生视频/2073311336997675009.json、视频生成/图生视频/2073311138300911617.json、视频生成/图生视频/2017463595512111106.json、视频生成/图生视频/2009155672465743874.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageScaleBy`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 8/9 个有
- `LTXAVTextEncoderLoader` —— 8/9 个有
- `LTXVAudioVAELoader` —— 8/9 个有
- `LTXVScheduler` —— 8/9 个有
- `CreateVideo` —— 6/9 个有
- `LTXVAudioVAEDecode` —— 6/9 个有
- `LTXVEmptyLatentAudio` —— 6/9 个有
- `SaveVideo` —— 6/9 个有
- `VAEDecode` —— 5/9 个有
- `ImageResizeKJv2` —— 4/9 个有
- `LTXVAudioVAEEncode` —— 4/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/9 个有
- `LoadAudio` —— 4/9 个有
- `MelBandRoFormerModelLoader` —— 4/9 个有
- `MelBandRoFormerSampler` —— 4/9 个有
- `SetLatentNoiseMask` —— 4/9 个有
- `SolidMask` —— 4/9 个有
- `TrimAudioDuration` —— 4/9 个有
- `VAEDecodeTiled` —— 4/9 个有
- `VHS_VideoCombine` —— 3/9 个有
- `easy cleanGpuUsed` —— 3/9 个有
- `LayerUtility: PurgeVRAM V2` —— 2/9 个有
- `PreviewAudio` —— 2/9 个有
- `PrimitiveFloat` —— 2/9 个有
- `DualCLIPLoaderGGUF` —— 1/9 个有
- `GetNode` —— 1/9 个有
- `LTX2SamplingPreviewOverride` —— 1/9 个有
- `LTX2_NAG` —— 1/9 个有
- `LTXVSetAudioVideoMaskByTime` —— 1/9 个有
- `PrimitiveBoolean` —— 1/9 个有
- `ResizeImageMaskNode` —— 1/9 个有
- `SaveImage` —— 1/9 个有
- `SimpleCalculatorKJ` —— 1/9 个有
- `TextGenerateLTX2Prompt` —— 1/9 个有
- `UnetLoaderGGUF` —— 1/9 个有
- `VAELoader` —— 1/9 个有
- `VAELoaderKJ` —— 1/9 个有
- `VRAM_Debug` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 6 | 100% |
| 高度 | 25 | 25 - 25 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，6 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，6 个样本，取值集中（一致性 100%）

---
name: unknown_workflow_video_lora_sampler_971
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.517
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoader, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, INTConstant, ImageResizeKJv2, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEDecode, LTXVAudioVideoMask, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SetNode, SimpleCalculatorKJ, UNETLoader, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [平台全量/LTX-2.3_-_V2V_Foley视频增加音频_2036327671340208130.json, 音频生成/音频生成/LTX-2.3视频增加音频及时长_2046161682556264450.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_971

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/LTX-2.3_-_V2V_Foley视频增加音频_2036327671340208130.json、音频生成/音频生成/LTX-2.3视频增加音频及时长_2046161682556264450.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：52%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVAudioVideoMask`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `SimpleCalculatorKJ`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoaderGGUF` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `LTXVChunkFeedForward` —— 1/2 个有
- `LTXVImgToVideoInplace` —— 1/2 个有
- `LTXVLatentUpsampler` —— 1/2 个有
- `LTXVLoopingSampler` —— 1/2 个有
- `LTXVPreprocess` —— 1/2 个有
- `LTXVScheduler` —— 1/2 个有
- `LatentUpscaleBy` —— 1/2 个有
- `LatentUpscaleModelLoader` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `ToInt` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有
- `VAEEncode` —— 1/2 个有
- `VAEEncodeTiled` —— 1/2 个有
- `VRAM_Debug` —— 1/2 个有

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

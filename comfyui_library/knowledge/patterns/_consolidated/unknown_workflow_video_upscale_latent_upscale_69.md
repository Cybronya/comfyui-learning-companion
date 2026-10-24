---
name: unknown_workflow_video_upscale_latent_upscale_69
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.5216
common_nodes: [CFGGuider, CLIPTextEncode, CR Float To Integer, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, GetNode, ImageResizeKJv2, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LTXVSpatioTemporalTiledVAEDecode, LatentUpscaleModelLoader, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, PreviewImage, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SetNode, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/LTX-2 I2V - With VBVR （图生视频）音画同步视频生成高级工作流_2044073301101776898.json, 视频生成/图生视频/LTX-2.3 (自定义音频输入) 拆分子图版图生视频-高级工作流_2088577329542033409.json, 视频生成/图生视频/LTX-2.3 自定义音频 拆分子图版图生视频-高级工作流_2088612314143617026.json, 视频生成/文生视频/LTX-2_3 I2V (自定义音频输入) 拆分子图版-高级工作流_2031360924904333314.json, 视频生成/文生视频/LTX-2_3 I2V ID-Lora Vs No Lora创建一致的 AI 角色语音_2037139782387638274.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_69

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/LTX-2 I2V - With VBVR （图生视频）音画同步视频生成高级工作流_2044073301101776898.json、视频生成/图生视频/LTX-2.3 (自定义音频输入) 拆分子图版图生视频-高级工作流_2088577329542033409.json、视频生成/图生视频/LTX-2.3 自定义音频 拆分子图版图生视频-高级工作流_2088612314143617026.json、视频生成/文生视频/LTX-2_3 I2V (自定义音频输入) 拆分子图版-高级工作流_2031360924904333314.json、视频生成/文生视频/LTX-2_3 I2V ID-Lora Vs No Lora创建一致的 AI 角色语音_2037139782387638274.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：52%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CR Float To Integer`
- `CheckpointLoaderSimple`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `GetNode`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LTXVSpatioTemporalTiledVAEDecode`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PreviewImage`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SetNode`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LTXVAudioVAEEncode` —— 4/5 个有
- `LTXVAudioVAELoader` —— 4/5 个有
- `LTXVScheduler` —— 4/5 个有
- `MathExpression|pysssss` —— 4/5 个有
- `MelBandRoFormerModelLoader` —— 4/5 个有
- `MelBandRoFormerSampler` —— 4/5 个有
- `SetLatentNoiseMask` —— 4/5 个有
- `ShowText|pysssss` —— 4/5 个有
- `SolidMask` —— 4/5 个有
- `StringReplace` —— 4/5 个有
- `TextGenerateLTX2Prompt` —— 4/5 个有
- `TrimAudioDuration` —— 4/5 个有
- `Audio Duration (mtb)` —— 3/5 个有
- `Qwen3ASRLoader` —— 3/5 个有
- `Qwen3ASRTranscribe` —— 3/5 个有
- `VAELoader` —— 2/5 个有
- `easy cleanGpuUsed` —— 2/5 个有
- `easy clearCacheAll` —— 2/5 个有
- `Audio To Text (mtb)` —— 1/5 个有
- `AudioAdjustVolume` —— 1/5 个有
- `BasicScheduler` —— 1/5 个有
- `CreateVideo` —— 1/5 个有
- `JoinStringMulti` —— 1/5 个有
- `LTXVReferenceAudio` —— 1/5 个有
- `Load Whisper (mtb)` —— 1/5 个有
- `RIFE VFI` —— 1/5 个有
- `RTXVideoSuperResolution` —— 1/5 个有
- `SaveVideo` —— 1/5 个有
- `SimpleMath+` —— 1/5 个有
- `VAELoaderKJ` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 121 | 121 - 121 | 5 | 100% |
| 高度 | 25 | 25 - 25 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 121，观测区间 121 - 121，5 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）

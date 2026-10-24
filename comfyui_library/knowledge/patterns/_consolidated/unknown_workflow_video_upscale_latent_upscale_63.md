---
name: unknown_workflow_video_upscale_latent_upscale_63
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.672
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, RandomNoise, SamplerCustomAdvanced, VAEDecode, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3 Sulphur Multi Frame 多帧生成视频_2075062217422229506.json, 视频生成/图生视频/LTX2.3 Sulphur 导演版_2075055600450494465.json, 视频生成/图生视频/LTX2.3+PromptRelay-多镜头分镜控制+逻辑控制+长视频+无字幕版图生视频_2058811131501830146.json, 视频生成/图生视频/LTX2.3-PromptRelay-V2-多镜头分镜控制+逻辑控制+长视频+无字幕版图生视频_2058206526581600258.json, 视频生成/图生视频/【LTX2.3+PromptRelay-V2】-多镜头分镜控制+逻辑控制+长视频+无字幕版图生视频_2058353151778058241.json, 视频生成/文生视频/LTX2.3 Sulphur TI2V 文生图生视频_2075062888326324225.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_63

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/LTX2.3 Sulphur Multi Frame 多帧生成视频_2075062217422229506.json、视频生成/图生视频/LTX2.3 Sulphur 导演版_2075055600450494465.json、视频生成/图生视频/LTX2.3+PromptRelay-多镜头分镜控制+逻辑控制+长视频+无字幕版图生视频_2058811131501830146.json、视频生成/图生视频/LTX2.3-PromptRelay-V2-多镜头分镜控制+逻辑控制+长视频+无字幕版图生视频_2058206526581600258.json、视频生成/图生视频/【LTX2.3+PromptRelay-V2】-多镜头分镜控制+逻辑控制+长视频+无字幕版图生视频_2058353151778058241.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `EmptyLTXVLatentVideo` —— 5/6 个有
- `Fast Groups Bypasser (rgthree)` —— 5/6 个有
- `LTXVEmptyLatentAudio` —— 5/6 个有
- `PromptRelayEncodeTimeline` —— 5/6 个有
- `GetImageSize` —— 4/6 个有
- `GetNode` —— 4/6 个有
- `ImageResizeKJv2` —— 4/6 个有
- `ImageScaleBy` —— 4/6 个有
- `LTXVChunkFeedForward` —— 4/6 个有
- `LTXVImgToVideoInplace` —— 4/6 个有
- `LTXVScheduler` —— 4/6 个有
- `SetNode` —— 4/6 个有
- `SimpleMath+` —— 4/6 个有
- `LTXVPreprocess` —— 3/6 个有
- `SaveImage` —— 3/6 个有
- `easy int` —— 3/6 个有
- `PrimitiveFloat` —— 2/6 个有
- `PrimitiveInt` —— 2/6 个有
- `easy showAnything` —— 2/6 个有
- `AudioCrop` —— 1/6 个有
- `LTXDirector` —— 1/6 个有
- `LTXDirectorGuide` —— 1/6 个有
- `LTXVAddGuideMulti` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `LoadAudio` —— 1/6 个有
- `MathExpression|pysssss` —— 1/6 个有
- `PreviewAudio` —— 1/6 个有
- `PrimitiveBoolean` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 481 | 5 | 25% |
| 高度 | 24 | 24 - 24 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 481，5 个样本，取值分散，一致性仅 25%
- 高度 中位数 24，观测区间 24 - 24，5 个样本，取值集中（一致性 100%）

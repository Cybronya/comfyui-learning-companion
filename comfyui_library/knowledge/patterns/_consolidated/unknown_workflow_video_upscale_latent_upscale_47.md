---
name: unknown_workflow_video_upscale_latent_upscale_47
type: Unknown Workflow
frequency: 8
level: weak
coverage: 0.492625
common_nodes: [CFGGuider, CLIPTextEncode, EmptyLTXVLatentVideo, GetNode, INTConstant, KSamplerSelect, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, PrimitiveFloat, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/LTX 2.3双人分镜视频生成_2059165088854138882.json, 视频生成/图生视频/LTX-2.3-图生视频_2055514596210946049.json, 视频生成/图生视频/LTX-2.3-首尾帧_2055556105299873793.json, 视频生成/图生视频/LTX-2.3_-_I2V_Short-Story_PromptRelay四图视频制作_2050871854566518786.json, 视频生成/图生视频/LTX-2.3首尾帧+语音数字人_2036654957595725826.json, 视频生成/图生视频/LTX-2一键稳定生成数字人制作表情口型同步视频对口型对嘴型音频图片生成数字人视频_2014350317235736578.json, 视频生成/图生视频/LTX-2图生视频：上传歌曲MP3，一键生成MV音乐视频！_2013887364019527681.json, 视频生成/文生视频/Ltx-2蒸馏对口型_2018224320958439425.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_47

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/LTX 2.3双人分镜视频生成_2059165088854138882.json、视频生成/图生视频/LTX-2.3-图生视频_2055514596210946049.json、视频生成/图生视频/LTX-2.3-首尾帧_2055556105299873793.json、视频生成/图生视频/LTX-2.3_-_I2V_Short-Story_PromptRelay四图视频制作_2050871854566518786.json、视频生成/图生视频/LTX-2.3首尾帧+语音数字人_2036654957595725826.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：49%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `INTConstant`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `ManualSigmas`
- `PrimitiveFloat`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 7/8 个有
- `ImageResizeKJv2` —— 7/8 个有
- `LTXVImgToVideoInplace` —— 7/8 个有
- `LoraLoaderModelOnly` —— 7/8 个有
- `DualCLIPLoader` —— 6/8 个有
- `SimpleCalculatorKJ` —— 6/8 个有
- `LTX2_NAG` —— 5/8 个有
- `ImageScaleBy` —— 4/8 个有
- `LTX2SamplingPreviewOverride` —— 4/8 个有
- `LTXVAudioVAEEncode` —— 4/8 个有
- `LoadAudio` —— 4/8 个有
- `MelBandRoFormerModelLoader` —— 4/8 个有
- `MelBandRoFormerSampler` —— 4/8 个有
- `PathchSageAttentionKJ` —— 4/8 个有
- `ResizeImageMaskNode` —— 4/8 个有
- `SetLatentNoiseMask` —— 4/8 个有
- `SimpleMath+` —— 4/8 个有
- `SolidMask` —— 4/8 个有
- `TrimAudioDuration` —— 4/8 个有
- `ComfySwitchNode` —— 3/8 个有
- `DualCLIPLoaderGGUF` —— 3/8 个有
- `UnetLoaderGGUF` —— 3/8 个有
- `Fast Groups Bypasser (rgthree)` —— 2/8 个有
- `ImageConcatMulti` —— 2/8 个有
- `LTX2AudioLatentNormalizingSampling` —— 2/8 个有
- `LTXVImgToVideoInplaceKJ` —— 2/8 个有
- `PromptRelayEncodeTimeline` —— 2/8 个有
- `Audio Duration (mtb)` —— 1/8 个有
- `AudioInfo` —— 1/8 个有
- `ComfyMathExpression` —— 1/8 个有
- `Context (rgthree)` —— 1/8 个有
- `Context Switch (rgthree)` —— 1/8 个有
- `JWFloatToInteger` —— 1/8 个有
- `LTX2AttentionTunerPatch` —— 1/8 个有
- `LTX2MemoryEfficientSageAttentionPatch` —— 1/8 个有
- `LTXVAddGuideMulti` —— 1/8 个有
- `LTXVCropGuides` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `ModelPatchTorchSettings` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 121 | 97 - 721 | 8 | 4% |
| 高度 | 25 | 24 - 25 | 8 | 99% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 121，观测区间 97 - 721，8 个样本，取值分散，一致性仅 4%
- 高度 中位数 25，观测区间 24 - 25，8 个样本，取值集中（一致性 99%）

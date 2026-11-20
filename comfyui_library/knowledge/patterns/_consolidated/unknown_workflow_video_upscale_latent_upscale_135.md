---
name: unknown_workflow_video_upscale_latent_upscale_135
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.564
common_nodes: [AudioAdjustVolume, CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, EmptyLTXVLatentVideo, Fast Groups Bypasser (rgthree), GetImageSize, GetNode, ImageResizeKJv2, ImageScaleBy, KSamplerSelect, LTX2LoraLoaderAdvanced, LTX2SamplingPreviewOverride, LTXAVTextEncoderLoader, LTXLatentAnchorAware, LTXTextAttentionAmplifier, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplaceKJ, LTXVLatentUpsamplerTiled, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, PreviewAudio, PreviewImage, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, STGGuiderAdvanced, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, Sigmas Easing, SolidMask, VAEDecode, VAELoaderKJ, VHS_VideoCombine, easy float, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/LTX2.3 Eros 口播数字人-首尾帧相同-V1.3_2082491190057988097.json, "视频生成/图生视频/LTX2.3 Eros 锚点视频生成 （MV, 数字人，脱口秀）_2075060521405083649.json"]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_135

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/LTX2.3 Eros 口播数字人-首尾帧相同-V1.3_2082491190057988097.json、视频生成/图生视频/LTX2.3 Eros 锚点视频生成 （MV, 数字人，脱口秀）_2075060521405083649.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：56%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioAdjustVolume`
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `GetNode`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `KSamplerSelect`
- `LTX2LoraLoaderAdvanced`
- `LTX2SamplingPreviewOverride`
- `LTXAVTextEncoderLoader`
- `LTXLatentAnchorAware`
- `LTXTextAttentionAmplifier`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplaceKJ`
- `LTXVLatentUpsamplerTiled`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PreviewAudio`
- `PreviewImage`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `STGGuiderAdvanced`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `Sigmas Easing`
- `SolidMask`
- `VAEDecode`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy float`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 1/2 个有
- `Apply Whisper` —— 1/2 个有
- `AudioCrop` —— 1/2 个有
- `GroupSwitcher` —— 1/2 个有
- `ImageFromBatch` —— 1/2 个有
- `JWStringToFloat` —— 1/2 个有
- `LTXVAddGuide` —— 1/2 个有
- `LTXVAudioVideoMask` —— 1/2 个有
- `LTXVLatentUpsampler` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `PainterAudioLength` —— 1/2 个有
- `Qwen3TTSModelLoader` —— 1/2 个有
- `Qwen3TTSVoiceClone` —— 1/2 个有
- `RTXVideoSuperResolution` —— 1/2 个有
- `SaveAudioAdvanced` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `SoundFlow_GetLength` —— 1/2 个有
- `TrimAudioDuration` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1 | - | 2 | 100% |
| 高度 | 24 | - | 2 | 100% |
| LoRA 模型强度 | 0.79 | - | 2 | 73% |
| LoRA 文本强度 | 0.5 | - | 2 | 0% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 24，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.79，样本不足，未给区间，2 个样本
- LoRA 文本强度 中位数 0.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 0%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

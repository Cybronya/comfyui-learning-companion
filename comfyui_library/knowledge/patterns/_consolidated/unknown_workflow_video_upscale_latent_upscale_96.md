---
name: unknown_workflow_video_upscale_latent_upscale_96
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.91175
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveBoolean, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SolidMask, TrimAudioDuration, VAEDecodeTiled, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/ltx2.3最接近即梦SD2的版本_2044674035950297090.json, 视频生成/图生视频/图生视频_2046040872004886529.json, 视频生成/图生视频/图生视频ltx_2045162483312234497.json, 视频生成/文生视频/LTX2.3 - 多功能可独立音频数字人_2047017723305140225.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_96

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/ltx2.3最接近即梦SD2的版本_2044674035950297090.json、视频生成/图生视频/图生视频_2046040872004886529.json、视频生成/图生视频/图生视频ltx_2045162483312234497.json、视频生成/文生视频/LTX2.3 - 多功能可独立音频数字人_2047017723305140225.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SolidMask`
- `TrimAudioDuration`
- `VAEDecodeTiled`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LTX2_NAG` —— 3/4 个有
- `LTXVChunkFeedForward` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `PathchSageAttentionKJ` —— 3/4 个有
- `PrimitiveFloat` —— 3/4 个有
- `Switch any [Crystools]` —— 3/4 个有
- `CR Text` —— 2/4 个有
- `Any Switch (rgthree)` —— 1/4 个有
- `AudioCrop` —— 1/4 个有
- `CM_IntToFloat` —— 1/4 个有
- `CreateVideo` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `LTXVPreprocess` —— 1/4 个有
- `PreviewAudio` —— 1/4 个有
- `QWEN_TextDisplay` —— 1/4 个有
- `RH_Captioner` —— 1/4 个有
- `ResizeImagesByLongerEdge` —— 1/4 个有
- `SimpleMath+` —— 1/4 个有
- `Text Find and Replace` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 4 | 100% |
| 高度 | 25 | 25 - 25 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，4 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）

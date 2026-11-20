---
name: unknown_workflow_video_upscale_latent_upscale_126
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.621
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, ImageResizeKJv2, KSamplerSelect, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, ManualSigmas, PreviewImage, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/LTXv2.3音频加载+图片加载=生成完美一致性数字人_2031753479793942530.json, 视频生成/图生视频/video_ltx2_3_i2v_kijai_three_stage_2039715377143353346.json, 视频生成/图生视频/video_ltx2_3_i2v_kijai_three_stage_2041087454286979073.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_126

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/LTXv2.3音频加载+图片加载=生成完美一致性数字人_2031753479793942530.json、视频生成/图生视频/video_ltx2_3_i2v_kijai_three_stage_2039715377143353346.json、视频生成/图生视频/video_ltx2_3_i2v_kijai_three_stage_2041087454286979073.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：62%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `ManualSigmas`
- `PreviewImage`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LTXVAudioVAEDecode` —— 2/3 个有
- `LTXVEmptyLatentAudio` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `LoraLoader` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `ResizeImagesByLongerEdge` —— 2/3 个有
- `CM_FloatToInt` —— 1/3 个有
- `LTX2_NAG` —— 1/3 个有
- `LTXVAudioVAEEncode` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有
- `PreviewAudio` —— 1/3 个有
- `PrimitiveBoolean` —— 1/3 个有
- `SDVN Load Image Url` —— 1/3 个有
- `SetLatentNoiseMask` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有
- `SolidMask` —— 1/3 个有
- `String` —— 1/3 个有
- `VHS_LoadAudioUpload` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | - | 2 | 100% |
| 高度 | 25 | - | 2 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）

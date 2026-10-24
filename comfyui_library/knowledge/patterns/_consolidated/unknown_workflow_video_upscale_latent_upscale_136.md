---
name: unknown_workflow_video_upscale_latent_upscale_136
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.878
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/LTX-2.5-I2V+双采样加速视频生成_2096206827863232514.json, 视频生成/图生视频/LTX2.5图生视频_2087770942218006530.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_136

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/LTX-2.5-I2V+双采样加速视频生成_2096206827863232514.json、视频生成/图生视频/LTX2.5图生视频_2087770942218006530.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CFGGuider` —— 1/2 个有
- `CR Prompt Text` —— 1/2 个有
- `EmptyImage` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `ImageScaleBy` —— 1/2 个有
- `LTXVCropGuides` —— 1/2 个有
- `LTXVDualCFGGuider` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `ModelAttentionBackend` —— 1/2 个有
- `PrimitiveBoolean` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `ResolutionSelector` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

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

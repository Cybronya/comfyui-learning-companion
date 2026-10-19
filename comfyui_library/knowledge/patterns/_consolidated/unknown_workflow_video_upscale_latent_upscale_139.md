---
name: unknown_workflow_video_upscale_latent_upscale_139
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.461
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, ImageResizeKJv2, KSamplerSelect, LTXFaceDetector, LTXLatentAnchorAware, LTXLikenessAnchor, LTXLikenessGuide, LTXTiledSampler, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplaceKJ, LTXVLatentUpsamplerTiled, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, PrimitiveBoolean, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, ResizeImageMaskNode, STGGuiderAdvanced, SamplerCustomAdvanced, SetNode, Sigmas Easing, UNETLoader, VAEDecode, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2074509736741003266.json, 视频生成/图生视频/2076879552093179906.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_139

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2074509736741003266.json、视频生成/图生视频/2076879552093179906.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：46%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXFaceDetector`
- `LTXLatentAnchorAware`
- `LTXLikenessAnchor`
- `LTXLikenessGuide`
- `LTXTiledSampler`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplaceKJ`
- `LTXVLatentUpsamplerTiled`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `ManualSigmas`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResizeImageMaskNode`
- `STGGuiderAdvanced`
- `SamplerCustomAdvanced`
- `SetNode`
- `Sigmas Easing`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`

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

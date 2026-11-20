---
name: unknown_workflow_video_upscale_latent_upscale_80
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8456
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/LTX-2.5-I2V+双采样加速视频生成_2096206827863232514.json, 视频生成/图生视频/LTX2.5图生视频_2087770942218006530.json, 视频生成/图生视频/LTX2.5图生视频一致性加强版V1_2087536517580414978.json, 视频生成/图生视频/LTX2.5图生视频（标准版工作流）_2087460376823820290.json, 视频生成/文生视频/LTX2.5图生视频（默认工作流）_2088281770851651585.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_80

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/LTX-2.5-I2V+双采样加速视频生成_2096206827863232514.json、视频生成/图生视频/LTX2.5图生视频_2087770942218006530.json、视频生成/图生视频/LTX2.5图生视频一致性加强版V1_2087536517580414978.json、视频生成/图生视频/LTX2.5图生视频（标准版工作流）_2087460376823820290.json、视频生成/文生视频/LTX2.5图生视频（默认工作流）_2088281770851651585.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
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
- `LTXVDualCFGGuider` —— 4/5 个有
- `PrimitiveBoolean` —— 4/5 个有
- `ResolutionSelector` —— 4/5 个有
- `CR Text` —— 3/5 个有
- `PreviewAny` —— 3/5 个有
- `RH_LLMAPI_Pro_Node` —— 3/5 个有
- `ResizeImageMaskNode` —— 3/5 个有
- `CFGGuider` —— 1/5 个有
- `CR Prompt Text` —— 1/5 个有
- `EmptyImage` —— 1/5 个有
- `GetImageSize` —— 1/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `ImageScaleBy` —— 1/5 个有
- `LTXVCropGuides` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `ModelAttentionBackend` —— 1/5 个有
- `PrimitiveFloat` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 5 | 100% |
| 高度 | 25 | 25 - 25 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，5 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）

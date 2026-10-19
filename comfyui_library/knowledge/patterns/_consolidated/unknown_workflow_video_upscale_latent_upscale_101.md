---
name: unknown_workflow_video_upscale_latent_upscale_101
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.637
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSize, ImageResizeKJv2, KSamplerSelect, LTX2_NAG, LTXFaceDetector, LTXLatentAnchorAware, LTXLikenessAnchor, LTXLikenessGuide, LTXTiledSampler, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplaceKJ, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PathchSageAttentionKJ, RandomNoise, ResizeImageMaskNode, STGGuiderAdvanced, SamplerCustomAdvanced, Seed (rgthree), UNETLoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2058875396149571585.json, 视频生成/图生视频/2060544603413106689.json, 视频生成/图生视频/9.LTX2.3 图生视频_2083566011248365570.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_101

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2058875396149571585.json、视频生成/图生视频/2060544603413106689.json、视频生成/图生视频/9.LTX2.3 图生视频_2083566011248365570.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：64%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTX2_NAG`
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
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `ResizeImageMaskNode`
- `STGGuiderAdvanced`
- `SamplerCustomAdvanced`
- `Seed (rgthree)`
- `UNETLoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `AudioAdjustVolume` —— 2/3 个有
- `ComfyMathExpression` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `JWInteger` —— 2/3 个有
- `LTXVLatentUpsamplerTiled` —— 2/3 个有
- `PrimitiveFloat` —— 2/3 个有
- `RTXVideoSuperResolution` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `Sigmas Easing` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `VAEDecode` —— 2/3 个有
- `VAELoaderKJ` —— 2/3 个有
- `BasicScheduler` —— 1/3 个有
- `LTXVChunkFeedForward` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `ModelPatchTorchSettings` —— 1/3 个有
- `ModelSamplingSD3` —— 1/3 个有
- `PromptRelaySmartEncode` —— 1/3 个有
- `VAELoader` —— 1/3 个有
- `XB_ROCmVAEDecodeTemporal` —— 1/3 个有
- `XB_VideoParamsMaster` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1 | 1 - 1 | 3 | 100% |
| 高度 | 24 | 24 - 24 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高度 中位数 24，观测区间 24 - 24，3 个样本，取值集中（一致性 100%）

---
name: unknown_workflow_video_upscale_latent_upscale_65
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.868
common_nodes: [CFGGuider, CLIPTextEncode, ComfySwitchNode, DualCLIPLoader, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageResizeKJv2, ImageScaleBy, ImageScaleToTotalPixels, JoinStrings, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveBoolean, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, ResizeImagesByLongerEdge, ResolutionSelector, SamplerCustomAdvanced, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VAELoaderKJ, VHS_VideoCombine, easy int]
problems: []
missing: []
members: [视频生成/图生视频/2077715453979484162.json, 视频生成/图生视频/2068937173436551170.json, 视频生成/图生视频/2072223946312867841.json, 视频生成/图生视频/2077284348637835265.json, 视频生成/图生视频/2081980799116730369.json, 视频生成/文生视频/LTX2.3 AI动漫 短剧文图生视频_2077737653902077953.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_65

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2077715453979484162.json、视频生成/图生视频/2068937173436551170.json、视频生成/图生视频/2072223946312867841.json、视频生成/图生视频/2077284348637835265.json、视频生成/图生视频/2081980799116730369.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `DualCLIPLoader`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `JoinStrings`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy int`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 6 | 100% |
| 高度 | 25 | 25 - 25 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，6 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，6 个样本，取值集中（一致性 100%）

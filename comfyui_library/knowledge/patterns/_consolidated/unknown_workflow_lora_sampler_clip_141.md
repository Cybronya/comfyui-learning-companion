---
name: unknown_workflow_lora_sampler_clip_141
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9035
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, CannyEdgePreprocessor, DWPreprocessor, DepthCrafter, DownloadAndLoadDepthCrafterModel, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSize, ImageResizeKJv2, KSamplerSelect, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SimpleMath+, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_LoadVideo]
problems: []
missing: []
members: [视频生成/图生视频/2037918767392493570.json, 视频生成/文生视频/Ltx-2.3 IC LoRA Union 视频控制_2032312720623669250.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_141

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2037918767392493570.json、视频生成/文生视频/Ltx-2.3 IC LoRA Union 视频控制_2032312720623669250.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CannyEdgePreprocessor`
- `DWPreprocessor`
- `DepthCrafter`
- `DownloadAndLoadDepthCrafterModel`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SimpleMath+`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_LoadVideo`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 1/2 个有
- `ImpactExecutionOrderController` —— 1/2 个有
- `LTXVAudioVAEDecode` —— 1/2 个有
- `LTXVImgToVideoConditionOnly` —— 1/2 个有
- `LTXVImgToVideoInplace` —— 1/2 个有
- `LTXVLatentUpsampler` —— 1/2 个有
- `LTXVScheduler` —— 1/2 个有
- `LatentUpscaleModelLoader` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `PrimitiveBoolean` —— 1/2 个有
- `ResizeImageMaskNode` —— 1/2 个有
- `SaveVideo` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有
- `VHS_VideoCombine` —— 1/2 个有
- `VHS_VideoInfo` —— 1/2 个有
- `VHS_VideoInfoLoaded` —— 1/2 个有
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

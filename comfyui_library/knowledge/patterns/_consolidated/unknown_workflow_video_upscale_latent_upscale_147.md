---
name: unknown_workflow_video_upscale_latent_upscale_147
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.77
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyFlux2LatentImage, EmptyLTXVLatentVideo, Fast Groups Bypasser (rgthree), Flux2Scheduler, GetImageSize, GetNode, INTConstant, ImageFromBatch, ImageResizeKJv2, Int, KSamplerSelect, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoraLoaderModelOnly, ManualSigmas, PreviewImage, PrimitiveBoolean, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SetNode, SimpleMath+, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, VAELoaderKJ, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, easy cleanGpuUsed]
problems: []
missing: []
members: [平台全量/LTX-2.3_ICLoRA_cameraman_v2-3D草图生成视频_2078240780807925761.json, 视频生成/图生视频/LTX-2.3_ICLoRA_cameraman_v2模型草图控制生成视频_2077646945077776386.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_147

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/LTX-2.3_ICLoRA_cameraman_v2-3D草图生成视频_2078240780807925761.json、视频生成/图生视频/LTX-2.3_ICLoRA_cameraman_v2模型草图控制生成视频_2077646945077776386.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyFlux2LatentImage`
- `EmptyLTXVLatentVideo`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `GetImageSize`
- `GetNode`
- `INTConstant`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `Int`
- `KSamplerSelect`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PreviewImage`
- `PrimitiveBoolean`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `MultiTextConcatenate` —— 1/2 个有

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

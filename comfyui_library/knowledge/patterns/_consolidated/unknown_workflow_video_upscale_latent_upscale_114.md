---
name: unknown_workflow_video_upscale_latent_upscale_114
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.948
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, CannyEdgePreprocessor, CheckpointLoaderSimple, CreateVideo, DWPreprocessor, DepthCrafter, DownloadAndLoadDepthCrafterModel, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSize, ImageResizeKJv2, KSamplerSelect, LTX2_NAG, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PreviewImage, PrimitiveBoolean, RandomNoise, SamplerCustomAdvanced, SaveVideo, SimpleMath+, UNETLoader, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, VRAMReserver, easy showAnything]
problems: []
missing: []
members: [视频生成/文生视频/LTX 2.3 视频控制高清增强_2040812593555709953.json, 视频生成/文生视频/LTX 2.3 音频驱动参考角色伪替换工作流_2040718940661354497.json, 视频生成/文生视频/LTX2.3 3.5套件｜一键控片·三阶渲染·视频生成_2068580767306964993.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_114

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/LTX 2.3 视频控制高清增强_2040812593555709953.json、视频生成/文生视频/LTX 2.3 音频驱动参考角色伪替换工作流_2040718940661354497.json、视频生成/文生视频/LTX2.3 3.5套件｜一键控片·三阶渲染·视频生成_2068580767306964993.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CannyEdgePreprocessor`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `DWPreprocessor`
- `DepthCrafter`
- `DownloadAndLoadDepthCrafterModel`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXAVTextEncoderLoader`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PreviewImage`
- `PrimitiveBoolean`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `VRAMReserver`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM V2` —— 2/3 个有
- `SDPoseOODLoader` —— 2/3 个有
- `SDPoseOODProcessor` —— 2/3 个有
- `Audio Duration (mtb)` —— 1/3 个有
- `DisTorchPurgeVRAMV2` —— 1/3 个有
- `Float to Int` —— 1/3 个有
- `GetLatentSizeAndCount` —— 1/3 个有
- `LTXFaceDetector` —— 1/3 个有
- `LTXLatentAnchorAware` —— 1/3 个有
- `LTXLikenessAnchor` —— 1/3 个有
- `LTXLikenessGuide` —— 1/3 个有
- `LTXVAudioVAEEncode` —— 1/3 个有
- `LoadAudio` —— 1/3 个有
- `MelBandRoFormerModelLoader` —— 1/3 个有
- `MelBandRoFormerSampler` —— 1/3 个有
- `PrimitiveFloat` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `SetLatentNoiseMask` —— 1/3 个有
- `SimpleCalculatorKJ` —— 1/3 个有
- `SolidMask` —— 1/3 个有
- `TrimAudioDuration` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 3 | 100% |
| 高度 | 25 | 24 - 25 | 3 | 98% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，3 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 24 - 25，3 个样本，取值集中（一致性 98%）

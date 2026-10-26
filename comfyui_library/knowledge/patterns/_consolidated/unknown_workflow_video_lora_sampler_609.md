---
name: unknown_workflow_video_lora_sampler_609
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.95525
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, CannyEdgePreprocessor, CheckpointLoaderSimple, CreateVideo, DWPreprocessor, DepthCrafter, DownloadAndLoadDepthCrafterModel, EmptyLTXVLatentVideo, GetImageSize, KSamplerSelect, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveBoolean, RandomNoise, SamplerCustomAdvanced, SaveVideo, SimpleMath+, VAEDecodeTiled, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded]
problems: []
missing: []
members: [视频生成/文生视频/LTX 2.3 IC-LoRA 视频上色工作流（手动提示）_2035643489333022722.json, 视频生成/文生视频/LTX 2.3 视频控制高清增强_2040812593555709953.json, 视频生成/文生视频/LTX 2.3 音频驱动参考角色伪替换工作流_2040718940661354497.json, 视频生成/文生视频/LTX2.3 3.5套件｜一键控片·三阶渲染·视频生成_2068580767306964993.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_609

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/LTX 2.3 IC-LoRA 视频上色工作流（手动提示）_2035643489333022722.json、视频生成/文生视频/LTX 2.3 视频控制高清增强_2040812593555709953.json、视频生成/文生视频/LTX 2.3 音频驱动参考角色伪替换工作流_2040718940661354497.json、视频生成/文生视频/LTX2.3 3.5套件｜一键控片·三阶渲染·视频生成_2068580767306964993.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CannyEdgePreprocessor`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `DWPreprocessor`
- `DepthCrafter`
- `DownloadAndLoadDepthCrafterModel`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `KSamplerSelect`
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
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveBoolean`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SimpleMath+`
- `VAEDecodeTiled`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 3/4 个有
- `ImageResizeKJv2` —— 3/4 个有
- `LTX2_NAG` —— 3/4 个有
- `LTXVLatentUpsampler` —— 3/4 个有
- `LatentUpscaleModelLoader` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `UNETLoader` —— 3/4 个有
- `VAELoader` —— 3/4 个有
- `VAELoaderKJ` —— 3/4 个有
- `VRAMReserver` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `LayerUtility: PurgeVRAM V2` —— 2/4 个有
- `SDPoseOODLoader` —— 2/4 个有
- `SDPoseOODProcessor` —— 2/4 个有
- `Audio Duration (mtb)` —— 1/4 个有
- `DisTorchPurgeVRAMV2` —— 1/4 个有
- `Float to Int` —— 1/4 个有
- `GemmaAPITextEncode` —— 1/4 个有
- `GetLatentSizeAndCount` —— 1/4 个有
- `Image_Resize_longsize` —— 1/4 个有
- `LTXFaceDetector` —— 1/4 个有
- `LTXLatentAnchorAware` —— 1/4 个有
- `LTXLikenessAnchor` —— 1/4 个有
- `LTXLikenessGuide` —— 1/4 个有
- `LTXVAudioVAEEncode` —— 1/4 个有
- `LoadAudio` —— 1/4 个有
- `MelBandRoFormerModelLoader` —— 1/4 个有
- `MelBandRoFormerSampler` —— 1/4 个有
- `PrimitiveFloat` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `PrimitiveString` —— 1/4 个有
- `ResizeImageMaskNode` —— 1/4 个有
- `SetLatentNoiseMask` —— 1/4 个有
- `SimpleCalculatorKJ` —— 1/4 个有
- `SolidMask` —— 1/4 个有
- `TrimAudioDuration` —— 1/4 个有
- `image_scale_pixel_v2` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 4 | 100% |
| 高度 | 25 | 24 - 25 | 4 | 98% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，4 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 24 - 25，4 个样本，取值集中（一致性 98%）

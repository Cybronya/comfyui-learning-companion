---
name: unknown_workflow_controlnet_video_upscale_5
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.592
common_nodes: [ACN_AdvancedControlNetApply, ADE_AnimateDiffLoaderWithContext, ADE_AnimateDiffSamplingSettings, ADE_ApplyAnimateDiffModelSimple, ADE_IterationOptsFreeInit, ADE_LoadAnimateDiffModel, ADE_StandardStaticContextOptions, ADE_UseEvolvedSampling, AIO_Preprocessor, Any Switch (rgthree), BasicScheduler, CLIPSetLastLayer, CLIPTextEncode, CR Apply LoRA Stack, CR Image Input Switch, CR LoRA Stack, CR Text, Change Channel Count, CheckpointLoaderSimple, Combine Masks, ConstrainImageforVideo|pysssss, ControlNetLoader, Cut By Mask, DWPreprocessor, FacialPartColoringFromPoseKps, Fast Groups Bypasser (rgthree), Fast Groups Muter (rgthree), FreeU_V2, Get Image Size, GetImageSizeAndCount, GetNode, GrowMask, INTConstant, Image To Mask, ImageConcatMulti, ImageScale, ImpactDilateMask, ImpactImageInfo, ImpactSEGSRangeFilter, ImpactSimpleDetectorSEGS, JWInteger, KSamplerAdvanced, LatentUpscaleBy, LineArtPreprocessor, Mask To Region, MaskBlur+, MaskToImage, MediaPipe-FaceMeshPreprocessor, ModelSamplingDiscrete, Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), Paste By Mask, Power Prompt (rgthree), Power Prompt - Simple (rgthree), PreviewImage, Primitive string multiline [Crystools], RebatchImages, SAMLoader, SamplerCustom, SamplerLCMCycle, ScaledSoftControlNetWeights, Seed (rgthree), SegsToCombinedMask, SetLatentNoiseMask, SetNode, TilePreprocessor, ToBinaryMask, UltralyticsDetectorProvider, VAEDecode, VAEEncode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, easy cleanGpuUsed, smZ CLIPTextEncode]
problems: []
missing: []
members: [平台全量/视频风格转绘(像素风)_1920684935051411458.json, 平台全量/视频风格转绘(版本2：可修改风格)_1915018686166695938.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_upscale_5

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/视频风格转绘(像素风)_1920684935051411458.json、平台全量/视频风格转绘(版本2：可修改风格)_1915018686166695938.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：59%

## 共有节点

全部 2 个 workflow 都包含：
- `ACN_AdvancedControlNetApply`
- `ADE_AnimateDiffLoaderWithContext`
- `ADE_AnimateDiffSamplingSettings`
- `ADE_ApplyAnimateDiffModelSimple`
- `ADE_IterationOptsFreeInit`
- `ADE_LoadAnimateDiffModel`
- `ADE_StandardStaticContextOptions`
- `ADE_UseEvolvedSampling`
- `AIO_Preprocessor`
- `Any Switch (rgthree)`
- `BasicScheduler`
- `CLIPSetLastLayer`
- `CLIPTextEncode`
- `CR Apply LoRA Stack`
- `CR Image Input Switch`
- `CR LoRA Stack`
- `CR Text`
- `Change Channel Count`
- `CheckpointLoaderSimple`
- `Combine Masks`
- `ConstrainImageforVideo|pysssss`
- `ControlNetLoader`
- `Cut By Mask`
- `DWPreprocessor`
- `FacialPartColoringFromPoseKps`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Muter (rgthree)`
- `FreeU_V2`
- `Get Image Size`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMask`
- `INTConstant`
- `Image To Mask`
- `ImageConcatMulti`
- `ImageScale`
- `ImpactDilateMask`
- `ImpactImageInfo`
- `ImpactSEGSRangeFilter`
- `ImpactSimpleDetectorSEGS`
- `JWInteger`
- `KSamplerAdvanced`
- `LatentUpscaleBy`
- `LineArtPreprocessor`
- `Mask To Region`
- `MaskBlur+`
- `MaskToImage`
- `MediaPipe-FaceMeshPreprocessor`
- `ModelSamplingDiscrete`
- `Mute / Bypass Relay (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Paste By Mask`
- `Power Prompt (rgthree)`
- `Power Prompt - Simple (rgthree)`
- `PreviewImage`
- `Primitive string multiline [Crystools]`
- `RebatchImages`
- `SAMLoader`
- `SamplerCustom`
- `SamplerLCMCycle`
- `ScaledSoftControlNetWeights`
- `Seed (rgthree)`
- `SegsToCombinedMask`
- `SetLatentNoiseMask`
- `SetNode`
- `TilePreprocessor`
- `ToBinaryMask`
- `UltralyticsDetectorProvider`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `smZ CLIPTextEncode`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.6 | - | 2 | 100% |
| 采样步数 | fixed | - | 2 | 100% |
| Prompt 约束强度(CFG) | 16 | - | 2 | 100% |
| 采样算法 | 2.2 | - | 2 | 100% |
| 调度器 | lcm | - | 2 | 100% |
| 重绘幅度 | sgm_uniform | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 最常用 fixed，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 16，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 2.2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，2 个样本，一致性 100%
- 重绘幅度 最常用 sgm_uniform，2 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 16，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

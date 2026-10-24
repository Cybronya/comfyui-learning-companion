---
name: unknown_workflow_video_upscale_latent_upscale_134
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.506
common_nodes: [Bjornulf_ShowInt, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, EmptyLatentImage, GetNode, INTConstant, JoinStrings, KSamplerSelect, LTX2_NAG, LTXVAddGuideMulti, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, Label (rgthree), LatentUpscaleModelLoader, LayerUtility: NumberCalculatorV2, LayerUtility: TextBox, LoadAudioUI, LoadImage, LoraLoaderModelOnly, ManualSigmas, MelBandRoFormerModelLoader, MelBandRoFormerSampler, MultiImageLoader, PathchSageAttentionKJ, PreviewImage, PrimitiveFloat, RH_Translator, ResizeImageMaskNode, SamplerCustom, Seed (rgthree), SetLatentNoiseMask, SetNode, SimpleCalculatorKJ, SolidMask, UNETLoader, VAEDecodeTiled, VAELoader, VHS_SelectImages, VHS_VideoCombine, easy convertAnything, easy showAnything, easy string]
problems: []
missing: []
members: [视频生成/图生视频/LTX+2.3首中尾帧(多帧)工作流_2085770570255392770.json, 视频生成/图生视频/工作流基础系列28-LTX+2.3首中尾帧(多帧)工作流_2063277265433219074.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_134

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/LTX+2.3首中尾帧(多帧)工作流_2085770570255392770.json、视频生成/图生视频/工作流基础系列28-LTX+2.3首中尾帧(多帧)工作流_2063277265433219074.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：51%

## 共有节点

全部 2 个 workflow 都包含：
- `Bjornulf_ShowInt`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `EmptyLatentImage`
- `GetNode`
- `INTConstant`
- `JoinStrings`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXVAddGuideMulti`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `Label (rgthree)`
- `LatentUpscaleModelLoader`
- `LayerUtility: NumberCalculatorV2`
- `LayerUtility: TextBox`
- `LoadAudioUI`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `MultiImageLoader`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `PrimitiveFloat`
- `RH_Translator`
- `ResizeImageMaskNode`
- `SamplerCustom`
- `Seed (rgthree)`
- `SetLatentNoiseMask`
- `SetNode`
- `SimpleCalculatorKJ`
- `SolidMask`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_SelectImages`
- `VHS_VideoCombine`
- `easy convertAnything`
- `easy showAnything`
- `easy string`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 121 | - | 2 | 100% |
| 高度 | 24 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 121，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 24，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

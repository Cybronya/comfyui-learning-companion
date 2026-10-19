---
name: unknown_workflow_lora_sampler_clip_144
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.779
common_nodes: [CFGGuider, CLIPTextEncode, CR Float To Integer, CR Text, ComfySwitchNode, CreateVideo, EmptyLTXVLatentVideo, Fast Bypasser (rgthree), FloatConstant, INTConstant, ImageResizeKJv2, KSamplerSelect, LTX2_NAG, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAddGuideMulti, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVSeparateAVLatent, LayerUtility: BooleanOperator, LiconMSR, LoadImage, LowVRAMCheckpointLoader, ManualSigmas, PreviewImage, PrimitiveBoolean, PromptRelayEncode, RH_LLMAPI_Pro_Node, RandomNoise, SamplerCustomAdvanced, SaveVideo, SimpleMath+, Text Find and Replace, VAEDecode, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/自动分镜-LTX-2.3-Licon-MSR-V2.0_2082802801167650818.json, 视频生成/文生视频/自动分镜-LTX-2.3-Licon-MSR-V2.0_2082802801167650818.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_144

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/自动分镜-LTX-2.3-Licon-MSR-V2.0_2082802801167650818.json、视频生成/文生视频/自动分镜-LTX-2.3-Licon-MSR-V2.0_2082802801167650818.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CR Float To Integer`
- `CR Text`
- `ComfySwitchNode`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `Fast Bypasser (rgthree)`
- `FloatConstant`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXAVTextEncoderLoader`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAddGuideMulti`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LayerUtility: BooleanOperator`
- `LiconMSR`
- `LoadImage`
- `LowVRAMCheckpointLoader`
- `ManualSigmas`
- `PreviewImage`
- `PrimitiveBoolean`
- `PromptRelayEncode`
- `RH_LLMAPI_Pro_Node`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SimpleMath+`
- `Text Find and Replace`
- `VAEDecode`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 241 | - | 2 | 100% |
| 高度 | 50 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 241，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 50，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

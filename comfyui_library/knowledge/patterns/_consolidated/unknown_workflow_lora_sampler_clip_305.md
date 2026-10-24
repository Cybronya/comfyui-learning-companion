---
name: unknown_workflow_lora_sampler_clip_305
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.705
common_nodes: [BasicScheduler, CLIPTextEncode, ComfyMathExpression, ComfySwitchNode, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, INTConstant, ImageFromBatch, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXSequencer, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LoadAudioUI, LoraLoaderModelOnly, MathExpression|pysssss, MelBandRoFormerModelLoader, MelBandRoFormerSampler, MultiImageLoader, PathchSageAttentionKJ, PreviewAudio, PromptRelayEncodeTimeline, SamplerCustom, SetLatentNoiseMask, SetNode, SimpleMath+, SolidMask, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VisualizeSigmasKJ, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3最强漫剧工作流包含音频参考_2056272692512387073.json, 视频生成/图生视频/LTX2.3最强漫剧工作流包含音频参考_2058414222178086914.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_305

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/LTX2.3最强漫剧工作流包含音频参考_2056272692512387073.json、视频生成/图生视频/LTX2.3最强漫剧工作流包含音频参考_2058414222178086914.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：70%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `INTConstant`
- `ImageFromBatch`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXSequencer`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LoadAudioUI`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `MultiImageLoader`
- `PathchSageAttentionKJ`
- `PreviewAudio`
- `PromptRelayEncodeTimeline`
- `SamplerCustom`
- `SetLatentNoiseMask`
- `SetNode`
- `SimpleMath+`
- `SolidMask`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VisualizeSigmasKJ`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 1/2 个有
- `SaveVideo` —— 1/2 个有
- `VHS_VideoCombine` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 361 | - | 2 | 100% |
| 高度 | 25 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 361，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

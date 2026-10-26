---
name: unknown_workflow_video_sampler_clip_222
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8135
common_nodes: [BasicScheduler, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, ImpactConditionalBranch, Int, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVImgToVideoInplaceKJ, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, PathchSageAttentionKJ, PreviewImage, PrimitiveBoolean, PromptRelayEncodeTimeline, ResizeImagesByLongerEdge, SamplerCustom, SetNode, UnetLoaderGGUF, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_VideoCombine, VRAMReserver, VisualizeSigmasKJ]
problems: []
missing: []
members: [图片生成/反推提示词/70-ltx23_2052732244107776001.json, 视频生成/文生视频/LTX2.3低显存高质量工作流_2052627481596833794.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_222

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/70-ltx23_2052732244107776001.json、视频生成/文生视频/LTX2.3低显存高质量工作流_2052627481596833794.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `ImpactConditionalBranch`
- `Int`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVImgToVideoInplaceKJ`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `PrimitiveBoolean`
- `PromptRelayEncodeTimeline`
- `ResizeImagesByLongerEdge`
- `SamplerCustom`
- `SetNode`
- `UnetLoaderGGUF`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `VRAMReserver`
- `VisualizeSigmasKJ`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 481 | - | 2 | 75% |
| 高度 | 24 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 481，样本不足，未给区间，2 个样本
- 高度 中位数 24，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

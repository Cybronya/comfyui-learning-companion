---
name: unknown_workflow_upscale_latent_upscale_sampler_29
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7645
common_nodes: [BasicGuider, CLIPLoader, ComfySwitchNode, GetVideoComponents, LoadImage, LoadVideo, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DurationPlannerT8, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3OutputTrimT8, MiniMaxH3SafeAVSaveT8Advanced, MiniMaxH3TwoPassAudioAuditT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, MiniMaxH3VDNExecutionPlanT8Advanced, MiniMaxH3VDNModelComposerT8Advanced, MiniMaxH3VDNRefinePlanT8Advanced, PreviewAny, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAELoader, Video Slice]
problems: []
missing: []
members: [视频生成/文生视频/H3｜VDN 12NFE高质量二采｜商品展示 Hero Shot_2107777467430817794.json, 视频生成/文生视频/MiniMax H3｜通用视频生成｜VDN 12步高清版_2108578118234632193.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_29

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/H3｜VDN 12NFE高质量二采｜商品展示 Hero Shot_2107777467430817794.json、视频生成/文生视频/MiniMax H3｜通用视频生成｜VDN 12步高清版_2108578118234632193.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfySwitchNode`
- `GetVideoComponents`
- `LoadImage`
- `LoadVideo`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DurationPlannerT8`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3OutputTrimT8`
- `MiniMaxH3SafeAVSaveT8Advanced`
- `MiniMaxH3TwoPassAudioAuditT8Advanced`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `MiniMaxH3VDNExecutionPlanT8Advanced`
- `MiniMaxH3VDNModelComposerT8Advanced`
- `MiniMaxH3VDNRefinePlanT8Advanced`
- `PreviewAny`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAELoader`
- `Video Slice`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

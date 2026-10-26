---
name: unknown_workflow_video_sampler_unet_80
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.375
common_nodes: [Any Switch (rgthree), BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, GetNode, ImageResizeKJv2, ImpactConditionalBranch, Int, KSamplerSelect, LoadAudio, LoadImage, MathExpression|pysssss, MiniMaxChunkFeedForward, MiniMaxH3ImageToVideo, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, MiniMaxLowVRAMAttention, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveStringMultiline, ResolutionSelector, SelfLiftH3Sampler, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VRGDG_MiniMaxH3AudioDrive, 孤海注释, 布尔孤海, 忽略多组孤海]
problems: []
missing: []
members: [视频生成/文生视频/自用版   Minimax H3 文生+首尾+图参多合一生视频二采高清放大工作流V6.0_2100491353854668802.json, 视频生成/文生视频/自用版   Minimax H3 文生+首尾+图参多合一生视频二采高清放大工作流V6.1_2098342858284691457.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_80

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/自用版   Minimax H3 文生+首尾+图参多合一生视频二采高清放大工作流V6.0_2100491353854668802.json、视频生成/文生视频/自用版   Minimax H3 文生+首尾+图参多合一生视频二采高清放大工作流V6.1_2098342858284691457.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：38%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `GetNode`
- `ImageResizeKJv2`
- `ImpactConditionalBranch`
- `Int`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `MathExpression|pysssss`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `MiniMaxLowVRAMAttention`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SelfLiftH3Sampler`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VRGDG_MiniMaxH3AudioDrive`
- `孤海注释`
- `布尔孤海`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

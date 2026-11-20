---
name: unknown_workflow_video_lora_sampler_515
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.620833
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, ModelPreviewOverrideKJ, ResolutionSelector, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/H3-self-数字人_文字驱动_2104056713530925057.json, 视频生成/图生视频/MICAS西游_Camera_3_2107469660680708097.json, 视频生成/图生视频/MICAS西游：Camera 3_2103441968356483073.json, 视频生成/图生视频/Mini  max  H3视频小脸不崩坏_2098335113011613698.json, 视频生成/图生视频/MiniMax H3 黑科技加速双采-self-lift工作流_2098836942896062465.json, 视频生成/图生视频/Minimax H3 + Self-lift双采快速超长工作流_2104549240100970498.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_515

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/H3-self-数字人_文字驱动_2104056713530925057.json、视频生成/图生视频/MICAS西游_Camera_3_2107469660680708097.json、视频生成/图生视频/MICAS西游：Camera 3_2103441968356483073.json、视频生成/图生视频/Mini  max  H3视频小脸不崩坏_2098335113011613698.json、视频生成/图生视频/MiniMax H3 黑科技加速双采-self-lift工作流_2098836942896062465.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：62%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `H3SigmaRefiner` —— 5/6 个有
- `MiniMaxChunkFeedForward` —— 5/6 个有
- `MiniMaxLowVRAMAttention` —— 5/6 个有
- `PrimitiveFloat` —— 5/6 个有
- `SelfLiftH3Sampler` —— 5/6 个有
- `PrimitiveStringMultiline` —— 3/6 个有
- `CR Text` —— 2/6 个有
- `CreateVideo` —— 2/6 个有
- `SetNode` —— 2/6 个有
- `EmptyImage` —— 1/6 个有
- `GetNode` —— 1/6 个有
- `LTXVSeparateAVLatent` —— 1/6 个有
- `PreviewAny` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `QwenH3PromptLocal` —— 1/6 个有
- `RHMiniMaxH3PromptOptimizerMedia` —— 1/6 个有
- `SelfLiftAvatarH3Sampler` —— 1/6 个有
- `easy showAnything` —— 1/6 个有
- `int _O` —— 1/6 个有
- `忽略多组孤海` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_video_lora_sampler_280
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.672571
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, H3SigmaRefiner, KSamplerSelect, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, ResolutionSelector, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/反推提示词/Minimax_H3_Best_Fast_2097990442091638786.json, 图片生成/图生图/1-Aiden-黑科技加速双采-self-lift工作流_2098914289888358402.json, 图片生成/图生图/1-Aiden-黑科技加速双采-self-lift工作流_2098968774253830146.json, 图片生成/图生图/全能参考加速双采-self-lift工作流_2100211203405602818.json, 图片生成/文生图/Minimaxh3的视频复刻 伪原创（selflift版）_2110397654776770561.json, 视频生成/图生视频/MICAS西游_Camera_3_2107469660680708097.json, 视频生成/文生视频/短剧助手：加速双采-self-lift_2097990357018570753.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_280

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/反推提示词/Minimax_H3_Best_Fast_2097990442091638786.json、图片生成/图生图/1-Aiden-黑科技加速双采-self-lift工作流_2098914289888358402.json、图片生成/图生图/1-Aiden-黑科技加速双采-self-lift工作流_2098968774253830146.json、图片生成/图生图/全能参考加速双采-self-lift工作流_2100211203405602818.json、图片生成/文生图/Minimaxh3的视频复刻 伪原创（selflift版）_2110397654776770561.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 6/7 个有
- `SelfLiftH3Sampler` —— 6/7 个有
- `LoadImage` —— 5/7 个有
- `CreateVideo` —— 4/7 个有
- `EmptyImage` —— 3/7 个有
- `GetNode` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `SetNode` —— 3/7 个有
- `Anything Everywhere3` —— 2/7 个有
- `MiniMaxH3MediaLoaderFantastic` —— 2/7 个有
- `MiniMaxH3ReferenceSplitter` —— 2/7 个有
- `Prompts Everywhere` —— 2/7 个有
- `孤海注释` —— 2/7 个有
- `CR Text` —— 1/7 个有
- `ComfySwitchNode` —— 1/7 个有
- `LoadAudio` —— 1/7 个有
- `PathchSageAttentionKJ` —— 1/7 个有
- `PlaySound|pysssss` —— 1/7 个有
- `SelfLiftAvatarH3Sampler` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

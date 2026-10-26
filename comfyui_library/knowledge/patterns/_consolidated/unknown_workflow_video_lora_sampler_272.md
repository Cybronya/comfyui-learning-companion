---
name: unknown_workflow_video_lora_sampler_272
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.740875
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, H3SigmaRefiner, KSamplerSelect, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveStringMultiline, ResolutionSelector, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/反推提示词/Minimax_H3_Best_Fast_2097990442091638786.json, 图片生成/图生图/1-Aiden-黑科技加速双采-self-lift工作流_2098914289888358402.json, 图片生成/图生图/1-Aiden-黑科技加速双采-self-lift工作流_2098968774253830146.json, 图片生成/图生图/全能参考加速双采-self-lift工作流_2100211203405602818.json, 图片生成/文生图/Minimaxh3的视频复刻 伪原创（selflift版）_2110397654776770561.json, 视频生成/图生视频/Minimaxh3的视频复刻_伪原创selflift版_2114523078490411009.json, 视频生成/文生视频/1-Aiden-黑科技加速双采-self-lift工作流_2097588130751799297.json, 视频生成/文生视频/短剧助手：加速双采-self-lift_2097990357018570753.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_272

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/反推提示词/Minimax_H3_Best_Fast_2097990442091638786.json、图片生成/图生图/1-Aiden-黑科技加速双采-self-lift工作流_2098914289888358402.json、图片生成/图生图/1-Aiden-黑科技加速双采-self-lift工作流_2098968774253830146.json、图片生成/图生图/全能参考加速双采-self-lift工作流_2100211203405602818.json、图片生成/文生图/Minimaxh3的视频复刻 伪原创（selflift版）_2110397654776770561.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 8 个 workflow 都包含：
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
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 6/8 个有
- `LoadImage` —— 6/8 个有
- `SelfLiftH3Sampler` —— 6/8 个有
- `GetNode` —— 4/8 个有
- `SetNode` —— 4/8 个有
- `孤海注释` —— 3/8 个有
- `Anything Everywhere3` —— 2/8 个有
- `EmptyImage` —— 2/8 个有
- `LoadAudio` —— 2/8 个有
- `MiniMaxH3MediaLoaderFantastic` —— 2/8 个有
- `MiniMaxH3ReferenceSplitter` —— 2/8 个有
- `PlaySound|pysssss` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `Prompts Everywhere` —— 2/8 个有
- `SelfLiftAvatarH3Sampler` —— 2/8 个有
- `ComfySwitchNode` —— 1/8 个有
- `PathchSageAttentionKJ` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

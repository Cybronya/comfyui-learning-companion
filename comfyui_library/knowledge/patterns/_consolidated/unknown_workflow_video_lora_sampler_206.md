---
name: unknown_workflow_video_lora_sampler_206
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.596111
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, H3SigmaRefiner, KSamplerSelect, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, ResolutionSelector, SelfLiftH3Sampler, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/反推提示词/Minimax_H3_Best_Fast_2097990442091638786.json, 图片生成/图生图/Minimax_H3_Best_Fast_2097990442091638786.json, 视频生成/图生视频/H3-8STEP-双采_2101940350767165442.json, 视频生成/图生视频/LAOBA  黑科技加速双采-self-lift工作流_2099340731876986882.json, 视频生成/图生视频/MICAS西游_Camera_3_2107469660680708097.json, 视频生成/图生视频/MICAS西游：Camera 3_2103441968356483073.json, 视频生成/图生视频/MiniMax H3 黑科技加速双采-self-lift工作流_2098836942896062465.json, 视频生成/图生视频/Minimax H3 + Self-lift双采快速超长工作流_2104549240100970498.json, 视频生成/文生视频/短剧助手：加速双采-self-lift_2097990357018570753.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_206

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/反推提示词/Minimax_H3_Best_Fast_2097990442091638786.json、图片生成/图生图/Minimax_H3_Best_Fast_2097990442091638786.json、视频生成/图生视频/H3-8STEP-双采_2101940350767165442.json、视频生成/图生视频/LAOBA  黑科技加速双采-self-lift工作流_2099340731876986882.json、视频生成/图生视频/MICAS西游_Camera_3_2107469660680708097.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：60%

## 共有节点

全部 9 个 workflow 都包含：
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
- `SelfLiftH3Sampler`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 7/9 个有
- `LoadImage` —— 6/9 个有
- `SetNode` —— 5/9 个有
- `GetNode` —— 4/9 个有
- `Anything Everywhere3` —— 3/9 个有
- `CreateVideo` —— 3/9 个有
- `MiniMaxH3MediaLoaderFantastic` —— 3/9 个有
- `MiniMaxH3ReferenceSplitter` —— 3/9 个有
- `Prompts Everywhere` —— 3/9 个有
- `CR Text` —— 2/9 个有
- `ComfySwitchNode` —— 2/9 个有
- `PathchSageAttentionKJ` —— 2/9 个有
- `EmptyImage` —— 1/9 个有
- `LoadAudio` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `QwenH3PromptLocal` —— 1/9 个有
- `easy showAnything` —— 1/9 个有
- `忽略多组孤海` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

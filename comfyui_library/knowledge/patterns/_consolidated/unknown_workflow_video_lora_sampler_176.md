---
name: unknown_workflow_video_lora_sampler_176
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.816727
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, CreateVideo, H3SigmaRefiner, KSamplerSelect, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveStringMultiline, SelfLiftH3Sampler, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/黑科技加速双采-self-lift工作流-3图1音_2102289015847350274.json, 视频生成/图生视频/黑科技加速双采-self-lift工作流-4图1音_2102284106150273026.json, 视频生成/图生视频/黑科技加速双采-self-lift工作流-5图1音_2108825320408309761.json, 视频生成/图生视频/黑科技加速双采-self-lift工作流-6图1音_2108828857859141634.json, 视频生成/图生视频/黑科技加速双采-self-lift工作流_2097505105535913985.json, 视频生成/图生视频/黑科技加速双采-self-lift工作流_2097859473883881474.json, 视频生成/图生视频/黑科技加速双采-self-lift工作流_2099386693676785665.json, 视频生成/图生视频/黑科技加速双采-self-lift工作流_2109640374049402882.json, 视频生成/图生视频/黑科技加速双采-self-lift高动态_2102398843047469057.json, 视频生成/文生视频/1-Aiden-黑科技加速双采-self-lift工作流_2097588130751799297.json, 视频生成/文生视频/满血版minimax h3黑科技加速内置双采-self-lift工作流_2097892303456260098.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_176

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/黑科技加速双采-self-lift工作流-3图1音_2102289015847350274.json、视频生成/图生视频/黑科技加速双采-self-lift工作流-4图1音_2102284106150273026.json、视频生成/图生视频/黑科技加速双采-self-lift工作流-5图1音_2108825320408309761.json、视频生成/图生视频/黑科技加速双采-self-lift工作流-6图1音_2108828857859141634.json、视频生成/图生视频/黑科技加速双采-self-lift工作流_2097505105535913985.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `CreateVideo`
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
- `SelfLiftH3Sampler`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 10/11 个有
- `LoadImage` —— 7/11 个有
- `Int` —— 4/11 个有
- `SDVN Load Image Url` —— 4/11 个有
- `VHS_LoadAudio` —— 4/11 个有
- `LoraLoaderBypassModelOnly` —— 3/11 个有
- `LoadAudio` —— 2/11 个有
- `QwenH3PromptLocal` —— 2/11 个有
- `easy cleanGpuUsed` —— 2/11 个有
- `easy showAnything` —— 2/11 个有
- `孤海注释` —— 2/11 个有
- `AudioCrop` —— 1/11 个有
- `Text` —— 1/11 个有
- `VHS_LoadVideo` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

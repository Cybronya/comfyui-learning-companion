---
name: unknown_workflow_video_lora_sampler_320
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.878667
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, H3SigmaRefiner, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, PrimitiveFloat, ResolutionSelector, SelfLiftH3Sampler, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [数字人/数字人/MiniMaxH3带货视频生成工作流_2112497234167291905.json, 视频生成/图生视频/CGD加电影lora_2104927511938428929.json, 视频生成/图生视频/H3-8STEP-双采-音频_2102375764057481217.json, 视频生成/图生视频/H3-8STEP-双采_2101940350767165442.json, 视频生成/图生视频/LAOBA  黑科技加速双采-self-lift工作流_2099340731876986882.json, 视频生成/图生视频/MINIMAX H3 急速双采 + 无线时长_2099690271108845570.json, 视频生成/图生视频/MINIMAX_H3_急速双采_+_无线时长_2100409429870075905.json, 视频生成/图生视频/MINIMAX_H3_急速双采_+_无线时长_2100496703639089154.json, 视频生成/图生视频/Minimax H3 SelfLift 图生视频_2115640648958308353.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_320

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（数字人/数字人/MiniMaxH3带货视频生成工作流_2112497234167291905.json、视频生成/图生视频/CGD加电影lora_2104927511938428929.json、视频生成/图生视频/H3-8STEP-双采-音频_2102375764057481217.json、视频生成/图生视频/H3-8STEP-双采_2101940350767165442.json、视频生成/图生视频/LAOBA  黑科技加速双采-self-lift工作流_2099340731876986882.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `ResolutionSelector`
- `SelfLiftH3Sampler`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ModelPreviewOverrideKJ` —— 8/9 个有
- `PrimitiveStringMultiline` —— 8/9 个有
- `CreateVideo` —— 7/9 个有
- `AudioConcat` —— 4/9 个有
- `MiniMaxH3MotionContext` —— 3/9 个有
- `MiniMaxH3MotionContextSaveLatent` —— 3/9 个有
- `MiniMaxH3MotionContextTrim` —— 3/9 个有
- `VHS_MergeImages` —— 3/9 个有
- `LoadAudio` —— 2/9 个有
- `QwenH3PromptLocal` —— 2/9 个有
- `easy showAnything` —— 2/9 个有
- `BlockSparseAttention` —— 1/9 个有
- `ImageBatch` —— 1/9 个有
- `ImageFromBatch` —— 1/9 个有
- `MiniMaxH3AddGuide` —— 1/9 个有
- `TrimAudioDuration` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

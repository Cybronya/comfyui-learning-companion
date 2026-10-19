---
name: unknown_workflow_video_lora_sampler_81
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.811471
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, H3SigmaRefiner, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, PrimitiveFloat, PrimitiveStringMultiline, ResolutionSelector, SelfLiftH3Sampler, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MINIMAX H3 急速双采 + 无线时长_2099690271108845570.json, 视频生成/图生视频/MINIMAX_H3_急速双采_+_无线时长_2100409429870075905.json, 视频生成/图生视频/MINIMAX_H3_急速双采_+_无线时长_2100496703639089154.json, 视频生成/图生视频/Mini  max  H3视频小脸不崩坏_2098335113011613698.json, 视频生成/图生视频/MiniMax H3 导演skill+双采2k直出_2106288951286915073.json, 视频生成/图生视频/MiniMax-H3-导演skill-双采2k直出.json, 视频生成/图生视频/MiniMax_二采_selflift_急速工作流_2099671590920351746.json, 视频生成/图生视频/MiniMax_二采_selflift_急速工作流自用_2105654345877512193.json, 视频生成/图生视频/绘影-Minimax H3-参考生视频-self-lift双采-1080P-V1.2_2099315406128369665.json, 视频生成/图生视频/黑科技加速双采-self-lift-Heng_2100234461106499585.json, 视频生成/文生视频/1-Aiden-黑科技加速双采-self-lift工作流_2097588130751799297.json, 视频生成/文生视频/H3视频生成self-lift加速双采工作流_2097856577159127042.json, 视频生成/文生视频/MiniMax H3 导演skill+双采2k直出_2103795804296273922.json, 视频生成/文生视频/啊癫 黑科技加速双采-self-lift工作流_2097728195679309825.json, 视频生成/文生视频/满血版minimax h3黑科技加速内置双采-self-lift工作流_2097892303456260098.json, 视频生成/文生视频/黑科技加速双采-self-lift工作流_加画风Lora版_2101959966662946817.json, 视频生成/文生视频/黑科技加速双采-self-lift工作流_改清晰版_2101892912144539649.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_81

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/MINIMAX H3 急速双采 + 无线时长_2099690271108845570.json、视频生成/图生视频/MINIMAX_H3_急速双采_+_无线时长_2100409429870075905.json、视频生成/图生视频/MINIMAX_H3_急速双采_+_无线时长_2100496703639089154.json、视频生成/图生视频/Mini  max  H3视频小脸不崩坏_2098335113011613698.json、视频生成/图生视频/MiniMax H3 导演skill+双采2k直出_2106288951286915073.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 17 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SelfLiftH3Sampler`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 15/17 个有
- `ModelPreviewOverrideKJ` —— 15/17 个有
- `MiniMaxChunkFeedForward` —— 13/17 个有
- `MiniMaxLowVRAMAttention` —— 13/17 个有
- `CreateVideo` —— 10/17 个有
- `MiniMaxH3SigmaShift` —— 6/17 个有
- `VHS_LoadVideo` —— 6/17 个有
- `Fast Groups Bypasser (rgthree)` —— 5/17 个有
- `LoadAudio` —— 5/17 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/17 个有
- `MiniMaxH3MotionContext` —— 5/17 个有
- `MiniMaxH3MotionContextSaveLatent` —— 5/17 个有
- `MiniMaxH3MotionContextTrim` —— 5/17 个有
- `AudioConcat` —— 3/17 个有
- `Label (rgthree)` —— 3/17 个有
- `MiniMaxH3Unified` —— 3/17 个有
- `VHS_MergeImages` —— 3/17 个有
- `Fast Groups Muter (rgthree)` —— 2/17 个有
- `IAMCCS_VRAMCleanup` —— 2/17 个有
- `MiniMaxH3MotionContextLoadLatent` —— 2/17 个有
- `SaveVideo` —— 2/17 个有
- `YuanMultiImage` —— 2/17 个有
- `孤海注释` —— 2/17 个有
- `AudioCrop` —— 1/17 个有
- `LoraLoaderBypassModelOnly` —— 1/17 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

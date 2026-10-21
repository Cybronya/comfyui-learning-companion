---
name: unknown_workflow_sampler_unet_vae_62
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.6806
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, PrimitiveFloat, PrimitiveStringMultiline, ResolutionSelector, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/DsiwaV2 小脸高动态selflift_2100417664513568770.json, 视频生成/图生视频/FastH3 V2 SelfLift 1080P_2100495010562134018.json, 视频生成/图生视频/H3 taomate 3步加速 中远距离不崩脸_2099163346699374593.json, 视频生成/图生视频/H3视频衔接_2095145130473902082.json, 视频生成/图生视频/MiniMax H3 sigma强化+潜空间放大工作流-小脸不崩-脸不油，高动态不崩脸_2093136040067428353.json, 视频生成/图生视频/MiniMax H3图生视频(多参考)_2091406664456040450.json, 视频生成/图生视频/Minimax H3 脸不崩！打斗不糊！H3 sigma强化+超清放大，生成1080P视频，效果极佳，不过速度为普通流的2倍_2089537626373181442.json, 视频生成/图生视频/Minimaxh3双采浅空间放大_2092523112779837442.json, 视频生成/文生视频/Minimax H3 双采样全能参考高清工作流｜超分放大｜4倍加速｜8倍加速_2092731840196079618.json, 视频生成/文生视频/Minimax H3 双采样全能参考｜真实电影感｜超分高清放大｜4倍加速｜8倍加速_2094320738051383298.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_62

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/DsiwaV2 小脸高动态selflift_2100417664513568770.json、视频生成/图生视频/FastH3 V2 SelfLift 1080P_2100495010562134018.json、视频生成/图生视频/H3 taomate 3步加速 中远距离不崩脸_2099163346699374593.json、视频生成/图生视频/H3视频衔接_2095145130473902082.json、视频生成/图生视频/MiniMax H3 sigma强化+潜空间放大工作流-小脸不崩-脸不油，高动态不崩脸_2093136040067428353.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `H3SigmaRefiner` —— 9/10 个有
- `LoraLoaderModelOnly` —— 9/10 个有
- `BasicGuider` —— 8/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/10 个有
- `ModelAttentionBackend` —— 8/10 个有
- `ModelPreviewOverrideKJ` —— 8/10 个有
- `RandomNoise` —— 8/10 个有
- `SamplerCustomAdvanced` —— 8/10 个有
- `GetNode` —— 7/10 个有
- `LTXVConcatAVLatent` —— 7/10 个有
- `LTXVSeparateAVLatent` —— 7/10 个有
- `MinimaxH3LatentUpscaler3D` —— 7/10 个有
- `SetNode` —— 7/10 个有
- `SplitSigmas` —— 7/10 个有
- `MiniMaxLowVRAMAttention` —— 6/10 个有
- `MiniMaxChunkFeedForward` —— 4/10 个有
- `LoadAudio` —— 3/10 个有
- `SolAttnMiniMax` —— 3/10 个有
- `孤海注释` —— 3/10 个有
- `ConditioningZeroOut` —— 2/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `FlashVSRNode` —— 2/10 个有
- `HAIGC_VideoLoader` —— 2/10 个有
- `SelfLiftAvatarH3Sampler` —— 2/10 个有
- `Sleep` —— 2/10 个有
- `easy seed` —— 2/10 个有
- `BlockSparseAttention` —— 1/10 个有
- `CR Text Concatenate` —— 1/10 个有
- `FL_UnloadAllModels` —— 1/10 个有
- `Float` —— 1/10 个有
- `GetImageRangeFromBatch` —— 1/10 个有
- `LoraLoaderBypassModelOnly` —— 1/10 个有
- `MiniMaxH3AddGuide` —— 1/10 个有
- `MiniMaxH3BlockCacheT8` —— 1/10 个有
- `MinimaxH3LatentUpscalerNode2D` —— 1/10 个有
- `MuyeTextEditOutput` —— 1/10 个有
- `VHS_LoadVideo` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

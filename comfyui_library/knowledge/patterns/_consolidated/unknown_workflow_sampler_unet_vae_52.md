---
name: unknown_workflow_sampler_unet_vae_52
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.634182
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveStringMultiline, ResolutionSelector, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/DsiwaV2 小脸高动态selflift_2100417664513568770.json, 视频生成/图生视频/FastH3 V2 SelfLift 1080P_2100495010562134018.json, 视频生成/图生视频/H3 taomate 3步加速 中远距离不崩脸_2099163346699374593.json, 视频生成/图生视频/H3视频衔接_2095145130473902082.json, 视频生成/图生视频/MiniMax H3 sigma强化+潜空间放大工作流-小脸不崩-脸不油，高动态不崩脸_2093136040067428353.json, 视频生成/图生视频/MiniMax H3图生视频(多参考)_2091406664456040450.json, 视频生成/图生视频/MiniMax_H3_双采样潜空间放大直出1080p_2096948674386550786.json, 视频生成/图生视频/Minimax H3 多图参考 真实感极佳_2092151387793747970.json, 视频生成/图生视频/Minimax H3双模双采工作流-小脸不崩-脸不油，高动态不崩脸_2093185884203085826.json, 视频生成/图生视频/Minimaxh3双采浅空间放大_2092523112779837442.json, 视频生成/文生视频/H3 高清优化版-小脸不崩-运动不模糊_2089690104179810306.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_52

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/DsiwaV2 小脸高动态selflift_2100417664513568770.json、视频生成/图生视频/FastH3 V2 SelfLift 1080P_2100495010562134018.json、视频生成/图生视频/H3 taomate 3步加速 中远距离不崩脸_2099163346699374593.json、视频生成/图生视频/H3视频衔接_2095145130473902082.json、视频生成/图生视频/MiniMax H3 sigma强化+潜空间放大工作流-小脸不崩-脸不油，高动态不崩脸_2093136040067428353.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `H3SigmaRefiner` —— 10/11 个有
- `LoraLoaderModelOnly` —— 10/11 个有
- `BasicGuider` —— 9/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 9/11 个有
- `ModelAttentionBackend` —— 9/11 个有
- `RandomNoise` —— 9/11 个有
- `SamplerCustomAdvanced` —— 9/11 个有
- `GetNode` —— 8/11 个有
- `LTXVConcatAVLatent` —— 8/11 个有
- `LTXVSeparateAVLatent` —— 8/11 个有
- `MinimaxH3LatentUpscaler3D` —— 8/11 个有
- `SetNode` —— 8/11 个有
- `SplitSigmas` —— 8/11 个有
- `MiniMaxLowVRAMAttention` —— 6/11 个有
- `MiniMaxChunkFeedForward` —— 4/11 个有
- `SolAttnMiniMax` —— 4/11 个有
- `ConditioningZeroOut` —— 2/11 个有
- `Label (rgthree)` —— 2/11 个有
- `SelfLiftAvatarH3Sampler` —— 2/11 个有
- `easy cleanGpuUsed` —— 2/11 个有
- `easy seed` —— 2/11 个有
- `BlockSparseAttention` —— 1/11 个有
- `FL_UnloadAllModels` —— 1/11 个有
- `GetImageRangeFromBatch` —— 1/11 个有
- `LayerUtility: PurgeVRAM V2` —— 1/11 个有
- `LoadAudio` —— 1/11 个有
- `LoraLoaderBypassModelOnly` —— 1/11 个有
- `MiniMaxH3AddGuide` —— 1/11 个有
- `MiniMaxH3BlockCacheT8` —— 1/11 个有
- `VHS_LoadVideo` —— 1/11 个有
- `孤海注释` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

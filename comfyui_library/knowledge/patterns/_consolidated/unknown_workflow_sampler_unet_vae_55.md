---
name: unknown_workflow_sampler_unet_vae_55
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.664143
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, ResolutionSelector, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/DsiwaV2 小脸高动态selflift_2100417664513568770.json, 视频生成/图生视频/FastH3 V2 SelfLift 1080P_2100495010562134018.json, 视频生成/图生视频/H3 taomate 3步加速 中远距离不崩脸_2099163346699374593.json, 视频生成/图生视频/H3视频衔接_2095145130473902082.json, 视频生成/图生视频/MiniMax H3 sigma强化+潜空间放大工作流-小脸不崩-脸不油，高动态不崩脸_2093136040067428353.json, 视频生成/图生视频/MiniMax H3图生视频(多参考)_2091406664456040450.json, 视频生成/图生视频/MiniMax H3图生视频动作面部优化工作流_2089680420211347458.json, 视频生成/图生视频/MiniMax_H3_二次采样+放大文戏工作流_2096179690426949633.json, 视频生成/图生视频/Minimax H3 人物电影级视频工作流（完美解决脸部崩坏问题）_2089732704005877761.json, 视频生成/图生视频/Minimax H3 图生视频 双采样+sigma强化 潜空间放大工作流 小脸不崩漫剧必备！_2089543355335274497.json, 视频生成/图生视频/Minimax H3 图生视频 双采样+sigma强化 潜空间放大工作流 小脸不崩漫剧必备！_2089917740520919041.json, 视频生成/图生视频/minimaxh3的selflift+二采+音频参考_2105937177262772225.json, 视频生成/文生视频/minimaxh3的selflift+二采_2101192695308963842.json, 视频生成/文生视频/收藏级！H3 加速+二采+打斗全能工作流拆解系列05集_2092970619469123586.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_55

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/DsiwaV2 小脸高动态selflift_2100417664513568770.json、视频生成/图生视频/FastH3 V2 SelfLift 1080P_2100495010562134018.json、视频生成/图生视频/H3 taomate 3步加速 中远距离不崩脸_2099163346699374593.json、视频生成/图生视频/H3视频衔接_2095145130473902082.json、视频生成/图生视频/MiniMax H3 sigma强化+潜空间放大工作流-小脸不崩-脸不油，高动态不崩脸_2093136040067428353.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `H3SigmaRefiner` —— 13/14 个有
- `LoraLoaderModelOnly` —— 13/14 个有
- `ModelPreviewOverrideKJ` —— 13/14 个有
- `BasicGuider` —— 12/14 个有
- `MiniMaxH3SigmaShift` —— 12/14 个有
- `ModelAttentionBackend` —— 12/14 个有
- `PrimitiveStringMultiline` —— 12/14 个有
- `RandomNoise` —— 12/14 个有
- `SamplerCustomAdvanced` —— 12/14 个有
- `SaveVideo` —— 12/14 个有
- `LTXVConcatAVLatent` —— 11/14 个有
- `LTXVSeparateAVLatent` —— 11/14 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 11/14 个有
- `GetNode` —— 10/14 个有
- `SetNode` —— 10/14 个有
- `SplitSigmas` —— 9/14 个有
- `MinimaxH3LatentUpscaler3D` —— 7/14 个有
- `SolAttnMiniMax` —— 6/14 个有
- `MiniMaxChunkFeedForward` —— 5/14 个有
- `MiniMaxLowVRAMAttention` —— 5/14 个有
- `ConditioningZeroOut` —— 4/14 个有
- `MinimaxH3LatentUpscalerNode3D` —— 4/14 个有
- `SelfLiftAvatarH3Sampler` —— 4/14 个有
- `LoadAudio` —— 2/14 个有
- `PlaySound|pysssss` —— 2/14 个有
- `VHS_LoadVideo` —— 2/14 个有
- `VHS_VideoCombine` —— 2/14 个有
- `easy seed` —— 2/14 个有
- `孤海注释` —— 2/14 个有
- `BlockSparseAttention` —— 1/14 个有
- `CR Prompt Text` —— 1/14 个有
- `FL_UnloadAllModels` —— 1/14 个有
- `GetImageRangeFromBatch` —— 1/14 个有
- `LoraLoaderBypassModelOnly` —— 1/14 个有
- `MiniMaxH3AddGuide` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

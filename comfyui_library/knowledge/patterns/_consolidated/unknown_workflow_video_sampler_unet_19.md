---
name: unknown_workflow_video_sampler_unet_19
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.434706
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, Float, GetNode, KSamplerSelect, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, ResolutionSelector, SetNode, Text, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/AITUDOU-MiniMax H3 Skill2.0 全能参考版单采_2098354620342030337.json, 视频生成/图生视频/AITUDOU-MiniMax H3 打斗-单采_2095430334602113026.json, 视频生成/图生视频/AITUDOU-MiniMax H3 打斗-双采_2095430950619537409.json, 视频生成/图生视频/AITUDOU-MiniMax H3 配合Skill短片自用-双采_2093313656774807553.json, 视频生成/图生视频/AITUDOU-MiniMax H3 配合Skill自用短片-单采_2093313597047918594.json, 视频生成/图生视频/AITUDOU-MiniMax H3 配合Skill自用短片-单采_2094575888913485825.json, 视频生成/图生视频/AITUDOU-MiniMax+H3+SelfLift+影视级情绪表达+SKILL_2104111411025764354.json, 视频生成/图生视频/AITUDOU-MiniMax+H3+SelfLift+影视级情绪表达+SKILL_2106320510052298754.json, 视频生成/图生视频/Fused-MiniMax H3 战斗增强-1280单采_2097598203356073986.json, 视频生成/图生视频/Fused-MiniMax H3-战斗增强-双采_2097606528458121218.json, 视频生成/图生视频/H3最强电影LORA+巅峰双采去油PRO版_2100507019949203458.json, 视频生成/图生视频/MiniMax H3 双采样 潜空间放大DSW（二次优化）_2095748408920330241.json, 视频生成/图生视频/MiniMax H3 双采样 潜空间放大_2090792067181137921.json, 视频生成/图生视频/MiniMax H3 双采样 潜空间放大（二次优化）_2091136885820313602.json, 视频生成/图生视频/MiniMax H3-单采_2102816230406189058.json, 视频生成/文生视频/H3最强电影LORA+巅峰双采去油PRO版_2094788799023894529.json, 视频生成/文生视频/MiniMax H3 8.29_2093713039521566722.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_19

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/AITUDOU-MiniMax H3 Skill2.0 全能参考版单采_2098354620342030337.json、视频生成/图生视频/AITUDOU-MiniMax H3 打斗-单采_2095430334602113026.json、视频生成/图生视频/AITUDOU-MiniMax H3 打斗-双采_2095430950619537409.json、视频生成/图生视频/AITUDOU-MiniMax H3 配合Skill短片自用-双采_2093313656774807553.json、视频生成/图生视频/AITUDOU-MiniMax H3 配合Skill自用短片-单采_2093313597047918594.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：43%

## 共有节点

全部 17 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `Float`
- `GetNode`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `ResolutionSelector`
- `SetNode`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 16/17 个有
- `BasicGuider` —— 15/17 个有
- `RandomNoise` —— 15/17 个有
- `SamplerCustomAdvanced` —— 15/17 个有
- `Fast Groups Bypasser (rgthree)` —— 14/17 个有
- `Label (rgthree)` —— 13/17 个有
- `SplitSigmas` —— 12/17 个有
- `H3SigmaRefiner` —— 9/17 个有
- `LTXVSeparateAVLatent` —— 9/17 个有
- `MinimaxH3LatentUpscaler3D` —— 8/17 个有
- `ModelAttentionBackend` —— 8/17 个有
- `LTXVConcatAVLatent` —— 6/17 个有
- `ExtendIntermediateSigmas` —— 3/17 个有
- `PT_H3ConcatAVLatent` —— 3/17 个有
- `PrimitiveFloat` —— 3/17 个有
- `SolAttnMiniMax` —— 3/17 个有
- `easy cleanGpuUsed` —— 3/17 个有
- `ConditioningZeroOut` —— 2/17 个有
- `LoadAudio` —— 2/17 个有
- `SelfLiftH3Sampler` —— 2/17 个有
- `AudioSeparation` —— 1/17 个有
- `LoraLoaderBypassModelOnly` —— 1/17 个有
- `MiniMaxH3BlockCacheT8` —— 1/17 个有
- `MiniMaxH3VoiceLibraryLoadT8` —— 1/17 个有
- `MinimaxH3LatentUpscalerNode3D` —— 1/17 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

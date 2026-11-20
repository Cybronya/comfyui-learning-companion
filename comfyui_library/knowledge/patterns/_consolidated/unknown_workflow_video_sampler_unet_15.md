---
name: unknown_workflow_video_sampler_unet_15
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.466278
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, Float, KSamplerSelect, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, ResolutionSelector, Text, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/AITUDOU-MiniMax+H3+lightx2v+8step+高动态加速流_2088160159993516034.json, 图片生成/图生图/AITUDOU-MiniMax_H3_短剧公司版本_2113459502426185730.json, 图片生成/文生图/MiniMax H3 短剧生成 _ 9图3音色参考 _ 省算力高动态加速版_2091615916835557378.json, 视频生成/图生视频/AITUDOU-MiniMax H3 Skill2.0 全能参考版单采_2098354620342030337.json, 视频生成/图生视频/AITUDOU-MiniMax H3 打斗-单采_2095430334602113026.json, 视频生成/图生视频/AITUDOU-MiniMax H3 打斗-双采_2095430950619537409.json, 视频生成/图生视频/AITUDOU-MiniMax H3 短剧公司版本_2113173574050729986.json, 视频生成/图生视频/AITUDOU-MiniMax H3 配合Skill短片自用-双采_2093313656774807553.json, 视频生成/图生视频/AITUDOU-MiniMax H3 配合Skill自用短片-单采_2093313597047918594.json, 视频生成/图生视频/AITUDOU-MiniMax H3 配合Skill自用短片-单采_2094575888913485825.json, 视频生成/图生视频/AITUDOU-MiniMax+H3+SelfLift+影视级情绪表达+SKILL_2104111411025764354.json, 视频生成/图生视频/AITUDOU-MiniMax+H3+SelfLift+影视级情绪表达+SKILL_2106320510052298754.json, 视频生成/图生视频/Fused-MiniMax H3 战斗增强-1280单采_2097598203356073986.json, 视频生成/图生视频/Fused-MiniMax H3-战斗增强-双采_2097606528458121218.json, 视频生成/图生视频/H3最强电影LORA+巅峰双采去油PRO版_2100507019949203458.json, 视频生成/图生视频/MiniMax H3 双采样 潜空间放大DSW（二次优化）_2095748408920330241.json, 视频生成/图生视频/MiniMax H3 双采样 潜空间放大_2090792067181137921.json, 视频生成/图生视频/MiniMax H3 双采样 潜空间放大（二次优化）_2091136885820313602.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_15

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/AITUDOU-MiniMax+H3+lightx2v+8step+高动态加速流_2088160159993516034.json、图片生成/图生图/AITUDOU-MiniMax_H3_短剧公司版本_2113459502426185730.json、图片生成/文生图/MiniMax H3 短剧生成 _ 9图3音色参考 _ 省算力高动态加速版_2091615916835557378.json、视频生成/图生视频/AITUDOU-MiniMax H3 Skill2.0 全能参考版单采_2098354620342030337.json、视频生成/图生视频/AITUDOU-MiniMax H3 打斗-单采_2095430334602113026.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：47%

## 共有节点

全部 18 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `Float`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `ResolutionSelector`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 17/18 个有
- `LoraLoaderModelOnly` —— 17/18 个有
- `SetNode` —— 17/18 个有
- `BasicGuider` —— 16/18 个有
- `RandomNoise` —— 16/18 个有
- `SamplerCustomAdvanced` —— 16/18 个有
- `Label (rgthree)` —— 15/18 个有
- `Fast Groups Bypasser (rgthree)` —— 13/18 个有
- `SplitSigmas` —— 10/18 个有
- `H3SigmaRefiner` —— 9/18 个有
- `LTXVSeparateAVLatent` —— 7/18 个有
- `ModelAttentionBackend` —— 7/18 个有
- `MinimaxH3LatentUpscaler3D` —— 6/18 个有
- `LoadAudio` —— 5/18 个有
- `ConditioningZeroOut` —— 4/18 个有
- `LTXVConcatAVLatent` —— 4/18 个有
- `SelfLiftH3Sampler` —— 4/18 个有
- `PT_H3ConcatAVLatent` —— 3/18 个有
- `PrimitiveFloat` —— 3/18 个有
- `SolAttnMiniMax` —— 3/18 个有
- `easy cleanGpuUsed` —— 3/18 个有
- `ExtendIntermediateSigmas` —— 2/18 个有
- `AudioSeparation` —— 1/18 个有
- `EmptyImage` —— 1/18 个有
- `LoraLoaderBypassModelOnly` —— 1/18 个有
- `MiniMaxH3VoiceLibraryLoadT8` —— 1/18 个有
- `MinimaxH3LatentUpscalerNode3D` —— 1/18 个有
- `PreviewImage` —— 1/18 个有
- `SaveImage` —— 1/18 个有
- `SigmasGraph` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

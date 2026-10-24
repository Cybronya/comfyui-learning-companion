---
name: unknown_workflow_video_sampler_unet_26
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.451462
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, GetNode, KSamplerSelect, Label (rgthree), LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, ResolutionSelector, SetNode, Text, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/AITUDOU-MiniMax+H3+SelfLift+影视级情绪表达+SKILL_2104111411025764354.json, 视频生成/图生视频/AITUDOU-MiniMax+H3+SelfLift+影视级情绪表达+SKILL_2106320510052298754.json, 视频生成/图生视频/AITUDOU-MiniMax+H3+lightx2v+8step+高动态加速流_2087230947061223426.json, 视频生成/图生视频/AITUDOU-MiniMax+H3+全能参考+数字人+人物音频一致性_2086164860592807937.json, 视频生成/图生视频/AITUDOU-MiniMax+H3+全能参考（1280分辨率）加速流_2085330061422579714.json, 视频生成/图生视频/Fused-MiniMax H3 战斗增强-1280单采_2097598203356073986.json, 视频生成/图生视频/MiniMax H3 DSW全能多参1280分辨率加速工作流_2092879864431988738.json, 视频生成/图生视频/MiniMax H3 全能多参1280分辨率3_4Harness专用_2094567538721116161.json, 视频生成/图生视频/MiniMax H3 全能多参1280分辨率加速工作流_2085980820623413250.json, 视频生成/图生视频/MiniMax H3 全能多参DSW工作流Harness专用_2095550051505491970.json, 视频生成/图生视频/MiniMax H3 双采样 潜空间放大DSW（二次优化）_2095748408920330241.json, 视频生成/图生视频/MiniMax H3 双采样 潜空间放大_2090792067181137921.json, 视频生成/图生视频/MiniMax H3 双采样 潜空间放大（二次优化）_2091136885820313602.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_26

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/AITUDOU-MiniMax+H3+SelfLift+影视级情绪表达+SKILL_2104111411025764354.json、视频生成/图生视频/AITUDOU-MiniMax+H3+SelfLift+影视级情绪表达+SKILL_2106320510052298754.json、视频生成/图生视频/AITUDOU-MiniMax+H3+lightx2v+8step+高动态加速流_2087230947061223426.json、视频生成/图生视频/AITUDOU-MiniMax+H3+全能参考+数字人+人物音频一致性_2086164860592807937.json、视频生成/图生视频/AITUDOU-MiniMax+H3+全能参考（1280分辨率）加速流_2085330061422579714.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：45%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `KSamplerSelect`
- `Label (rgthree)`
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
- `LoraLoaderModelOnly` —— 12/13 个有
- `BasicGuider` —— 11/13 个有
- `RandomNoise` —— 11/13 个有
- `SamplerCustomAdvanced` —— 11/13 个有
- `Float` —— 8/13 个有
- `PrimitiveFloat` —— 8/13 个有
- `SigmasGraph` —— 7/13 个有
- `H3SigmaRefiner` —— 6/13 个有
- `LoadAudio` —— 6/13 个有
- `ModelAttentionBackend` —— 5/13 个有
- `SolAttnMiniMax` —— 4/13 个有
- `VHS_LoadVideo` —— 4/13 个有
- `Fast Groups Bypasser (rgthree)` —— 3/13 个有
- `LTXVSeparateAVLatent` —— 3/13 个有
- `PT_H3ConcatAVLatent` —— 3/13 个有
- `SplitSigmas` —— 3/13 个有
- `easy cleanGpuUsed` —— 3/13 个有
- `ConditioningZeroOut` —— 2/13 个有
- `LoadVideo` —— 2/13 个有
- `LoraLoaderBypassModelOnly` —— 2/13 个有
- `MinimaxH3LatentUpscaler3D` —— 2/13 个有
- `SelfLiftH3Sampler` —— 2/13 个有
- `ExtendIntermediateSigmas` —— 1/13 个有
- `MinimaxH3LatentUpscalerNode3D` —— 1/13 个有
- `PreviewAny` —— 1/13 个有
- `RH_LLMAPI_Pro_Node` —— 1/13 个有
- `ZNGB_AudioCrop` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

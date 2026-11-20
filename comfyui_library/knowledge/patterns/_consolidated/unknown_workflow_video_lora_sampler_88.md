---
name: unknown_workflow_video_lora_sampler_88
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.463056
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, Float, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, Text, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/AITUDOU-MiniMax+H3+lightx2v+8step+高动态加速流_2088160159993516034.json, 图片生成/图生图/AITUDOU-MiniMax_H3_短剧公司版本_2113459502426185730.json, 图片生成/文生图/MiniMax H3 短剧生成 _ 9图3音色参考 _ 省算力高动态加速版_2091615916835557378.json, 平台全量/AITUDOU-MiniMax H3 Skill2.0 全能参考版单采_2099072668573196290.json, 平台全量/MiniMax H3 短剧创作-分镜视频工作流_2115395659619721218.json, 平台全量/MiniMax_H3_短剧创作-分镜视频工作流_2117815235531853825.json, 平台全量/短剧制作全流程-MiniMax H3 分镜视频工作流_2117640914402373633.json, 视频生成/图生视频/AITUDOU-MiniMax H3 Skill2.0 全能参考版单采_2098354620342030337.json, 视频生成/图生视频/AITUDOU-MiniMax H3 打斗-单采_2095430334602113026.json, 视频生成/图生视频/AITUDOU-MiniMax H3 打斗-双采_2095430950619537409.json, 视频生成/图生视频/AITUDOU-MiniMax H3 短剧公司版本_2113173574050729986.json, 视频生成/图生视频/AITUDOU-MiniMax H3 配合Skill短片自用-双采_2093313656774807553.json, 视频生成/图生视频/Fused-MiniMax H3 战斗增强-1280单采_2097598203356073986.json, 视频生成/图生视频/Fused-MiniMax H3-战斗增强-双采_2097606528458121218.json, 视频生成/图生视频/H3最强电影LORA+巅峰双采去油PRO版_2100507019949203458.json, 视频生成/图生视频/MiniMax_H3-单采_2106176867115036673.json, 视频生成/文生视频/H3最强电影LORA+巅峰双采去油PRO版_2094788799023894529.json, 视频生成/文生视频/MiniMax H3 8.29_2093713039521566722.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_88

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/AITUDOU-MiniMax+H3+lightx2v+8step+高动态加速流_2088160159993516034.json、图片生成/图生图/AITUDOU-MiniMax_H3_短剧公司版本_2113459502426185730.json、图片生成/文生图/MiniMax H3 短剧生成 _ 9图3音色参考 _ 省算力高动态加速版_2091615916835557378.json、平台全量/AITUDOU-MiniMax H3 Skill2.0 全能参考版单采_2099072668573196290.json、平台全量/MiniMax H3 短剧创作-分镜视频工作流_2115395659619721218.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：46%

## 共有节点

全部 18 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `Float`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 17/18 个有
- `SetNode` —— 17/18 个有
- `Fast Groups Bypasser (rgthree)` —— 16/18 个有
- `H3SigmaRefiner` —— 9/18 个有
- `Label (rgthree)` —— 9/18 个有
- `LoadAudio` —— 8/18 个有
- `SplitSigmas` —— 8/18 个有
- `LTXVConcatAVLatent` —— 6/18 个有
- `LTXVSeparateAVLatent` —— 6/18 个有
- `MinimaxH3LatentUpscaler3D` —— 6/18 个有
- `ConditioningZeroOut` —— 5/18 个有
- `ModelAttentionBackend` —— 5/18 个有
- `SelfLiftH3Sampler` —— 5/18 个有
- `ExtendIntermediateSigmas` —— 3/18 个有
- `孤海注释` —— 3/18 个有
- `AudioSeparation` —— 2/18 个有
- `EmptyImage` —— 2/18 个有
- `PreviewImage` —— 2/18 个有
- `MiniMaxH3BlockCacheT8` —— 1/18 个有
- `MiniMaxH3VoiceLibraryLoadT8` —— 1/18 个有
- `SaveImage` —— 1/18 个有
- `SigmasGraph` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

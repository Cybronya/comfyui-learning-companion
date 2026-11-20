---
name: unknown_workflow_sampler_unet_vae_38
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.538067
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/H3fast-v2全参加速_2114204441510502401.json, 图片生成/图生图/H3fast-v2全参加速_2114209096059678722.json, 图片生成/图生图/H3无损融合单采【官方满血API画布级本地流】_2114199673937420289.json, 图片生成/图生图/H3融合模型专属双采【16步高清PLUS_低显存危！】_2114200843313565697.json, 图片生成/图生图/MiniMax H3-多参考生视频-666_2106965266444935170.json, 图片生成/图生图/小脸不崩！打斗不糊！H3_sigma强化+潜空间放大工作流（不油啦！）_2113788878191681537.json, 图片生成/文生图/MiniMax H3-多参考生视频（8.31最佳）_2094270099418079233.json, 数字人/数字人/H3二采_2111323289078550530.json, 数字人/数字人/MiniMax H3-多参考生视频-优化版_2111992528827412482.json, 视频生成/图生视频/H3融合模型专属双采【16步高清PLUS 低显存危！】_2111450243706482690.json, 视频生成/图生视频/MiniMax H3 sigma强化+潜空间放大工作流-小脸不崩-脸不油，高动态不崩脸_2093136040067428353.json, 视频生成/图生视频/MiniMax H3-多参考生视频-高质量hybrid_2095884837700853761.json, 视频生成/图生视频/小脸不崩！打斗不糊！H3_sigma强化+潜空间放大工作流不油啦！_2113764205437476866.json, 视频生成/图生视频/小脸不崩！打斗不糊！H3_sigma强化+潜空间放大工作流不油啦！_2113765550089396225.json, 视频生成/文生视频/Minimax H3优化！浅空间二次放大！优化小脸和打斗_2087552804436140033.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_38

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/H3fast-v2全参加速_2114204441510502401.json、图片生成/图生图/H3fast-v2全参加速_2114209096059678722.json、图片生成/图生图/H3无损融合单采【官方满血API画布级本地流】_2114199673937420289.json、图片生成/图生图/H3融合模型专属双采【16步高清PLUS_低显存危！】_2114200843313565697.json、图片生成/图生图/MiniMax H3-多参考生视频-666_2106965266444935170.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：54%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 13/15 个有
- `LoraLoaderModelOnly` —— 13/15 个有
- `SetNode` —— 13/15 个有
- `LTXVConcatAVLatent` —— 12/15 个有
- `LTXVSeparateAVLatent` —— 12/15 个有
- `MinimaxH3LatentUpscaler3D` —— 12/15 个有
- `SplitSigmas` —— 12/15 个有
- `ModelAttentionBackend` —— 11/15 个有
- `LoadAudio` —— 10/15 个有
- `MiniMaxH3SigmaShift` —— 9/15 个有
- `VHS_VideoCombine` —— 9/15 个有
- `ModelPreviewOverrideKJ` —— 8/15 个有
- `PrimitiveStringMultiline` —— 8/15 个有
- `VHS_LoadVideo` —— 8/15 个有
- `忽略多组孤海` —— 8/15 个有
- `CreateVideo` —— 7/15 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/15 个有
- `SaveVideo` —— 7/15 个有
- `easy float` —— 7/15 个有
- `PreviewImage` —— 6/15 个有
- `BlockSparseAttention` —— 5/15 个有
- `H3SigmaRefiner` —— 5/15 个有
- `Text` —— 5/15 个有
- `EmptyImage` —— 3/15 个有
- `JjkShowText` —— 3/15 个有
- `QwenH3PromptLocal` —— 3/15 个有
- `easy cleanGpuUsed` —— 3/15 个有
- `PainterVRAM` —— 2/15 个有
- `easy positive` —— 2/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/15 个有
- `ManualSigmas` —— 1/15 个有
- `MiniMaxLowVRAMAttention` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_video_sampler_unet_21
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.551067
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetNode, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, RandomNoise, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/AITUDOU-MiniMax-H3-FastVideo极速多参_2108436780260356097.json, 视频生成/图生视频/H3极速测试工作流_2109473161694760961.json, 视频生成/图生视频/H3融合模型专属双采【16步高清PLUS 低显存危！】_2111450243706482690.json, 视频生成/图生视频/H3超强工作流_2107296344921698306.json, 视频生成/图生视频/H3高质量全能参考（二采加速版）_2088785262628397058.json, 视频生成/图生视频/MINIMAX-H3 显存终极优化工作流_2090382657434767361.json, 视频生成/图生视频/MINIMAX-H3 武打戏特化工作流_2091850926716973058.json, 视频生成/图生视频/Minimax H3 game aisee_2102192548696641537.json, 视频生成/图生视频/Minimax_H3_第三视角游戏UI_2102925824583356417.json, 视频生成/图生视频/Minimax_H3_第三视角游戏UI_2103671322130862082.json, 视频生成/图生视频/Minimax_H3_第三视角游戏UI_2104844593358524418.json, 视频生成/文生视频/0912Singularity模型双采放大_2098568338380247042.json, 视频生成/文生视频/0916台词优化正反打镜头Singularity模型双采放大_2100172773640458242.json, 视频生成/文生视频/Minimax H3 Singularity 超双采放大（参考生视频）_2098158457118609410.json, 视频生成/文生视频/Minimax H3 第三视角（游戏UI）_2100511191582994433.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_21

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/AITUDOU-MiniMax-H3-FastVideo极速多参_2108436780260356097.json、视频生成/图生视频/H3极速测试工作流_2109473161694760961.json、视频生成/图生视频/H3融合模型专属双采【16步高清PLUS 低显存危！】_2111450243706482690.json、视频生成/图生视频/H3超强工作流_2107296344921698306.json、视频生成/图生视频/H3高质量全能参考（二采加速版）_2088785262628397058.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：55%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 14/15 个有
- `PrimitiveStringMultiline` —— 14/15 个有
- `ResolutionSelector` —— 14/15 个有
- `LTXVConcatAVLatent` —— 13/15 个有
- `LTXVSeparateAVLatent` —— 13/15 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 13/15 个有
- `PrimitiveFloat` —— 13/15 个有
- `BlockSparseAttention` —— 12/15 个有
- `LoraLoaderModelOnly` —— 12/15 个有
- `ModelAttentionBackend` —— 12/15 个有
- `SplitSigmas` —— 12/15 个有
- `easy float` —— 12/15 个有
- `VHS_LoadVideo` —— 11/15 个有
- `MiniMaxChunkFeedForward` —— 10/15 个有
- `MiniMaxLowVRAMAttention` —— 10/15 个有
- `忽略多组孤海` —— 9/15 个有
- `DisableNoise` —— 8/15 个有
- `ExtendIntermediateSigmas` —— 8/15 个有
- `Lora Loader Stack (rgthree)` —— 8/15 个有
- `MinimaxH3LatentUpscaler3D` —— 8/15 个有
- `LatentUpscaleBy` —— 5/15 个有
- `Fast Groups Bypasser (rgthree)` —— 4/15 个有
- `MiniMaxH3SigmaShift` —— 4/15 个有
- `ModelPreviewOverrideKJ` —— 4/15 个有
- `H3SigmaRefiner` —— 2/15 个有
- `Label (rgthree)` —— 2/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/15 个有
- `PreviewImage` —— 2/15 个有
- `Float` —— 1/15 个有
- `Int` —— 1/15 个有
- `JjkShowText` —— 1/15 个有
- `JjkText` —— 1/15 个有
- `RHLLMChatNode` —— 1/15 个有
- `Text` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

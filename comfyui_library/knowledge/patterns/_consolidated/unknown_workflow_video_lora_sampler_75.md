---
name: unknown_workflow_video_lora_sampler_75
type: Unknown Workflow
frequency: 19
level: moderate
coverage: 0.513789
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetNode, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3官方工作流 _ 首尾帧生成视频_2090003109429989378.json, 视频生成/图生视频/MiniMax+H3  9 图_2088611634561503233.json, 视频生成/图生视频/MiniMax+H3+lightx2v+8step_2088449363017293825.json, 视频生成/图生视频/MiniMax+H3-8.24_2091826993972203521.json, 视频生成/图生视频/MiniMax+H3-二采优化版_2102312716324130817.json, 视频生成/图生视频/MiniMax+H3-多参考生视频-优化版0909_2097580929232498689.json, 视频生成/图生视频/MiniMax+H3-多参考生视频（9图片+3视频+3音频）_2101587742454009857.json, 视频生成/图生视频/MiniMax+H3-多参考生视频（9图片+3视频+3音频）二采_2109901185510629378.json, 视频生成/图生视频/MiniMax_H3-多参考7P3A2V生视频-二采优化版_2100561807021797378.json, 视频生成/图生视频/MiniMax_H3-多参考7P3A2V生视频-优化版_2100555142960603138.json, 视频生成/图生视频/Minimax H3 Singularity V2双采工作流_2111850491918512130.json, 视频生成/图生视频/Minimax H3 game aisee_2102192548696641537.json, 视频生成/图生视频/Minimax_H3_第三视角游戏UI_2102925824583356417.json, 视频生成/图生视频/Minimax_H3_第三视角游戏UI_2103671322130862082.json, 视频生成/图生视频/Minimax_H3_第三视角游戏UI_2104844593358524418.json, 视频生成/文生视频/0912Singularity模型双采放大_2098568338380247042.json, 视频生成/文生视频/0916台词优化正反打镜头Singularity模型双采放大_2100172773640458242.json, 视频生成/文生视频/Minimax H3 Singularity 超双采放大（参考生视频）_2098158457118609410.json, 视频生成/文生视频/Minimax H3 第三视角（游戏UI）_2100511191582994433.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_75

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3官方工作流 _ 首尾帧生成视频_2090003109429989378.json、视频生成/图生视频/MiniMax+H3  9 图_2088611634561503233.json、视频生成/图生视频/MiniMax+H3+lightx2v+8step_2088449363017293825.json、视频生成/图生视频/MiniMax+H3-8.24_2091826993972203521.json、视频生成/图生视频/MiniMax+H3-二采优化版_2102312716324130817.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：51%

## 共有节点

全部 19 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 18/19 个有
- `VAEDecode` —— 18/19 个有
- `VAEDecodeAudio` —— 18/19 个有
- `LoadAudio` —— 17/19 个有
- `PrimitiveFloat` —— 17/19 个有
- `LTXVConcatAVLatent` —— 15/19 个有
- `LTXVSeparateAVLatent` —— 15/19 个有
- `SplitSigmas` —— 15/19 个有
- `VHS_LoadVideo` —— 14/19 个有
- `easy float` —— 14/19 个有
- `忽略多组孤海` —— 13/19 个有
- `MinimaxH3LatentUpscaler3D` —— 10/19 个有
- `ModelAttentionBackend` —— 10/19 个有
- `Text` —— 10/19 个有
- `BlockSparseAttention` —— 9/19 个有
- `DisableNoise` —— 9/19 个有
- `ExtendIntermediateSigmas` —— 9/19 个有
- `Lora Loader Stack (rgthree)` —— 9/19 个有
- `MiniMaxChunkFeedForward` —— 9/19 个有
- `MiniMaxLowVRAMAttention` —— 9/19 个有
- `PrimitiveStringMultiline` —— 9/19 个有
- `LatentUpscaleBy` —— 5/19 个有
- `PreviewImage` —— 3/19 个有
- `EmptyImage` —— 2/19 个有
- `Fast Groups Bypasser (rgthree)` —— 2/19 个有
- `Float` —— 2/19 个有
- `SigmasGraph` —— 2/19 个有
- `孤海注释` —— 2/19 个有
- `CreateVideo` —— 1/19 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/19 个有
- `MiniMaxH3AVDecodeT8` —— 1/19 个有
- `RunningHub Deepcleaner` —— 1/19 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

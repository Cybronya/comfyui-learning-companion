---
name: unknown_workflow_video_sampler_unet_10
type: Unknown Workflow
frequency: 24
level: moderate
coverage: 0.529542
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetNode, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/MINIMAX-H3】文戏-低配版_2098930194206781441.json, 图片生成/图生图/MINIMAX-H3】文戏-低配版_2098987992739303425.json, 图片生成/图生图/MINIMAX-H3】文戏-低配版_2099663709462425601.json, 图片生成/图生图/MiniMax H3-多参考生视频-666_2106965266444935170.json, 图片生成/图生图/【MINIMAX-H3】八月最强文戏-低配版_2100550270982909953.json, 图片生成/文生图/MINIMAX-H3 显存终极优化工作流_2090698454728269825.json, 图片生成/文生图/MiniMax H3-多参考生视频（8.31最佳）_2094270099418079233.json, 数字人/数字人/H3二采_2111323289078550530.json, 数字人/数字人/【MINIMAX-H3】八月最强文戏-低配版_2100034371259555842.json, 视频生成/图生视频/H3短剧工作流-低配版9.12_2099422256219906050.json, 视频生成/图生视频/H3融合模型专属双采【16步高清PLUS 低显存危！】_2111450243706482690.json, 视频生成/图生视频/MINIMAX-H3 显存终极优化工作流_2090382657434767361.json, 视频生成/图生视频/MINIMAX-H3 武打戏特化工作流_2091850926716973058.json, 视频生成/图生视频/MINIMAX-H3-全自动打斗武戏-15秒8分钟_2097790484570796033.json, 视频生成/图生视频/MINIMAX-H3开源 最强文戏-低配版_2094767825419333634.json, 视频生成/图生视频/MiniMax H3全能参考，二采放大_2092138431697735681.json, 视频生成/图生视频/Minimax H3 game aisee_2102192548696641537.json, 视频生成/图生视频/Minimax_H3_第三视角游戏UI_2102925824583356417.json, 视频生成/图生视频/Minimax_H3_第三视角游戏UI_2103671322130862082.json, 视频生成/图生视频/Minimax_H3_第三视角游戏UI_2104844593358524418.json, 视频生成/文生视频/0912Singularity模型双采放大_2098568338380247042.json, 视频生成/文生视频/0916台词优化正反打镜头Singularity模型双采放大_2100172773640458242.json, 视频生成/文生视频/Minimax H3 Singularity 超双采放大（参考生视频）_2098158457118609410.json, 视频生成/文生视频/Minimax H3 第三视角（游戏UI）_2100511191582994433.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_10

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（图片生成/图生图/MINIMAX-H3】文戏-低配版_2098930194206781441.json、图片生成/图生图/MINIMAX-H3】文戏-低配版_2098987992739303425.json、图片生成/图生图/MINIMAX-H3】文戏-低配版_2099663709462425601.json、图片生成/图生图/MiniMax H3-多参考生视频-666_2106965266444935170.json、图片生成/图生图/【MINIMAX-H3】八月最强文戏-低配版_2100550270982909953.json…）

- **类型**：Unknown Workflow
- **样本数**：24
- **可信度**：中等可信
- **平均知识覆盖**：53%

## 共有节点

全部 24 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LTXVConcatAVLatent` —— 23/24 个有
- `LTXVSeparateAVLatent` —— 23/24 个有
- `LoadAudio` —— 23/24 个有
- `LoraLoaderModelOnly` —— 23/24 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 23/24 个有
- `ModelAttentionBackend` —— 20/24 个有
- `忽略多组孤海` —— 19/24 个有
- `MinimaxH3LatentUpscaler3D` —— 18/24 个有
- `ExtendIntermediateSigmas` —— 16/24 个有
- `SplitSigmas` —— 16/24 个有
- `VHS_LoadVideo` —— 15/24 个有
- `PrimitiveStringMultiline` —— 13/24 个有
- `MiniMaxChunkFeedForward` —— 12/24 个有
- `MiniMaxLowVRAMAttention` —— 12/24 个有
- `easy float` —— 12/24 个有
- `H3SigmaRefiner` —— 11/24 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 11/24 个有
- `PreviewImage` —— 11/24 个有
- `BlockSparseAttention` —— 9/24 个有
- `CR Prompt Text` —— 9/24 个有
- `DisableNoise` —— 8/24 个有
- `INTConstant` —— 8/24 个有
- `Lora Loader Stack (rgthree)` —— 8/24 个有
- `LatentUpscaleBy` —— 5/24 个有
- `MiniMaxH3SigmaShift` —— 5/24 个有
- `ModelPreviewOverrideKJ` —— 5/24 个有
- `EmptyImage` —— 4/24 个有
- `Fast Groups Bypasser (rgthree)` —— 4/24 个有
- `Text` —— 3/24 个有
- `PreviewAny` —— 1/24 个有
- `RH_LLMAPI_Pro_Node` —— 1/24 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

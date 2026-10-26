---
name: unknown_workflow_sampler_unet_vae_64
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.550083
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/MINIMAX-H3】文戏-低配版_2098930194206781441.json, 图片生成/图生图/MINIMAX-H3】文戏-低配版_2098987992739303425.json, 图片生成/图生图/MINIMAX-H3】文戏-低配版_2099663709462425601.json, 图片生成/图生图/MiNiMaxH3_六图+三音频参考_2114212580704219138.json, 图片生成/图生图/【MINIMAX-H3】八月最强文戏-低配版_2100550270982909953.json, 图片生成/文生图/MINIMAX-H3 显存终极优化工作流_2090698454728269825.json, 数字人/数字人/【MINIMAX-H3】八月最强文戏-低配版_2100034371259555842.json, 视频生成/图生视频/H3短剧工作流-低配版9.12_2099422256219906050.json, 视频生成/图生视频/H3视频衔接_2095145130473902082.json, 视频生成/图生视频/MINIMAX-H3 显存终极优化工作流_2090382657434767361.json, 视频生成/图生视频/MINIMAX-H3 武打戏特化工作流_2091850926716973058.json, 视频生成/图生视频/MINIMAX-H3-全自动打斗武戏-15秒8分钟_2097790484570796033.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_64

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/MINIMAX-H3】文戏-低配版_2098930194206781441.json、图片生成/图生图/MINIMAX-H3】文戏-低配版_2098987992739303425.json、图片生成/图生图/MINIMAX-H3】文戏-低配版_2099663709462425601.json、图片生成/图生图/MiNiMaxH3_六图+三音频参考_2114212580704219138.json、图片生成/图生图/【MINIMAX-H3】八月最强文戏-低配版_2100550270982909953.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：55%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
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
- `GetNode` —— 11/12 个有
- `H3SigmaRefiner` —— 11/12 个有
- `LTXVConcatAVLatent` —— 11/12 个有
- `LTXVSeparateAVLatent` —— 11/12 个有
- `LoadAudio` —— 11/12 个有
- `LoraLoaderModelOnly` —— 11/12 个有
- `MinimaxH3LatentUpscaler3D` —— 11/12 个有
- `ModelAttentionBackend` —— 11/12 个有
- `PreviewImage` —— 11/12 个有
- `SetNode` —— 11/12 个有
- `VHS_VideoCombine` —— 11/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/12 个有
- `INTConstant` —— 8/12 个有
- `忽略多组孤海` —— 8/12 个有
- `CR Prompt Text` —— 7/12 个有
- `ExtendIntermediateSigmas` —— 7/12 个有
- `PrimitiveStringMultiline` —— 6/12 个有
- `MiniMaxChunkFeedForward` —— 5/12 个有
- `MiniMaxLowVRAMAttention` —— 5/12 个有
- `VHS_LoadVideo` —— 5/12 个有
- `EmptyImage` —— 4/12 个有
- `MiniMaxH3SigmaShift` —— 4/12 个有
- `ModelPreviewOverrideKJ` —— 4/12 个有
- `SplitSigmas` —— 4/12 个有
- `Fast Groups Bypasser (rgthree)` —— 3/12 个有
- `CreateVideo` —— 1/12 个有
- `FL_UnloadAllModels` —— 1/12 个有
- `GetImageRangeFromBatch` —— 1/12 个有
- `LoraLoaderBypassModelOnly` —— 1/12 个有
- `MiniMaxH3AddGuide` —— 1/12 个有
- `PreviewAny` —— 1/12 个有
- `RH_LLMAPI_Pro_Node` —— 1/12 个有
- `SaveVideo` —— 1/12 个有
- `SolAttnMiniMax` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_video_upscale_latent_upscale_32
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.4334
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetNode, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, MinimaxH3LatentUpscaler3D, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/MiniMax-H3_全能参考_长视频_2108379264335831041.json, 视频生成/图生视频/MINIMAX-H3 显存终极优化工作流_2090382657434767361.json, 视频生成/图生视频/MINIMAX-H3 武打戏特化工作流_2091850926716973058.json, 视频生成/图生视频/MiniMax-H3_全能参考_长视频_2085702104550825985.json, 视频生成/图生视频/MiniMax-H3_全能参考_长视频_2105590333219364866.json, 视频生成/图生视频/MiniMax-H3_全能参考_长视频_2108378852060913666.json, 视频生成/图生视频/MiniMax-H3_全能参考_长视频_2116305572885782530.json, 视频生成/图生视频/MiniMax-H3_全能参考_长视频_2116387251621023746.json, 视频生成/文生视频/MiniMax-H3_全能参考_长视频_2085702104550825985.json, 视频生成/视频生视频/MiniMax-H3_全能参考_长视频_2085702104550825985.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_32

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（平台全量/MiniMax-H3_全能参考_长视频_2108379264335831041.json、视频生成/图生视频/MINIMAX-H3 显存终极优化工作流_2090382657434767361.json、视频生成/图生视频/MINIMAX-H3 武打戏特化工作流_2091850926716973058.json、视频生成/图生视频/MiniMax-H3_全能参考_长视频_2085702104550825985.json、视频生成/图生视频/MiniMax-H3_全能参考_长视频_2105590333219364866.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：43%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `MinimaxH3LatentUpscaler3D`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ModelAttentionBackend` —— 9/10 个有
- `Any Switch (rgthree)` —— 8/10 个有
- `ExtendIntermediateSigmas` —— 8/10 个有
- `Fast Groups Bypasser (rgthree)` —— 8/10 个有
- `GetImageRangeFromBatch` —— 8/10 个有
- `INTConstant` —— 8/10 个有
- `ImageAddNoise` —— 8/10 个有
- `ImageFromBatch` —— 8/10 个有
- `MiniMaxH3AddGuide` —— 8/10 个有
- `Seed (rgthree)` —— 8/10 个有
- `TrimAudioDuration` —— 8/10 个有
- `VHS_VideoInfoLoaded` —— 8/10 个有
- `BatchImagesNode` —— 7/10 个有
- `BlockSparseAttention` —— 5/10 个有
- `GetImagesFromBatchIndexed` —— 5/10 个有
- `PreviewAny` —— 5/10 个有
- `easy forLoopEnd` —— 5/10 个有
- `easy forLoopStart` —— 5/10 个有
- `easy ifElse` —— 5/10 个有
- `easy isNone` —— 5/10 个有
- `easy lengthAnything` —— 5/10 个有
- `easy promptConcat` —— 5/10 个有
- `easy showAnything` —— 4/10 个有
- `RepeatImageBatch` —— 3/10 个有
- `ComfySwitchNode` —— 2/10 个有
- `ConditioningZeroOut` —— 2/10 个有
- `H3SigmaRefiner` —— 2/10 个有
- `ImageScaleToTotalPixels` —— 2/10 个有
- `MiniMaxChunkFeedForward` —— 2/10 个有
- `MiniMaxLowVRAMAttention` —— 2/10 个有
- `PreviewImage` —— 2/10 个有
- `SelfLiftH3Sampler` —— 2/10 个有
- `忽略多组孤海` —— 2/10 个有
- `ColorTransfer` —— 1/10 个有
- `PrimitiveBoolean` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

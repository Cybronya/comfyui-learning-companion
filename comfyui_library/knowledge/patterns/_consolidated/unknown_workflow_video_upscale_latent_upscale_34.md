---
name: unknown_workflow_video_upscale_latent_upscale_34
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.407
common_nodes: [Any Switch (rgthree), BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, ExtendIntermediateSigmas, Fast Groups Bypasser (rgthree), GetImageRangeFromBatch, GetNode, ImageAddNoise, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, MiniMaxH3AddGuide, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3SigmaShift, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, ModelPreviewOverrideKJ, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, Seed (rgthree), SetNode, TrimAudioDuration, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax-H3_全能参考_长视频_2085702104550825985.json, 视频生成/图生视频/MiniMax-H3_全能参考_长视频_2105590333219364866.json, 视频生成/图生视频/MiniMax-H3_全能参考_长视频_2108378852060913666.json, 视频生成/图生视频/MiniMax-H3_导演台长视频_2097299993232236545.json, 视频生成/图生视频/MiniMax-H3_导演台长视频_2103031580498415618.json, 视频生成/图生视频/MiniMax-H3_导演台长视频_2105589907493314562.json, 视频生成/图生视频/MiniMax-H3_导演台长视频_2108378297288712194.json, 视频生成/文生视频/MiniMax-H3_全能参考_长视频_2085702104550825985.json, 视频生成/视频生视频/MiniMax-H3_全能参考_长视频_2085702104550825985.json, 视频生成/视频生视频/MiniMax-H3_导演台长视频_2097299993232236545.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_34

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3_全能参考_长视频_2085702104550825985.json、视频生成/图生视频/MiniMax-H3_全能参考_长视频_2105590333219364866.json、视频生成/图生视频/MiniMax-H3_全能参考_长视频_2108378852060913666.json、视频生成/图生视频/MiniMax-H3_导演台长视频_2097299993232236545.json、视频生成/图生视频/MiniMax-H3_导演台长视频_2103031580498415618.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：41%

## 共有节点

全部 10 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ExtendIntermediateSigmas`
- `Fast Groups Bypasser (rgthree)`
- `GetImageRangeFromBatch`
- `GetNode`
- `ImageAddNoise`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `MiniMaxH3AddGuide`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3SigmaShift`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `Seed (rgthree)`
- `SetNode`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 9/10 个有
- `VHS_VideoInfoLoaded` —— 9/10 个有
- `SplitSigmas` —— 8/10 个有
- `easy forLoopEnd` —— 8/10 个有
- `easy forLoopStart` —— 8/10 个有
- `easy showAnything` —— 7/10 个有
- `PrimitiveBoolean` —— 6/10 个有
- `BatchImagesNode` —— 5/10 个有
- `BlockSparseAttention` —— 5/10 个有
- `ComfySwitchNode` —— 5/10 个有
- `GetVideoComponents` —— 5/10 个有
- `ImageFromBatch` —— 5/10 个有
- `LoadAudio` —— 5/10 个有
- `LoadImage` —— 5/10 个有
- `MiniMaxH3ReferenceToVideo` —— 5/10 个有
- `PreviewImage` —— 5/10 个有
- `PrimitiveFloat` —— 5/10 个有
- `PrimitiveInt` —— 5/10 个有
- `PrimitiveStringMultiline` —— 5/10 个有
- `easy anythingInversedSwitch` —— 5/10 个有
- `easy batchAnything` —— 5/10 个有
- `easy cleanGpuUsed` —— 5/10 个有
- `easy mergeVideosFromPaths` —— 5/10 个有
- `easy minimaxH3ToVideo` —— 5/10 个有
- `easy multiTrackEditor` —— 5/10 个有
- `easy multiTrackInfoOutput` —— 5/10 个有
- `easy multiTrackTaskOutput` —— 5/10 个有
- `easy saveVideo` —— 5/10 个有
- `GetImagesFromBatchIndexed` —— 3/10 个有
- `PreviewAny` —— 3/10 个有
- `easy ifElse` —— 3/10 个有
- `easy isNone` —— 3/10 个有
- `easy lengthAnything` —— 3/10 个有
- `easy promptConcat` —— 3/10 个有
- `RepeatImageBatch` —— 2/10 个有
- `ColorTransfer` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

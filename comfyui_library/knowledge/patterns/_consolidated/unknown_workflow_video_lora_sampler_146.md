---
name: unknown_workflow_video_lora_sampler_146
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.413154
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, ExtendIntermediateSigmas, GetImageRangeFromBatch, GetNode, ImageAddNoise, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, MiniMaxH3AddGuide, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3SigmaShift, ModelAttentionBackend, ModelPreviewOverrideKJ, RandomNoise, SamplerCustomAdvanced, Seed (rgthree), SetNode, TrimAudioDuration, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax-H3_全能参考_长视频_2085702104550825985.json, 视频生成/图生视频/MiniMax-H3_全能参考_长视频_2105590333219364866.json, 视频生成/图生视频/MiniMax-H3_全能参考_长视频_2108378852060913666.json, 视频生成/图生视频/MiniMax-H3_导演台长视频_2097299993232236545.json, 视频生成/图生视频/MiniMax-H3_导演台长视频_2103031580498415618.json, 视频生成/图生视频/MiniMax-H3_导演台长视频_2105589907493314562.json, 视频生成/图生视频/MiniMax-H3_导演台长视频_2108378297288712194.json, 视频生成/图生视频/MiniMax-H3_导演台长视频_2113647217943859201.json, 视频生成/图生视频/MiniMax-H3_导演台长视频_2113786461760876545.json, 视频生成/图生视频/MiniMax-H3_导演台长视频_2113787802507894786.json, 视频生成/文生视频/MiniMax-H3_全能参考_长视频_2085702104550825985.json, 视频生成/视频生视频/MiniMax-H3_全能参考_长视频_2085702104550825985.json, 视频生成/视频生视频/MiniMax-H3_导演台长视频_2097299993232236545.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_146

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3_全能参考_长视频_2085702104550825985.json、视频生成/图生视频/MiniMax-H3_全能参考_长视频_2105590333219364866.json、视频生成/图生视频/MiniMax-H3_全能参考_长视频_2108378852060913666.json、视频生成/图生视频/MiniMax-H3_导演台长视频_2097299993232236545.json、视频生成/图生视频/MiniMax-H3_导演台长视频_2103031580498415618.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：41%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ExtendIntermediateSigmas`
- `GetImageRangeFromBatch`
- `GetNode`
- `ImageAddNoise`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `MiniMaxH3AddGuide`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `RandomNoise`
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
- `INTConstant` —— 12/13 个有
- `VHS_VideoInfoLoaded` —— 12/13 个有
- `easy forLoopEnd` —— 11/13 个有
- `easy forLoopStart` —— 11/13 个有
- `Any Switch (rgthree)` —— 10/13 个有
- `Fast Groups Bypasser (rgthree)` —— 10/13 个有
- `LTXVConcatAVLatent` —— 10/13 个有
- `LTXVSeparateAVLatent` —— 10/13 个有
- `MinimaxH3LatentUpscaler3D` —— 10/13 个有
- `ResolutionSelector` —— 10/13 个有
- `easy showAnything` —— 10/13 个有
- `PrimitiveBoolean` —— 9/13 个有
- `BatchImagesNode` —— 8/13 个有
- `BlockSparseAttention` —— 8/13 个有
- `ComfySwitchNode` —— 8/13 个有
- `GetVideoComponents` —— 8/13 个有
- `PreviewImage` —— 8/13 个有
- `PrimitiveInt` —— 8/13 个有
- `SplitSigmas` —— 8/13 个有
- `easy anythingInversedSwitch` —— 8/13 个有
- `easy batchAnything` —— 8/13 个有
- `easy cleanGpuUsed` —— 8/13 个有
- `easy mergeVideosFromPaths` —— 8/13 个有
- `easy minimaxH3ToVideo` —— 8/13 个有
- `easy multiTrackEditor` —— 8/13 个有
- `easy multiTrackInfoOutput` —— 8/13 个有
- `easy multiTrackTaskOutput` —— 8/13 个有
- `easy saveVideo` —— 8/13 个有
- `ImageFromBatch` —— 5/13 个有
- `LoadAudio` —— 5/13 个有
- `LoadImage` —— 5/13 个有
- `MiniMaxH3ReferenceToVideo` —— 5/13 个有
- `PrimitiveFloat` —— 5/13 个有
- `PrimitiveStringMultiline` —— 5/13 个有
- `ConditioningZeroOut` —— 3/13 个有
- `GetImagesFromBatchIndexed` —— 3/13 个有
- `PreviewAny` —— 3/13 个有
- `SelfLiftH3Sampler` —— 3/13 个有
- `easy anythingIndexSwitch` —— 3/13 个有
- `easy ifElse` —— 3/13 个有
- `easy isNone` —— 3/13 个有
- `easy lengthAnything` —— 3/13 个有
- `easy promptConcat` —— 3/13 个有
- `EmptyImage` —— 2/13 个有
- `RepeatImageBatch` —— 2/13 个有
- `ColorTransfer` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

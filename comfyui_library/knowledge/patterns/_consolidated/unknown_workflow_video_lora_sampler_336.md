---
name: unknown_workflow_video_lora_sampler_336
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.413667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, ComfySwitchNode, ExtendIntermediateSigmas, GetImageRangeFromBatch, GetNode, GetVideoComponents, ImageAddNoise, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, MiniMaxH3AddGuide, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3SigmaShift, ModelAttentionBackend, ModelPreviewOverrideKJ, PreviewImage, PrimitiveBoolean, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, Seed (rgthree), SetNode, TrimAudioDuration, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine, easy anythingInversedSwitch, easy batchAnything, easy cleanGpuUsed, easy forLoopEnd, easy forLoopStart, easy mergeVideosFromPaths, easy minimaxH3ToVideo, easy multiTrackEditor, easy multiTrackInfoOutput, easy multiTrackTaskOutput, easy saveVideo, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax-H3_导演台长视频_2097299993232236545.json, 视频生成/图生视频/MiniMax-H3_导演台长视频_2103031580498415618.json, 视频生成/图生视频/MiniMax-H3_导演台长视频_2105589907493314562.json, 视频生成/图生视频/MiniMax-H3_导演台长视频_2108378297288712194.json, 视频生成/图生视频/MiniMax-H3_导演台长视频_2113647217943859201.json, 视频生成/图生视频/MiniMax-H3_导演台长视频_2113786461760876545.json, 视频生成/图生视频/MiniMax-H3_导演台长视频_2113787802507894786.json, 视频生成/文生视频/MiniMax-H3_导演台长视频_2115629820280401921.json, 视频生成/视频生视频/MiniMax-H3_导演台长视频_2097299993232236545.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_336

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3_导演台长视频_2097299993232236545.json、视频生成/图生视频/MiniMax-H3_导演台长视频_2103031580498415618.json、视频生成/图生视频/MiniMax-H3_导演台长视频_2105589907493314562.json、视频生成/图生视频/MiniMax-H3_导演台长视频_2108378297288712194.json、视频生成/图生视频/MiniMax-H3_导演台长视频_2113647217943859201.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：41%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `ExtendIntermediateSigmas`
- `GetImageRangeFromBatch`
- `GetNode`
- `GetVideoComponents`
- `ImageAddNoise`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `MiniMaxH3AddGuide`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PreviewImage`
- `PrimitiveBoolean`
- `PrimitiveInt`
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
- `easy anythingInversedSwitch`
- `easy batchAnything`
- `easy cleanGpuUsed`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy mergeVideosFromPaths`
- `easy minimaxH3ToVideo`
- `easy multiTrackEditor`
- `easy multiTrackInfoOutput`
- `easy multiTrackTaskOutput`
- `easy saveVideo`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 8/9 个有
- `VHS_VideoInfoLoaded` —— 8/9 个有
- `BlockSparseAttention` —— 6/9 个有
- `ResolutionSelector` —— 6/9 个有
- `Any Switch (rgthree)` —— 5/9 个有
- `BatchImagesNode` —— 5/9 个有
- `Fast Groups Bypasser (rgthree)` —— 5/9 个有
- `LTXVConcatAVLatent` —— 5/9 个有
- `LTXVSeparateAVLatent` —— 5/9 个有
- `MinimaxH3LatentUpscaler3D` —— 5/9 个有
- `ConditioningZeroOut` —— 4/9 个有
- `SelfLiftH3Sampler` —— 4/9 个有
- `easy anythingIndexSwitch` —— 4/9 个有
- `SplitSigmas` —— 3/9 个有
- `EmptyImage` —— 2/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

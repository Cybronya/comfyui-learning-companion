---
name: unknown_workflow_video_lora_sampler_703
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.75325
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CR Text, ComfyMathExpression, CreateVideo, ExtendIntermediateSigmas, ImageFromBatch+, Int, KSamplerSelect, LazySwitchKJ, LoadImage, LoraLoaderModelOnly, MiniMaxH3AddGuide, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, ModelAttentionBackend, ModelPreviewOverrideKJ, PreviewAudio, PrimitiveBoolean, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, Seed (rgthree), SolAttnMiniMax, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideoPath, VHS_SelectFilename, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [平台全量/首尾视频生成视频_2105366155027374082.json, 数字人/数字人/海螺H3 视频引导生成视频 视频衔接_2105681969299410946.json, 数字人/数字人/视频引导生视频，视频衔接过渡_2105435289228496898.json, 视频生成/文生视频/Add Guide for MiniMax H3无限拼接长视频_2091906123728252929.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_703

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/首尾视频生成视频_2105366155027374082.json、数字人/数字人/海螺H3 视频引导生成视频 视频衔接_2105681969299410946.json、数字人/数字人/视频引导生视频，视频衔接过渡_2105435289228496898.json、视频生成/文生视频/Add Guide for MiniMax H3无限拼接长视频_2091906123728252929.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CR Text`
- `ComfyMathExpression`
- `CreateVideo`
- `ExtendIntermediateSigmas`
- `ImageFromBatch+`
- `Int`
- `KSamplerSelect`
- `LazySwitchKJ`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3AddGuide`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PreviewAudio`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `Seed (rgthree)`
- `SolAttnMiniMax`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideoPath`
- `VHS_SelectFilename`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AudioConcat` —— 3/4 个有
- `GetImageSizeAndCount` —— 3/4 个有
- `ImageBatchMulti` —— 3/4 个有
- `ImageFromBatch` —— 3/4 个有
- `MultiplicationNode` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `SaveVideo` —— 3/4 个有
- `SimpleMath+` —— 3/4 个有
- `SoundFlow_GetLength` —— 3/4 个有
- `SoundFlow_TrimAudio` —— 3/4 个有
- `YusuLoadVideoUI` —— 3/4 个有
- `GH_ImageVideoComparer` —— 2/4 个有
- `GoohaiRatioAndResolution` —— 2/4 个有
- `RH_LLMAPI_Pro_Node` —— 2/4 个有
- `ResolutionSelector` —— 2/4 个有
- `Text Find and Replace` —— 2/4 个有
- `Fast Bypasser (rgthree)` —— 1/4 个有
- `GetImageRangeFromBatch` —— 1/4 个有
- `ImpactExecutionOrderController` —— 1/4 个有
- `MiniMaxH3HybridLoader` —— 1/4 个有
- `MultiMergeVideos` —— 1/4 个有
- `SDVN Any List` —— 1/4 个有
- `TextSplitByDelimiter` —— 1/4 个有
- `TrimAudioDuration` —— 1/4 个有
- `easy indexAnything` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_lora_sampler_unet_48
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.442
common_nodes: [BasicScheduler, BatchCount+, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, CreateVideo, ExtendIntermediateSigmas, GetImageRangeFromBatch, GetNode, GetVideoComponents, H3AudioRefineSampler, H3FrozenVideoCache, ImageAddNoise, ImageBatchMulti, KSamplerSelect, LoadVideo, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AddGuide, MiniMaxH3AudioGuideFeather, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxLowVRAMAttention, ModelAttentionBackend, PathchSageAttentionKJ, PreviewAny, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, SaveVideo, SetNode, StringReplace, Text Concatenate, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VideoFrameSample, VideoTemporalCrop, easy batchAnything, easy float, easy forLoopEnd, easy forLoopStart, easy ifElse, easy indexAnything, easy lengthAnything, easy mergeVideosFromPaths, easy minimaxH3ToVideo, easy multiTrackEditor, easy multiTrackInfoOutput, easy multiTrackTaskOutput, easy promptLine, easy saveVideo, easy string]
problems: []
missing: []
members: [图片生成/反推提示词/MiniMax H3超灵活的导演台，SelfLift双采、无缝无色差超长视频 (2.0)_2106650378539458562.json, 图片生成/文生图/MiniMax H3超灵活的导演台，SelfLift双采、无缝衔接超长视频 (无缝双采1.5)_2100251279346987010.json, 视频生成/文生视频/MiniMax H3超灵活的导演台，双采、无缝衔接超长视频，音频修复(无缝1.0)_2096611262351364097.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_48

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/反推提示词/MiniMax H3超灵活的导演台，SelfLift双采、无缝无色差超长视频 (2.0)_2106650378539458562.json、图片生成/文生图/MiniMax H3超灵活的导演台，SelfLift双采、无缝衔接超长视频 (无缝双采1.5)_2100251279346987010.json、视频生成/文生视频/MiniMax H3超灵活的导演台，双采、无缝衔接超长视频，音频修复(无缝1.0)_2096611262351364097.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：44%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `BatchCount+`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `CreateVideo`
- `ExtendIntermediateSigmas`
- `GetImageRangeFromBatch`
- `GetNode`
- `GetVideoComponents`
- `H3AudioRefineSampler`
- `H3FrozenVideoCache`
- `ImageAddNoise`
- `ImageBatchMulti`
- `KSamplerSelect`
- `LoadVideo`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3AddGuide`
- `MiniMaxH3AudioGuideFeather`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `SaveVideo`
- `SetNode`
- `StringReplace`
- `Text Concatenate`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VideoFrameSample`
- `VideoTemporalCrop`
- `easy batchAnything`
- `easy float`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy ifElse`
- `easy indexAnything`
- `easy lengthAnything`
- `easy mergeVideosFromPaths`
- `easy minimaxH3ToVideo`
- `easy multiTrackEditor`
- `easy multiTrackInfoOutput`
- `easy multiTrackTaskOutput`
- `easy promptLine`
- `easy saveVideo`
- `easy string`

**可变部分**（部分 workflow 才有）：
- `SelfLiftH3Sampler` —— 2/3 个有
- `BasicGuider` —— 1/3 个有
- `ColorTransfer` —— 1/3 个有
- `ComfySwitchNode` —— 1/3 个有
- `LTXVConcatAVLatent` —— 1/3 个有
- `LTXVSeparateAVLatent` —— 1/3 个有
- `ManualSigmas` —— 1/3 个有
- `MinimaxH3LatentUpscaler3D` —— 1/3 个有
- `RandomNoise` —— 1/3 个有
- `SamplerCustomAdvanced` —— 1/3 个有
- `SplitSigmas` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

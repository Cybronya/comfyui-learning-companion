---
key: 图片生成/文生图/MiniMax H3超灵活的导演台，SelfLift双采、无缝衔接超长视频 (无缝双采1.5)_2100251279346987010.json
name: MiniMax H3超灵活的导演台，SelfLift双采、无缝衔接超长视频 (无缝双采1.5)_2100251279346987010
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/MiniMax H3超灵活的导演台，SelfLift双采、无缝衔接超长视频 (无缝双采1.5)_2100251279346987010.json
hash: 191918d1d42c6c82
coverage: 0.432331
learned_at: 2026-10-15 22:26:50
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, easy multiTrackInfoOutput, VAELoader, VAELoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, Note, GetNode, GetNode, ConditioningZeroOut, GetNode, easy mergeVideosFromPaths, ComfyMathExpression, Note, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, easy ifElse, SetNode, SetNode, easy string, GetNode, GetNode, ComfyMathExpression, SetNode, SetNode, easy ifElse, StringReplace, StringReplace, StringReplace, StringReplace, StringReplace, StringReplace, easy promptLine, easy lengthAnything, easy string, easy forLoopStart, Text Concatenate, easy forLoopEnd, GetNode, easy promptLine, ComfyMathExpression, easy indexAnything, easy mergeVideosFromPaths, VideoFrameSample, GetNode, GetNode, GetNode, SetNode, SetNode, easy lengthAnything, easy forLoopStart, easy promptLine, easy indexAnything, SetNode, SetNode, GetNode, easy forLoopEnd, easy batchAnything, MarkdownNote, MarkdownNote, ComfyMathExpression, easy mergeVideosFromPaths, easy ifElse, VideoFrameSample, ComfyMathExpression, easy indexAnything, easy lengthAnything, ComfyMathExpression, easy indexAnything, GetNode, easy ifElse, easy saveVideo, PrimitiveBoolean, SetNode, Note, SetNode, SetNode, SetNode, GetNode, ComfyMathExpression, ComfyMathExpression, SetNode, GetNode, easy ifElse, ComfyMathExpression, SetNode, GetNode, SetNode, GetNode, ComfyMathExpression, GetNode, GetNode, easy promptLine, PathchSageAttentionKJ, SetNode, SetNode, GetNode, easy mergeVideosFromPaths, easy multiTrackTaskOutput, GetNode, MarkdownNote, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, Reroute, SetNode, SetNode, PrimitiveInt, easy ifElse, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, easy batchAnything, SetNode, Reroute, Reroute, GetNode, Reroute, GetNode, GetNode, Reroute, Reroute, GetNode, Reroute, Reroute, easy forLoopStart, Reroute, SetNode, PreviewAny, GetNode, easy saveVideo, VAEDecode, VAEDecodeAudio, CreateVideo, GetNode, GetNode, GetNode, GetNode, SetNode, PreviewAny, easy forLoopEnd, SetNode, VideoFrameSample, GetNode, GetVideoComponents, PreviewAny, easy mergeVideosFromPaths, GetVideoComponents, BatchCount+, ComfyMathExpression, GetNode, VideoTemporalCrop, SaveVideo, SaveVideo, ComfyMathExpression, CLIPLoader, ImageAddNoise, GetImageRangeFromBatch, GetNode, GetNode, ImageBatchMulti, GetVideoComponents, MiniMaxH3AddGuide, GetImageRangeFromBatch, ImageAddNoise, ComfyMathExpression, GetImageRangeFromBatch, ImageBatchMulti, ImageAddNoise, ComfyMathExpression, SetNode, GetVideoComponents, VideoFrameSample, easy mergeVideosFromPaths, easy ifElse, Note, ComfyMathExpression, VideoFrameSample, easy ifElse, MiniMaxH3AddGuide, easy ifElse, Note, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxLowVRAMAttention, Note, ModelAttentionBackend, LoraLoaderBypassModelOnly, MiniMaxH3AudioGuideFeather, easy minimaxH3ToVideo, UNETLoader, ImageAddNoise, ImageAddNoise, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, SetNode, PrimitiveBoolean, PrimitiveBoolean, PrimitiveInt, PrimitiveInt, PreviewAny, H3FrozenVideoCache, H3AudioRefineSampler, GetImageRangeFromBatch, MiniMaxH3AddGuide, MiniMaxH3AudioGuideFeather, PrimitiveStringMultiline, PrimitiveInt, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, PrimitiveFloat, easy float, GetImageRangeFromBatch, ConditioningZeroOut, KSamplerSelect, Note, ExtendIntermediateSigmas, BasicScheduler, easy ifElse, GetNode, Reroute, Reroute, SetNode, GetNode, PrimitiveBoolean, PrimitiveBoolean, easy ifElse, PrimitiveFloat, PrimitiveInt, Note, Note, easy float, LoadVideo, SelfLiftH3Sampler, easy multiTrackEditor]
patterns: []
missing: []
---

# 图片生成/文生图/MiniMax H3超灵活的导演台，SelfLift双采、无缝衔接超长视频 (无缝双采1.5)_2100251279346987010.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/MiniMax H3超灵活的导演台，SelfLift双采、无缝衔接超长视频 (无缝双采1.5)_2100251279346987010.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（266 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy multiTrackInfoOutput`
- `VAELoader`
- `VAELoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `Note`
- `GetNode`
- `GetNode`
- `ConditioningZeroOut`
- `GetNode`
- `easy mergeVideosFromPaths`
- `ComfyMathExpression`
- `Note`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy ifElse`
- `SetNode`
- `SetNode`
- `easy string`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `SetNode`
- `SetNode`
- `easy ifElse`
- `StringReplace`
- `StringReplace`
- `StringReplace`
- `StringReplace`
- `StringReplace`
- `StringReplace`
- `easy promptLine`
- `easy lengthAnything`
- `easy string`
- `easy forLoopStart`
- `Text Concatenate`
- `easy forLoopEnd`
- `GetNode`
- `easy promptLine`
- `ComfyMathExpression`
- `easy indexAnything`
- `easy mergeVideosFromPaths`
- `VideoFrameSample`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `easy lengthAnything`
- `easy forLoopStart`
- `easy promptLine`
- `easy indexAnything`
- `SetNode`
- `SetNode`
- `GetNode`
- `easy forLoopEnd`
- `easy batchAnything`
- `MarkdownNote`
- `MarkdownNote`
- `ComfyMathExpression`
- `easy mergeVideosFromPaths`
- `easy ifElse`
- `VideoFrameSample`
- `ComfyMathExpression`
- `easy indexAnything`
- `easy lengthAnything`
- `ComfyMathExpression`
- `easy indexAnything`
- `GetNode`
- `easy ifElse`
- `easy saveVideo`
- `PrimitiveBoolean`
- `SetNode`
- `Note`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `SetNode`
- `GetNode`
- `easy ifElse`
- `ComfyMathExpression`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `easy promptLine`
- `PathchSageAttentionKJ`
- `SetNode`
- `SetNode`
- `GetNode`
- `easy mergeVideosFromPaths`
- `easy multiTrackTaskOutput`
- `GetNode`
- `MarkdownNote`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Reroute`
- `SetNode`
- `SetNode`
- `PrimitiveInt`
- `easy ifElse`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy batchAnything`
- `SetNode`
- `Reroute`
- `Reroute`
- `GetNode`
- `Reroute`
- `GetNode`
- `GetNode`
- `Reroute`
- `Reroute`
- `GetNode`
- `Reroute`
- `Reroute`
- `easy forLoopStart`
- `Reroute`
- `SetNode`
- `PreviewAny`
- `GetNode`
- `easy saveVideo`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `CreateVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `PreviewAny`
- `easy forLoopEnd`
- `SetNode`
- `VideoFrameSample`
- `GetNode`
- `GetVideoComponents`
- `PreviewAny`
- `easy mergeVideosFromPaths`
- `GetVideoComponents`
- `BatchCount+`
- `ComfyMathExpression`
- `GetNode`
- `VideoTemporalCrop`
- `SaveVideo`
- `SaveVideo`
- `ComfyMathExpression`
- `CLIPLoader`
- `ImageAddNoise`
- `GetImageRangeFromBatch`
- `GetNode`
- `GetNode`
- `ImageBatchMulti`
- `GetVideoComponents`
- `MiniMaxH3AddGuide`
- `GetImageRangeFromBatch`
- `ImageAddNoise`
- `ComfyMathExpression`
- `GetImageRangeFromBatch`
- `ImageBatchMulti`
- `ImageAddNoise`
- `ComfyMathExpression`
- `SetNode`
- `GetVideoComponents`
- `VideoFrameSample`
- `easy mergeVideosFromPaths`
- `easy ifElse`
- `Note`
- `ComfyMathExpression`
- `VideoFrameSample`
- `easy ifElse`
- `MiniMaxH3AddGuide`
- `easy ifElse`
- `Note`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxLowVRAMAttention`
- `Note`
- `ModelAttentionBackend`
- `LoraLoaderBypassModelOnly` ★核心
- `MiniMaxH3AudioGuideFeather`
- `easy minimaxH3ToVideo`
- `UNETLoader` ★核心
- `ImageAddNoise`
- `ImageAddNoise`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveInt`
- `PreviewAny`
- `H3FrozenVideoCache`
- `H3AudioRefineSampler` ★核心
- `GetImageRangeFromBatch`
- `MiniMaxH3AddGuide`
- `MiniMaxH3AudioGuideFeather`
- `PrimitiveStringMultiline`
- `PrimitiveInt`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PrimitiveFloat`
- `easy float`
- `GetImageRangeFromBatch`
- `ConditioningZeroOut`
- `KSamplerSelect` ★核心
- `Note`
- `ExtendIntermediateSigmas`
- `BasicScheduler`
- `easy ifElse`
- `GetNode`
- `Reroute`
- `Reroute`
- `SetNode`
- `GetNode`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `easy ifElse`
- `PrimitiveFloat`
- `PrimitiveInt`
- `Note`
- `Note`
- `easy float`
- `LoadVideo`
- `SelfLiftH3Sampler` ★核心
- `easy multiTrackEditor`

## 知识

覆盖率 **43%**（115/266）

**有卡**：`easy multiTrackInfoOutput`、`VAELoader`、`ConditioningZeroOut`、`easy mergeVideosFromPaths`、`ComfyMathExpression`、`easy string`、`StringReplace`、`easy promptLine`、`easy lengthAnything`、`easy forLoopStart`、`Text Concatenate`、`easy forLoopEnd`、`easy indexAnything`、`VideoFrameSample`、`easy batchAnything`、`easy saveVideo`、`PrimitiveBoolean`、`PathchSageAttentionKJ`、`easy multiTrackTaskOutput`、`VAEDecode`、`VAEDecodeAudio`、`CreateVideo`、`GetVideoComponents`、`BatchCount+`、`VideoTemporalCrop`、`SaveVideo`、`CLIPLoader`、`ImageAddNoise`、`GetImageRangeFromBatch`、`ImageBatchMulti`、`MiniMaxH3AddGuide`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxLowVRAMAttention`、`ModelAttentionBackend`、`LoraLoaderBypassModelOnly`、`MiniMaxH3AudioGuideFeather`、`easy minimaxH3ToVideo`、`UNETLoader`、`LoraLoaderModelOnly`、`H3FrozenVideoCache`、`H3AudioRefineSampler`、`easy float`、`KSamplerSelect`、`ExtendIntermediateSigmas`、`BasicScheduler`、`LoadVideo`、`SelfLiftH3Sampler`、`easy multiTrackEditor`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、UNETLoader、H3AudioRefineSampler、KSamplerSelect

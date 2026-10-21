---
key: 图片生成/文生图/MiniMax H3超灵活导演台SelfLift双采无缝无色差超长视频2.0，图生视频方案_2107543879313612802.json
name: MiniMax H3超灵活导演台SelfLift双采无缝无色差超长视频2.0，图生视频方案_2107543879313612802
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/MiniMax H3超灵活导演台SelfLift双采无缝无色差超长视频2.0，图生视频方案_2107543879313612802.json
hash: bd20c816e214c45e
coverage: 0.496644
learned_at: 2026-10-20 01:50:46
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, easy multiTrackInfoOutput, VAELoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, ConditioningZeroOut, GetNode, easy mergeVideosFromPaths, ComfyMathExpression, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, easy ifElse, SetNode, SetNode, easy string, GetNode, GetNode, ComfyMathExpression, SetNode, SetNode, easy ifElse, StringReplace, StringReplace, StringReplace, StringReplace, StringReplace, StringReplace, easy promptLine, easy lengthAnything, easy string, easy forLoopStart, Text Concatenate, easy forLoopEnd, GetNode, easy promptLine, ComfyMathExpression, easy indexAnything, easy mergeVideosFromPaths, VideoFrameSample, GetNode, GetNode, SetNode, SetNode, easy lengthAnything, easy forLoopStart, easy promptLine, easy indexAnything, SetNode, SetNode, GetNode, easy forLoopEnd, easy batchAnything, ComfyMathExpression, easy mergeVideosFromPaths, easy ifElse, VideoFrameSample, ComfyMathExpression, easy indexAnything, easy lengthAnything, ComfyMathExpression, easy indexAnything, GetNode, easy ifElse, easy saveVideo, PrimitiveBoolean, SetNode, SetNode, SetNode, GetNode, ComfyMathExpression, ComfyMathExpression, easy ifElse, ComfyMathExpression, SetNode, SetNode, ComfyMathExpression, GetNode, GetNode, easy promptLine, PathchSageAttentionKJ, SetNode, SetNode, GetNode, easy mergeVideosFromPaths, easy multiTrackTaskOutput, GetNode, GetNode, SetNode, SetNode, Reroute, SetNode, PrimitiveInt, easy ifElse, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, easy batchAnything, SetNode, Reroute, Reroute, GetNode, Reroute, GetNode, Reroute, GetNode, Reroute, Reroute, easy forLoopStart, Reroute, SetNode, PreviewAny, easy saveVideo, VAEDecode, VAEDecodeAudio, GetNode, SetNode, PreviewAny, easy forLoopEnd, VideoFrameSample, GetNode, PreviewAny, easy mergeVideosFromPaths, GetVideoComponents, BatchCount+, ComfyMathExpression, VideoTemporalCrop, SaveVideo, ComfyMathExpression, CLIPLoader, ImageAddNoise, GetImageRangeFromBatch, ImageBatchMulti, GetVideoComponents, ImageBatchMulti, GetVideoComponents, VideoFrameSample, easy mergeVideosFromPaths, easy ifElse, ComfyMathExpression, VideoFrameSample, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxLowVRAMAttention, ModelAttentionBackend, LoraLoaderBypassModelOnly, MiniMaxH3AudioGuideFeather, easy minimaxH3ToVideo, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, SetNode, PrimitiveBoolean, PrimitiveBoolean, PrimitiveInt, PreviewAny, H3FrozenVideoCache, H3AudioRefineSampler, MiniMaxH3AddGuide, PrimitiveStringMultiline, PrimitiveInt, GetNode, GetNode, SetNode, GetNode, ConditioningZeroOut, ExtendIntermediateSigmas, BasicScheduler, easy ifElse, Reroute, SetNode, PrimitiveBoolean, PrimitiveInt, easy float, LoadVideo, KSamplerSelect, GetNode, SetNode, GetNode, GetNode, easy float, PrimitiveInt, ComfySwitchNode, GetNode, GetNode, Reroute, GetNode, GetNode, Reroute, SetNode, PrimitiveInt, SetNode, GetNode, GetVideoComponents, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, MiniMaxH3AddGuide, MiniMaxH3AddGuide, ComfyMathExpression, SaveVideo, CreateVideo, easy float, GetNode, SelfLiftH3Sampler, GetNode, GetNode, PrimitiveInt, VAELoader, MiniMaxH3AudioGuideFeather, easy ifElse, easy ifElse, ComfySwitchNode, SetNode, GetNode, easy float, ComfySwitchNode, easy ifElse, PrimitiveFloat, ImageAddNoise, PrimitiveBoolean, CreateVideo, GetNode, GetVideoComponents, GetNode, VideoFrameSample, SetNode, PrimitiveFloat, ImageAddNoise, ComfyMathExpression, ImageAddNoise, ImageAddNoise, GetImageRangeFromBatch, GetImageRangeFromBatch, GetImageRangeFromBatch, GetImageRangeFromBatch, GetVideoComponents, ColorTransfer, easy multiTrackEditor, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/MiniMax H3超灵活导演台SelfLift双采无缝无色差超长视频2.0，图生视频方案_2107543879313612802.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/MiniMax H3超灵活导演台SelfLift双采无缝无色差超长视频2.0，图生视频方案_2107543879313612802.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（298 个）：
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
- `GetNode`
- `GetNode`
- `ConditioningZeroOut`
- `GetNode`
- `easy mergeVideosFromPaths`
- `ComfyMathExpression`
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
- `SetNode`
- `SetNode`
- `GetNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `easy ifElse`
- `ComfyMathExpression`
- `SetNode`
- `SetNode`
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
- `GetNode`
- `SetNode`
- `SetNode`
- `Reroute`
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
- `Reroute`
- `GetNode`
- `Reroute`
- `Reroute`
- `easy forLoopStart`
- `Reroute`
- `SetNode`
- `PreviewAny`
- `easy saveVideo`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `GetNode`
- `SetNode`
- `PreviewAny`
- `easy forLoopEnd`
- `VideoFrameSample`
- `GetNode`
- `PreviewAny`
- `easy mergeVideosFromPaths`
- `GetVideoComponents`
- `BatchCount+`
- `ComfyMathExpression`
- `VideoTemporalCrop`
- `SaveVideo`
- `ComfyMathExpression`
- `CLIPLoader`
- `ImageAddNoise`
- `GetImageRangeFromBatch`
- `ImageBatchMulti`
- `GetVideoComponents`
- `ImageBatchMulti`
- `GetVideoComponents`
- `VideoFrameSample`
- `easy mergeVideosFromPaths`
- `easy ifElse`
- `ComfyMathExpression`
- `VideoFrameSample`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `LoraLoaderBypassModelOnly` ★核心
- `MiniMaxH3AudioGuideFeather`
- `easy minimaxH3ToVideo`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PreviewAny`
- `H3FrozenVideoCache`
- `H3AudioRefineSampler` ★核心
- `MiniMaxH3AddGuide`
- `PrimitiveStringMultiline`
- `PrimitiveInt`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `ConditioningZeroOut`
- `ExtendIntermediateSigmas`
- `BasicScheduler`
- `easy ifElse`
- `Reroute`
- `SetNode`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `easy float`
- `LoadVideo`
- `KSamplerSelect` ★核心
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `easy float`
- `PrimitiveInt`
- `ComfySwitchNode`
- `GetNode`
- `GetNode`
- `Reroute`
- `GetNode`
- `GetNode`
- `Reroute`
- `SetNode`
- `PrimitiveInt`
- `SetNode`
- `GetNode`
- `GetVideoComponents`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `MiniMaxH3AddGuide`
- `MiniMaxH3AddGuide`
- `ComfyMathExpression`
- `SaveVideo`
- `CreateVideo`
- `easy float`
- `GetNode`
- `SelfLiftH3Sampler` ★核心
- `GetNode`
- `GetNode`
- `PrimitiveInt`
- `VAELoader`
- `MiniMaxH3AudioGuideFeather`
- `easy ifElse`
- `easy ifElse`
- `ComfySwitchNode`
- `SetNode`
- `GetNode`
- `easy float`
- `ComfySwitchNode`
- `easy ifElse`
- `PrimitiveFloat`
- `ImageAddNoise`
- `PrimitiveBoolean`
- `CreateVideo`
- `GetNode`
- `GetVideoComponents`
- `GetNode`
- `VideoFrameSample`
- `SetNode`
- `PrimitiveFloat`
- `ImageAddNoise`
- `ComfyMathExpression`
- `ImageAddNoise`
- `ImageAddNoise`
- `GetImageRangeFromBatch`
- `GetImageRangeFromBatch`
- `GetImageRangeFromBatch`
- `GetImageRangeFromBatch`
- `GetVideoComponents`
- `ColorTransfer`
- `easy multiTrackEditor`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **50%**（148/298）

**有卡**：`easy multiTrackInfoOutput`、`VAELoader`、`ConditioningZeroOut`、`easy mergeVideosFromPaths`、`ComfyMathExpression`、`easy string`、`StringReplace`、`easy promptLine`、`easy lengthAnything`、`easy forLoopStart`、`Text Concatenate`、`easy forLoopEnd`、`easy indexAnything`、`VideoFrameSample`、`easy batchAnything`、`easy saveVideo`、`PrimitiveBoolean`、`PathchSageAttentionKJ`、`easy multiTrackTaskOutput`、`VAEDecode`、`VAEDecodeAudio`、`GetVideoComponents`、`BatchCount+`、`VideoTemporalCrop`、`SaveVideo`、`CLIPLoader`、`ImageAddNoise`、`GetImageRangeFromBatch`、`ImageBatchMulti`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxLowVRAMAttention`、`ModelAttentionBackend`、`LoraLoaderBypassModelOnly`、`MiniMaxH3AudioGuideFeather`、`easy minimaxH3ToVideo`、`UNETLoader`、`LoraLoaderModelOnly`、`H3FrozenVideoCache`、`H3AudioRefineSampler`、`MiniMaxH3AddGuide`、`ExtendIntermediateSigmas`、`BasicScheduler`、`easy float`、`LoadVideo`、`KSamplerSelect`、`CreateVideo`、`SelfLiftH3Sampler`、`ColorTransfer`、`easy multiTrackEditor`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、SaveImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

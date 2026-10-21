---
name: text_to_image_lora_sampler_clip_282
type: Text To Image
frequency: 3
level: strong
coverage: 0.528667
common_nodes: [BasicScheduler, BatchCount+, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, CreateVideo, EmptyLatentImage, ExtendIntermediateSigmas, GetImageRangeFromBatch, GetNode, GetVideoComponents, H3AudioRefineSampler, H3FrozenVideoCache, ImageAddNoise, ImageBatchMulti, JjkText, KSampler, KSamplerSelect, LoadVideo, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AddGuide, MiniMaxH3AudioGuideFeather, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxLowVRAMAttention, ModelAttentionBackend, PathchSageAttentionKJ, PreviewAny, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, SaveVideo, SetNode, StringReplace, Text Concatenate, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VideoFrameSample, VideoTemporalCrop, easy batchAnything, easy float, easy forLoopEnd, easy forLoopStart, easy ifElse, easy indexAnything, easy lengthAnything, easy mergeVideosFromPaths, easy minimaxH3ToVideo, easy multiTrackEditor, easy multiTrackInfoOutput, easy multiTrackTaskOutput, easy promptLine, easy saveVideo, easy string, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/MiniMax H3超灵活导演台2.0｜SelfLift双采无缝无色差超长视频_2107365074129211393.json, 图片生成/文生图/MiniMax H3超灵活导演台SelfLift双采无缝无色差超长视频2.0，图生视频方案_2107543879313612802.json, 视频生成/文生视频/MiniMax H3 超灵活导演台｜双采无缝衔接长视频+音频修复_2096893633508237313.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_282

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/反推提示词/MiniMax H3超灵活导演台2.0｜SelfLift双采无缝无色差超长视频_2107365074129211393.json、图片生成/文生图/MiniMax H3超灵活导演台SelfLift双采无缝无色差超长视频2.0，图生视频方案_2107543879313612802.json、视频生成/文生视频/MiniMax H3 超灵活导演台｜双采无缝衔接长视频+音频修复_2096893633508237313.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：53%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `BatchCount+`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `CreateVideo`
- `EmptyLatentImage`
- `ExtendIntermediateSigmas`
- `GetImageRangeFromBatch`
- `GetNode`
- `GetVideoComponents`
- `H3AudioRefineSampler`
- `H3FrozenVideoCache`
- `ImageAddNoise`
- `ImageBatchMulti`
- `JjkText`
- `KSampler`
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
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ColorTransfer` —— 2/3 个有
- `ComfySwitchNode` —— 2/3 个有
- `SelfLiftH3Sampler` —— 2/3 个有
- `BasicGuider` —— 1/3 个有
- `LTXVConcatAVLatent` —— 1/3 个有
- `LTXVSeparateAVLatent` —— 1/3 个有
- `ManualSigmas` —— 1/3 个有
- `MinimaxH3LatentUpscaler3D` —— 1/3 个有
- `RandomNoise` —— 1/3 个有
- `SamplerCustomAdvanced` —— 1/3 个有
- `SaveImage` —— 1/3 个有
- `SplitSigmas` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足

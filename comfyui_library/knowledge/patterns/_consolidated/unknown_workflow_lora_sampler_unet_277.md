---
name: unknown_workflow_lora_sampler_unet_277
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.537
common_nodes: [BasicGuider, BasicScheduler, BlockSparseAttention, Bookmark (rgthree), CLIPLoader, ComfyMathExpression, ComfySwitchNode, ConditioningZeroOut, CreateVideo, GetImageSizeAndCount, GetNode, ImageBatch, ImageFromBatch, ImageResizeKJv2, KSamplerSelect, Label (rgthree), LoadImage, LoraLoaderModelOnly, MiniMaxH3AddGuide, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, ModelAttentionBackend, PlaySound|pysssss, PrimitiveBoolean, PrimitiveStringMultiline, RandomNoise, RepeatImageBatch, SamplerCustomAdvanced, SaveVideo, SelfLiftH3Sampler, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoInfo, easy int]
problems: []
missing: []
members: [平台全量/MiniMaxH3视频编辑-人物替换_2117855596811735041.json, 视频生成/视频生视频/海螺H3视频编辑-人物替换V2-强化替换效果_2092546456971464705.json, 视频生成/视频生视频/海螺H3视频编辑-人物替换V3-优化加速强化效果_2117592285784395778.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_277

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/MiniMaxH3视频编辑-人物替换_2117855596811735041.json、视频生成/视频生视频/海螺H3视频编辑-人物替换V2-强化替换效果_2092546456971464705.json、视频生成/视频生视频/海螺H3视频编辑-人物替换V3-优化加速强化效果_2117592285784395778.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：54%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `BlockSparseAttention`
- `Bookmark (rgthree)`
- `CLIPLoader`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `ConditioningZeroOut`
- `CreateVideo`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageBatch`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `Label (rgthree)`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3AddGuide`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `PlaySound|pysssss`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `RepeatImageBatch`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SelfLiftH3Sampler`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoInfo`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `ImageBatchMulti` —— 2/3 个有
- `ResolutionSelector` —— 2/3 个有
- `VHS_LoadVideoFFmpeg` —— 2/3 个有
- `easy anythingIndexSwitch` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `AudioConcat` —— 1/3 个有
- `ConcatenateVideo` —— 1/3 个有
- `EmptyAudio` —— 1/3 个有
- `EndLoop` —— 1/3 个有
- `ManualSigmas` —— 1/3 个有
- `MiniMaxChunkFeedForward` —— 1/3 个有
- `MiniMaxLowVRAMAttention` —— 1/3 个有
- `RegexExtract` —— 1/3 个有
- `StartLoop` —— 1/3 个有
- `StringFormat` —— 1/3 个有
- `TrimAudioDuration` —— 1/3 个有
- `easy float` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

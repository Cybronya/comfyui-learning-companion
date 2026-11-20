---
name: unknown_workflow_lora_sampler_unet_161
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.4304
common_nodes: [AudioConcat, BasicGuider, BasicScheduler, CLIPLoader, ColorMatchV2, ComfyMathExpression, ComfySwitchNode, CreateVideo, GetImageRangeFromBatch, GetNode, INTConstant, Image Batch, ImageAddNoise, ImageFromBatch, ImageScale, KSamplerSelect, LLAIDownloadVideo, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3AddGuide, MiniMaxH3LoadLatent, MiniMaxH3LoopTrim, MiniMaxH3ReferenceToVideo, MiniMaxH3SaveLatent, MiniMaxH3SigmaShift, MiniMaxH3VideoExtender, MiniMaxH3VideoMerge, ModelAttentionBackend, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveVideo, SetNode, ShowAnything|Mie, TrimAudioDuration, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, easy minimaxH3AudioLock]
problems: []
missing: []
members: [图片生成/图生图/Minimax多帧插入或者视频续写_2114255700733022209.json, 图片生成/图生图/Minimax多帧插入或者视频续写_2115283492492890113.json, 平台全量/Minimax多帧插入或者视频续写_2117406476267507714.json, 视频生成/图生视频/Minimax多帧插入或者视频续写_2114880369383272450.json, 视频生成/视频生视频/Minimax多帧插入或者视频续写_2102590341739274241.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_161

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Minimax多帧插入或者视频续写_2114255700733022209.json、图片生成/图生图/Minimax多帧插入或者视频续写_2115283492492890113.json、平台全量/Minimax多帧插入或者视频续写_2117406476267507714.json、视频生成/图生视频/Minimax多帧插入或者视频续写_2114880369383272450.json、视频生成/视频生视频/Minimax多帧插入或者视频续写_2102590341739274241.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：43%

## 共有节点

全部 5 个 workflow 都包含：
- `AudioConcat`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ColorMatchV2`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `CreateVideo`
- `GetImageRangeFromBatch`
- `GetNode`
- `INTConstant`
- `Image Batch`
- `ImageAddNoise`
- `ImageFromBatch`
- `ImageScale`
- `KSamplerSelect`
- `LLAIDownloadVideo`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3AddGuide`
- `MiniMaxH3LoadLatent`
- `MiniMaxH3LoopTrim`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SaveLatent`
- `MiniMaxH3SigmaShift`
- `MiniMaxH3VideoExtender`
- `MiniMaxH3VideoMerge`
- `ModelAttentionBackend`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetNode`
- `ShowAnything|Mie`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `easy minimaxH3AudioLock`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 4/5 个有
- `AnyIsEmpty` —— 3/5 个有
- `AudioInfo` —— 3/5 个有
- `EmptyAudio` —— 3/5 个有
- `Float` —— 3/5 个有
- `Int` —— 3/5 个有
- `VHS_LoadVideo` —— 3/5 个有
- `ArchAi3D_Any_Index_Switch` —— 2/5 个有
- `AudioCrop` —— 2/5 个有
- `BlockSparseAttention` —— 2/5 个有
- `ColorTransfer` —— 2/5 个有
- `ComfyNumberConvert` —— 2/5 个有
- `ConditioningZeroOut` —— 2/5 个有
- `ExtendIntermediateSigmas` —— 2/5 个有
- `GetVideoComponents` —— 2/5 个有
- `ImageBatchMulti` —— 2/5 个有
- `LoadVideo` —— 2/5 个有
- `MiniMaxH3AudioGuideFeather` —— 2/5 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/5 个有
- `MiniMaxLowVRAMAttention` —— 2/5 个有
- `NumberClamp` —— 2/5 个有
- `PathchSageAttentionKJ` —— 2/5 个有
- `SelfLiftAvatarH3Sampler` —— 2/5 个有
- `VideoFrameSample` —— 2/5 个有
- `VideoTemporalCrop` —— 2/5 个有
- `获取视频信息` —— 2/5 个有
- `PreviewImage` —— 1/5 个有
- `VHS_VideoInfo` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

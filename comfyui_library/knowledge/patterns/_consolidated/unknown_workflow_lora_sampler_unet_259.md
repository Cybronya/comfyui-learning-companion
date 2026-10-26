---
name: unknown_workflow_lora_sampler_unet_259
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.4715
common_nodes: [AudioConcat, AudioCrop, BasicGuider, BasicScheduler, CLIPLoader, ColorMatchV2, ComfyMathExpression, ComfySwitchNode, CreateVideo, GetImageRangeFromBatch, GetNode, INTConstant, Image Batch, ImageAddNoise, ImageFromBatch, ImageScale, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3AddGuide, MiniMaxH3ReferenceToVideo, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, SetNode, TrimAudioDuration, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, easy minimaxH3AudioLock]
problems: []
missing: []
members: [图片生成/图生图/Minimax多帧插入或者视频续写_2114255700733022209.json, 视频生成/图生视频/Minimax多帧插入或者视频续写_2102590341739274241.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_259

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Minimax多帧插入或者视频续写_2114255700733022209.json、视频生成/图生视频/Minimax多帧插入或者视频续写_2102590341739274241.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：47%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioConcat`
- `AudioCrop`
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
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3AddGuide`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetNode`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `easy minimaxH3AudioLock`

**可变部分**（部分 workflow 才有）：
- `LLAIDownloadVideo` —— 1/2 个有
- `MiniMaxH3LoadLatent` —— 1/2 个有
- `MiniMaxH3LoopTrim` —— 1/2 个有
- `MiniMaxH3SaveLatent` —— 1/2 个有
- `MiniMaxH3SigmaShift` —— 1/2 个有
- `MiniMaxH3VideoExtender` —— 1/2 个有
- `MiniMaxH3VideoMerge` —— 1/2 个有
- `ModelAttentionBackend` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `ShowAnything|Mie` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

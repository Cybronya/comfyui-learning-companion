---
name: unknown_workflow_video_lora_sampler_446
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.4816
common_nodes: [AudioConcatenate, BasicScheduler, CLIPLoader, CM_FloatBinaryOperation, CM_IntBinaryOperation, CM_IntToFloat, CreateVideo, FloatConstant, GetImageSize, INTConstant, ImageBatch, ImageExpandBatch+, ImageFromBatch+, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, MiniMaxLowVRAMAttention, ModelAttentionBackend, PrimitiveStringMultiline, ResolutionSelector, SaveVideo, TrimAudioDuration, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine, easy compare, easy forLoopEnd, easy forLoopStart, easy ifElse, easy mathInt]
problems: []
missing: []
members: [图片生成/图生图/Minimax动作迁移_latent接续，优化版_2114255450542788610.json, 视频生成/图生视频/Minimax动作迁移_2104782824657211394.json, 视频生成/图生视频/Minimax动作迁移_latent接续，优化版_2110928214188191745.json, 视频生成/图生视频/Minimax动作迁移_latent接续，优化版_2113781959360073729.json, 视频生成/图生视频/Minimax动作迁移_官方接续_2105994599452995586.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_446

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Minimax动作迁移_latent接续，优化版_2114255450542788610.json、视频生成/图生视频/Minimax动作迁移_2104782824657211394.json、视频生成/图生视频/Minimax动作迁移_latent接续，优化版_2110928214188191745.json、视频生成/图生视频/Minimax动作迁移_latent接续，优化版_2113781959360073729.json、视频生成/图生视频/Minimax动作迁移_官方接续_2105994599452995586.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：48%

## 共有节点

全部 5 个 workflow 都包含：
- `AudioConcatenate`
- `BasicScheduler`
- `CLIPLoader`
- `CM_FloatBinaryOperation`
- `CM_IntBinaryOperation`
- `CM_IntToFloat`
- `CreateVideo`
- `FloatConstant`
- `GetImageSize`
- `INTConstant`
- `ImageBatch`
- `ImageExpandBatch+`
- `ImageFromBatch+`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveVideo`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy compare`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy ifElse`
- `easy mathInt`

**可变部分**（部分 workflow 才有）：
- `ImageFromBatch` —— 4/5 个有
- `ModelPreviewOverrideKJ` —— 4/5 个有
- `BasicGuider` —— 3/5 个有
- `ImageToMask` —— 3/5 个有
- `LTXVConcatAVLatent` —— 3/5 个有
- `LTXVSeparateAVLatent` —— 3/5 个有
- `LatentConcat` —— 3/5 个有
- `LatentCut` —— 3/5 个有
- `MaskComposite` —— 3/5 个有
- `MaskToImage` —— 3/5 个有
- `RandomNoise` —— 3/5 个有
- `RepeatImageBatch` —— 3/5 个有
- `SamplerCustomAdvanced` —— 3/5 个有
- `SetLatentNoiseMask` —— 3/5 个有
- `SolidMask` —— 3/5 个有
- `ConditioningZeroOut` —— 2/5 个有
- `H3SigmaRefiner` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `SelfLiftH3Sampler` —— 2/5 个有
- `EmptyImage` —— 1/5 个有
- `MiniMaxH3AddGuide` —— 1/5 个有
- `MiniMaxH3MotionContext` —— 1/5 个有
- `MiniMaxH3MotionContextTrim` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

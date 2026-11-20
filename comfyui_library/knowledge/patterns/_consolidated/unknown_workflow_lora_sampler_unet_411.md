---
name: unknown_workflow_lora_sampler_unet_411
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.387
common_nodes: [BasicGuider, BlockSparseAttention, CLIPLoader, ComfyMathExpression, Fast Groups Muter (rgthree), GetNode, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, MiniMaxH3MotionContext, MiniMaxH3MotionContextSaveLatent, MiniMaxH3MotionContextTrim, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, ModelAttentionBackend, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResizeImageMaskNode, ResolutionSelector, SamplerCustomAdvanced, Seed (rgthree), SetNode, StringFormat, TrimAudioDuration, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo]
problems: []
missing: []
members: [视频生成/图生视频/minimax-h3-长视频多段单采衔接-V1_2115684586847035393.json, 视频生成/图生视频/minimax-h3延长视频_2103268121476952066.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_411

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/minimax-h3-长视频多段单采衔接-V1_2115684586847035393.json、视频生成/图生视频/minimax-h3延长视频_2103268121476952066.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：39%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BlockSparseAttention`
- `CLIPLoader`
- `ComfyMathExpression`
- `Fast Groups Muter (rgthree)`
- `GetNode`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MiniMaxH3MotionContext`
- `MiniMaxH3MotionContextSaveLatent`
- `MiniMaxH3MotionContextTrim`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResizeImageMaskNode`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `Seed (rgthree)`
- `SetNode`
- `StringFormat`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 1/2 个有
- `BasicScheduler` —— 1/2 个有
- `ComfySwitchNode` —— 1/2 个有
- `CreateVideo` —— 1/2 个有
- `GetLatentSize` —— 1/2 个有
- `ImageBatch` —— 1/2 个有
- `ImageFromBatch` —— 1/2 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/2 个有
- `MiniMaxH3MotionContextLoadLatent` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `PrimitiveBoolean` —— 1/2 个有
- `PrimitiveString` —— 1/2 个有
- `RepeatImageBatch` —— 1/2 个有
- `SaveVideo` —— 1/2 个有
- `VHS_VideoCombine` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

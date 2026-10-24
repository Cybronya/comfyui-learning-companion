---
name: unknown_workflow_video_upscale_latent_upscale_144
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.938
common_nodes: [BasicGuider, CLIPLoader, CR Seed, ComfyMathExpression, ImpactConditionalBranch, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3MotionContext, MiniMaxH3MotionContextSaveLatent, MiniMaxH3TwoPassDetailMixerT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, ModelAttentionBackend, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SolAttnMiniMax, UNETLoader, VAELoader, VHS_VideoCombine, Yuan_H3MotionContextLoadLatent, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/t8大佬的文武双全工作流_2099453228814528513.json, 视频生成/文生视频/动态生成_2093350007784173570.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_144

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/t8大佬的文武双全工作流_2099453228814528513.json、视频生成/文生视频/动态生成_2093350007784173570.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CR Seed`
- `ComfyMathExpression`
- `ImpactConditionalBranch`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3MotionContext`
- `MiniMaxH3MotionContextSaveLatent`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `ModelAttentionBackend`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SolAttnMiniMax`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`
- `Yuan_H3MotionContextLoadLatent`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Float` —— 1/2 个有
- `ImageBatchMulti` —— 1/2 个有
- `ImageFromBatch` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `MiniMaxChunkFeedForward` —— 1/2 个有
- `MiniMaxH3AudioConditioningT8` —— 1/2 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 1/2 个有
- `MiniMaxLowVRAMAttention` —— 1/2 个有
- `ModelPatchTorchSettings` —— 1/2 个有
- `Yuan_MiniMaxH3Video` —— 1/2 个有
- `easy anythingIndexSwitch` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

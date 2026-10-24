---
name: unknown_workflow_lora_sampler_unet_311
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.482
common_nodes: [BasicGuider, BlockSparseAttention, CLIPLoader, ComfyMathExpression, CreateVideo, GetNode, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SemanticBridgeApplyT8, MiniMaxH3SemanticBridgeConfigT8, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax-H3 极限复杂场景 _ 高速运动大动态 _ 高质感无画面劣化  抗形变模糊工作流  （工作版）_2108809186309136386.json, 视频生成/文生视频/H3全能参考工作流_2086287689682350082.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_311

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3 极限复杂场景 _ 高速运动大动态 _ 高质感无画面劣化  抗形变模糊工作流  （工作版）_2108809186309136386.json、视频生成/文生视频/H3全能参考工作流_2086287689682350082.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：48%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BlockSparseAttention`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `GetNode`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SemanticBridgeApplyT8`
- `MiniMaxH3SemanticBridgeConfigT8`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Astra` —— 1/2 个有
- `BasicScheduler` —— 1/2 个有
- `Fast Bypasser (rgthree)` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `MiniMaxChunkFeedForward` —— 1/2 个有
- `MiniMaxH3AVDecodeT8` —— 1/2 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 1/2 个有
- `MiniMaxH3SigmaShift` —— 1/2 个有
- `MiniMaxLowVRAMAttention` —— 1/2 个有
- `PrimitiveBoolean` —— 1/2 个有
- `RunningHub Deepcleaner` —— 1/2 个有
- `SplitSigmas` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有
- `VHS_VideoCombine` —— 1/2 个有
- `VRAM_Debug` —— 1/2 个有
- `easy ifElse` —— 1/2 个有
- `布尔孤海` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

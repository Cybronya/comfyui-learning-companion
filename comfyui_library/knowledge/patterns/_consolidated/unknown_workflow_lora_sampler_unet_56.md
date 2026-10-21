---
name: unknown_workflow_lora_sampler_unet_56
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.49
common_nodes: [BasicGuider, BlockSparseAttention, CLIPLoader, ComfyMathExpression, CreateVideo, GetNode, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SemanticBridgeApplyT8, MiniMaxH3SemanticBridgeConfigT8, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/H3全能参考工作流_2086287689682350082.json, 视频生成/图生视频/MiniMax-H3 极限复杂场景 _ 高速运动大动态 _ 高质感无画面劣化  抗形变模糊工作流  （工作版）_2108809186309136386.json, 视频生成/文生视频/H3全能参考工作流_2086287689682350082.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_56

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/H3全能参考工作流_2086287689682350082.json、视频生成/图生视频/MiniMax-H3 极限复杂场景 _ 高速运动大动态 _ 高质感无画面劣化  抗形变模糊工作流  （工作版）_2108809186309136386.json、视频生成/文生视频/H3全能参考工作流_2086287689682350082.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：49%

## 共有节点

全部 3 个 workflow 都包含：
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
- `Astra` —— 2/3 个有
- `BasicScheduler` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `MiniMaxH3AVDecodeT8` —— 2/3 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 2/3 个有
- `RunningHub Deepcleaner` —— 2/3 个有
- `VHS_VideoCombine` —— 2/3 个有
- `Fast Bypasser (rgthree)` —— 1/3 个有
- `MiniMaxChunkFeedForward` —— 1/3 个有
- `MiniMaxH3SigmaShift` —— 1/3 个有
- `MiniMaxLowVRAMAttention` —— 1/3 个有
- `PrimitiveBoolean` —— 1/3 个有
- `SplitSigmas` —— 1/3 个有
- `VHS_LoadVideo` —— 1/3 个有
- `VRAM_Debug` —— 1/3 个有
- `easy ifElse` —— 1/3 个有
- `布尔孤海` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

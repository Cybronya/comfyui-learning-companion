---
name: unknown_workflow_video_lora_sampler_858
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8585
common_nodes: [BasicScheduler, CLIPLoader, CR Prompt Text, ComfyMathExpression, ConditioningZeroOut, ExtendIntermediateSigmas, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PixaromaLabel, PlaySound|pysssss, ResolutionSelector, SelfLiftAvatarH3Sampler, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 360度环绕视频+Selflift 专用高分辨率生成作流_2106000852258480129.json, 视频生成/图生视频/MiniMax H3 无限时长工作流 SelfLite版 一次30S以上_2103920884787535874.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_858

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 360度环绕视频+Selflift 专用高分辨率生成作流_2106000852258480129.json、视频生成/图生视频/MiniMax H3 无限时长工作流 SelfLite版 一次30S以上_2103920884787535874.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `ExtendIntermediateSigmas`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PixaromaLabel`
- `PlaySound|pysssss`
- `ResolutionSelector`
- `SelfLiftAvatarH3Sampler`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `AudioConcat` —— 1/2 个有
- `AudioCrop` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `GetImageRangeFromBatch` —— 1/2 个有
- `ImageBatchExtendWithOverlap` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `MiniMaxH3AddGuide` —— 1/2 个有
- `MiniMaxH3ImageToVideo` —— 1/2 个有
- `MiniMaxH3ReferenceToVideo` —— 1/2 个有
- `PixaromaDuration` —— 1/2 个有
- `PixaromaGetNode` —— 1/2 个有
- `PixaromaGroupSwitch` —— 1/2 个有
- `PixaromaSetNode` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

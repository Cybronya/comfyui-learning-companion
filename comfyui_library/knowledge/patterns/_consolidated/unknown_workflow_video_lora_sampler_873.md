---
name: unknown_workflow_video_lora_sampler_873
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.858
common_nodes: [BasicScheduler, CLIPLoader, CR Prompt Text, ComfyMathExpression, ConditioningZeroOut, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, ModelPreviewOverrideKJ, PixaromaLabel, PlaySound|pysssss, ResolutionSelector, SelfLiftAvatarH3Sampler, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 360度环绕视频+Selflift 专用高分辨率生成作流_2106000852258480129.json, 视频生成/图生视频/MiniMax H3 无限时长工作流 SelfLite版 一次30S以上_2103920884787535874.json, 视频生成/图生视频/MiniMax_H3_360度环绕视频+Selflift_专用高分辨率生成作流_2115645907449499649.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_873

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 360度环绕视频+Selflift 专用高分辨率生成作流_2106000852258480129.json、视频生成/图生视频/MiniMax H3 无限时长工作流 SelfLite版 一次30S以上_2103920884787535874.json、视频生成/图生视频/MiniMax_H3_360度环绕视频+Selflift_专用高分辨率生成作流_2115645907449499649.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
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
- `ExtendIntermediateSigmas` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `MiniMaxH3ImageToVideo` —— 2/3 个有
- `MiniMaxLowVRAMAttention` —— 2/3 个有
- `PrimitiveFloat` —— 2/3 个有
- `AudioConcat` —— 1/3 个有
- `AudioCrop` —— 1/3 个有
- `BlockSparseAttention` —— 1/3 个有
- `GetImageRangeFromBatch` —— 1/3 个有
- `H3SigmaRefiner` —— 1/3 个有
- `ImageBatchExtendWithOverlap` —— 1/3 个有
- `LoadAudio` —— 1/3 个有
- `MiniMaxH3AddGuide` —— 1/3 个有
- `MiniMaxH3ReferenceToVideo` —— 1/3 个有
- `PixaromaDuration` —— 1/3 个有
- `PixaromaGetNode` —— 1/3 个有
- `PixaromaGroupSwitch` —— 1/3 个有
- `PixaromaSetNode` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

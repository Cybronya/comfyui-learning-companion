---
name: unknown_workflow_lora_sampler_unet_198
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.66725
common_nodes: [BasicScheduler, BlockSparseAttention, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, CreateVideo, ExtendIntermediateSigmas, GetImageRangeFromBatch, GetVideoComponents, ImageAddNoise, ImageBatchMulti, KSamplerSelect, LoadAudio, LoadImage, LoadVideo, LoraLoaderModelOnly, MiniMaxH3AddGuide, MiniMaxH3AudioGuideFeather, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, ResolutionSelector, SaveVideo, SelfLiftH3Sampler, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VideoFrameSample, VideoTemporalCrop]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 真·上下文无缝无色差长视频，SelfLift双采(简易版)_2105615690806939649.json, 视频生成/图生视频/MiniMax H3 真·上下文无缝无色差长视频，SelfLift双采，无放大模型(简易整理版)_2108935950406610946.json, 视频生成/图生视频/MiniMax H3 真·无缝无色差上下文长视频，适配快速动作武戏，SelfLift双采(简易版)_2113128832604659713.json, 视频生成/文生视频/MiniMax H3 SelfLift双采_2100249506242711553.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_198

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 真·上下文无缝无色差长视频，SelfLift双采(简易版)_2105615690806939649.json、视频生成/图生视频/MiniMax H3 真·上下文无缝无色差长视频，SelfLift双采，无放大模型(简易整理版)_2108935950406610946.json、视频生成/图生视频/MiniMax H3 真·无缝无色差上下文长视频，适配快速动作武戏，SelfLift双采(简易版)_2113128832604659713.json、视频生成/文生视频/MiniMax H3 SelfLift双采_2100249506242711553.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `BlockSparseAttention`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `CreateVideo`
- `ExtendIntermediateSigmas`
- `GetImageRangeFromBatch`
- `GetVideoComponents`
- `ImageAddNoise`
- `ImageBatchMulti`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `MiniMaxH3AddGuide`
- `MiniMaxH3AudioGuideFeather`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveVideo`
- `SelfLiftH3Sampler`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VideoFrameSample`
- `VideoTemporalCrop`

**可变部分**（部分 workflow 才有）：
- `ColorTransfer` —— 3/4 个有
- `ComfySwitchNode` —— 3/4 个有
- `PrimitiveBoolean` —— 3/4 个有
- `VHS_LoadVideo` —— 3/4 个有
- `easy float` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `VideoConcatenate` —— 1/4 个有
- `忽略多组孤海` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

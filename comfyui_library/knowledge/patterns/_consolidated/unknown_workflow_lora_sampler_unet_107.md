---
name: unknown_workflow_lora_sampler_unet_107
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.666
common_nodes: [BasicScheduler, BlockSparseAttention, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, CreateVideo, ExtendIntermediateSigmas, GetImageRangeFromBatch, GetVideoComponents, ImageAddNoise, ImageBatchMulti, KSamplerSelect, LoadImage, LoadVideo, LoraLoaderModelOnly, MiniMaxH3AddGuide, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, SaveVideo, UNETLoader, VAEDecode, VAELoader, VideoFrameSample]
problems: []
missing: []
members: [平台全量/H3二创神器，保姆级超快人物替换&动作迁移，支持1080p超长视频创作_2117280147819814914.json, 视频生成/图生视频/MiniMax H3 真·上下文无缝无色差长视频，SelfLift双采(简易版)_2105615690806939649.json, 视频生成/图生视频/MiniMax H3 真·上下文无缝无色差长视频，SelfLift双采，无放大模型(简易整理版)_2108935950406610946.json, 视频生成/图生视频/MiniMax H3 真·无缝无色差上下文长视频，适配快速动作武戏，SelfLift双采(简易版)_2113128832604659713.json, 视频生成/图生视频/MiniMax_H3_图生视频_首尾帧视频_加速版_2115585985688981506.json, 视频生成/图生视频/MiniMax_H3_真·上下文无缝无色差长视频，SelfLift双采，无放大模型(简易版)_2114884153253654529.json, 视频生成/文生视频/MiniMax H3 SelfLift双采_2100249506242711553.json, 视频生成/视频生视频/MiniMax H3 真·无缝无色差上下文长视频，适配快速动作武戏，SelfLift双采(简易版)_2113128832604659713.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_107

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（平台全量/H3二创神器，保姆级超快人物替换&动作迁移，支持1080p超长视频创作_2117280147819814914.json、视频生成/图生视频/MiniMax H3 真·上下文无缝无色差长视频，SelfLift双采(简易版)_2105615690806939649.json、视频生成/图生视频/MiniMax H3 真·上下文无缝无色差长视频，SelfLift双采，无放大模型(简易整理版)_2108935950406610946.json、视频生成/图生视频/MiniMax H3 真·无缝无色差上下文长视频，适配快速动作武戏，SelfLift双采(简易版)_2113128832604659713.json、视频生成/图生视频/MiniMax_H3_图生视频_首尾帧视频_加速版_2115585985688981506.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 8 个 workflow 都包含：
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
- `LoadImage`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `MiniMaxH3AddGuide`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VideoFrameSample`

**可变部分**（部分 workflow 才有）：
- `ColorTransfer` —— 7/8 个有
- `ComfySwitchNode` —— 7/8 个有
- `LoadAudio` —— 7/8 个有
- `MiniMaxH3AudioGuideFeather` —— 7/8 个有
- `PrimitiveBoolean` —— 7/8 个有
- `ResolutionSelector` —— 7/8 个有
- `SelfLiftH3Sampler` —— 7/8 个有
- `VAEDecodeAudio` —— 7/8 个有
- `VHS_LoadVideo` —— 7/8 个有
- `VideoTemporalCrop` —— 7/8 个有
- `easy float` —— 6/8 个有
- `BasicGuider` —— 1/8 个有
- `DisableNoise` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `GetImageSize` —— 1/8 个有
- `GetNode` —— 1/8 个有
- `ImageExpandBatch+` —— 1/8 个有
- `ImageFromBatch` —— 1/8 个有
- `ImageScale` —— 1/8 个有
- `MiniMaxChunkFeedForward` —— 1/8 个有
- `MiniMaxH3SparkAttentionAuto` —— 1/8 个有
- `MiniMaxH3TemporalWindow` —— 1/8 个有
- `MinimaxH3LatentUpscaler3D` —— 1/8 个有
- `SamplerCustomAdvanced` —— 1/8 个有
- `SelfLiftSplitLowH3` —— 1/8 个有
- `SelfLiftSplitTransitionH3` —— 1/8 个有
- `SetNode` —— 1/8 个有
- `SpectrumApplyMiniMaxH3` —— 1/8 个有
- `VideoConcatenate` —— 1/8 个有
- `孤海注释` —— 1/8 个有
- `忽略多组孤海` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_video_lora_sampler_1001
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.3335
common_nodes: [Any Switch (rgthree), BasicScheduler, BlockSparseAttention, CLIPLoader, ComfyMathExpression, EmptyImage, Fast Groups Bypasser (rgthree), GetNode, GoohaiUniversalSlider, KSamplerSelect, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3AudioSelect, MiniMaxH3MediaLoaderFantastic, MiniMaxH3MultimodalChat, MiniMaxH3ReferenceSplitter, MiniMaxH3SigmaShift, MiniMaxH3SparkAttentionSM89, MiniMaxH3UnifiedToVideo, ModelAttentionBackend, ModelPreviewOverrideKJ, PreviewImage, RTXVideoFrameGeneration, SetNode, ShowText|pysssss, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, VRAM_Debug]
problems: []
missing: []
members: [视频生成/文生视频/4-MiniMaxh-H3-全能生视频工作流-V5-latent分块二采_2113454316114759682.json, 视频生成/文生视频/4-MiniMaxh-H3-全能生视频工作流-V5-单采2K直出-RH版_2113465285872275458.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_1001

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/4-MiniMaxh-H3-全能生视频工作流-V5-latent分块二采_2113454316114759682.json、视频生成/文生视频/4-MiniMaxh-H3-全能生视频工作流-V5-单采2K直出-RH版_2113465285872275458.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：33%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BasicScheduler`
- `BlockSparseAttention`
- `CLIPLoader`
- `ComfyMathExpression`
- `EmptyImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `GoohaiUniversalSlider`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3AudioSelect`
- `MiniMaxH3MediaLoaderFantastic`
- `MiniMaxH3MultimodalChat`
- `MiniMaxH3ReferenceSplitter`
- `MiniMaxH3SigmaShift`
- `MiniMaxH3SparkAttentionSM89`
- `MiniMaxH3UnifiedToVideo`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PreviewImage`
- `RTXVideoFrameGeneration`
- `SetNode`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `VRAM_Debug`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `LTXVConcatAVLatent` —— 1/2 个有
- `LTXVSeparateAVLatent` —— 1/2 个有
- `ManualSigmas` —— 1/2 个有
- `MiniMaxH3SigmaRefiner` —— 1/2 个有
- `MiniMaxH3TiledSampler` —— 1/2 个有
- `MinimaxH3LatentUpscaler3D` —— 1/2 个有
- `RandomNoise` —— 1/2 个有
- `SamplerCustomAdvanced` —— 1/2 个有
- `SelfLiftAvatarH3Sampler` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

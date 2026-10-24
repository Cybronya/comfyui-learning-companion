---
name: unknown_workflow_video_lora_sampler_917
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8685
common_nodes: [BasicScheduler, CLIPLoader, ComfySwitchNode, Fast Groups Bypasser (rgthree), KSamplerSelect, LayerUtility: NumberCalculatorV2, LoraLoaderModelOnly, MiniMaxH3AudioLock, MiniMaxH3MediaLoaderFantastic, MiniMaxH3MultimodalChat, MiniMaxH3ReferenceSplitter, MiniMaxH3SigmaShift, MiniMaxH3UnifiedToVideo, ModelAttentionBackend, ModelPreviewOverrideKJ, ShowText|pysssss, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/4-MiniMaxh-H3-全能生视频工作流-V4-latent分块二采_2087412509618823169.json, 视频生成/文生视频/4-MiniMaxh-H3-全能生视频工作流-V4-单采2K直出-RH版_2098811422074556417.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_917

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/4-MiniMaxh-H3-全能生视频工作流-V4-latent分块二采_2087412509618823169.json、视频生成/文生视频/4-MiniMaxh-H3-全能生视频工作流-V4-单采2K直出-RH版_2098811422074556417.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfySwitchNode`
- `Fast Groups Bypasser (rgthree)`
- `KSamplerSelect`
- `LayerUtility: NumberCalculatorV2`
- `LoraLoaderModelOnly`
- `MiniMaxH3AudioLock`
- `MiniMaxH3MediaLoaderFantastic`
- `MiniMaxH3MultimodalChat`
- `MiniMaxH3ReferenceSplitter`
- `MiniMaxH3SigmaShift`
- `MiniMaxH3UnifiedToVideo`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 1/2 个有
- `BlockSparseAttention` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `H3SigmaRefiner` —— 1/2 个有
- `LTXVConcatAVLatent` —— 1/2 个有
- `LTXVSeparateAVLatent` —— 1/2 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/2 个有
- `MiniMaxH3TiledSampler` —— 1/2 个有
- `MinimaxH3LatentUpscaler3D` —— 1/2 个有
- `RandomNoise` —— 1/2 个有
- `SamplerCustomAdvanced` —— 1/2 个有
- `SelfLiftH3Sampler` —— 1/2 个有
- `VRAM_Debug` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_video_lora_sampler_765
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6985
common_nodes: [BasicScheduler, ConditioningZeroOut, FeiHouEasyH3RH, FeiHouEasyH3RHLoader, FeiHouEasyH3RHOutput, GetNode, H3SigmaRefiner, KSamplerSelect, Label (rgthree), LoraLoaderModelOnly, MiniMaxH3SemanticBridgeApplyT8, MiniMaxH3SemanticBridgeConfigT8, ModelAttentionBackend, ModelPreviewOverrideKJ, RunningHub Deepcleaner, SelfLiftAvatarH3Sampler, SetNode, VAEDecode, VAEDecodeAudio, VHS_VideoCombine, easy clearCacheAll]
problems: []
missing: []
members: [视频生成/图生视频/MinimaxH3-文戏V1.0版_2105295502089740290.json, 视频生成/图生视频/MinimaxH3-武戏V1.3版_2107062415434280962.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_765

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/MinimaxH3-文戏V1.0版_2105295502089740290.json、视频生成/图生视频/MinimaxH3-武戏V1.3版_2107062415434280962.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：70%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `ConditioningZeroOut`
- `FeiHouEasyH3RH`
- `FeiHouEasyH3RHLoader`
- `FeiHouEasyH3RHOutput`
- `GetNode`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `Label (rgthree)`
- `LoraLoaderModelOnly`
- `MiniMaxH3SemanticBridgeApplyT8`
- `MiniMaxH3SemanticBridgeConfigT8`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `RunningHub Deepcleaner`
- `SelfLiftAvatarH3Sampler`
- `SetNode`
- `VAEDecode`
- `VAEDecodeAudio`
- `VHS_VideoCombine`
- `easy clearCacheAll`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderBypassModelOnly` —— 1/2 个有
- `VRAM_Debug` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

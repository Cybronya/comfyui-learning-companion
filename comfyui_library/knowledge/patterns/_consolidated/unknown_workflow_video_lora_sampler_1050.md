---
name: unknown_workflow_video_lora_sampler_1050
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.861
common_nodes: [BasicScheduler, BlockSparseAttention, ComfySwitchNode, ConditioningZeroOut, KSamplerSelect, Label (rgthree), LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3IntegrationAdapterGH, MiniMaxH3IntegrationGH, MiniMaxH3SigmaShift, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveBoolean, PrimitiveInt, SaveImage, SelfLiftH3Sampler, UNETLoader, VAEDecode, VAEDecodeAudio, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 极简全能工作流_2113629621248942081.json, 视频生成/图生视频/MiniMax_H3_极简全能工作流_2115258399221960705.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_1050

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 极简全能工作流_2113629621248942081.json、视频生成/图生视频/MiniMax_H3_极简全能工作流_2115258399221960705.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `BlockSparseAttention`
- `ComfySwitchNode`
- `ConditioningZeroOut`
- `KSamplerSelect`
- `Label (rgthree)`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3IntegrationAdapterGH`
- `MiniMaxH3IntegrationGH`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `SaveImage`
- `SelfLiftH3Sampler`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VHS_VideoCombine`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

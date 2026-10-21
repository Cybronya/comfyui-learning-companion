---
name: unknown_workflow_video_lora_sampler_843
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.818
common_nodes: [BasicGuider, BasicScheduler, BlockSparseAttention, ComfySwitchNodeV2, FeiHouEasyH3RH, FeiHouEasyH3RHDurationCrop, FeiHouEasyH3RHLoraStack, FeiHouEasyH3RHOutput, FeiHouEasyH3RHPromptPreview, FeiHouEasyH3RHRemixLoader, KSamplerSelect, MiniMaxH3SigmaShift, ModelAttentionBackend, RandomSeedNoise, SamplerCustomAdvanced, SetNode, VAEDecode, VAEDecodeAudio, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/minimax多参考生视频_2100587600846352386.json, 视频生成/文生视频/minimax多参考生视频V2单采_2107119860105957377.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_843

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/minimax多参考生视频_2100587600846352386.json、视频生成/文生视频/minimax多参考生视频V2单采_2107119860105957377.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `BlockSparseAttention`
- `ComfySwitchNodeV2`
- `FeiHouEasyH3RH`
- `FeiHouEasyH3RHDurationCrop`
- `FeiHouEasyH3RHLoraStack`
- `FeiHouEasyH3RHOutput`
- `FeiHouEasyH3RHPromptPreview`
- `FeiHouEasyH3RHRemixLoader`
- `KSamplerSelect`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `RandomSeedNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `VAEDecode`
- `VAEDecodeAudio`
- `VHS_VideoCombine`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

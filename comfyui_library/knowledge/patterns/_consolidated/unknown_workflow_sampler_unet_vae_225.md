---
name: unknown_workflow_sampler_unet_vae_225
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.58
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, GetNode, KSamplerSelect, MiniMaxH3ImageToVideo, MiniMaxH3MotionContext, PreviewAudio, RandomNoise, SamplerCustomAdvanced, SaveAudioAdvanced, SetNode, UNETLoader, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [数字人/数字人/minimaxh3长文本朗读_2093225848043294722.json, 数字人/数字人/minimaxh3长文本朗读_2093235944957759489.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_225

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/minimaxh3长文本朗读_2093225848043294722.json、数字人/数字人/minimaxh3长文本朗读_2093235944957759489.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：58%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `GetNode`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3MotionContext`
- `PreviewAudio`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveAudioAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `TrimAudioDuration` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

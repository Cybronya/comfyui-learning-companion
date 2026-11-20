---
name: unknown_workflow_sampler_vae_88
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.975
common_nodes: [BasicGuider, BasicScheduler, CreateVideo, LoadAudio, LoadImage, MiniMaxH3Easy, MiniMaxH3EasyLoader, MiniMaxH3EasyOutput, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecode, VAEDecodeAudio]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 一站式工作流_2110358590795108353.json, 视频生成/文生视频/MinimaxH3工作流多合一极简版_2088792747246444545.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_88

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 一站式工作流_2110358590795108353.json、视频生成/文生视频/MinimaxH3工作流多合一极简版_2088792747246444545.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CreateVideo`
- `LoadAudio`
- `LoadImage`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyLoader`
- `MiniMaxH3EasyOutput`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecode`
- `VAEDecodeAudio`

**可变部分**（部分 workflow 才有）：
- `KSamplerSelect` —— 1/2 个有
- `LoadVideo` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `MiniMaxH3TurboLoRA` —— 1/2 个有
- `MiniMaxH3TurboSampler` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

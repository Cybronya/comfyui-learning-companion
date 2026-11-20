---
name: unknown_workflow_video_sampler_vae_235
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7725
common_nodes: [BasicGuider, BasicScheduler, KSamplerSelect, LoadImage, MiniMaxH3Easy, MiniMaxH3EasyLoader, MiniMaxH3EasyOutput, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, SamplerCustomAdvanced, VAEDecode, VAEDecodeAudio, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/54.MiniMax H3 Easy v2_2088141868772188161.json, 视频生成/文生视频/MinimaxH3 Easy多合一工作流+全节点注释_2088851369838071810.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_235

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/54.MiniMax H3 Easy v2_2088141868772188161.json、视频生成/文生视频/MinimaxH3 Easy多合一工作流+全节点注释_2088851369838071810.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyLoader`
- `MiniMaxH3EasyOutput`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `VAEDecodeAudio`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `LoraLoaderBypassModelOnly` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `PlaySound|pysssss` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

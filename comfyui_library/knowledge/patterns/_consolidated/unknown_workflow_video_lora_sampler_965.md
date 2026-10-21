---
name: unknown_workflow_video_lora_sampler_965
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.732
common_nodes: [BasicGuider, CLIPLoader, CR Text, LoraLoaderModelOnly, MiniMaxH3Unified, PathchSageAttentionKJ, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/简单用_2096538181641527298.json, 视频生成/文生视频/鱼酥大佬的工作流，借用一下_2097157731659632641.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_965

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/简单用_2096538181641527298.json、视频生成/文生视频/鱼酥大佬的工作流，借用一下_2097157731659632641.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CR Text`
- `LoraLoaderModelOnly`
- `MiniMaxH3Unified`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `KSamplerSelect` —— 1/2 个有
- `MiniMaxH3AVDecodeT8` —— 1/2 个有
- `MiniMaxH3DualClockSamplerT8` —— 1/2 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `VideoCombineV2` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

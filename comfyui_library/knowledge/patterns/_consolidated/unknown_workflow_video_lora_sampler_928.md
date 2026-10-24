---
name: unknown_workflow_video_lora_sampler_928
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.911
common_nodes: [BasicGuider, CLIPLoader, CR Text, Fast Groups Bypasser (rgthree), LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3Unified, PathchSageAttentionKJ, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/MinimaxH3全功能加速工作流（目前有bug等rh修复）_2085696451409170433.json, 视频生成/文生视频/鱼酥大佬的工作流，借用一下_2097157731659632641.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_928

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/MinimaxH3全功能加速工作流（目前有bug等rh修复）_2085696451409170433.json、视频生成/文生视频/鱼酥大佬的工作流，借用一下_2097157731659632641.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CR Text`
- `Fast Groups Bypasser (rgthree)`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
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
- `Label (rgthree)` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_video_lora_sampler_417
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8952
common_nodes: [CFGGuider, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Minimax_H3 多图参考短剧制作，加速工作流_2088187262285729793.json, 视频生成/图生视频/Minimax_H3_多图参考加速工作流_2099764393121771521.json, 视频生成/图生视频/Minimax_H3_多图参考加速工作流_2099848729263169538.json, 视频生成/文生视频/H3全能参考工作流_2093000289442942977.json, 视频生成/文生视频/Minimax_H3 多图参考加速工作流_2085701590907969537.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_417

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/Minimax_H3 多图参考短剧制作，加速工作流_2088187262285729793.json、视频生成/图生视频/Minimax_H3_多图参考加速工作流_2099764393121771521.json、视频生成/图生视频/Minimax_H3_多图参考加速工作流_2099848729263169538.json、视频生成/文生视频/H3全能参考工作流_2093000289442942977.json、视频生成/文生视频/Minimax_H3 多图参考加速工作流_2085701590907969537.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 4/5 个有
- `KSamplerSelect` —— 4/5 个有
- `PrimitiveStringMultiline` —— 4/5 个有
- `H3AudioRefineSampler` —— 3/5 个有
- `H3FrozenVideoCache` —— 3/5 个有
- `MiniMaxH3SigmaShift` —— 3/5 个有
- `MiniMaxH3TurboSampler` —— 3/5 个有
- `ModelAttentionBackend` —— 3/5 个有
- `SolAttnPatch` —— 3/5 个有
- `ImpactSwitch` —— 1/5 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 1/5 个有
- `MuyeTextEditOutput` —— 1/5 个有
- `VHS_LoadVideo` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

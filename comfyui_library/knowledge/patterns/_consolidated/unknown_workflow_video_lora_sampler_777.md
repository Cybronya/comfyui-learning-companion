---
name: unknown_workflow_video_lora_sampler_777
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.85
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, ImageResizeKJv2, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PT_H3ConcatAVLatent, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEEncode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Minimax参考生视频+加速放大_2087734040970481666.json, 视频生成/图生视频/minimax h3超级加强！清晰度天花板_2088308372293640194.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_777

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Minimax参考生视频+加速放大_2087734040970481666.json、视频生成/图生视频/minimax h3超级加强！清晰度天花板_2088308372293640194.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PT_H3ConcatAVLatent`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `CreateVideo` —— 1/2 个有
- `ImpactConditionalBranch` —— 1/2 个有
- `Int` —— 1/2 个有
- `MathExpression_UTK` —— 1/2 个有
- `ModelAttentionBackend` —— 1/2 个有
- `RIFE VFI` —— 1/2 个有
- `ResizeShortestToNode` —— 1/2 个有
- `VAEEncodeAudio` —— 1/2 个有
- `VAEEncodeTiled` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有
- `easy clearCacheAll` —— 1/2 个有
- `获取视频信息` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

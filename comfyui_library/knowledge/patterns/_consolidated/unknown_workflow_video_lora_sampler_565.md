---
name: unknown_workflow_video_lora_sampler_565
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.90125
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, ImageResizeKJv2, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PT_H3ConcatAVLatent, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Minimax参考生视频+加速放大_2087734040970481666.json, 视频生成/图生视频/minimax h3超级加强！清晰度天花板_2088308372293640194.json, 视频生成/图生视频/v3 minimax h3超级加强！清晰度天花板_2088502342512631810.json, 视频生成/图生视频/v4 minimax h3-Sigmas 区间控制_2089033224172425217.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_565

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Minimax参考生视频+加速放大_2087734040970481666.json、视频生成/图生视频/minimax h3超级加强！清晰度天花板_2088308372293640194.json、视频生成/图生视频/v3 minimax h3超级加强！清晰度天花板_2088502342512631810.json、视频生成/图生视频/v4 minimax h3-Sigmas 区间控制_2089033224172425217.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
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
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ModelAttentionBackend` —— 3/4 个有
- `VAEEncodeTiled` —— 3/4 个有
- `ExtendIntermediateSigmas` —— 2/4 个有
- `H3SigmaRefiner` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `VAEEncode` —— 2/4 个有
- `CR Prompt Text` —— 1/4 个有
- `CreateVideo` —— 1/4 个有
- `ImpactConditionalBranch` —— 1/4 个有
- `Int` —— 1/4 个有
- `MathExpression_UTK` —— 1/4 个有
- `ModelPreviewOverrideKJ` —— 1/4 个有
- `RIFE VFI` —— 1/4 个有
- `ResizeShortestToNode` —— 1/4 个有
- `SaveImage` —— 1/4 个有
- `VAEEncodeAudio` —— 1/4 个有
- `VHS_LoadVideo` —— 1/4 个有
- `easy clearCacheAll` —— 1/4 个有
- `solarL_VideoFrameRelay` —— 1/4 个有
- `获取视频信息` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

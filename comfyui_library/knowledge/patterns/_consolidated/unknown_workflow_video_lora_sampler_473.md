---
name: unknown_workflow_video_lora_sampler_473
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9504
common_nodes: [BasicGuider, CLIPLoader, CR Prompt Text, ComfyMathExpression, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/10Eros Test4双时钟MiniMax海螺H3社群动态表情包_2087121681432268801.json, 视频生成/图生视频/10Eros Test4双时钟MiniMax海螺H3社群动态表情包_2087167996421828610.json, 视频生成/图生视频/H3 极速导演台｜图生·首尾帧·多参一体化（8步双时钟）_2086807475478683649.json, 视频生成/图生视频/H3打戏自用（T8流大改）_2101622728154505217.json, 视频生成/图生视频/Minmax h3-10Eros-max-Sigmas值调度_2088833172883722242.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_473

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/10Eros Test4双时钟MiniMax海螺H3社群动态表情包_2087121681432268801.json、视频生成/图生视频/10Eros Test4双时钟MiniMax海螺H3社群动态表情包_2087167996421828610.json、视频生成/图生视频/H3 极速导演台｜图生·首尾帧·多参一体化（8步双时钟）_2086807475478683649.json、视频生成/图生视频/H3打戏自用（T8流大改）_2101622728154505217.json、视频生成/图生视频/Minmax h3-10Eros-max-Sigmas值调度_2088833172883722242.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfyMathExpression`
- `LoraLoaderBypassModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ModelAttentionBackend` —— 4/5 个有
- `LoadImage` —— 3/5 个有
- `PrimitiveFloat` —— 3/5 个有
- `ResolutionSelector` —— 3/5 个有
- `ExtendIntermediateSigmas` —— 2/5 个有
- `H3SigmaRefiner` —— 2/5 个有
- `Int` —— 2/5 个有
- `WujiCleaner` —— 2/5 个有
- `WujiImageLoader` —— 2/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `MiniMaxChunkFeedForward` —— 1/5 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 1/5 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 1/5 个有
- `MiniMaxLowVRAMAttention` —— 1/5 个有
- `RHMiniMaxH3PromptOptimizer` —— 1/5 个有
- `SolAttnMiniMax` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

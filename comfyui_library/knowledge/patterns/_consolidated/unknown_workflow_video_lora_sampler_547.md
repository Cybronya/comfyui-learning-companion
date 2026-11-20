---
name: unknown_workflow_video_lora_sampler_547
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.814333
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3海螺四步加速多合一_2085737590669529090.json, 视频生成/文生视频/MiniMax H3海螺四步加速多合一_2085738060221861890.json, 视频生成/文生视频/MiniMax-H3 4步加速 _ 全能多参音视频生成_2087364898803245057.json, 视频生成/文生视频/Minimax H3 参考生成_2088114013229113346.json, 视频生成/文生视频/Minimax H3 文生视频_2087105033031737345.json, 视频生成/文生视频/Minimax-H3-4步加速（T8节点+提示词强化）_2086825206148063234.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_547

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3海螺四步加速多合一_2085737590669529090.json、视频生成/文生视频/MiniMax H3海螺四步加速多合一_2085738060221861890.json、视频生成/文生视频/MiniMax-H3 4步加速 _ 全能多参音视频生成_2087364898803245057.json、视频生成/文生视频/Minimax H3 参考生成_2088114013229113346.json、视频生成/文生视频/Minimax H3 文生视频_2087105033031737345.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `LoraLoaderBypassModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 5/6 个有
- `MiniMaxH3DualClockSamplerT8` —— 5/6 个有
- `LoadAudio` —— 4/6 个有
- `PrimitiveFloat` —— 4/6 个有
- `PrimitiveStringMultiline` —— 4/6 个有
- `Fast Groups Bypasser (rgthree)` —— 3/6 个有
- `CR Prompt Text` —— 2/6 个有
- `Int` —— 2/6 个有
- `PreviewAny` —— 2/6 个有
- `RHHiddenNodes` —— 2/6 个有
- `GetVideoComponents` —— 1/6 个有
- `LoadVideo` —— 1/6 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 1/6 个有
- `RHLLMChatNode` —— 1/6 个有
- `ShowText|fofo` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

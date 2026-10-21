---
name: unknown_workflow_video_sampler_unet_72
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.770333
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3MultiRateSamplerEXPT8, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/文生图/MiniMax H3 int8文生视频 _4步加速_提示词优化工作流_2090316979256254466.json, 视频生成/图生视频/MINIMAX-H3图生视频_2093614146712592385.json, 视频生成/图生视频/MiniMax H3 多参考图生视频_4步加速_提示词自动优化_2090474972128047106.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_72

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/MiniMax H3 int8文生视频 _4步加速_提示词优化工作流_2090316979256254466.json、视频生成/图生视频/MINIMAX-H3图生视频_2093614146712592385.json、视频生成/图生视频/MiniMax H3 多参考图生视频_4步加速_提示词自动优化_2090474972128047106.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3MultiRateSamplerEXPT8`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Any To String (mtb)` —— 2/3 个有
- `BatchImagesNode` —— 2/3 个有
- `JoinStringMulti` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `LoraLoaderBypassModelOnly` —— 2/3 个有
- `StringConcatenate` —— 2/3 个有
- `UniBlockSwap` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `llama_cpp_instruct_adv` —— 2/3 个有
- `llama_cpp_model_loader` —— 2/3 个有
- `llama_cpp_parameters` —— 2/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `MiniMaxH3SigmaShift` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

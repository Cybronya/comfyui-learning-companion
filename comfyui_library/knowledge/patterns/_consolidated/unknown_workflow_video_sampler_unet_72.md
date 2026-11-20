---
name: unknown_workflow_video_sampler_unet_72
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.792
common_nodes: [Any To String (mtb), BasicGuider, BatchImagesNode, CLIPLoader, ComfyMathExpression, JoinStringMulti, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3MultiRateSamplerEXPT8, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, StringConcatenate, UNETLoader, UniBlockSwap, VAELoader, VHS_VideoCombine, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [图片生成/文生图/MiniMax H3 int8文生视频 _4步加速_提示词优化工作流_2090316979256254466.json, 视频生成/图生视频/MiniMax H3 多参考图生视频_4步加速_提示词自动优化_2090474972128047106.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_72

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/MiniMax H3 int8文生视频 _4步加速_提示词优化工作流_2090316979256254466.json、视频生成/图生视频/MiniMax H3 多参考图生视频_4步加速_提示词自动优化_2090474972128047106.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `Any To String (mtb)`
- `BasicGuider`
- `BatchImagesNode`
- `CLIPLoader`
- `ComfyMathExpression`
- `JoinStringMulti`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3MultiRateSamplerEXPT8`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `StringConcatenate`
- `UNETLoader`
- `UniBlockSwap`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 1/2 个有
- `LoraLoaderBypassModelOnly` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `MiniMaxH3SigmaShift` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

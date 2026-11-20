---
name: unknown_workflow_video_sampler_unet_76
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8095
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, LoadImage, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 图生视频高质量加速版_2084173235788275713.json, 视频生成/图生视频/MiniMax-H3 单图换装工作流_2097684790219726850.json, 视频生成/图生视频/Minimax H3 图生视频｜冻结时间 360 环绕、首尾画面循环闭环｜+ HyperFlow 8 步 LoRA_2104492606691569665.json, 视频生成/文生视频/MiNiMax H3 高质量工作流_2092902067592585217.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_76

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 图生视频高质量加速版_2084173235788275713.json、视频生成/图生视频/MiniMax-H3 单图换装工作流_2097684790219726850.json、视频生成/图生视频/Minimax H3 图生视频｜冻结时间 360 环绕、首尾画面循环闭环｜+ HyperFlow 8 步 LoRA_2104492606691569665.json、视频生成/文生视频/MiNiMax H3 高质量工作流_2092902067592585217.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `LoadImage`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 3/4 个有
- `KSamplerSelect` —— 3/4 个有
- `Label (rgthree)` —— 3/4 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/4 个有
- `ModelAttentionBackend` —— 3/4 个有
- `LoraLoaderBypassModelOnly` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `MiniMaxH3AudioConditioningT8` —— 2/4 个有
- `MiniMaxH3DualClockSamplerT8` —— 2/4 个有
- `MiniMaxH3ImageToVideo` —— 2/4 个有
- `PrimitiveFloat` —— 2/4 个有
- `PrimitiveInt` —— 2/4 个有
- `Float` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `LayerUtility: TextBox` —— 1/4 个有
- `MiniMaxH3AVDecodeT8` —— 1/4 个有
- `MiniMaxH3ReferenceToVideo` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `SolAttnMiniMax` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

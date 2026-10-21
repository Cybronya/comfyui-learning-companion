---
name: unknown_workflow_video_sampler_unet_59
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.812667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3 首尾帧视频生成 _ 提示词强化 _ 超分_2084660541540360193.json, 视频生成/文生视频/Minimax-H3 文生视频_2084501246035185665.json, 视频生成/文生视频/Minimax_文生视频_8步加速_2077975666892558338.json, 视频生成/文生视频/mini_max文生视频_2084531376707166209.json, 视频生成/文生视频/minimax_h3 4steps加速_2085757759953399809.json, 视频生成/文生视频/minimax_阿里8步加速_文生视频_图生视频_全能参考三合一_2095489469662187522.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_59

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 首尾帧视频生成 _ 提示词强化 _ 超分_2084660541540360193.json、视频生成/文生视频/Minimax-H3 文生视频_2084501246035185665.json、视频生成/文生视频/Minimax_文生视频_8步加速_2077975666892558338.json、视频生成/文生视频/mini_max文生视频_2084531376707166209.json、视频生成/文生视频/minimax_h3 4steps加速_2085757759953399809.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
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
- `LoraLoaderModelOnly` —— 3/6 个有
- `Fast Groups Bypasser (rgthree)` —— 2/6 个有
- `LoadImage` —— 2/6 个有
- `PathchSageAttentionKJ` —— 2/6 个有
- `KepStringLiteral` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `MiniMaxH3GenerationTailLoader` —— 1/6 个有
- `MiniMaxH3PromptEnhancer` —— 1/6 个有
- `MiniMaxH3ReferenceToVideo` —— 1/6 个有
- `MuyeTextEditOutput` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有
- `RTXVideoSuperResolution` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

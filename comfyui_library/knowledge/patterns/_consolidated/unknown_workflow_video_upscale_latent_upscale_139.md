---
name: unknown_workflow_video_upscale_latent_upscale_139
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.496
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CR Text, ComfyMathExpression, ExtendIntermediateSigmas, GetNode, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, MiniMaxH3AVDecodeT8, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3ReferenceToVideo, MiniMaxH3SemanticBridgeApplyT8, MiniMaxH3SemanticBridgeConfigT8, ModelAttentionBackend, Pipe from any [Crystools], Pipe to/edit any [Crystools], PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, SimpleMath+, SolAttnMiniMax, SplitSigmas, UNETLoader, VAELoader, VHS_VideoCombine, easy blocker, easy boolean, easy ifElse]
problems: []
missing: []
members: [视频生成/图生视频/H3_多参生视频_2108931656911507457.json, 视频生成/图生视频/minimax_H3_多参_2108804190872096769.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_139

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/H3_多参生视频_2108931656911507457.json、视频生成/图生视频/minimax_H3_多参_2108804190872096769.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：50%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CR Text`
- `ComfyMathExpression`
- `ExtendIntermediateSigmas`
- `GetNode`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SemanticBridgeApplyT8`
- `MiniMaxH3SemanticBridgeConfigT8`
- `ModelAttentionBackend`
- `Pipe from any [Crystools]`
- `Pipe to/edit any [Crystools]`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `SimpleMath+`
- `SolAttnMiniMax`
- `SplitSigmas`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`
- `easy blocker`
- `easy boolean`
- `easy ifElse`

**可变部分**（部分 workflow 才有）：
- `LoadVideo` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

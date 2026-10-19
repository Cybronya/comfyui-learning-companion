---
name: unknown_workflow_video_sampler_unet_63
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.44025
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetNode, KSamplerSelect, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax-H3-FastVideo多参极速版_2108479598177636354.json, 视频生成/图生视频/MiniMax-H3开源 8step+高动态加速流图生视频_2088598452845506561.json, 视频生成/图生视频/MiniMax_H3-单采_2106176867115036673.json, 视频生成/图生视频/minimax_H3_文戏工作流急速版_2107639659634454529.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_63

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3-FastVideo多参极速版_2108479598177636354.json、视频生成/图生视频/MiniMax-H3开源 8step+高动态加速流图生视频_2088598452845506561.json、视频生成/图生视频/MiniMax_H3-单采_2106176867115036673.json、视频生成/图生视频/minimax_H3_文戏工作流急速版_2107639659634454529.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：44%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `ModelAttentionBackend` —— 3/4 个有
- `BlockSparseAttention` —— 2/4 个有
- `EmptyImage` —— 2/4 个有
- `ExtendIntermediateSigmas` —— 2/4 个有
- `Float` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `Text` —— 2/4 个有
- `H3SigmaRefiner` —— 1/4 个有
- `LoraLoaderBypassModelOnly` —— 1/4 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 1/4 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 1/4 个有
- `MiniMaxH3SigmaShift` —— 1/4 个有
- `ModelPreviewOverrideKJ` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `PrimitiveFloat` —— 1/4 个有
- `SigmasGraph` —— 1/4 个有
- `easy float` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

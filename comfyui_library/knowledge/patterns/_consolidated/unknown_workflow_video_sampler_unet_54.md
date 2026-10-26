---
name: unknown_workflow_video_sampler_unet_54
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.629667
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/minimax H3 武斗 10.14_2109929662204960769.json, 视频生成/图生视频/minimax h3 参考生视频_2085558159850172417.json, 视频生成/图生视频/minimax+taomate_workflow_2099426301223456770.json, 视频生成/图生视频/minimaxH3官方工作流（定向调优版）_2114543091377070082.json, 视频生成/图生视频/minimax_H3_文戏工作流急速版_2107639659634454529.json, 视频生成/文生视频/H3全能参考工作流_2086287689682350082.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_54

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/minimax H3 武斗 10.14_2109929662204960769.json、视频生成/图生视频/minimax h3 参考生视频_2085558159850172417.json、视频生成/图生视频/minimax+taomate_workflow_2099426301223456770.json、视频生成/图生视频/minimaxH3官方工作流（定向调优版）_2114543091377070082.json、视频生成/图生视频/minimax_H3_文戏工作流急速版_2107639659634454529.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
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
- `BasicScheduler` —— 5/6 个有
- `BlockSparseAttention` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/6 个有
- `PrimitiveStringMultiline` —— 5/6 个有
- `GetNode` —— 4/6 个有
- `LoadAudio` —— 4/6 个有
- `ModelAttentionBackend` —— 4/6 个有
- `SetNode` —— 4/6 个有
- `Fast Groups Bypasser (rgthree)` —— 3/6 个有
- `ManualSigmas` —— 3/6 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 3/6 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 3/6 个有
- `ModelPreviewOverrideKJ` —— 3/6 个有
- `Astra` —— 2/6 个有
- `CreateVideo` —— 2/6 个有
- `MiniMaxH3AVDecodeT8` —— 2/6 个有
- `RunningHub Deepcleaner` —— 2/6 个有
- `SaveVideo` —— 2/6 个有
- `EmptyImage` —— 1/6 个有
- `ExtendIntermediateSigmas` —— 1/6 个有
- `LoraLoaderBypassModelOnly` —— 1/6 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 1/6 个有
- `MiniMaxH3SigmaShift` —— 1/6 个有
- `PreviewAny` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `Text` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

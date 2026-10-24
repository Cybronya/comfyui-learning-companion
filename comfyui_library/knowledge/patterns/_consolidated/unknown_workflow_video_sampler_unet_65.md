---
name: unknown_workflow_video_sampler_unet_65
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.869
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3 Ref2VA 多参考生视频极速超清 2K_2101695103294328834.json, 视频生成/文生视频/MiniMax H3开源版 多模态 图生视频【开源】_2084505380671021058.json, 视频生成/文生视频/MiniMax H3满血加速优化版 多模态生视频【快速高清 】_2085727977836466178.json, 视频生成/文生视频/MiniMax H3满血版 生视频【4步加速优化版+可出1080】_2085719967990898690.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_65

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 Ref2VA 多参考生视频极速超清 2K_2101695103294328834.json、视频生成/文生视频/MiniMax H3开源版 多模态 图生视频【开源】_2084505380671021058.json、视频生成/文生视频/MiniMax H3满血加速优化版 多模态生视频【快速高清 】_2085727977836466178.json、视频生成/文生视频/MiniMax H3满血版 生视频【4步加速优化版+可出1080】_2085719967990898690.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 3/4 个有
- `LoadAudio` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有
- `PathchSageAttentionKJ` —— 2/4 个有
- `RTXVideoSuperResolution` —— 2/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `MiniMaxH3AVDecodeT8` —— 1/4 个有
- `MiniMaxH3AudioConditioningT8` —— 1/4 个有
- `MiniMaxH3BlockCacheT8` —— 1/4 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 1/4 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/4 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 1/4 个有
- `RH_MinimaxHailuoH3ContextIrMultimodal` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_video_sampler_unet_32
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.821
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadAudio, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3加速优化版  全能参考(9图  _ 3音频 _ 3视频)_2086280720103858177.json, 视频生成/文生视频/MiniMax H3加速优化版  全能参考（人物_场景_音频）_2085671993520771073.json, 视频生成/文生视频/MiniMax H3开源版 全能多参音生视频 （9图3视频3音频）_2084924322795311105.json, 视频生成/文生视频/MiniMax H3开源版 多模态 图生视频【开源】_2084505380671021058.json, 视频生成/文生视频/MiniMax H3满血加速优化版 多模态生视频【快速高清 】_2085727977836466178.json, 视频生成/文生视频/MiniMax H3满血版 生视频【4步加速优化版+可出1080】_2085719967990898690.json, 视频生成/文生视频/MiniMax+H3+refV1.2Lora-多参考工作流（全接口开放内部开发版）_2096531122523033602.json, 视频生成/文生视频/MiniMax+H3+新ref V1.0 Lora 阿里8步版本-多参考工作流_2096537181975310338.json, 视频生成/文生视频/minimax h3 二采高清工作流_2089238048839131137.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_32

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3加速优化版  全能参考(9图  _ 3音频 _ 3视频)_2086280720103858177.json、视频生成/文生视频/MiniMax H3加速优化版  全能参考（人物_场景_音频）_2085671993520771073.json、视频生成/文生视频/MiniMax H3开源版 全能多参音生视频 （9图3视频3音频）_2084924322795311105.json、视频生成/文生视频/MiniMax H3开源版 多模态 图生视频【开源】_2084505380671021058.json、视频生成/文生视频/MiniMax H3满血加速优化版 多模态生视频【快速高清 】_2085727977836466178.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadAudio`
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
- `easy cleanGpuUsed` —— 6/9 个有
- `JjkText` —— 5/9 个有
- `LoraLoaderModelOnly` —— 5/9 个有
- `PathchSageAttentionKJ` —— 5/9 个有
- `VHS_LoadVideo` —— 5/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/9 个有
- `RTXVideoSuperResolution` —— 4/9 个有
- `Fast Groups Muter (rgthree)` —— 3/9 个有
- `GetNode` —— 3/9 个有
- `LoadVideo` —— 3/9 个有
- `SetNode` —— 3/9 个有
- `MiniMaxH3SigmaShift` —— 2/9 个有
- `ImageResizeKJv2` —— 1/9 个有
- `Int` —— 1/9 个有
- `LoraLoaderBypassModelOnly` —— 1/9 个有
- `MiniMaxH3BlockCacheT8` —— 1/9 个有
- `PT_H3ConcatAVLatent` —— 1/9 个有
- `PainterVRAM` —— 1/9 个有
- `VAEEncode` —— 1/9 个有
- `VAEEncodeAudio` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_sampler_unet_vae_130
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8896
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3全能参考_2084306466529439745.json, 视频生成/文生视频/MiniMax H3开源版 多模态 图生视频【开源】_2084505380671021058.json, 视频生成/文生视频/MiniMax H3满血加速优化版 多模态生视频【快速高清 】_2085727977836466178.json, 视频生成/文生视频/MiniMax H3满血版 生视频【4步加速优化版+可出1080】_2085719967990898690.json, 视频生成/文生视频/MinimaxH3多参生视频+(量化加速版)_2084546214854483969.json, 视频生成/文生视频/Minimax参考生视频 高质量 加速版_2086430508090744833.json, 视频生成/文生视频/minimaxH3文生视频武器打斗转用工作流_2095690809084571649.json, 视频生成/文生视频/【遇见AI】minimax H3 高动态打斗场景武术动作二采修复+提示词skill工作流_2095684866888257537.json, 视频生成/文生视频/剑斗多参模式_2094373732667187201.json, 视频生成/文生视频/战斗双采首尾帧模式_2094373774731862018.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_130

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3全能参考_2084306466529439745.json、视频生成/文生视频/MiniMax H3开源版 多模态 图生视频【开源】_2084505380671021058.json、视频生成/文生视频/MiniMax H3满血加速优化版 多模态生视频【快速高清 】_2085727977836466178.json、视频生成/文生视频/MiniMax H3满血版 生视频【4步加速优化版+可出1080】_2085719967990898690.json、视频生成/文生视频/MinimaxH3多参生视频+(量化加速版)_2084546214854483969.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ReferenceToVideo` —— 9/10 个有
- `PrimitiveFloat` —— 9/10 个有
- `ResolutionSelector` —— 9/10 个有
- `easy cleanGpuUsed` —— 7/10 个有
- `CreateVideo` —— 6/10 个有
- `SaveVideo` —— 6/10 个有
- `LoraLoaderModelOnly` —— 5/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/10 个有
- `DisableNoise` —— 4/10 个有
- `LoadAudio` —— 4/10 个有
- `PathchSageAttentionKJ` —— 4/10 个有
- `VHS_VideoCombine` —— 4/10 个有
- `ExtendIntermediateSigmas` —— 3/10 个有
- `JjkText` —— 3/10 个有
- `RTXVideoSuperResolution` —— 3/10 个有
- `SplitSigmasDenoise` —— 3/10 个有
- `CLIPTextEncode` —— 2/10 个有
- `MiniMaxH3BlockCacheT8` —— 2/10 个有
- `PrimitiveInt` —— 2/10 个有
- `ImageResizeKJv2` —— 1/10 个有
- `Label (rgthree)` —— 1/10 个有
- `MiniMaxH3ImageToVideo` —— 1/10 个有
- `SplitSigmas` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

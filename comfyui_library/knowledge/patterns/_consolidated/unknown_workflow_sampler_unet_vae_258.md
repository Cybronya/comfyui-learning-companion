---
name: unknown_workflow_sampler_unet_vae_258
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.838
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3 Ref2VA 多参考生视频极速超清 2K_2101695103294328834.json, 视频生成/文生视频/MiniMax H3 多图参考 开源版_2094392605172912129.json, 视频生成/文生视频/MiniMax H3 多模态参考生视频（开源版）_2084993447697674241.json, 视频生成/文生视频/MiniMax H3 文图生视频、参考生视频多合一工作流-B站UP主@好奇漫步_2086134141166383105.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_258

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 Ref2VA 多参考生视频极速超清 2K_2101695103294328834.json、视频生成/文生视频/MiniMax H3 多图参考 开源版_2094392605172912129.json、视频生成/文生视频/MiniMax H3 多模态参考生视频（开源版）_2084993447697674241.json、视频生成/文生视频/MiniMax H3 文图生视频、参考生视频多合一工作流-B站UP主@好奇漫步_2086134141166383105.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：84%

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

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 3/4 个有
- `LoadAudio` —— 3/4 个有
- `SaveVideo` —— 3/4 个有
- `GetVideoComponents` —— 2/4 个有
- `LoadVideo` —— 2/4 个有
- `ComfySwitchNode` —— 1/4 个有
- `MiniMaxH3AVDecodeT8` —— 1/4 个有
- `MiniMaxH3AudioConditioningT8` —— 1/4 个有
- `MiniMaxH3ImageToVideo` —— 1/4 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 1/4 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `RH_MinimaxHailuoH3ContextIrMultimodal` —— 1/4 个有
- `VHS_VideoCombine` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

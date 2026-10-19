---
name: unknown_workflow_video_sampler_unet_61
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.89875
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, LoadImage, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 全能参考生视频加速版_2098615905507958786.json, 视频生成/图生视频/minimax h3 多参工作流_2094717859841794049.json, 视频生成/文生视频/MiniMax-H3-FL2VA-T8-Turbo_2086083227437060098.json, 视频生成/文生视频/海螺Minimax_H3文生视频_2084118934588055553.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_61

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 全能参考生视频加速版_2098615905507958786.json、视频生成/图生视频/minimax h3 多参工作流_2094717859841794049.json、视频生成/文生视频/MiniMax-H3-FL2VA-T8-Turbo_2086083227437060098.json、视频生成/文生视频/海螺Minimax_H3文生视频_2084118934588055553.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `LoadImage`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/4 个有
- `ModelAttentionBackend` —— 3/4 个有
- `PathchSageAttentionKJ` —— 3/4 个有
- `SolAttnMiniMax` —— 3/4 个有
- `ExtendIntermediateSigmas` —— 2/4 个有
- `IntToString` —— 2/4 个有
- `LoadAudio` —— 2/4 个有
- `LoraLoaderBypassModelOnly` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `PreviewAny` —— 2/4 个有
- `Seed_` —— 2/4 个有
- `VHS_LoadVideo` —— 2/4 个有
- `text-util-join-text` —— 2/4 个有
- `Text` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

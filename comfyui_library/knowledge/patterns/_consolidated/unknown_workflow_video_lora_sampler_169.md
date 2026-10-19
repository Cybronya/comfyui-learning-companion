---
name: unknown_workflow_video_lora_sampler_169
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.880818
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/minmax生图工作流_2097534784162582529.json, 视频生成/图生视频/【官模】Lightx2v正式版+8步加速+_+Minimax双时钟参考生视频V1_2087816150808879105.json, 视频生成/图生视频/双时钟采样6步极速参考生视频_2085777514399625218.json, 视频生成/图生视频/海螺Minimax_H3_图生视频_2084150796144435202.json, 视频生成/图生视频/海螺Minimax_H3_音频生视频_2084557773223841793.json, 视频生成/图生视频/海螺Minimax_H3_首尾帧_2084163001497776130.json, 视频生成/图生视频/海螺Minimax_H3多主体生视频_2084156493078814722.json, 视频生成/图生视频/自用 4步加速 图生视频_2100517066590744577.json, 视频生成/图生视频/音频驱动 H3数字人 唱歌MV（多参视频生成）_2092869013713022978.json, 视频生成/图生视频/音频驱动 H3数字人_2092779198917210114.json, 视频生成/文生视频/(8步高质量极速)Minimax_H3开源版_短剧漫剧_创意视频文生视频（600步新加速LORA）_2100562439568969730.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_169

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/minmax生图工作流_2097534784162582529.json、视频生成/图生视频/【官模】Lightx2v正式版+8步加速+_+Minimax双时钟参考生视频V1_2087816150808879105.json、视频生成/图生视频/双时钟采样6步极速参考生视频_2085777514399625218.json、视频生成/图生视频/海螺Minimax_H3_图生视频_2084150796144435202.json、视频生成/图生视频/海螺Minimax_H3_音频生视频_2084557773223841793.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `LoraLoaderBypassModelOnly`
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
- `LoadImage` —— 10/11 个有
- `ModelAttentionBackend` —— 7/11 个有
- `CR Prompt Text` —— 5/11 个有
- `LoadAudio` —— 4/11 个有
- `PrimitiveStringMultiline` —— 4/11 个有
- `PreviewAudio` —— 2/11 个有
- `PreviewImage` —— 2/11 个有
- `SolAttnMiniMax` —— 2/11 个有
- `TrimAudioDuration` —— 2/11 个有
- `EmptyImage` —— 1/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/11 个有
- `MiniMaxH3TurboLoRA` —— 1/11 个有
- `SaveImage` —— 1/11 个有
- `Text` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

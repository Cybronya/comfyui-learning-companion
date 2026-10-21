---
name: unknown_workflow_video_sampler_unet_31
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.847636
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, LoadImage, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/多图参考生成视频Minimax+H3 极致满血1K-10秒 双bf16-+sage加速_2090611037820243970.json, 视频生成/图生视频/海螺Minimax_H3_图生视频_2084150796144435202.json, 视频生成/图生视频/海螺Minimax_H3_音频生视频_2084557773223841793.json, 视频生成/图生视频/海螺Minimax_H3_首尾帧_2084163001497776130.json, 视频生成/图生视频/海螺Minimax_H3多主体生视频_2084156493078814722.json, 视频生成/图生视频/自用 4步加速 图生视频_2100517066590744577.json, 视频生成/图生视频/音频驱动 H3数字人 唱歌MV（多参视频生成）_2092869013713022978.json, 视频生成/图生视频/音频驱动 H3数字人_2092779198917210114.json, 视频生成/图生视频/高质量-Minimax H3音频驱动数字人BF16-max-手动提示词_2099743464232669186.json, 视频生成/文生视频/MiniMax H3音频驱动数字人-加速版-参考生视频-超长时长_2100241874136166402.json, 视频生成/文生视频/MiniMax H3音频驱动数字人-加速版-参考生视频-长视频直出_2100530217365364737.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_31

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/多图参考生成视频Minimax+H3 极致满血1K-10秒 双bf16-+sage加速_2090611037820243970.json、视频生成/图生视频/海螺Minimax_H3_图生视频_2084150796144435202.json、视频生成/图生视频/海螺Minimax_H3_音频生视频_2084557773223841793.json、视频生成/图生视频/海螺Minimax_H3_首尾帧_2084163001497776130.json、视频生成/图生视频/海螺Minimax_H3多主体生视频_2084156493078814722.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `LoadImage`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderBypassModelOnly` —— 9/11 个有
- `MiniMaxH3DualClockSamplerT8` —— 9/11 个有
- `ModelAttentionBackend` —— 8/11 个有
- `CR Prompt Text` —— 7/11 个有
- `LoadAudio` —— 6/11 个有
- `TrimAudioDuration` —— 5/11 个有
- `PreviewAudio` —— 4/11 个有
- `SolAttnMiniMax` —— 4/11 个有
- `PrimitiveStringMultiline` —— 3/11 个有
- `BasicScheduler` —— 2/11 个有
- `JjkText` —— 2/11 个有
- `KSamplerSelect` —— 2/11 个有
- `孤海注释` —— 2/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有
- `LayerUtility: PurgeVRAM V2` —— 1/11 个有
- `LoraLoaderModelOnly` —— 1/11 个有
- `Text` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

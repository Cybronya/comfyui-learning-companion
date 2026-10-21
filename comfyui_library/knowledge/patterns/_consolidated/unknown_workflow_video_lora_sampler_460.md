---
name: unknown_workflow_video_lora_sampler_460
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7898
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, LoadImage, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/加速版 只需4步，300s，0.9倍百万像素 minimax h3 4步加速lightx2v_2086649957204979713.json, 视频生成/文生视频/双时钟采样6步极速图文生视频_2085767587174113281.json, 视频生成/文生视频/开源版Minimax H3 多合一T8版本+全节点注释_2086677614869172225.json, 视频生成/文生视频/开源版Minimax H3视频全功能加速图片参考turbo4步加速短视频生成_2086660578432610305.json, 视频生成/文生视频/打斗专用工作流MINIMAX-H3_2089439571347066881.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_460

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/加速版 只需4步，300s，0.9倍百万像素 minimax h3 4步加速lightx2v_2086649957204979713.json、视频生成/文生视频/双时钟采样6步极速图文生视频_2085767587174113281.json、视频生成/文生视频/开源版Minimax H3 多合一T8版本+全节点注释_2086677614869172225.json、视频生成/文生视频/开源版Minimax H3视频全功能加速图片参考turbo4步加速短视频生成_2086660578432610305.json、视频生成/文生视频/打斗专用工作流MINIMAX-H3_2089439571347066881.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3AudioConditioningT8` —— 4/5 个有
- `PrimitiveStringMultiline` —— 4/5 个有
- `BasicScheduler` —— 2/5 个有
- `KSamplerSelect` —— 2/5 个有
- `MiniMaxH3DualClockSamplerT8` —— 2/5 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 2/5 个有
- `CR Text` —— 1/5 个有
- `LoadAudio` —— 1/5 个有
- `MiniMaxH3ReferenceToVideo` —— 1/5 个有
- `PT_H3ConcatAVLatent` —— 1/5 个有
- `PlaySound|pysssss` —— 1/5 个有
- `VAEEncode` —— 1/5 个有
- `VHS_LoadVideo` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
